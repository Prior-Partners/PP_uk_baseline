"""Tests for scripts/assets/extra.css — the board tokens match the approved palette.

Input/output CRS: n/a (stylesheet only). Data layer: catalogue site skin (tests).

The stylesheet's --pp3-* tokens for Day and Night must equal the approved
values, and every colour the contrast table checks must be a colour the
stylesheet declares, so the contrast check measures the palette that ships.
"""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path
from types import ModuleType

import pytest

REPO = Path(__file__).resolve().parents[1]
CSS = (REPO / "scripts" / "assets" / "extra.css").read_text(encoding="utf-8")

# The approved palette: the board's tokens, Day background #FAFAFA, and the
# owner's AA adjustments of 16 October 2026 (Day secondary text, Night links),
# and the orange theme rows of 17 October 2026 (darker in Day for AA).
APPROVED = {
    r"body": {
        "--pp3-accent": "#005DFF", "--pp3-hover": "#d6e4ff", "--pp3-orange": "#FF511D",
        "--pp3-bar": "#d9d9d9", "--pp3-onbar": "#121212", "--pp3-strip": "#121212",
    },
    r'\[data-md-color-scheme="default"\]': {
        "--pp3-bg": "hsl(0, 0%, 98%)", "--pp3-primary": "#000", "--pp3-type": "#5f5f5f",
        "--pp3-muted": "#5f5f5f", "--pp3-mark": "#8a8a8a", "--pp3-line": "rgba(0, 0, 0, .28)",
        "--pp3-link": "#005DFF", "--pp-orange-label": "#C22D00",
    },
    r'\[data-md-color-scheme="slate"\]': {
        "--pp3-bg": "hsl(0, 0%, 4%)", "--pp3-primary": "#fff", "--pp3-type": "#c8c8c8",
        "--pp3-muted": "#9a9a9a", "--pp3-mark": "#9a9a9a", "--pp3-line": "rgba(255, 255, 255, .22)",
        "--pp3-link": "#d6e4ff", "--pp-orange-label": "#FF511D",
    },
}
COLOUR = re.compile(r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?\b|hsl\([^)]*\)|rgba\([^)]*\)")


def load_contrast() -> ModuleType:
    path = REPO / "scripts" / "dev" / "check_contrast.py"
    spec = importlib.util.spec_from_file_location("check_contrast_for_css_test", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules["check_contrast_for_css_test"] = mod
    spec.loader.exec_module(mod)
    return mod


def rgb8(contrast: ModuleType, value: str) -> tuple[int, int, int, float]:
    """A colour as the browser stores it: 8-bit channels (hsl 98% = #FAFAFA)."""
    r, g, b, a = contrast.parse_colour(value)
    return round(r * 255), round(g * 255), round(b * 255), round(a, 3)


def tokens(selector: str) -> dict[str, str]:
    """The --pp3-* and --pp-* declarations of the first rule whose selector is exactly ``selector``."""
    found = re.search(r"(?m)^" + selector + r"\s*\{([^}]*)\}", CSS)
    assert found, f"no rule for {selector}"
    return {name: value.strip() for name, value in
            re.findall(r"(--pp3?-[a-z-]+)\s*:\s*([^;]+);", found.group(1))}


@pytest.mark.parametrize("selector", list(APPROVED))
def test_tokens_equal_the_approved_palette(selector: str) -> None:
    contrast = load_contrast()
    declared = tokens(selector)
    for name, value in APPROVED[selector].items():
        assert name in declared, f"{name} missing in {selector}"
        assert rgb8(contrast, declared[name]) == rgb8(contrast, value), \
            f"{selector} {name}: {declared[name]} instead of {value}"


def test_contrast_table_checks_colours_the_stylesheet_declares() -> None:
    contrast = load_contrast()
    declared = {rgb8(contrast, c) for c in COLOUR.findall(CSS)}
    for pair in contrast.TOKEN_PAIRS:
        for key in ("fg", "bg"):
            assert rgb8(contrast, pair[key]) in declared, \
                f"{pair['mode']} / {pair['name']}: {pair[key]} is not declared in extra.css"


def test_font_stacks_are_gt_america_with_arial_only() -> None:
    stacks = re.findall(r"--pp3-(?:mono|sans)\s*:\s*([^;]+);", CSS)
    assert stacks == ['"GT America Mono", Arial, sans-serif', '"GT America", Arial, sans-serif']
    for banned in ("Segoe", "Consolas", "SFMono", "Helvetica", "-apple-system", "ui-monospace", "Roboto"):
        assert banned not in CSS, f"{banned} found in extra.css"


def test_theme_colour_squares_are_gone() -> None:
    assert ".md-nav__item:nth-child" not in CSS
    assert "--pp-theme" not in CSS
