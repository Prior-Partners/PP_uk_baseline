"""WCAG reference values, parsing, compositing and token threshold tests.

Input/output CRS: n/a (colour tokens only).
Data layer: catalogue development checks (tests).
"""

import importlib.util
from pathlib import Path
import subprocess
import sys

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "dev" / "check_contrast.py"
SPEC = importlib.util.spec_from_file_location("check_contrast", SCRIPT)
assert SPEC and SPEC.loader
contrast = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(contrast)


@pytest.mark.parametrize("fg,bg,expected", [
    ("#000", "#fff", 21.0),
    ("#5f5f5f", "#FAFAFA", 6.12),
    ("#8a8a8a", "#FAFAFA", 3.31),
    ("#005DFF", "hsl(0,0%,4%)", 3.78),
    ("#FF511D", "#121212", 5.75),
])
def test_known_ratios(fg, bg, expected):
    assert contrast.ratio(fg, bg) == pytest.approx(expected, abs=0.005)


def test_opaque_ratio_is_symmetric():
    assert contrast.ratio("#123", "#fed") == pytest.approx(contrast.ratio("#fed", "#123"))
    assert contrast.ratio("#123", "#123") == 1


@pytest.mark.parametrize("short,long", [("#abc", "#aabbcc"), ("#FFF", "#ffffff"),
                                       ("hsl(120,100%,50%)", "#00ff00"),
                                       ("hsl(-120,100%,50%)", "#0000ff"),
                                       ("hsl(480, 100%, 50%)", "#00ff00"),
                                       ("rgba(255,0,0,1)", "#ff0000")])
def test_equivalent_colour_formats(short, long):
    assert contrast.ratio(short, "#fff") == pytest.approx(contrast.ratio(long, "#fff"))


def test_alpha_composites_in_srgb_before_linearisation():
    assert contrast.ratio("rgba(0,0,0,0)", "#fff") == 1
    assert contrast.ratio("rgba(0,0,0,1)", "#fff") == 21
    assert contrast.ratio("rgba(0,0,0,.5)", "#fff") == pytest.approx(3.976653, abs=0.000001)
    # Black at 28% over #fafafa gives precisely 180/255 in each channel.
    assert contrast.ratio("rgba(0,0,0,.28)", "#fafafa") == pytest.approx(contrast.ratio("#b4b4b4", "#fafafa"))
    assert contrast.ratio("rgba(255,255,255,.5)", "#000") == pytest.approx(5.280823, abs=0.000001)


def test_luminance_linear_branch():
    assert contrast.luminance((0.04, 0.04, 0.04)) == pytest.approx(0.04 / 12.92)


@pytest.mark.parametrize("value", ["red", "#abcd", "#ggg", "#1234567", "rgb(0,0,0)",
                                   "rgba(0,0,0,2)", "rgba(256,0,0,1)", "rgba(-1,0,0,1)",
                                   "rgba(0,0,0)", "rgba(nan,0,0,1)", "rgba(0,0,0,inf)",
                                   "hsl(0,101%,50%)", "hsl(0,50%,-1%)", "hsl(0,0,0)",
                                   "hsl(inf,0%,0%)", "", None])
def test_invalid_colours_raise_meaningful_errors(value):
    with pytest.raises(ValueError):
        contrast.ratio(value, "#fff")


def test_background_must_be_opaque():
    with pytest.raises(ValueError, match="opaque"):
        contrast.ratio("#000", "rgba(255,255,255,.5)")
    assert contrast.ratio("#000", "rgba(255,255,255,1)") == 21


def test_token_colours_match_approved_palette():
    expected = {
        ("Day", "Body text"): ("#5f5f5f", "#FAFAFA"),
        ("Day", "Secondary text"): ("#5f5f5f", "#FAFAFA"),
        ("Day", "Primary text"): ("#000", "#FAFAFA"),
        ("Day", "Links"): ("#005DFF", "#FAFAFA"),
        ("Day", "Chip text"): ("#121212", "#d9d9d9"),
        ("Day", "Active chip text"): ("#fff", "#005DFF"),
        ("Day", "Hover chip text"): ("#121212", "#d6e4ff"),
        ("Day", "Orange kicker"): ("#FF511D", "#121212"),
        ("Day", "Cobalt focus ring"): ("#005DFF", "#FAFAFA"),
        ("Day", "Non-text marks"): ("#8a8a8a", "#FAFAFA"),
        ("Day", "Hairlines"): ("rgba(0,0,0,.28)", "#FAFAFA"),
        ("Night", "Body text"): ("#c8c8c8", "hsl(0,0%,4%)"),
        ("Night", "Secondary text"): ("#9a9a9a", "hsl(0,0%,4%)"),
        ("Night", "Primary text"): ("#fff", "hsl(0,0%,4%)"),
        ("Night", "Links"): ("#d6e4ff", "hsl(0,0%,4%)"),
        ("Night", "Chip text"): ("#121212", "#d9d9d9"),
        ("Night", "Active chip text"): ("#fff", "#005DFF"),
        ("Night", "Hover chip text"): ("#121212", "#d6e4ff"),
        ("Night", "Orange kicker"): ("#FF511D", "#121212"),
        ("Night", "Cobalt focus ring"): ("#005DFF", "hsl(0,0%,4%)"),
        ("Night", "Non-text marks"): ("#9a9a9a", "hsl(0,0%,4%)"),
        ("Night", "Hairlines"): ("rgba(255,255,255,.22)", "hsl(0,0%,4%)"),
        ("Night", "Orange on Night background"): ("#FF511D", "hsl(0,0%,4%)"),
        ("Day", "Orange page titles (large text)"): ("#FF511D", "#FAFAFA"),
        ("Day", "Orange theme rows"): ("#FF511D", "#FAFAFA"),
    }
    actual = {(pair["mode"], pair["name"]): (pair["fg"], pair["bg"])
              for pair in contrast.TOKEN_PAIRS}
    assert actual == expected
    assert len(contrast.TOKEN_PAIRS) == len(expected)


def test_all_approved_tokens_pass_and_every_pair_is_printed(capsys):
    assert contrast.main([]) == 0
    output = capsys.readouterr().out
    assert len(output.splitlines()) == len(contrast.TOKEN_PAIRS) + 1
    for pair in contrast.TOKEN_PAIRS:
        assert f"{pair['mode']} / {pair['name']}" in output
    assert output.count("decorative, reported only") == 2
    assert "0 required failures" in output
    for mode in ("Day", "Night"):
        pairs = {pair["name"]: pair for pair in contrast.TOKEN_PAIRS if pair["mode"] == mode}
        assert set(pairs) >= {"Body text", "Secondary text", "Primary text", "Links", "Chip text",
                              "Active chip text", "Hover chip text", "Orange kicker", "Cobalt focus ring",
                              "Non-text marks", "Hairlines"}
        assert pairs["Cobalt focus ring"]["minimum"] == 3.0
        assert pairs["Non-text marks"]["minimum"] == 3.0
        assert pairs["Hairlines"]["minimum"] is None


@pytest.mark.parametrize("minimum", [4.5, 3.0])
def test_required_failure_changes_exit_code(monkeypatch, capsys, minimum):
    monkeypatch.setattr(contrast, "TOKEN_PAIRS", [{"mode": "Test", "name": "Failure",
                                                 "fg": "#fff", "bg": "#fff", "minimum": minimum}])
    assert contrast.main([]) == 1
    assert "1 required failures" in capsys.readouterr().out


def test_decorative_failure_is_reported_only(monkeypatch, capsys):
    monkeypatch.setattr(contrast, "TOKEN_PAIRS", [{"mode": "Test", "name": "Hairline",
                                                 "fg": "#fff", "bg": "#fff", "minimum": None}])
    assert contrast.main([]) == 0
    assert "INFO Test / Hairline: 1.00:1" in capsys.readouterr().out


def test_threshold_uses_unrounded_ratio(monkeypatch):
    monkeypatch.setattr(contrast, "TOKEN_PAIRS", [{"mode": "Test", "name": "Boundary",
                                                 "fg": "#000", "bg": "#fff", "minimum": 4.5}])
    monkeypatch.setattr(contrast, "ratio", lambda fg, bg: 4.4999)
    assert contrast.main([]) == 1
    monkeypatch.setattr(contrast, "ratio", lambda fg, bg: 4.5)
    assert contrast.main([]) == 0


def test_cli_default_and_bad_arguments():
    result = subprocess.run([sys.executable, "-B", str(SCRIPT)], capture_output=True, text=True)
    assert result.returncode == 0 and "PASS Contrast:" in result.stdout
    result = subprocess.run([sys.executable, "-B", str(SCRIPT), "--unknown"], capture_output=True, text=True)
    assert result.returncode == 2


def test_accepted_pair_is_reported_not_failed(capsys):
    assert contrast.main([]) == 0
    output = capsys.readouterr().out
    assert "ACCEPTED Day / Orange theme rows" in output
    assert "accepted below it (owner, 27 October 2026)" in output


def test_live_accepts_only_day_theme_rows_in_the_title_orange(monkeypatch, tmp_path, capsys):
    (tmp_path / "index.html").write_text("<p>x</p>", encoding="utf-8")
    row = {"mode": "Day", "width": 1440, "page": "home", "ratio": 3.12, "need": 4.5,
           "element": "span", "text": "ADM", "colour": "rgb(255, 81, 29)", "theme_row": True}
    monkeypatch.setattr(contrast, "check_live", lambda site: (10, [row]))
    assert contrast.main(["--live", str(tmp_path)]) == 0
    assert "1 accepted" in capsys.readouterr().out
    for other in (dict(row, theme_row=False), dict(row, mode="Night"), dict(row, colour="rgb(1, 2, 3)")):
        monkeypatch.setattr(contrast, "check_live", lambda site, other=other: (10, [other]))
        assert contrast.main(["--live", str(tmp_path)]) == 1
