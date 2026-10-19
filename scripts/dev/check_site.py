"""Compare preservation invariants in two built MkDocs sites (standard library).

Input/output CRS: n/a (built site files only).
Data layer: catalogue development checks.

With --night-maps the candidate may carry Day and Night pictures: each Day map reference must be
followed by its Night twin (maps/night/<name>.png), both files must exist, and instead of whole-file
hashes the map area of every Day and Night picture must equal the baseline picture's map area
pixel for pixel (only the panel beside the map is redrawn). That comparison needs Pillow.
"""

from __future__ import annotations

import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import posixpath
import sys
from urllib.parse import unquote, urlsplit

# The map panel of a 150 dpi preview picture, in pixels (left, top, right, bottom).
MAP_AREA = (47, 47, 1205, 1193)


class PageParser(HTMLParser):
    """Collect primary navigation, article heading ids and map references."""

    VOID = frozenset("area base br col embed hr img input link meta param source track wbr".split())

    def __init__(self, route: str) -> None:
        super().__init__(convert_charrefs=True)
        self.route = route
        self.stack: list[tuple[str, bool, bool]] = []
        self.nav: list[tuple[str, str | None, str]] = []
        self.headings: list[str] = []
        self.maps: list[str] = []
        self.captures: list[tuple[int, str, str | None, list[str]]] = []
        self.primary_nav_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        classes = (attributes.get("class") or "").split()
        parent_nav = self.stack[-1][1] if self.stack else False
        parent_article = self.stack[-1][2] if self.stack else False
        primary = tag == "nav" and "md-nav--primary" in classes
        self.primary_nav_count += int(primary)
        in_nav = parent_nav or primary
        in_article = parent_article or tag == "article"
        if tag not in self.VOID:
            self.stack.append((tag, in_nav, in_article))
        if in_nav and tag in {"a", "label"} and "md-nav__link" in classes:
            href = attributes.get("href") if tag == "a" else None
            if tag == "a" and href is None:
                raise ValueError(f"{self.route}: navigation link has no href")
            self.captures.append((len(self.stack), tag, href, []))
        if in_article and tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            if attributes.get("id") is not None:
                self.headings.append(attributes["id"])
        if tag == "img" and attributes.get("src"):
            source = urlsplit(attributes["src"])
            path = unquote(source.path)
            if "maps" in path.split("/") and path.endswith(".png"):
                if source.scheme or source.netloc:
                    self.maps.append(attributes["src"])
                else:
                    relative = path.lstrip("/") if path.startswith("/") else posixpath.join(
                        posixpath.dirname(self.route), path
                    )
                    self.maps.append(posixpath.normpath(relative))

    def handle_data(self, data: str) -> None:
        if any(tag in {"script", "style"} for tag, _, _ in self.stack):
            return
        for _, _, _, parts in self.captures:
            parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                while self.captures and self.captures[-1][0] > index:
                    _, kind, href, parts = self.captures.pop()
                    self.nav.append((kind, href, " ".join("".join(parts).split())))
                del self.stack[index:]
                break

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            self.handle_endtag(tag)


def serialise(value: object) -> str:
    """Return JSON without changing content or array order."""
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def excerpt(before: str, after: str) -> str:
    """Show context around the first differing character, including insertions."""
    offset = next((i for i, pair in enumerate(zip(before, after)) if pair[0] != pair[1]),
                  min(len(before), len(after)))
    start = max(0, offset - 25)
    stop = offset + 40
    return (f"first difference at character {offset}: baseline {serialise(before[start:stop])}; "
            f"candidate {serialise(after[start:stop])}")


def read_site(root: Path) -> dict:
    """Read a built site; reject missing entry points or malformed search data."""
    if not root.is_dir() or not (root / "index.html").is_file():
        raise ValueError(f"{root}: expected a built site containing index.html")
    search_path = root / "search" / "search_index.json"
    search = json.loads(search_path.read_text(encoding="utf-8"))
    if not isinstance(search, dict) or not isinstance(search.get("config"), dict):
        raise ValueError(f"{search_path}: expected an object with a config object")
    if not isinstance(search.get("docs"), list):
        raise ValueError(f"{search_path}: docs must be an array")
    for index, doc in enumerate(search["docs"]):
        if not isinstance(doc, dict) or any(not isinstance(doc.get(key), str)
                                            for key in ("location", "title", "text")):
            raise ValueError(f"{search_path}: docs[{index}] requires string location, title and text")
    pages = {}
    for path in sorted(root.rglob("*.html")):
        route = path.relative_to(root).as_posix()
        parser = PageParser(route)
        parser.feed(path.read_text(encoding="utf-8"))
        parser.close()
        pages[route] = parser
    if pages["index.html"].primary_nav_count != 1:
        raise ValueError(f"{root / 'index.html'}: expected one nav.md-nav--primary")
    assets = {}
    for folder, pattern in (("maps", "**/*.png"), ("fonts", "*.woff2")):
        hashes = {}
        for path in sorted((root / folder).glob(pattern)):
            with path.open("rb") as stream:
                hashes[path.relative_to(root).as_posix()] = hashlib.file_digest(stream, "sha256").hexdigest()
        assets[folder] = hashes
    return {"search": search, "pages": pages, **assets}


def sequence_differences(name: str, before: list, after: list) -> list[str]:
    """Describe every changed, added or missing ordered item."""
    differences = []
    for index in range(max(len(before), len(after))):
        if index >= len(before):
            differences.append(f"{name}[{index}] added: {serialise(after[index])}")
        elif index >= len(after):
            differences.append(f"{name}[{index}] missing: {serialise(before[index])}")
        elif before[index] != after[index]:
            differences.append(f"{name}[{index}] changed: {serialise(before[index])} -> {serialise(after[index])}")
    return differences


def search_differences(before: dict, after: dict) -> list[str]:
    """Compare exact search payloads and diagnose changes by location."""
    differences = []
    if before["config"] != after["config"]:
        differences.append("Search config changed: " + excerpt(serialise(before["config"]), serialise(after["config"])))
    old_docs, new_docs = before["docs"], after["docs"]
    if serialise(old_docs) == serialise(new_docs):
        return differences
    differences.append("Search docs serialised JSON changed: " + excerpt(serialise(old_docs), serialise(new_docs)))
    grouped = []
    for docs in (old_docs, new_docs):
        by_location = {}
        for doc in docs:
            by_location.setdefault(doc["location"], []).append(doc)
        grouped.append(by_location)
    old, new = grouped
    for location in sorted(old.keys() | new.keys()):
        for index in range(max(len(old.get(location, [])), len(new.get(location, [])))):
            name = f"Search location {serialise(location)} occurrence {index + 1}"
            if index >= len(old.get(location, [])):
                differences.append(f"{name} added: {serialise(new[location][index])}")
            elif index >= len(new.get(location, [])):
                differences.append(f"{name} missing: {serialise(old[location][index])}")
            else:
                left, right = old[location][index], new[location][index]
                for field in ("title", "text"):
                    if left[field] != right[field]:
                        differences.append(f"{name} {field} changed: " + excerpt(left[field], right[field]))
                left_extra = {key: value for key, value in left.items() if key not in {"location", "title", "text"}}
                right_extra = {key: value for key, value in right.items() if key not in {"location", "title", "text"}}
                if serialise(left_extra) != serialise(right_extra):
                    differences.append(f"{name} other fields changed: {serialise(left_extra)} -> {serialise(right_extra)}")
    differences.extend(sequence_differences("Search location order", [d["location"] for d in old_docs],
                                           [d["location"] for d in new_docs]))
    return differences


def night_of(reference: str) -> str:
    """The Night twin of a Day map reference: maps/<name>.png -> maps/night/<name>.png."""
    return posixpath.join(posixpath.dirname(reference), "night", posixpath.basename(reference))


def is_night(reference: str) -> bool:
    return posixpath.basename(posixpath.dirname(urlsplit(reference).path)) == "night"


def map_area_differences(baseline: Path, candidate: Path, old: dict, new: dict) -> list[str]:
    """Day and Night files pair up, and every map area equals the baseline picture's."""
    from PIL import Image                      # only needed with --night-maps

    differences = []
    old_day = {path for path in old["maps"] if path.count("/") == 1}
    new_day = {path for path in new["maps"] if path.count("/") == 1}
    new_night = {path for path in new["maps"] if path.count("/") == 2 and is_night(path)}
    others = sorted(set(new["maps"]) - new_day - new_night)
    differences += [f"Map file missing: {path}" for path in sorted(old_day - new_day)]
    differences += [f"Map file added: {path}" for path in sorted(new_day - old_day)]
    differences += [f"Unexpected map file: {path}" for path in others]
    differences += [f"Night picture missing: {night_of(path)}" for path in sorted(new_day)
                    if night_of(path) not in new_night]
    differences += [f"Night picture without a Day picture: {path}" for path in sorted(new_night)
                    if posixpath.join("maps", posixpath.basename(path)) not in new_day]
    for path in sorted(old_day & new_day):             # RGBA: a transparent map area must fail too
        with Image.open(baseline / path) as image:
            expected = image.convert("RGBA").crop(MAP_AREA).tobytes()
        for twin in (path, night_of(path)):
            if twin in new["maps"]:
                with Image.open(candidate / twin) as image:
                    if image.convert("RGBA").crop(MAP_AREA).tobytes() != expected:
                        differences.append(f"Map area changed: {twin}")
    return differences


def compare_sites(baseline: Path, candidate: Path, labels: dict[str, str] | None = None,
                  night_maps: bool = False) -> list[dict]:
    """Return checks with baseline/candidate counts and all preservation differences."""
    old, new = read_site(baseline), read_site(candidate)
    labels = labels or {}
    checks = []

    def add(name: str, left_count: int, right_count: int, differences: list[str]) -> None:
        checks.append({"name": name, "baseline": left_count, "candidate": right_count,
                       "differences": differences})

    add("Search", len(old["search"]["docs"]), len(new["search"]["docs"]),
        search_differences(old["search"], new["search"]))
    left_routes, right_routes = set(old["pages"]), set(new["pages"])
    route_diffs = [f"Route missing: {route}" for route in sorted(left_routes - right_routes)]
    route_diffs += [f"Route added: {route}" for route in sorted(right_routes - left_routes)]
    add("Routes", len(left_routes), len(right_routes), route_diffs)
    nav_diffs, label_diffs, permitted = [], [], []
    used_labels = set()
    for route in sorted(left_routes & right_routes):
        left_nav, right_nav = old["pages"][route].nav, new["pages"][route].nav
        nav_diffs.extend(sequence_differences(
            f"Nav target in {route}", [(kind, href) for kind, href, _ in left_nav],
            [(kind, href) for kind, href, _ in right_nav]))
        for index in range(max(len(left_nav), len(right_nav))):
            name = f"Nav label in {route}[{index}]"
            if index >= len(left_nav):
                label_diffs.append(f"{name} added: {serialise(right_nav[index][2])}")
            elif index >= len(right_nav):
                label_diffs.append(f"{name} missing: {serialise(left_nav[index][2])}")
            else:
                before, after = left_nav[index][2], right_nav[index][2]
                if after == before:
                    continue
                change = f"{serialise(before)} -> {serialise(after)}"
                if after == labels.get(before) and left_nav[index][:2] == right_nav[index][:2]:
                    permitted.append(f"{name} permitted: {change}")
                    used_labels.add(before)
                else:
                    label_diffs.append(f"{name} changed without permission: {change}")
    nav_counts = [sum(len(page.nav) for page in data["pages"].values()) for data in (old, new)]
    add("Nav order", *nav_counts, nav_diffs)
    add("Nav labels", *nav_counts, label_diffs)
    checks[-1]["permitted"] = permitted
    checks[-1]["unused"] = [f"Unused label mapping: {serialise(before)} -> {serialise(after)}"
                             for before, after in labels.items() if before not in used_labels]
    night_diffs, night_count = [], 0
    for name, attribute in (("Headings", "headings"), ("Map references", "maps")):
        differences, right_count = [], 0
        for route in sorted(left_routes | right_routes):
            left = getattr(old["pages"][route], attribute) if route in left_routes else []
            right = getattr(new["pages"][route], attribute) if route in right_routes else []
            if attribute == "maps" and night_maps:
                night = [reference for reference in right if is_night(reference)]
                right = [reference for reference in right if not is_night(reference)]
                night_count += len(night)
                # every Day picture whose Night file exists is followed by it, and nothing else
                expected = [twin for reference in right for twin in
                            ((reference, night_of(reference)) if night_of(reference) in new["maps"] else (reference,))]
                actual = getattr(new["pages"][route], attribute) if route in right_routes else []
                if actual != expected:
                    night_diffs.append(f"Night pictures in {route}: expected {serialise(expected)}, "
                                       f"found {serialise(actual)}")
            right_count += len(right)
            differences.extend(sequence_differences(f"{name} in {route}", left, right))
        add(name, sum(len(getattr(page, attribute)) for page in old["pages"].values()), right_count, differences)
    if night_maps:
        add("Night pictures", checks[-1]["candidate"], night_count, night_diffs)
        add("Map areas", len(old["maps"]), len(new["maps"]), map_area_differences(baseline, candidate, old, new))
    for folder, name in ((("fonts", "Font hashes"),) if night_maps else (("maps", "Map hashes"), ("fonts", "Font hashes"))):
        left, right = old[folder], new[folder]
        differences = []
        for path in sorted(left.keys() | right.keys()):
            if path not in right:
                differences.append(f"{name}: {path} missing")
            elif path not in left:
                differences.append(f"{name}: {path} added")
            elif left[path] != right[path]:
                differences.append(f"{name}: {path} SHA-256 changed: {left[path]} -> {right[path]}")
        add(name, len(left), len(right), differences)
    return checks


def summary(check: dict) -> str:
    """Format one stdout/report summary with counts."""
    information = (f", permitted={len(check['permitted'])}, unused={len(check['unused'])}"
                   if "permitted" in check else "")
    return (f"{'FAIL' if check['differences'] else 'PASS'} {check['name']}: "
            f"baseline={check['baseline']}, candidate={check['candidate']}, "
            f"differences={len(check['differences'])}{information}")


def main(argv: list[str] | None = None) -> int:
    """Run the comparison; return 0 for parity, 1 for drift, 2 for bad input."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--labels", type=Path, help="JSON object mapping permitted old labels to new labels")
    parser.add_argument("--report", type=Path, help="Write differences and label mapping usage to Markdown")
    parser.add_argument("--night-maps", action="store_true",
                        help="Candidate adds Night pictures: pair them and compare map areas, not file hashes")
    args = parser.parse_args(argv)
    try:
        labels = json.loads(args.labels.read_text(encoding="utf-8-sig")) if args.labels else {}
        if not isinstance(labels, dict) or any(not isinstance(value, str) for value in labels.values()):
            raise ValueError("--labels must contain a JSON object mapping strings to strings")
        # A report must never overwrite either input site or its allow-list.
        if args.report:
            report = args.report.resolve()
            if any(report.is_relative_to(root.resolve()) for root in (args.baseline, args.candidate)):
                raise ValueError("--report must be outside both input sites")
            if args.labels and report == args.labels.resolve():
                raise ValueError("--report must not overwrite --labels")
        checks = compare_sites(args.baseline, args.candidate, labels, args.night_maps)
        if args.report:
            lines = ["# Built-site preservation report", "", f"Baseline: {args.baseline}",
                     f"Candidate: {args.candidate}", ""]
            for check in checks:
                lines.extend([f"## {summary(check)}", ""])
                # Indented blocks preserve arbitrary search text and Markdown characters.
                for difference in check["differences"] + check.get("permitted", []) + check.get("unused", []):
                    lines.extend(["    " + line for line in difference.splitlines()] + [""])
            args.report.write_text("\n".join(lines), encoding="utf-8")
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    for check in checks:
        print(summary(check))
    return int(any(check["differences"] for check in checks))


if __name__ == "__main__":
    raise SystemExit(main())
