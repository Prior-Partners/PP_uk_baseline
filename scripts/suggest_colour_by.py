r"""Suggest candidate colour-by columns for each single-colour catalogue layer.

Input/output CRS: n/a (metadata only). Data layer: catalogue map styling prep.

For every uk_baseline layer that build_maps currently renders as a single brand
colour (i.e. no curated ``colour_by``), this lists candidate columns the owner
could nominate for a categorical or sequential colour-by. Candidates are drawn
from the planner's column statistics (``pg_stats.n_distinct``) so nothing scans
the tables:

* categorical  — text/boolean columns with 2..25 distinct values
* sequential   — numeric measure columns (not identifiers/codes/years)

Writes a markdown shortlist the owner can tick. Nothing is rendered or written
to the database.
"""
from __future__ import annotations

import logging
import re
from pathlib import Path

import psycopg

import build_maps as bm

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger(__name__)

OUT_MD = Path(__file__).resolve().parent / "colour_by_candidates.md"

# Columns that never make sense as a colour-by (identifiers, geometry, coordinate
# and shape-metric columns, names/codes). Matching is case-insensitive.
SKIP_EXACT = {"geom", "gid", "fid", "objectid", "id", "ogc_fid", "area_ha",
              "bng_e", "bng_n", "lat", "long", "long_", "latitude", "longitude",
              "easting", "northing", "x", "y", "id_original", "vxcount",
              "h3_count", "geometry_a", "areahectar", "area_km2", "orig_area",
              "shape_leng", "shape_length", "shape_area", "perc_manmade"}
SKIP_SUFFIX = ("cd", "nm", "nmw", "name", "_name", "id", "code", "_cd",
               "rank", "_rnk", "rnk")
NUMERIC_TYPES = {"int2", "int4", "int8", "float4", "float8", "numeric"}
TEXT_TYPES = {"text", "varchar", "bpchar", "bool"}
MAX_SEQ_SHOWN = 10   # wide census tables have dozens of measures; show a sample


def is_skippable(col: str) -> bool:
    c = col.lower()
    if c in SKIP_EXACT:
        return True
    if any(c.endswith(s) for s in SKIP_SUFFIX):
        return True
    if re.fullmatch(r"(19|20)\d{2}", c) or c in {"year", "yr"}:
        return True
    return False


def column_stats(cur, table):
    """(column, udt_type, est_distinct) for a table, from catalogue + pg_stats.

    est_distinct: positive = distinct count; negative = -(fraction of rows);
    None = no statistics gathered yet.
    """
    cur.execute(
        """SELECT a.attname, t.typname,
                  (SELECT s.n_distinct FROM pg_stats s
                   WHERE s.schemaname=%s AND s.tablename=%s AND s.attname=a.attname)
           FROM pg_attribute a JOIN pg_type t ON t.oid=a.atttypid
           WHERE a.attrelid=%s::regclass AND a.attnum>0 AND NOT a.attisdropped
           ORDER BY a.attnum""",
        (bm.SCHEMA, table, f"{bm.SCHEMA}.{table}"))
    return cur.fetchall()


def classify(rows, est_rows):
    """Split a table's columns into categorical / sequential candidates."""
    cats, seqs = [], []
    for col, typ, nd in rows:
        if is_skippable(col) or typ not in NUMERIC_TYPES | TEXT_TYPES:
            continue
        # resolve n_distinct estimate to an absolute count
        if nd is None:
            distinct = None
        elif nd < 0:
            distinct = int(round(-nd * est_rows)) if est_rows else None
        else:
            distinct = int(nd)
        if typ in TEXT_TYPES:
            if distinct is not None and 2 <= distinct <= 25:
                cats.append((col, distinct))
        elif typ in NUMERIC_TYPES:
            # a numeric measure: many distinct values (or unknown) → sequential
            if distinct is None or distinct >= 10:
                seqs.append((col, distinct))
    return cats, seqs


def main() -> None:
    with psycopg.connect(bm.conninfo()) as conn, conn.cursor() as cur:
        specs = bm.build_specs(cur)
        single = [s for s in specs if not s.get("colour_by")]
        lines = ["# Colour-by candidates for single-colour layers", "",
                 f"{len(single)} layers currently render as a single brand colour. "
                 "Tick a column to colour by, or leave as-is. For categoricals with "
                 ">~12 classes, propose a reduced recat (see the POI / functional-sites "
                 "CASE pattern in build_maps.py).", ""]
        for s in sorted(single, key=lambda x: x["table"]):
            rows = column_stats(cur, s["table"])
            cats, seqs = classify(rows, s.get("est_rows", 0))
            if not cats and not seqs:
                continue
            kind = bm.kind_of(s.get("gtype"))
            lines.append(f"## `{s['table']}`  ({kind}, ~{s.get('est_rows', 0):,} rows)")
            if cats:
                lines.append("- **categorical:** "
                             + ", ".join(f"`{c}` ({n})" for c, n in cats))
            if seqs:
                shown = ", ".join(f"`{c}`" + (f" ({n})" if n else "")
                                  for c, n in seqs[:MAX_SEQ_SHOWN])
                more = (f"  … +{len(seqs) - MAX_SEQ_SHOWN} more measures"
                        if len(seqs) > MAX_SEQ_SHOWN else "")
                lines.append(f"- **sequential:** {shown}{more}")
            lines.append("")
        OUT_MD.write_text("\n".join(lines), encoding="utf-8")
        log.info("Wrote %s (%d layers with candidates)", OUT_MD,
                 sum(1 for _l in lines if _l.startswith("## ")))


if __name__ == "__main__":
    main()
