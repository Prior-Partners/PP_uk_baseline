"""Screenshots, browser checks and a contact sheet for a built catalogue site (development).

Input/output CRS: n/a. Data layer: catalogue site (development check).

Serves a built site on 127.0.0.1 and, with Playwright (Chromium), opens it in
Night and Day (the reader's system setting, emulated) at 1440 px and 375 px:
the home page, a theme page, a layer page, and search open with a query.
For every view it records console errors, failed requests, the GT America
faces in use and sideways scrolling, then saves a screenshot. Pillow joins the
16 screenshots into one labelled contact sheet. A JSON report holds the checks.

Usage:
    python scripts/dev/shoot_contact_sheet.py <built site> <output folder> [--query battlefield]

Exit code 0 when every check passes, 1 otherwise.
"""
from __future__ import annotations

import argparse
import functools
import http.server
import json
import socketserver
import sys
import threading
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import Page, sync_playwright

PAGES = [
    ("home", "Home", ""),
    ("theme", "Theme page (HER)", "HER/"),
    ("layer", "Layer page (battlefields)", "HER/her_historicengland_battlefields_may2026/"),
    ("search", "Search open", ""),
]
MODES = [("night", "Night", "dark", "slate"), ("day", "Day", "light", "default")]
WIDTHS = [(1440, 900), (375, 812)]
FAMILIES = ("GT America", "GT America Mono")


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map,
                      ".js": "text/javascript", ".css": "text/css", ".woff2": "font/woff2",
                      ".json": "application/json", ".svg": "image/svg+xml"}

    def log_message(self, format: str, *args: object) -> None:  # noqa: A002 - stdlib signature
        pass


def serve(site: Path) -> tuple[socketserver.TCPServer, str]:
    """A local server for ``site`` on a free port, running in a thread."""
    handler = functools.partial(QuietHandler, directory=str(site))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, f"http://127.0.0.1:{server.server_address[1]}/"


def open_search(page: Page, width: int, query: str) -> None:
    """Open Material's search, type the query and wait for results."""
    if width < 960:                                   # phone: the header search button
        page.click('label.md-header__button[for="__search"]')
    page.click(".md-search__input")
    page.keyboard.type(query, delay=40)
    page.wait_for_selector(".md-search-result__item", timeout=15000)
    page.wait_for_timeout(400)


def check_view(page: Page) -> dict[str, Any]:
    """Facts about the page as rendered."""
    return page.evaluate("""() => {
        const faces = [...document.fonts].filter(f => f.status === 'loaded')
            .map(f => `${f.family.replace(/"/g, '')} ${f.weight}`);
        const imgs = [...document.images].filter(i => i.getBoundingClientRect().top < innerHeight);
        return {
          scheme: document.body.getAttribute('data-md-color-scheme'),
          faces: [...new Set(faces)].sort(),
          sideways: document.documentElement.scrollWidth > document.documentElement.clientWidth,
          broken_images: imgs.filter(i => i.complete && i.naturalWidth === 0).map(i => i.src),
        };
    }""")


def shoot(site: Path, out: Path, query: str) -> dict[str, Any]:
    server, base = serve(site)
    screens = out / "screens"
    screens.mkdir(parents=True, exist_ok=True)
    report: dict[str, Any] = {"base": base, "views": [], "failures": []}
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            for mode, mode_label, colour, scheme in MODES:
                for width, height in WIDTHS:
                    context = browser.new_context(viewport={"width": width, "height": height},
                                                  color_scheme=colour, device_scale_factor=1)
                    page = context.new_page()
                    errors: list[str] = []
                    page.on("console", lambda m, e=errors: e.append(m.text) if m.type == "error" else None)
                    page.on("pageerror", lambda exc, e=errors: e.append(str(exc)))
                    page.on("requestfailed", lambda r, e=errors: e.append(f"failed: {r.url}"))
                    page.on("response", lambda r, e=errors: e.append(f"{r.status}: {r.url}")
                            if r.status >= 400 else None)
                    for key, label, path in PAGES:
                        page.goto(base + path, wait_until="networkidle")
                        page.evaluate("document.fonts.ready.then(() => true)")
                        if key == "search":
                            open_search(page, width, query)
                        page.wait_for_timeout(300)
                        facts = check_view(page)
                        shot = screens / f"{mode}_{width}_{key}.png"
                        page.screenshot(path=str(shot))
                        view = {"mode": mode, "width": width, "page": key, "file": shot.name, **facts}
                        report["views"].append(view)
                        problems = []
                        if facts["scheme"] != scheme:
                            problems.append(f"scheme {facts['scheme']} instead of {scheme}")
                        if facts["sideways"]:
                            problems.append("sideways scroll")
                        if facts["broken_images"]:
                            problems.append(f"broken images {facts['broken_images']}")
                        for family in FAMILIES:
                            if not any(f.startswith(family + " ") for f in facts["faces"]):
                                problems.append(f"{family} not loaded")
                        for problem in problems:
                            report["failures"].append(f"{mode} {width} {key}: {problem}")
                    for error in errors:
                        report["failures"].append(f"{mode} {width}: console or network: {error}")
                    context.close()
            browser.close()
    finally:
        server.shutdown()
    return report


def contact_sheet(out: Path) -> Path:
    """Join the 16 screenshots: rows = pages; columns = Night/Day at 1440 and 375 px."""
    screens = out / "screens"
    row_h, pad, label_h, head_h = 450, 18, 34, 110
    columns = [("night", 1440, "Night · 1440 px"), ("day", 1440, "Day · 1440 px"),
               ("night", 375, "Night · 375 px"), ("day", 375, "Day · 375 px")]
    tiles: dict[tuple[str, int, str], Image.Image] = {}
    widths = []
    for mode, width, _ in columns:
        w = None
        for key, _, _ in PAGES:
            img = Image.open(screens / f"{mode}_{width}_{key}.png").convert("RGB")
            scaled = img.resize((round(img.width * row_h / img.height), row_h), Image.LANCZOS)
            tiles[(mode, width, key)] = scaled
            w = scaled.width
        widths.append(w)
    sheet_w = sum(widths) + pad * (len(columns) + 1) + 190
    sheet_h = head_h + len(PAGES) * (row_h + label_h + pad) + pad
    sheet = Image.new("RGB", (sheet_w, sheet_h), (43, 36, 44))           # P+P Aubergine
    draw = ImageDraw.Draw(sheet)
    font_dir = Path(r"C:\Windows\Fonts")
    big = ImageFont.truetype(str(font_dir / "arialbd.ttf"), 26)        # brand fallback: Arial
    small = ImageFont.truetype(str(font_dir / "arial.ttf"), 17)
    cream = (241, 238, 223)
    draw.text((pad, 20), "UK Baseline data catalogue — board restyle (local demo)", font=big, fill=cream)
    for r, (key, label, _) in enumerate(PAGES):
        y = head_h + r * (row_h + label_h + pad)
        draw.text((pad, y + label_h + row_h // 2 - 10), label, font=small, fill=cream)
        x = pad + 190
        for c, (mode, width, col_label) in enumerate(columns):
            if r == 0:
                draw.text((x, head_h - 28), col_label, font=small, fill=cream)
            sheet.paste(tiles[(mode, width, key)], (x, y + label_h))
            x += widths[c] + pad
    path = out / "contact_sheet.png"
    sheet.save(path, optimize=True)
    return path


def decode_maps(site: Path) -> tuple[int, list[str]]:
    """Verify, then fully decode, every preview PNG (Day and Night); return (count, problems).

    ``verify()`` checks the file's structure and checksums only; ``load()``
    decodes the pixels, so a broken image stream is caught too.
    """
    problems = []
    files = sorted((site / "maps").glob("**/*.png"))
    for path in files:
        try:
            with Image.open(path) as img:
                img.verify()
            with Image.open(path) as img:              # verify() leaves the image unusable
                img.load()
        except Exception as exc:  # noqa: BLE001 - every unreadable map is reported, then the next
            problems.append(f"{path.relative_to(site / 'maps').as_posix()}: {exc}")
    return len(files), problems


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("site", type=Path, help="built site folder (mkdocs build output)")
    p.add_argument("out", type=Path, help="folder for screens/, contact_sheet.png and report.json")
    p.add_argument("--query", default="battlefield", help="search query for the search view")
    args = p.parse_args(argv)
    report = shoot(args.site.resolve(), args.out, args.query)
    maps, bad_maps = decode_maps(args.site.resolve())
    report["maps_decoded"] = maps - len(bad_maps)
    report["failures"] += [f"map does not decode: {problem}" for problem in bad_maps]
    print(f"{maps - len(bad_maps)} of {maps} preview maps decode")
    report["contact_sheet"] = str(contact_sheet(args.out))
    (args.out / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"{len(report['views'])} views, {len(report['failures'])} failures; sheet: {report['contact_sheet']}")
    for failure in report["failures"]:
        print("  " + failure)
    return 0 if not report["failures"] else 1


if __name__ == "__main__":
    sys.exit(main())
