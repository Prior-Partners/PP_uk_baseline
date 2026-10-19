"""Tests for scripts/build_catalogue.py — site-only safety, snapshots and paths.

Input/output CRS: n/a (metadata only). Data layer: catalogue generation (tests).

No test touches the database or the share: every reader and writer that could
is replaced with a stand-in, and every output goes to a temporary folder.
"""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from types import ModuleType
from typing import Any

import pytest

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_catalogue.py"


def load_module(name: str = "build_catalogue_under_test") -> ModuleType:
    """Import a fresh copy of the generator from its file."""
    spec = importlib.util.spec_from_file_location(name, SCRIPT)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def make_records() -> list[dict[str, Any]]:
    """Two small layers in two themes, shaped like ``read_metadata()`` output."""
    return [
        {
            "theme": "ADM",
            "table": "adm_test_boundary_2026",
            "raw_comment": "Test boundary 2026. Second sentence.\nSHORT NAME\n- Test boundary\nSOURCE\n- Test org.",
            "description": "Test boundary 2026. Second sentence.",
            "sections": {"SHORT NAME": "- Test boundary", "SOURCE": "- Test org."},
            "columns": [
                {"name": "fid", "type": "integer", "comment": "Primary key."},
                {"name": "geom", "type": "geometry(MultiPolygon,27700)", "comment": None},
            ],
        },
        {
            "theme": "HER",
            "table": "her_test_sites_2026",
            "raw_comment": "Test sites 2026.\nLICENCE\n- OGL v3.0",
            "description": "Test sites 2026.",
            "sections": {"LICENCE": "- OGL v3.0"},
            "columns": [{"name": "name", "type": "text", "comment": "Site name | with a pipe."}],
        },
    ]


@pytest.fixture()
def gen(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> ModuleType:
    """The generator with its database, register and styles readers stubbed."""
    mod = load_module()
    monkeypatch.setattr(mod, "read_metadata", lambda: make_records())
    monkeypatch.setattr(mod, "read_short_names", lambda: {"her_test_sites_2026": "Test sites"})
    monkeypatch.setattr(mod, "_approved_themes", lambda: {"ADM"})
    monkeypatch.setattr(mod, "SHARE", tmp_path / "share")
    return mod


def tree(root: Path) -> dict[str, bytes]:
    """Relative path -> bytes for docs/ and mkdocs.yml under ``root``."""
    out = {p.relative_to(root).as_posix(): p.read_bytes()
           for p in (root / "docs").rglob("*") if p.is_file()}
    out["mkdocs.yml"] = (root / "mkdocs.yml").read_bytes()
    return out


def test_paths_resolve_to_the_repository() -> None:
    mod = load_module()
    assert mod.REPO == REPO
    assert mod.OUT == REPO
    assert mod.DOCS == REPO / "docs"
    assert mod.MAPS_DIR == REPO / "docs" / "maps"
    assert mod.ASSETS == REPO / "scripts" / "assets"
    assert (mod.ASSETS / "extra.css").is_file()
    assert len(list((mod.ASSETS / "fonts").glob("*.woff2"))) == 4


def test_import_reads_nothing_on_the_share(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    styles = tmp_path / "styles.json"
    styles.write_text(json.dumps({"_approved": ["ADM"]}), encoding="utf-8")
    monkeypatch.setenv("UK_BASELINE_STYLES", str(styles))
    mod = load_module("build_catalogue_import_check")
    # Read at import time, the styles file would have filled APPROVED.
    assert mod.APPROVED == set()
    assert mod.MAP_TABLES is None


def test_site_only_never_touches_the_share(gen: ModuleType, monkeypatch: pytest.MonkeyPatch,
                                           tmp_path: Path) -> None:
    calls: list[str] = []
    monkeypatch.setattr(gen, "render_xlsx", lambda *a: calls.append("xlsx"))
    monkeypatch.setattr(gen, "render_html", lambda *a: calls.append("html"))
    out = tmp_path / "out"
    out.mkdir()
    stale = out / "uk_baseline_catalogue.xlsx"
    stale.write_text("old local copy", encoding="utf-8")

    gen.main(["--site-only", "--out-dir", str(out), "--maps-dir", str(tmp_path / "maps")])

    assert calls == []
    assert not (tmp_path / "share").exists()
    assert stale.exists()                      # site-only deletes nothing outside docs/
    assert (out / "docs" / "index.md").is_file()
    assert (out / "mkdocs.yml").is_file()
    assert (out / ".catalogue_fingerprint.json").is_file()


def test_full_mode_still_writes_both_share_files(gen: ModuleType, monkeypatch: pytest.MonkeyPatch,
                                                 tmp_path: Path) -> None:
    written: list[Path] = []
    monkeypatch.setattr(gen, "render_xlsx", lambda records, built, path: written.append(path))
    monkeypatch.setattr(gen, "render_html", lambda records, built, path: written.append(path))
    out = tmp_path / "out"
    out.mkdir()
    stale = out / "uk_baseline_catalogue.html"
    stale.write_text("old local copy", encoding="utf-8")

    gen.main(["--out-dir", str(out), "--maps-dir", str(tmp_path / "maps")])

    share = tmp_path / "share"
    assert written == [share / "uk_baseline_catalogue.xlsx", share / "uk_baseline_catalogue.html"]
    assert share.is_dir()
    assert not stale.exists()                  # full mode removes the old local copies, as before
    assert (out / "docs" / "index.md").is_file()


def test_snapshot_replay_renders_the_same_site(gen: ModuleType, monkeypatch: pytest.MonkeyPatch,
                                               tmp_path: Path) -> None:
    maps = tmp_path / "maps"
    maps.mkdir()
    (maps / "adm_test_boundary_2026.png").write_bytes(b"png")
    snap = tmp_path / "snap.json"
    first = tmp_path / "first"
    gen.main(["--site-only", "--out-dir", str(first), "--maps-dir", str(maps),
              "--save-snapshot", str(snap), "--built", "15 October 2026"])

    data = json.loads(snap.read_text(encoding="utf-8"))
    assert data["built"] == "15 October 2026"
    assert data["approved"] == ["ADM"]
    assert data["maps"] == ["adm_test_boundary_2026"]
    assert [r["short_name"] for r in data["records"]] == ["Test boundary", "Test sites"]

    # A fresh module that cannot reach the database, register or styles file,
    # and whose maps folder is empty: the snapshot alone must drive the render.
    replay = load_module("build_catalogue_replay")

    def unreachable(*_a: object) -> None:
        raise AssertionError("a replay must not read the database, register or styles file")

    monkeypatch.setattr(replay, "read_metadata", unreachable)
    monkeypatch.setattr(replay, "read_short_names", unreachable)
    monkeypatch.setattr(replay, "_approved_themes", unreachable)
    empty = tmp_path / "no_maps"
    empty.mkdir()
    second = tmp_path / "second"
    replay.main(["--from-snapshot", str(snap), "--site-only", "--out-dir", str(second),
                 "--maps-dir", str(empty)])

    assert tree(first) == tree(second)
    layer = (second / "docs" / "ADM" / "adm_test_boundary_2026.md").read_text(encoding="utf-8")
    assert "../../maps/adm_test_boundary_2026.png" in layer
    assert "last updated 15 October 2026" in (second / "mkdocs.yml").read_text(encoding="utf-8")


def test_night_picture_is_paired_with_the_day_picture(gen: ModuleType, tmp_path: Path) -> None:
    maps = tmp_path / "maps"
    (maps / "night").mkdir(parents=True)
    (maps / "adm_test_boundary_2026.png").write_bytes(b"png")
    out = tmp_path / "out"
    gen.main(["--site-only", "--out-dir", str(out), "--maps-dir", str(maps)])
    single = (out / "docs" / "ADM" / "adm_test_boundary_2026.md").read_text(encoding="utf-8")
    assert 'class="layer-map">' in single and "maps/night/" not in single

    (maps / "night" / "adm_test_boundary_2026.png").write_bytes(b"png")
    gen.main(["--site-only", "--out-dir", str(out), "--maps-dir", str(maps)])
    paired = (out / "docs" / "ADM" / "adm_test_boundary_2026.md").read_text(encoding="utf-8")
    day = '<img src="../../maps/adm_test_boundary_2026.png"'
    night = '<img src="../../maps/night/adm_test_boundary_2026.png"'
    assert day in paired and night in paired
    line = next(text for text in paired.splitlines() if day in text)
    assert night in line                       # one paragraph: no change to the search text
    assert line.index(day) < line.index(night)
    assert 'class="layer-map layer-map--day"' in line and 'class="layer-map layer-map--night"' in line


def test_resaving_a_replay_keeps_its_map_list(gen: ModuleType, tmp_path: Path) -> None:
    maps = tmp_path / "maps"
    maps.mkdir()
    (maps / "adm_test_boundary_2026.png").write_bytes(b"png")
    first_snap = tmp_path / "first.json"
    gen.main(["--site-only", "--out-dir", str(tmp_path / "capture"), "--maps-dir", str(maps),
              "--save-snapshot", str(first_snap)])

    # Replay on a machine without the PNGs and save the inputs again.
    empty = tmp_path / "no_maps"
    empty.mkdir()
    second_snap = tmp_path / "second.json"
    replay = load_module("build_catalogue_resave")
    replay.main(["--from-snapshot", str(first_snap), "--site-only", "--out-dir", str(tmp_path / "one"),
                 "--maps-dir", str(empty), "--save-snapshot", str(second_snap)])
    first = json.loads(first_snap.read_text(encoding="utf-8"))
    second = json.loads(second_snap.read_text(encoding="utf-8"))
    assert second["maps"] == first["maps"] == ["adm_test_boundary_2026"]

    again = load_module("build_catalogue_resave_again")
    again.main(["--from-snapshot", str(second_snap), "--site-only", "--out-dir", str(tmp_path / "two"),
                "--maps-dir", str(empty)])
    assert tree(tmp_path / "one") == tree(tmp_path / "two")


def test_a_fresh_output_folder_builds_on_its_own(gen: ModuleType, tmp_path: Path) -> None:
    out = tmp_path / "fresh"
    gen.main(["--site-only", "--out-dir", str(out), "--maps-dir", str(tmp_path / "maps")])
    for name in ("header.html", "palette.html", "logo.html", "nav-item.html"):
        assert (out / "overrides" / "partials" / name).is_file(), f"overrides/partials/{name} not copied"
    # The home page links the handbook PDF, which lives in the real docs/ only.
    (out / "docs" / "PP_Staff_Data_Management_Handbook.pdf").write_bytes(b"%PDF-1.4")
    built = subprocess.run([sys.executable, "-m", "mkdocs", "build", "--strict", "--quiet",
                            "-f", str(out / "mkdocs.yml"), "-d", str(tmp_path / "site")],
                           capture_output=True, text=True)
    assert built.returncode == 0, built.stdout + built.stderr
    assert (tmp_path / "site" / "index.html").is_file()


def test_a_build_inside_the_repository_does_not_copy_overrides(gen: ModuleType,
                                                               monkeypatch: pytest.MonkeyPatch,
                                                               tmp_path: Path) -> None:
    # A stand-in repository, so nothing touches the real docs/ or mkdocs.yml.
    fake_repo = tmp_path / "repo"
    (fake_repo / "overrides" / "partials").mkdir(parents=True)
    (fake_repo / "overrides" / "partials" / "header.html").write_text("x", encoding="utf-8")
    calls: list[tuple[Path, Path]] = []
    monkeypatch.setattr(gen.shutil, "copytree", lambda src, dst, **_k: calls.append((src, dst)))
    monkeypatch.setattr(gen, "REPO", fake_repo)
    monkeypatch.setattr(gen, "OUT", fake_repo)
    monkeypatch.setattr(gen, "DOCS", fake_repo / "docs")
    gen.render_mkdocs(make_records(), "15 October 2026")
    assert calls == []
    assert (fake_repo / "mkdocs.yml").is_file()


def test_load_snapshot_rejects_other_files(tmp_path: Path) -> None:
    mod = load_module()
    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps({"records": []}), encoding="utf-8")
    with pytest.raises(ValueError):
        mod.load_snapshot(bad)


def test_database_session_is_read_only(monkeypatch: pytest.MonkeyPatch) -> None:
    mod = load_module()
    events: list[Any] = []

    class FakeCursor:
        def __enter__(self) -> "FakeCursor":
            return self

        def __exit__(self, *_a: object) -> bool:
            return False

        def execute(self, *_a: object, **_k: object) -> None:
            events.append("execute")

        def fetchall(self) -> list[Any]:
            return []

    class FakeConnection:
        def __enter__(self) -> "FakeConnection":
            return self

        def __exit__(self, *_a: object) -> bool:
            return False

        def __setattr__(self, key: str, value: object) -> None:
            events.append((key, value))
            object.__setattr__(self, key, value)

        def cursor(self) -> FakeCursor:
            events.append("cursor")
            return FakeCursor()

    monkeypatch.setattr(mod, "conninfo", lambda: "dbname=test")
    monkeypatch.setattr(mod.psycopg, "connect", lambda *_a, **_k: FakeConnection())
    assert mod.read_metadata() == []
    assert events[0] == ("read_only", True)
    assert events.index("cursor") > 0
