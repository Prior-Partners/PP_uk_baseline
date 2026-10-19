"""Browser checks for the restyled catalogue site (development).

Input/output CRS: n/a. Data layer: catalogue site (development check).

Serves a built site on 127.0.0.1 and drives it with Playwright (Chromium):

  * header — the wordmark, "Data catalogue", the kicker with the layer count;
    no Material logo;
  * NIGHT / DAY chips — a click and the keyboard switch the scheme; the active
    chip is cobalt and its input is ticked; the choice survives a reload and an
    instant page change; keyboard focus is visible;
  * search — opens, finds results and closes with Escape, at 1440 and 375 px;
  * menu — each theme row's count equals that theme page's "N layers." line;
    the keyboard opens a theme; the drawer opens at 375 px; an open layer page
    lists "Columns";
  * layer page — the copy button puts exactly the table name on the clipboard,
    also after an instant page change and after Back; the columns header stays
    under the site header while a long table scrolls at 1440 px;
  * no sideways scrolling at 375 px;
  * colours (owner review, 17 October 2026) — in Night and Day, page titles
    are the brand orange; theme rows are orange when closed, hovered, focused,
    open and in the phone drawer; the theme count and search-result titles
    keep their own colours;
  * map pictures (owner review, 19 October 2026) — a layer page shows the
    Night picture in Night and the Day picture in Day, swaps (and loads the
    other) on a chip switch, and draws no frame line.

Usage:
    python scripts/dev/check_browser.py <built site> [--report <json>]

Exit code 0 when every check passes, 1 otherwise.
"""
from __future__ import annotations

import argparse
import functools
import http.server
import json
import re
import sys
import threading
from pathlib import Path
from typing import Any, Callable

from playwright.sync_api import Browser, Page, sync_playwright

LAYER = "HER/her_historicengland_battlefields_may2026/"
OTHER_LAYER_TITLE = "Conservation Areas"
LONG_TABLE = "DEM/dem_geods_oa_age_2021_22/"
COBALT = "rgb(0, 93, 255)"
ORANGE = "rgb(255, 81, 29)"                       # #FF511D, the brand orange
# Per mode: (system colour scheme, theme-row orange, primary text)
MODES = {"Night": ("dark", ORANGE, "rgb(255, 255, 255)"),
         "Day": ("light", "rgb(194, 45, 0)", "rgb(0, 0, 0)")}   # #C22D00 for AA on #FAFAFA
THEME_ROW = ".md-nav--primary > .md-nav__list > .md-nav__item--nested > label.md-nav__link"


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map,
                      ".js": "text/javascript", ".css": "text/css", ".woff2": "font/woff2",
                      ".json": "application/json", ".svg": "image/svg+xml"}

    def log_message(self, format: str, *args: object) -> None:  # noqa: A002 - stdlib signature
        pass


class Checks:
    """Collects named results; a failing assertion is recorded, not raised."""

    def __init__(self) -> None:
        self.results: list[dict[str, Any]] = []

    def run(self, name: str, fn: Callable[[], str | None]) -> None:
        try:
            detail = fn() or ""
            self.results.append({"check": name, "ok": True, "detail": detail})
        except Exception as exc:  # noqa: BLE001 - every failure is reported, then the next check runs
            self.results.append({"check": name, "ok": False, "detail": f"{type(exc).__name__}: {exc}"})


def expect(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def scheme(page: Page) -> str:
    return page.evaluate("document.body.getAttribute('data-md-color-scheme')")


def chip_background(page: Page, scheme_name: str) -> str:
    return page.evaluate(f"getComputedStyle(document.querySelector('.pp-chip--{scheme_name}')).backgroundColor")


def check_header(page: Page, base: str) -> str:
    page.goto(base, wait_until="networkidle")
    name = page.text_content(".pp-wordmark__name").strip()
    sub = page.text_content(".pp-wordmark__sub").strip()
    kick = " ".join(page.text_content(".pp-kick__inner").split())
    layers = re.search(r"(\d+) layers across (\d+) themes", page.text_content("article"))
    expect(name == "UK Baseline", f"wordmark {name!r}")
    expect(sub == "Data catalogue", f"sub-label {sub!r}")
    expect(layers is not None, "home page has no 'N layers across M themes' line")
    expected = f"Prior + Partners · uk_baseline · {layers.group(1)} layers"
    expect(kick == expected, f"kicker {kick!r}, expected {expected!r}")
    expect(not page.is_visible(".md-header__button.md-logo svg"), "Material logo still visible")
    return kick


def check_chips(browser: Browser, base: str) -> str:
    context = browser.new_context(viewport={"width": 1440, "height": 900}, color_scheme="light")
    page = context.new_page()
    page.goto(base, wait_until="networkidle")
    expect(scheme(page) == "default", f"first visit in a light system: {scheme(page)}")
    expect(page.is_checked("#__palette_0"), "DAY input not ticked on load")
    expect(chip_background(page, "default") == COBALT, "DAY chip not cobalt on load")
    page.click(".pp-chip--slate")
    page.wait_for_function("document.body.getAttribute('data-md-color-scheme') === 'slate'")
    expect(page.is_checked("#__palette_1") and not page.is_checked("#__palette_0"), "ticks not in step after click")
    expect(chip_background(page, "slate") == COBALT, "NIGHT chip not cobalt after click")
    page.reload(wait_until="networkidle")
    expect(scheme(page) == "slate", "choice lost after reload")
    page.click('article a:has-text("Administrative & Planning Boundaries")')
    page.wait_for_url("**/ADM/")
    expect(scheme(page) == "slate", "choice lost after an instant page change")
    page.focus("#__palette_1")
    page.keyboard.press("ArrowLeft")
    page.wait_for_function("document.body.getAttribute('data-md-color-scheme') === 'default'")
    outline = page.evaluate("getComputedStyle(document.querySelector('.pp-chip--default')).outlineStyle")
    expect(outline not in ("none", ""), f"no visible focus on the DAY chip ({outline})")
    context.close()
    return "click, keyboard, reload and page change all keep the chosen mode"


def check_search(browser: Browser, base: str, width: int) -> str:
    context = browser.new_context(viewport={"width": width, "height": 900 if width > 500 else 812})
    page = context.new_page()
    page.goto(base, wait_until="networkidle")
    if width < 960:
        page.click('label.md-header__button[for="__search"]')
    page.click(".md-search__input")
    page.keyboard.type("flood", delay=30)
    page.wait_for_selector(".md-search-result__item", timeout=15000)
    hits = page.locator(".md-search-result__item").count()
    page.keyboard.press("Escape")
    page.wait_for_function("!document.getElementById('__search').checked")
    context.close()
    return f"{hits} results for 'flood'; Escape closes"


def check_menu(browser: Browser, base: str, site: Path) -> str:
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    page = context.new_page()
    page.goto(base, wait_until="networkidle")
    rows = page.evaluate("""() => [...document.querySelectorAll('.pp-theme')].map(row => ({
        code: row.querySelector('.pp-theme__code').textContent.trim(),
        count: parseInt(row.parentElement.querySelector('.pp-theme__count').textContent, 10)}))""")
    expect(len(rows) == 12, f"{len(rows)} theme rows, expected 12")
    for row in rows:
        text = (site / row["code"] / "index.html").read_text(encoding="utf-8")
        found = re.search(r"<p>(\d+) layers?\.</p>", text)
        expect(found is not None and int(found.group(1)) == row["count"],
               f"{row['code']}: menu count {row['count']}, theme page {found.group(1) if found else 'none'}")
    label = page.locator(".md-nav--primary > .md-nav__list > .md-nav__item--nested > label.md-nav__link").first
    toggle = label.get_attribute("for")
    before = page.is_checked(f"#{toggle}")
    label.focus()
    page.keyboard.press("Enter")
    page.wait_for_timeout(300)
    expect(page.is_checked(f"#{toggle}") != before, "Enter on a theme row does not open or close it")
    page.goto(base + LAYER, wait_until="networkidle")
    expect(page.locator('.md-nav--primary a.md-nav__link[href$="#columns"]').count() > 0,
           "the open layer page does not list 'Columns'")
    context.close()
    phone = browser.new_context(viewport={"width": 375, "height": 812})
    page = phone.new_page()
    page.goto(base, wait_until="networkidle")
    page.click('label.md-header__button[for="__drawer"]')
    page.wait_for_function("document.getElementById('__drawer').checked")
    box = page.locator(".md-sidebar--primary").bounding_box()
    page.wait_for_timeout(500)                        # the drawer slides in
    box = page.locator(".md-sidebar--primary").bounding_box()
    expect(box is not None and box["x"] >= -1 and abs(box["y"]) <= 1 and box["height"] <= 812 + 1,
           f"drawer not on screen from the top: {box}")
    phone.close()
    return "12 counts match; Enter toggles a theme; drawer opens; Columns listed"


def check_copy(browser: Browser, base: str) -> str:
    context = browser.new_context(viewport={"width": 1440, "height": 900},
                                  permissions=["clipboard-read", "clipboard-write"])
    page = context.new_page()

    def copied(expected: str) -> None:
        page.click(".layer-table .md-clipboard")
        page.wait_for_timeout(300)
        got = page.evaluate("navigator.clipboard.readText()")
        expect(got == expected, f"clipboard {got!r}, expected {expected!r}")

    page.goto(base + LAYER, wait_until="networkidle")
    first = page.get_attribute(".layer-table .md-clipboard", "data-clipboard-text")
    expect(first == page.text_content(".layer-table code").strip(), "button text and chip differ")
    copied(first)
    page.click(f'.md-nav--primary a.md-nav__link:has-text("{OTHER_LAYER_TITLE}")')
    page.wait_for_function(f"!location.pathname.endsWith('/{LAYER}')")
    second = page.get_attribute(".layer-table .md-clipboard", "data-clipboard-text")
    expect(second != first, "the page did not change")
    copied(second)
    page.go_back(wait_until="networkidle")
    page.wait_for_function(f"location.pathname.endsWith('/{LAYER}')")
    copied(first)
    context.close()
    return f"copied {first}, then {second}, then {first} again after Back"


def check_sticky(browser: Browser, base: str) -> str:
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    page = context.new_page()
    page.goto(base + LONG_TABLE, wait_until="networkidle")
    page.evaluate("document.getElementById('columns').scrollIntoView()")
    page.mouse.wheel(0, 1500)
    page.wait_for_timeout(400)
    header_bottom = page.evaluate("document.querySelector('.md-header').getBoundingClientRect().bottom")
    th_top = page.evaluate("document.querySelector('article table th').getBoundingClientRect().top")
    rows_below = page.evaluate("""() => { const t = document.querySelector('article table');
        return t.getBoundingClientRect().bottom > innerHeight; }""")
    expect(rows_below, "table too short to test the sticky header")
    expect(abs(th_top - header_bottom) <= 2, f"column header at {th_top:.0f}px, site header ends at {header_bottom:.0f}px")
    context.close()
    return f"column header held at {th_top:.0f}px under the site header"


def check_no_sideways(browser: Browser, base: str) -> str:
    context = browser.new_context(viewport={"width": 375, "height": 812})
    page = context.new_page()
    wide = []
    for path in ("", "HER/", LAYER, LONG_TABLE):
        page.goto(base + path, wait_until="networkidle")
        if page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth"):
            wide.append(path or "home")
    context.close()
    expect(not wide, f"sideways scroll at 375 px on: {', '.join(wide)}")
    return "home, theme, layer and a long table fit 375 px"


def colour_of(page: Page, selector: str) -> str:
    return page.evaluate("s => getComputedStyle(document.querySelector(s)).color", selector)


def check_colours(browser: Browser, base: str) -> str:
    for mode, (system, row_orange, primary) in MODES.items():
        context = browser.new_context(viewport={"width": 1440, "height": 900}, color_scheme=system)
        page = context.new_page()
        page.goto(base + LAYER, wait_until="networkidle")
        expect(colour_of(page, "article h1") == ORANGE, f"{mode}: layer page title {colour_of(page, 'article h1')}")
        page.goto(base, wait_until="networkidle")
        expect(colour_of(page, "article h1") == ORANGE, f"{mode}: home title {colour_of(page, 'article h1')}")
        row = page.locator(THEME_ROW).first
        toggle = row.get_attribute("for")
        before = page.is_checked(f"#{toggle}")
        for state, act in (("closed", None), ("hovered", row.hover), ("focused", row.focus), ("open", row.click)):
            if act:
                act()
                page.wait_for_timeout(300)                # Material's colour transition
            got = row.evaluate("el => getComputedStyle(el).color")
            expect(got == row_orange, f"{mode}: theme row {state} is {got}, expected {row_orange}")
        expect(page.is_checked(f"#{toggle}") != before, f"{mode}: the click did not open the theme row")
        count = colour_of(page, ".pp-theme__count")
        expect(count != row_orange, f"{mode}: the theme count turned orange")
        page.click(".md-search__input")
        page.keyboard.type("flood", delay=30)
        page.wait_for_selector(".md-search-result__article h1", timeout=15000)
        title = colour_of(page, ".md-search-result__article h1")
        expect(title == primary, f"{mode}: search-result title {title}, expected {primary}")
        context.close()
        phone = browser.new_context(viewport={"width": 375, "height": 812}, color_scheme=system)
        page = phone.new_page()
        page.goto(base, wait_until="networkidle")
        page.click('label.md-header__button[for="__drawer"]')
        page.wait_for_function("document.getElementById('__drawer').checked")
        page.wait_for_timeout(500)                        # the drawer slides in
        got = colour_of(page, THEME_ROW)
        expect(got == row_orange, f"{mode}: drawer theme row {got}, expected {row_orange}")
        phone.close()
    return "titles and theme rows orange in Night and Day (closed, hovered, focused, open, drawer); count and search titles unchanged"


def loaded(page: Page, cls: str) -> None:
    page.wait_for_function(f"(() => {{ const i = document.querySelector('img.{cls}');"
                           f" return i && i.complete && i.naturalWidth > 0; }})()", timeout=15000)


def check_pictures(browser: Browser, base: str) -> str:
    for mode, (system, _, _) in MODES.items():
        want, other = (("layer-map--night", "layer-map--day") if mode == "Night"
                       else ("layer-map--day", "layer-map--night"))
        context = browser.new_context(viewport={"width": 1440, "height": 900}, color_scheme=system)
        page = context.new_page()
        fetched: list[str] = []
        page.on("request", lambda request: fetched.append(request.url) if "/maps/" in request.url else None)
        page.goto(base + LAYER, wait_until="networkidle")
        state = page.evaluate("""() => [...document.querySelectorAll('img.layer-map')].map(i => ({
            cls: i.className, shown: getComputedStyle(i).display !== 'none',
            border: getComputedStyle(i).borderTopWidth}))""")
        expect(len(state) == 2, f"{mode}: {len(state)} map pictures, expected Day and Night")
        expect(shown_pictures(page) == [f"layer-map {want}"], f"{mode}: shown {shown_pictures(page)}, expected {want}")
        expect(all(s["border"] == "0px" for s in state), f"{mode}: a frame line is still drawn")
        page.locator(f"img.{want}").scroll_into_view_if_needed()
        loaded(page, want)
        hidden = page.evaluate(f"document.querySelector('img.{other}').src")
        expect(hidden not in fetched, f"{mode}: the hidden picture was downloaded before switching")
        page.click(".pp-chip--default" if mode == "Night" else ".pp-chip--slate")
        page.wait_for_function("document.body.getAttribute('data-md-color-scheme') === "
                               f"'{'default' if mode == 'Night' else 'slate'}'")
        loaded(page, other)                           # the other picture appears and loads on the switch
        expect(shown_pictures(page) == [f"layer-map {other}"],
               f"{mode}: after switching, shown {shown_pictures(page)}, expected only {other}")
        expect(hidden in fetched, f"{mode}: the other picture was not fetched after switching")
        context.close()
    return ("Night shows only the Night picture, Day only the Day one; the hidden one is not downloaded "
            "until a chip switch, which shows and loads it; no frame line")


def shown_pictures(page: Page) -> list[str]:
    return page.evaluate("[...document.querySelectorAll('img.layer-map')]"
                         ".filter(i => getComputedStyle(i).display !== 'none').map(i => i.className)")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("site", type=Path, help="built site folder (mkdocs build output)")
    p.add_argument("--report", type=Path, help="write the results as JSON")
    p.add_argument("--only", help="comma-separated subset: header, chips, search, menu, copy, sticky, sideways, "
                                  "colours, pictures")
    args = p.parse_args(argv)
    wanted = {name.strip() for name in args.only.split(",")} if args.only else None
    site = args.site.resolve()
    handler = functools.partial(QuietHandler, directory=str(site))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{server.server_address[1]}/"
    checks = Checks()
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            page = browser.new_page(viewport={"width": 1440, "height": 900})
            plan: list[tuple[str, str, Callable[[], str | None]]] = [
                ("header", "header", lambda: check_header(page, base)),
                ("chips", "chips", lambda: check_chips(browser, base)),
                ("search", "search 1440", lambda: check_search(browser, base, 1440)),
                ("search", "search 375", lambda: check_search(browser, base, 375)),
                ("menu", "menu", lambda: check_menu(browser, base, site)),
                ("copy", "copy", lambda: check_copy(browser, base)),
                ("sticky", "sticky header", lambda: check_sticky(browser, base)),
                ("sideways", "no sideways scroll", lambda: check_no_sideways(browser, base)),
                ("colours", "colours", lambda: check_colours(browser, base)),
                ("pictures", "map pictures", lambda: check_pictures(browser, base)),
            ]
            for key, name, fn in plan:
                if wanted is None or key in wanted:
                    checks.run(name, fn)
            browser.close()
    finally:
        server.shutdown()
    for result in checks.results:
        print(f"{'PASS' if result['ok'] else 'FAIL'} {result['check']}: {result['detail']}")
    if args.report:
        args.report.write_text(json.dumps(checks.results, indent=2), encoding="utf-8")
    return 0 if all(r["ok"] for r in checks.results) else 1


if __name__ == "__main__":
    sys.exit(main())
