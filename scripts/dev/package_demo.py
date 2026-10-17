"""Package a built catalogue site as a local demo folder (development).

Input/output CRS: n/a. Data layer: catalogue site (local demo).

Copies, into a demo folder outside the repository:
  * the built site (``site/``, maps included),
  * ``serve_demo.py`` and ``start_demo.bat`` from this folder,
  * the contact sheet and its screenshots, when given,
so the demo keeps working after the repository goes back to ``main``.

Usage:
    python scripts/dev/package_demo.py <built site> <demo folder> [--shots <folder>]
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]

README = """UK Baseline data catalogue - local demo
========================================

Double-click start_demo.bat. It serves the site on http://localhost:8010/
(or the next free port) and opens your browser. Close its window to stop.

contact_sheet.png - Night and Day at 1440 px and 375 px: the home page, a theme
page, a layer page and search. The full screenshots are in screens\\.

Needs Python 3 (already on this computer). Nothing here is published.
"""


def looks_like_site(folder: Path) -> bool:
    """A folder MkDocs built: an index page and a search index."""
    return (folder / "index.html").is_file() and (folder / "search" / "search_index.json").is_file()


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("site", type=Path, help="built site folder (mkdocs build output)")
    p.add_argument("demo", type=Path, help="demo folder, outside the repository")
    p.add_argument("--shots", type=Path, help="folder holding contact_sheet.png and screens/")
    args = p.parse_args(argv)

    site, demo = args.site.resolve(), args.demo.resolve()
    target = demo / "site"
    if not looks_like_site(site):
        raise SystemExit(f"{site} is not a built site (no index.html or search index)")
    if demo == REPO or REPO in demo.parents:
        raise SystemExit(f"refusing to package inside the repository: {demo}")
    # Checked before anything is written or removed: the copy must never delete
    # or nest inside its own source.
    for folder in (demo, target):
        if folder == site or site in folder.parents or folder in site.parents:
            raise SystemExit(f"refusing to package: the site {site} and the demo {demo} overlap")
    demo.mkdir(parents=True, exist_ok=True)

    if target.exists():
        if not looks_like_site(target):
            raise SystemExit(f"refusing to replace {target}: it is not a built site")
        shutil.rmtree(target)
    shutil.copytree(site, target)
    for name in ("serve_demo.py", "start_demo.bat"):
        shutil.copy2(HERE / name, demo / name)
    (demo / "README.txt").write_text(README, encoding="utf-8")

    if args.shots:
        shutil.copy2(args.shots / "contact_sheet.png", demo / "contact_sheet.png")
        screens = demo / "screens"
        if screens.exists():
            shutil.rmtree(screens)
        shutil.copytree(args.shots / "screens", screens)

    pages = sum(1 for _ in target.rglob("*.html"))
    maps = sum(1 for _ in (target / "maps").glob("*.png")) if (target / "maps").is_dir() else 0
    print(f"Demo ready in {demo}: {pages} pages, {maps} maps")
    return 0


if __name__ == "__main__":
    sys.exit(main())
