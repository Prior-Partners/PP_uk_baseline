"""Check the approved Day/Night tokens using WCAG 2.x contrast calculations.

With ``--live <built site>`` it also serves the site and, with Playwright
(Chromium), measures every visible text node on the home page, a theme page and
two layer pages, in Night and Day at 1440 and 375 px, against its effective
background (``contrast_live.js``). Text must reach 4.5:1, large text 3:1.

Input/output CRS: n/a (colour tokens and built site files only).
Data layer: catalogue development checks.
"""

from __future__ import annotations

import argparse
import colorsys
import functools
import http.server
import json
import math
import re
import sys
import threading
from pathlib import Path


def parse_colour(value: str) -> tuple[float, float, float, float]:
    """Parse supported CSS colours as sRGB components and alpha in [0, 1]."""
    if not isinstance(value, str):
        raise ValueError("Colour must be a CSS string")
    value = value.strip().lower()
    if re.fullmatch(r"#[0-9a-f]{3}(?:[0-9a-f]{3})?", value):
        digits = value[1:]
        if len(digits) == 3:
            digits = "".join(character * 2 for character in digits)
        return (*(int(digits[index:index + 2], 16) / 255 for index in (0, 2, 4)), 1.0)
    match = re.fullmatch(r"(hsl|rgba)\(([^()]*)\)", value)
    if not match:
        raise ValueError(f"Unsupported colour: {value!r}")
    kind, content = match.groups()
    parts = [part.strip() for part in content.split(",")]
    if kind == "hsl":
        if len(parts) != 3 or not all(part.endswith("%") for part in parts[1:]):
            raise ValueError(f"Expected hsl(h,s%,l%): {value!r}")
        hue, saturation, lightness = float(parts[0]), float(parts[1][:-1]), float(parts[2][:-1])
        if not all(math.isfinite(number) for number in (hue, saturation, lightness)) or not (
            0 <= saturation <= 100 and 0 <= lightness <= 100
        ):
            raise ValueError(f"HSL components out of range: {value!r}")
        return (*colorsys.hls_to_rgb((hue % 360) / 360, lightness / 100, saturation / 100), 1.0)
    if len(parts) != 4:
        raise ValueError(f"Expected rgba(r,g,b,a): {value!r}")
    red, green, blue, alpha = (float(part) for part in parts)
    if not all(math.isfinite(number) for number in (red, green, blue, alpha)) or not (
        all(0 <= channel <= 255 for channel in (red, green, blue)) and 0 <= alpha <= 1
    ):
        raise ValueError(f"RGBA components out of range: {value!r}")
    return red / 255, green / 255, blue / 255, alpha


def luminance(channels: tuple[float, ...]) -> float:
    """Calculate relative luminance from three opaque sRGB components."""
    linear = [channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4
              for channel in channels]
    return sum(weight * channel for weight, channel in zip((0.2126, 0.7152, 0.0722), linear))


def ratio(fg: str, bg: str) -> float:
    """Return WCAG contrast, compositing foreground alpha over an opaque background."""
    foreground, background = parse_colour(fg), parse_colour(bg)
    if background[3] != 1:
        raise ValueError("Background must be opaque")
    alpha = foreground[3]
    composite = tuple(foreground[index] * alpha + background[index] * (1 - alpha) for index in range(3))
    first, second = luminance(composite), luminance(background[:3])
    return (max(first, second) + 0.05) / (min(first, second) + 0.05)


# Approved Day/Night palette, including white-on-cobalt active chips.
# Public, extensible table. None means decorative, reported only.
TOKEN_PAIRS: list[dict[str, str | float | None]] = []
for _mode, _background, _primary, _body, _secondary, _mark, _line, _link in (
    ("Day", "#FAFAFA", "#000", "#5f5f5f", "#5f5f5f", "#8a8a8a", "rgba(0,0,0,.28)", "#005DFF"),
    ("Night", "hsl(0,0%,4%)", "#fff", "#c8c8c8", "#9a9a9a", "#9a9a9a", "rgba(255,255,255,.22)", "#d6e4ff"),
):
    for _name, _foreground, _surface, _minimum in (
        ("Body text", _body, _background, 4.5),
        ("Secondary text", _secondary, _background, 4.5),
        ("Primary text", _primary, _background, 4.5),
        ("Links", _link, _background, 4.5),
        ("Chip text", "#121212", "#d9d9d9", 4.5),
        ("Active chip text", "#fff", "#005DFF", 4.5),
        ("Hover chip text", "#121212", "#d6e4ff", 4.5),
        ("Orange kicker", "#FF511D", "#121212", 4.5),
        ("Cobalt focus ring", "#005DFF", _background, 3.0),
        ("Non-text marks", _mark, _background, 3.0),
        ("Hairlines", _line, _background, None),
    ):
        TOKEN_PAIRS.append({"mode": _mode, "name": _name, "fg": _foreground,
                            "bg": _surface, "minimum": _minimum})
TOKEN_PAIRS.append({"mode": "Night", "name": "Orange on Night background", "fg": "#FF511D",
                    "bg": "hsl(0,0%,4%)", "minimum": 4.5})
# Owner review, 17 October 2026: orange page titles (large text) and theme rows.
TOKEN_PAIRS.append({"mode": "Day", "name": "Orange page titles (large text)", "fg": "#FF511D",
                    "bg": "#FAFAFA", "minimum": 3.0})
TOKEN_PAIRS.append({"mode": "Day", "name": "Orange theme rows", "fg": "#C22D00",
                    "bg": "#FAFAFA", "minimum": 4.5})


LIVE_PAGES = ("", "HER/", "HER/her_historicengland_battlefields_may2026/", "DEM/dem_geods_oa_age_2021_22/")
LIVE_VIEWS = (("Night", "dark", 1440, 900), ("Night", "dark", 375, 812),
              ("Day", "light", 1440, 900), ("Day", "light", 375, 812))


class _QuietHandler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map,
                      ".js": "text/javascript", ".css": "text/css", ".woff2": "font/woff2",
                      ".json": "application/json", ".svg": "image/svg+xml"}

    def log_message(self, format: str, *args: object) -> None:  # noqa: A002 - stdlib signature
        pass


def check_live(site: Path, pages: tuple[str, ...] = LIVE_PAGES) -> tuple[int, list[dict]]:
    """Measure every visible text node of ``pages`` in each view; return (sampled, failures)."""
    from playwright.sync_api import sync_playwright   # needed only for --live

    sampler = Path(__file__).with_name("contrast_live.js").read_text(encoding="utf-8")
    handler = functools.partial(_QuietHandler, directory=str(site))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{server.server_address[1]}/"
    sampled, failures = 0, []
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            for mode, scheme, width, height in LIVE_VIEWS:
                context = browser.new_context(viewport={"width": width, "height": height},
                                              color_scheme=scheme)
                page = context.new_page()
                for path in pages:
                    page.goto(base + path, wait_until="networkidle")
                    result = page.evaluate(sampler)
                    sampled += result["sampled"]
                    for failure in result["failures"]:
                        failures.append({"mode": mode, "width": width, "page": path or "home", **failure})
                context.close()
            browser.close()
    finally:
        server.shutdown()
    return sampled, failures


def main(argv: list[str] | None = None) -> int:
    """Print every pair and fail if any required ratio is below its threshold."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", type=Path, help="also measure the text of this built site in a browser")
    parser.add_argument("--report", type=Path, help="with --live, write every failure as JSON")
    args = parser.parse_args(argv)
    failures = 0
    try:
        for pair in TOKEN_PAIRS:
            measured = ratio(pair["fg"], pair["bg"])
            minimum = pair["minimum"]
            failed = minimum is not None and measured < minimum
            failures += int(failed)
            status = "INFO" if minimum is None else "FAIL" if failed else "PASS"
            requirement = "decorative, reported only" if minimum is None else f"minimum {minimum:.1f}:1"
            print(f"{status} {pair['mode']} / {pair['name']}: {measured:.2f}:1 "
                  f"({pair['fg']} on {pair['bg']}; {requirement})")
    except (ValueError, KeyError, TypeError) as error:
        print(f"ERROR: invalid token pair: {error}", file=sys.stderr)
        return 2
    print(f"{'FAIL' if failures else 'PASS'} Contrast: {len(TOKEN_PAIRS)} pairs, {failures} required failures")
    if args.live:
        if not (args.live / "index.html").is_file():
            print(f"ERROR: {args.live} is not a built site", file=sys.stderr)
            return 2
        sampled, live_failures = check_live(args.live.resolve())
        for failure in live_failures:
            print(f"FAIL {failure['mode']} {failure['width']} {failure['page']}: {failure['ratio']}:1 "
                  f"(needs {failure['need']}) {failure['element']} {failure['text']!r}")
        print(f"{'FAIL' if live_failures else 'PASS'} Live contrast: {sampled} text samples in "
              f"{len(LIVE_VIEWS) * len(LIVE_PAGES)} views, {len(live_failures)} below AA")
        if args.report:
            args.report.write_text(json.dumps(live_failures, indent=2, ensure_ascii=False), encoding="utf-8")
        failures += len(live_failures)
    return int(failures > 0)


if __name__ == "__main__":
    raise SystemExit(main())
