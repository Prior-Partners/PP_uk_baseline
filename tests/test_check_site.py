"""Preservation checks on copies of a small synthetic built site.

Input/output CRS: n/a (built site files only).
Data layer: catalogue development checks (tests).
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "dev" / "check_site.py"
SPEC = importlib.util.spec_from_file_location("check_site", SCRIPT)
assert SPEC and SPEC.loader
site = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(site)
FIXTURE = Path(__file__).parent / "fixtures" / "sites" / "minimal"


@pytest.fixture()
def sites(tmp_path: Path) -> tuple[Path, Path]:
    """Copy fixtures before changing any site content."""
    return tuple(shutil.copytree(FIXTURE, tmp_path / name) for name in ("baseline", "candidate"))


def replace(root: Path, route: str, before: str, after: str) -> None:
    path = root / route
    content = path.read_text(encoding="utf-8")
    assert before in content
    path.write_text(content.replace(before, after), encoding="utf-8")


def edit_search(root: Path, edit) -> None:
    path = root / "search" / "search_index.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    edit(data)
    path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


def differences(sites: tuple[Path, Path], check_name: str) -> str:
    check = next(check for check in site.compare_sites(*sites) if check["name"] == check_name)
    assert check["differences"], check_name
    return "\n".join(check["differences"])


def test_identical_sites_pass_with_counts_and_report(sites, tmp_path, capsys):
    report = tmp_path / "report.md"
    assert site.main([*(str(root) for root in sites), "--report", str(report)]) == 0
    output = capsys.readouterr().out.splitlines()
    assert len(output) == 8
    assert all(line.startswith("PASS ") for line in output)
    assert "baseline=3, candidate=3" in output[0]
    assert "Font hashes: baseline=4, candidate=4" in output[-1]
    assert "# Built-site preservation report" in report.read_text(encoding="utf-8")


@pytest.mark.parametrize("field,value", [
    ("text", "case, punctuation — unchanged."),
    ("text", "Case punctuation — unchanged."),
    ("text", "Case, punctuation — unchanged!"),
    ("text", "Case,  punctuation — unchanged."),
    ("title", "Catalogue changed"),
])
def test_search_content_is_exact(sites, field, value):
    edit_search(sites[1], lambda data: data["docs"][0].update({field: value}))
    message = differences(sites, "Search")
    assert f'{field} changed' in message
    assert 'location "" occurrence 1' in message
    assert "first difference at character" in message


def test_search_reports_all_locations_and_fields(sites, tmp_path):
    def edit(data):
        data["config"]["lang"] = ["fr"]
        data["docs"][0].update(title="Changed", text="Changed text")
        data["docs"].pop(1)
        data["docs"].append({"location": "new/", "title": "New", "text": "New text"})
    edit_search(sites[1], edit)
    report = tmp_path / "differences.md"
    assert site.main([*map(str, sites), "--report", str(report)]) == 1
    content = report.read_text(encoding="utf-8")
    for expected in ("Search config changed", "title changed", "text changed",
                     'location "HER/" occurrence 1 missing', 'location "new/" occurrence 1 added'):
        assert expected in content


def test_search_array_order_is_preserved(sites):
    edit_search(sites[1], lambda data: data["docs"].reverse())
    assert "Search location order[0] changed" in differences(sites, "Search")


def test_search_duplicate_locations_are_not_overwritten(sites):
    for root in sites:
        edit_search(root, lambda data: data["docs"].append(dict(data["docs"][0])))
    edit_search(sites[1], lambda data: data["docs"][-1].update(text="Duplicate changed"))
    assert 'location "" occurrence 2 text changed' in differences(sites, "Search")


def test_search_extra_fields_are_compared(sites):
    edit_search(sites[1], lambda data: data["docs"][0].update(extra="value"))
    assert "other fields changed" in differences(sites, "Search")


def test_json_formatting_and_object_key_order_do_not_matter(sites):
    path = sites[1] / "search" / "search_index.json"
    value = json.loads(path.read_text(encoding="utf-8"))
    path.write_text(json.dumps(value, sort_keys=True, ensure_ascii=True, indent=4), encoding="utf-8")
    assert site.main(list(map(str, sites))) == 0


def test_routes_added_and_missing_are_reported(sites):
    (sites[1] / "HER" / "index.html").rename(sites[1] / "HER" / "renamed.html")
    message = differences(sites, "Routes")
    assert "Route missing: HER/index.html" in message
    assert "Route added: HER/renamed.html" in message


def test_nav_href_order_is_exact(sites):
    replace(sites[1], "index.html", 'href="."', 'href="temporary"')
    replace(sites[1], "index.html", 'href="HER/"', 'href="."')
    replace(sites[1], "index.html", 'href="temporary"', 'href="HER/"')
    assert "Nav target in index.html[0] changed" in differences(sites, "Nav order")


@pytest.mark.parametrize("before,after,check,expected", [
    ('<li><a class="md-nav__link" href="#columns">Columns</a></li>', "",
     "Nav order", "Nav target in HER/index.html[3] changed"),
    ('href="#columns"', 'href="#details"',
     "Nav order", "Nav target in HER/index.html[3] changed"),
    ('href="#columns">Columns', 'href="#columns">Fields',
     "Nav labels", "Nav label in HER/index.html[3] changed without permission"),
    ('class="md-nav md-nav--primary"', 'class="md-nav"',
     "Nav order", "Nav target in HER/index.html[0] missing"),
])
def test_active_page_navigation_changes_fail(sites, before, after, check, expected):
    replace(sites[1], "HER/index.html", before, after)
    assert expected in differences(sites, check)
    assert site.main(list(map(str, sites))) == 1


def test_nested_page_label_change_requires_mapping(sites):
    replace(sites[1], "HER/index.html", 'href="#columns">Columns', 'href="#columns">Fields')
    assert "changed without permission" in differences(sites, "Nav labels")
    checks = site.compare_sites(*sites, {"Columns": "Fields"})
    assert not any(check["differences"] for check in checks)
    labels = next(check for check in checks if check["name"] == "Nav labels")
    assert labels["permitted"] == ['Nav label in HER/index.html[3] permitted: "Columns" -> "Fields"']
    assert labels["unused"] == []


def test_label_usage_is_reported_per_route_with_unused_mappings(sites, tmp_path, capsys):
    for route in ("index.html", "HER/index.html"):
        replace(sites[1], route, "Staff handbook", "Staff handbook (PDF) ↗")
    mapping = {"Staff handbook": "Staff handbook (PDF) ↗", "Absent": "Unused",
               "Home": "Homepage", "Heritage overview": "Heritage overview"}
    labels = tmp_path / "labels.json"
    # PowerShell's UTF-8 output may contain a byte-order mark.
    labels.write_text(json.dumps(mapping, ensure_ascii=False), encoding="utf-8-sig")
    report = tmp_path / "report.md"
    assert site.main([*map(str, sites), "--labels", str(labels), "--report", str(report)]) == 0
    assert "differences=0, permitted=2, unused=3" in capsys.readouterr().out
    content = report.read_text(encoding="utf-8")
    for route, index in (("index.html", 3), ("HER/index.html", 4)):
        assert f'Nav label in {route}[{index}] permitted: "Staff handbook" -> "Staff handbook (PDF) ↗"' in content
    for before, after in list(mapping.items())[1:]:
        assert f'Unused label mapping: "{before}" -> "{after}"' in content


def test_nav_ignores_other_navs_and_collapses_whitespace(sites):
    replace(sites[1], "index.html", "Ignored TOC", "Changed TOC")
    replace(sites[1], "index.html", "Catalogue drawer title", "Different drawer title")
    replace(sites[1], "index.html", "HER &amp; heritage", "  HER\n  &amp;   heritage  ")
    assert site.main(list(map(str, sites))) == 0


@pytest.mark.parametrize("before,after", [("Staff handbook", "Staff handbook (PDF) ↗"),
                                          ("HER &amp; heritage", "Heritage section")])
def test_labels_require_explicit_allow_list(sites, tmp_path, before, after):
    replace(sites[1], "index.html", before, after)
    assert "changed without permission" in differences(sites, "Nav labels")
    labels = tmp_path / "labels.json"
    labels.write_text(json.dumps({before.replace("&amp;", "&"): after}), encoding="utf-8")
    assert site.main([*map(str, sites), "--labels", str(labels)]) == 0
    replace(sites[1], "index.html", after, "Unauthorised label")
    assert site.main([*map(str, sites), "--labels", str(labels)]) == 1


def test_allow_list_does_not_permit_href_changes(sites, tmp_path):
    labels = tmp_path / "labels.json"
    labels.write_text('{"Home": "Homepage"}', encoding="utf-8")
    replace(sites[1], "index.html", ">Home<", ">Homepage<")
    replace(sites[1], "index.html", 'href="."', 'href="elsewhere/"')
    assert site.main([*map(str, sites), "--labels", str(labels)]) == 1
    labels_check = next(check for check in site.compare_sites(*sites, {"Home": "Homepage"})
                        if check["name"] == "Nav labels")
    assert labels_check["permitted"] == []
    assert labels_check["unused"] == ['Unused label mapping: "Home" -> "Homepage"']


@pytest.mark.parametrize("before,after", [('id="columns"', 'id="new-columns"'),
                                          ('id="columns"', ""),
                                          ('id="columns"', 'id="details"')])
def test_heading_ids_are_ordered_and_page_specific(sites, before, after):
    replace(sites[1], "HER/index.html", before, after)
    assert "Headings in HER/index.html" in differences(sites, "Headings")


def test_headings_outside_articles_are_ignored(sites):
    replace(sites[1], "index.html", 'id="outside-article"', 'id="changed"')
    assert site.main(list(map(str, sites))) == 0


def test_heading_order_changes_fail(sites):
    replace(sites[1], "HER/index.html", '<h2 id="columns">Columns</h2><h3 id="details">Details</h3>',
            '<h3 id="details">Details</h3><h2 id="columns">Columns</h2>')
    assert "Headings in HER/index.html[1] changed" in differences(sites, "Headings")


def test_maps_are_compared_per_page(sites):
    replace(sites[1], "index.html", "maps/home.png", "maps/heritage.png")
    replace(sites[1], "HER/index.html", "maps/heritage.png", "maps/home.png")
    message = differences(sites, "Map references")
    assert "in index.html" in message and "in HER/index.html" in message


def test_map_references_resolve_relative_paths(sites):
    replace(sites[1], "HER/index.html", "../maps/heritage.png", "/maps/heritage.png?v=2#preview")
    assert site.main(list(map(str, sites))) == 0


def test_missing_and_repeated_map_references_fail(sites):
    replace(sites[1], "index.html", '<img src="maps/home.png" alt="Home preview">', "")
    replace(sites[1], "HER/index.html", "</article>", '<img src="../maps/heritage.png"></article>')
    message = differences(sites, "Map references")
    assert "missing" in message and "added" in message


@pytest.mark.parametrize("folder,file,check", [("maps", "home.png", "Map hashes"),
                                              ("fonts", "mono_light.woff2", "Font hashes")])
@pytest.mark.parametrize("action", ["change", "remove", "add"])
def test_asset_bytes_and_file_sets_are_preserved(sites, folder, file, check, action):
    path = sites[1] / folder / file
    if action == "change":
        path.write_bytes(path.read_bytes() + b"\x00\xff")
        expected = "SHA-256 changed"
    elif action == "remove":
        path.unlink()
        expected = "missing"
    else:
        path.with_name("new" + path.suffix).write_bytes(b"new asset")
        expected = "added"
    assert expected in differences(sites, check)


@pytest.mark.parametrize("payload", ["not json", "[]", '{"config":{},"docs":{}}',
                                    '{"config":{},"docs":[{"location":"a"}]}',
                                    '{"config":[],"docs":[]}'])
def test_bad_search_input_returns_two(sites, payload, capsys):
    (sites[1] / "search" / "search_index.json").write_text(payload, encoding="utf-8")
    assert site.main(list(map(str, sites))) == 2
    assert "ERROR:" in capsys.readouterr().err


@pytest.mark.parametrize("path", ["index.html", "search/search_index.json"])
def test_missing_required_input_returns_two(sites, path):
    (sites[1] / path).unlink()
    assert site.main(list(map(str, sites))) == 2


def test_missing_primary_nav_returns_two(sites):
    replace(sites[1], "index.html", "md-nav--primary", "not-primary")
    assert site.main(list(map(str, sites))) == 2


@pytest.mark.parametrize("payload", ["[]", '{"Home":1}', "not json"])
def test_bad_label_mapping_returns_two(sites, tmp_path, payload):
    labels = tmp_path / "labels.json"
    labels.write_text(payload, encoding="utf-8")
    assert site.main([*map(str, sites), "--labels", str(labels)]) == 2


def test_report_cannot_overwrite_an_input(sites):
    report = sites[0] / "index.html"
    original = report.read_bytes()
    assert site.main([*map(str, sites), "--report", str(report)]) == 2
    assert report.read_bytes() == original


def test_unwritable_report_destination_returns_two(sites, tmp_path):
    assert site.main([*map(str, sites), "--report", str(tmp_path / "absent" / "report.md")]) == 2


def test_cli_exit_codes(sites):
    def run(*args):
        return subprocess.run([sys.executable, "-B", str(SCRIPT), *map(str, args)],
                              capture_output=True, text=True, encoding="utf-8")
    assert run(*sites).returncode == 0
    replace(sites[1], "HER/index.html", 'id="columns"', 'id="changed"')
    result = run(*sites)
    assert result.returncode == 1 and "FAIL Headings" in result.stdout
    assert run(sites[0], sites[1] / "absent").returncode == 2
    assert run().returncode == 2
