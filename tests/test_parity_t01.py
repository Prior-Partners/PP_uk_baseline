"""Tests for scripts/dev/parity_t01.py — strict comparison and the drift check.

Input/output CRS: n/a (metadata only). Data layer: catalogue generation (tests).

Synthetic trees only; the drift test commits them to a throwaway git repository
in pytest's temporary folder.
"""
from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path
from types import ModuleType

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "dev" / "parity_t01.py"


def load_parity() -> ModuleType:
    spec = importlib.util.spec_from_file_location("parity_t01_under_test", SCRIPT)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules["parity_t01_under_test"] = mod
    spec.loader.exec_module(mod)
    return mod


def render() -> dict[str, bytes]:
    """A small render as the generator writes it on Windows (CRLF text)."""
    return {
        "docs/index.md": b"# Home\r\n\r\nText.\r\n",
        "docs/stylesheets/extra.css": b"body{margin:0}\r\n",
        "docs/fonts/a.woff2": b"\x00\x01binary\r\n",
        "mkdocs.yml": b"site_name: x\r\n",
    }


def test_identical_trees_pass() -> None:
    p = load_parity()
    assert p.is_identical(p.compare(render(), render()))


def test_line_endings_alone_fail_the_strict_comparison() -> None:
    p = load_parity()
    other = render()
    other["docs/index.md"] = other["docs/index.md"].replace(b"\r\n", b"\n")
    result = p.compare(render(), other)
    assert result[3] == ["docs/index.md"]
    assert not p.is_identical(result)


def test_missing_font_or_stylesheet_fails() -> None:
    p = load_parity()
    for missing in ("docs/fonts/a.woff2", "docs/stylesheets/extra.css"):
        other = render()
        del other[missing]
        result = p.compare(render(), other)
        assert result[0] == [missing]
        assert not p.is_identical(result)


def _commit(repo: Path, files: dict[str, bytes]) -> str:
    subprocess.run(["git", "init", "-q", str(repo)], check=True)
    for name, data in files.items():
        path = repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    git = ["git", "-C", str(repo), "-c", "user.name=test", "-c", "user.email=test@example.invalid",
           "-c", "core.autocrlf=false"]
    subprocess.run(git + ["add", "-A"], check=True)
    subprocess.run(git + ["commit", "-q", "-m", "baseline"], check=True)
    return subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"], check=True,
                          capture_output=True, text=True).stdout.strip()


def committed_baseline() -> dict[str, bytes]:
    """The same content as ``render()``, stored as git stores text: LF."""
    files = {k: (v.replace(b"\r\n", b"\n") if not k.endswith(".woff2") else v)
             for k, v in render().items()}
    files["docs/PP_Staff_Data_Management_Handbook.pdf"] = b"%PDF-1.4"
    return files


def test_drift_check_passes_on_the_same_content(tmp_path: Path) -> None:
    p = load_parity()
    rev = _commit(tmp_path / "repo", committed_baseline())
    committed = p.committed_tree(tmp_path / "repo", rev)
    assert set(committed) == set(committed_baseline())
    assert p.is_identical(p.drift_check(render(), committed))


def test_drift_check_fails_on_changed_text_stale_page_or_binary(tmp_path: Path) -> None:
    p = load_parity()
    base = committed_baseline()
    base["docs/ADM/old_layer.md"] = b"# Old\n"          # a page the render no longer writes
    rev = _commit(tmp_path / "repo", base)
    committed = p.committed_tree(tmp_path / "repo", rev)

    stale = p.drift_check(render(), committed)
    assert stale[1] == ["docs/ADM/old_layer.md"]
    assert not p.is_identical(stale)

    changed = render()
    changed["docs/index.md"] = b"# Home\r\n\r\nOther text.\r\n"
    changed["docs/fonts/a.woff2"] = b"\x00\x01binary\n"     # a binary is never folded
    result = p.drift_check(changed, {k: v for k, v in committed.items() if k != "docs/ADM/old_layer.md"})
    assert result[2] == ["docs/fonts/a.woff2", "docs/index.md"]
    assert not p.is_identical(result)


def test_only_the_handbook_is_exempt(tmp_path: Path) -> None:
    p = load_parity()
    base = committed_baseline()
    base["docs/other.pdf"] = b"%PDF-1.4"
    rev = _commit(tmp_path / "repo", base)
    result = p.drift_check(render(), p.committed_tree(tmp_path / "repo", rev))
    assert result[1] == ["docs/other.pdf"]
