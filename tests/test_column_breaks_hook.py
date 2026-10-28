"""Tests for hooks/column_breaks.py — break points in the Columns tables (owner, 28 October 2026).

Input/output CRS: n/a (built HTML only). Data layer: catalogue site (tests).

Column names break only after "_" and "&", geometry types only after "(" and ","; nothing else on
the page changes, and the text a reader (or search) sees is the same.
"""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path
from types import ModuleType

import pytest

REPO = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def hook() -> ModuleType:
    spec = importlib.util.spec_from_file_location("column_breaks", REPO / "hooks" / "column_breaks.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def columns_table(*rows: tuple[str, str]) -> str:
    body = "".join(f"<tr>\n<td><code>{n}</code></td>\n<td><code>{t}</code></td>\n<td>Note.</td>\n</tr>\n"
                   for n, t in rows)
    return ("<table>\n<thead>\n<tr>\n<th>Column</th>\n<th>Type</th>\n<th>Description / unit</th>\n</tr>\n"
            f"</thead>\n<tbody>\n{body}</tbody>\n</table>")


@pytest.mark.parametrize("name, marked", [
    ("naptan_code", "naptan_<wbr>code"),
    ("msoa21hclnm", "msoa21hclnm"),
    ("irradiation__electromedical&amp;electrotherapeutic_eqm",
     "irradiation__<wbr>electromedical&amp;<wbr>electrotherapeutic_<wbr>eqm"),
    ("No cars or vans in household _perc", "No cars or vans in household _perc"),
])
def test_names_break_after_underscore_and_ampersand(hook: ModuleType, name: str, marked: str) -> None:
    assert hook.break_name(name) == marked


@pytest.mark.parametrize("type_, marked", [
    ("geometry(MultiPolygon,27700)", "geometry(<wbr>MultiPolygon,<wbr>27700)"),
    ("character varying(50)", "character varying(50)"),
    ("double precision", "double precision"),
])
def test_only_geometry_types_get_break_points(hook: ModuleType, type_: str, marked: str) -> None:
    assert hook.break_type(type_) == marked


def test_only_the_columns_table_changes_and_its_text_stays(hook: ModuleType) -> None:
    other = "<table>\n<thead>\n<tr>\n<th>Code</th>\n<th>Theme</th>\n</tr>\n</thead>\n<tbody>\n" \
            "<tr>\n<td><code>stop_name</code></td>\n<td><code>geometry(Point,27700)</code></td>\n</tr>\n</tbody>\n</table>"
    page = f"<p>See <code>uk_baseline.mob_dft_bods_bus_stops</code>.</p>\n{other}\n" + columns_table(
        ("stop_name", "character varying(500)"), ("geom", "geometry(Point,27700)"))
    out = hook.on_page_content(page)
    assert out.count("<wbr>") == 3                        # stop_<wbr>name, geometry(<wbr>Point,<wbr>27700)
    assert out.startswith(page[:page.rindex("<table>")])  # the text and the other table are untouched
    assert re.sub(r"<wbr>", "", out) == page
