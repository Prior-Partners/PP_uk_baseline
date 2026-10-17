"""Tests for the --live part of scripts/dev/check_contrast.py.

Input/output CRS: n/a (built site files only). Data layer: catalogue development checks (tests).

Runs the browser sampler on tiny synthetic sites. Skipped when Playwright or its
Chromium is not installed.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType

import pytest

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "dev" / "check_contrast.py"


def load() -> ModuleType:
    spec = importlib.util.spec_from_file_location("check_contrast_live_under_test", SCRIPT)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules["check_contrast_live_under_test"] = mod
    spec.loader.exec_module(mod)
    return mod


def run_live(site: Path) -> tuple[int, list[dict]]:
    pytest.importorskip("playwright.sync_api")
    try:
        return load().check_live(site, pages=("",))
    except Exception as exc:  # noqa: BLE001 - only a missing browser turns into a skip
        if "Executable doesn't exist" in str(exc):
            pytest.skip("Playwright's Chromium is not installed")
        raise


def test_live_sampler_passes_readable_text(tmp_path: Path) -> None:
    (tmp_path / "index.html").write_text(
        "<!doctype html><html><body style='background:#fafafa'>"
        "<p style='color:#5f5f5f'>Readable secondary text</p>"
        "<input placeholder='Search' style='color:#000'>"
        "</body></html>", encoding="utf-8")
    sampled, failures = run_live(tmp_path)
    assert sampled >= 2
    assert failures == []


def test_opacity_and_near_misses_are_reported(tmp_path: Path) -> None:
    (tmp_path / "index.html").write_text(
        "<!doctype html><html><body style='background:#ffffff'>"
        "<p style='color:#000;opacity:.5'>Faded itself</p>"
        "<div style='opacity:.5'><p style='color:#000'>Faded by its parent</p></div>"
        "<div style='background:#dadada'><p style='color:#606060'>Just under 4.5</p></div>"
        "<p style='color:#000;opacity:0'>Invisible</p>"
        "<p style='color:#000'>Plain black</p>"
        "</body></html>", encoding="utf-8")
    sampled, failures = run_live(tmp_path)
    texts = {failure["text"] for failure in failures}
    assert {"Faded itself", "Faded by its parent", "Just under 4.5"} <= texts
    assert "Invisible" not in texts and "Plain black" not in texts
    near = next(failure for failure in failures if failure["text"] == "Just under 4.5")
    assert near["ratio"] == 4.5          # 4.498:1 — shown rounded, failed on the exact value
    # 4 visible texts in each of the views; fully transparent text is not sampled.
    assert sampled == 4 * len(load().LIVE_VIEWS)


def test_live_sampler_reports_faint_text(tmp_path: Path) -> None:
    (tmp_path / "index.html").write_text(
        "<!doctype html><html><body style='background:#fafafa'>"
        "<p style='color:#8a8a8a'>Too faint</p>"
        "<h1 style='color:#8a8a8a;font-size:30px'>Large text passes at 3:1</h1>"
        "</body></html>", encoding="utf-8")
    sampled, failures = run_live(tmp_path)
    texts = [failure["text"] for failure in failures]
    assert "Too faint" in texts
    assert all("Large text" not in text for text in texts)
    assert sampled >= 2
