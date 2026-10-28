"""MkDocs hook: line-break points in the Columns table of every layer page.

Input/output CRS: n/a (built HTML only). Data layer: catalogue site (presentation).

Owner, 28 October 2026: long column names split at any letter ("naptan_cod / e"). In each
Columns table this hook adds a <wbr> break point after every "_" and "&" in a column name, and
after every "(" and "," in a geometry type ("geometry( / MultiPolygon, / 27700)"). No break
follows an underscore that comes after a space (it would leave a lone "_") or that is followed by
another underscore. <wbr> carries no text, so the page text, search and copying stay the same;
extra.css stops the browser splitting these cells anywhere else.
"""
from __future__ import annotations

import re
from typing import Any

# A layer page's Columns table: the only table whose header starts "Column", "Type".
COLUMNS_TABLE = re.compile(r"<table>\s*<thead>\s*<tr>\s*<th>Column</th>\s*<th>Type</th>.*?</table>", re.S)
ROW = re.compile(r"(<tr>\s*<td><code>)([^<]*)(</code></td>\s*<td><code>)([^<]*)(</code></td>)")


def break_name(name: str) -> str:
    """Break points after "_" and "&" in an HTML-escaped column name."""
    return re.sub(r"(?<! )_(?!_)", "_<wbr>", name).replace("&amp;", "&amp;<wbr>")


def break_type(type_: str) -> str:
    """Break points after "(" and "," in a geometry type; other types already break at their space."""
    if not type_.startswith("geometry("):
        return type_
    return type_.replace("(", "(<wbr>").replace(",", ",<wbr>")


def _table(match: re.Match[str]) -> str:
    return ROW.sub(lambda r: r[1] + break_name(r[2]) + r[3] + break_type(r[4]) + r[5], match[0])


def on_page_content(html: str, **kwargs: Any) -> str:
    return COLUMNS_TABLE.sub(_table, html)
