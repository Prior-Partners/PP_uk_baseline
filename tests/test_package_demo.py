"""Tests for scripts/dev/package_demo.py and scripts/dev/serve_demo.py.

Input/output CRS: n/a (built site files only). Data layer: catalogue local demo (tests).

Packaging refuses folders that overlap the source site and leaves them untouched;
a normal package holds the site and the launcher. The demo server opens the
browser at the address it actually bound, including the fallback port.
"""
from __future__ import annotations

import importlib.util
import socket
import sys
import time
from pathlib import Path
from types import ModuleType

import pytest

REPO = Path(__file__).resolve().parents[1]
DEV = REPO / "scripts" / "dev"


def load(name: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(f"{name}_under_test", DEV / f"{name}.py")
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[f"{name}_under_test"] = mod
    spec.loader.exec_module(mod)
    return mod


def built_site(folder: Path) -> Path:
    (folder / "search").mkdir(parents=True)
    (folder / "index.html").write_text("<p>home</p>", encoding="utf-8")
    (folder / "search" / "search_index.json").write_text('{"config": {}, "docs": []}', encoding="utf-8")
    return folder


def test_packaging_a_site(tmp_path: Path) -> None:
    site = built_site(tmp_path / "build")
    demo = tmp_path / "demo"
    load("package_demo").main([str(site), str(demo)])
    for name in ("site/index.html", "serve_demo.py", "start_demo.bat", "README.txt"):
        assert (demo / name).is_file(), name


@pytest.mark.parametrize("layout", ["site inside demo", "demo inside site", "same folder"])
def test_overlapping_folders_are_refused_and_left_alone(tmp_path: Path, layout: str) -> None:
    if layout == "site inside demo":
        demo = tmp_path / "demo"
        site = built_site(demo / "site")
    elif layout == "demo inside site":
        site = built_site(tmp_path / "build")
        demo = site / "demo"
    else:
        site = built_site(tmp_path / "build")
        demo = site
    before = sorted(p.relative_to(tmp_path).as_posix() for p in tmp_path.rglob("*"))
    with pytest.raises(SystemExit, match="overlap"):
        load("package_demo").main([str(site), str(demo)])
    after = sorted(p.relative_to(tmp_path).as_posix() for p in tmp_path.rglob("*"))
    assert after == before
    assert (site / "index.html").is_file()


def test_browser_opens_the_bound_address_also_on_the_fallback_port(tmp_path: Path,
                                                                    monkeypatch: pytest.MonkeyPatch) -> None:
    serve = load("serve_demo")
    site = built_site(tmp_path / "site")
    monkeypatch.setattr(serve, "SITE", site)
    monkeypatch.delenv("DEMO_NO_BROWSER", raising=False)
    opened: list[str] = []
    monkeypatch.setattr(serve.webbrowser, "open", lambda url: opened.append(url) or True)
    # Serve for a moment only: long enough for the browser timer (0.6 s) to fire.
    monkeypatch.setattr(serve.DemoServer, "serve_forever", lambda self, *a, **k: time.sleep(1.2))
    holder = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        holder.bind(("127.0.0.1", serve.FIRST_PORT))
    except OSError:
        holder.close()
        pytest.skip(f"port {serve.FIRST_PORT} is already in use on this machine")
    holder.listen()
    try:
        assert serve.main([]) == 0
    finally:
        holder.close()
    assert len(opened) == 1
    port = int(opened[0].rsplit(":", 1)[1].strip("/"))
    assert opened[0] == f"http://localhost:{port}/"
    assert serve.FIRST_PORT < port <= serve.LAST_PORT
