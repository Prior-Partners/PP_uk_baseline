r"""Build per-layer interactive preview maps for the uk_baseline catalogue.

Input/output CRS: reads EPSG:27700, renders in EPSG:4326 (Leaflet). Data layer:
catalogue map generation.

Reuses the sdf_console preview-map approach (folium / Leaflet, CartoDB Positron
basemap, brand colours, GeoJSON style_function + tooltip). For each layer it
pulls only the geometries in a fixed window from PostGIS (Milton Keynes for
layers with data there; the South Downs countryside window otherwise), reprojects
and simplifies, styles by the layer's most significant column, adds a legend/key,
and saves a standalone interactive HTML to catalogue/docs/maps/<table>.html.

Two fixed windows keep snapshots repeatable across frequent data updates.
"""
from __future__ import annotations

import json
import logging
import os
import re
from pathlib import Path

import branca.colormap as cm
import folium
import psycopg
from branca.element import Element
from dotenv import dotenv_values

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger(__name__)

# Override with the UK_BASELINE_ENV environment variable for portability.
ENV = Path(os.environ.get(
    "UK_BASELINE_ENV",
    r"C:\Users\po.nienchen\OneDrive - priorpartners.com"
    r"\Documents\05_Code_Scripts\data_import\Natural_England\.env"))
SCHEMA = "uk_baseline"
OUT = Path(__file__).resolve().parents[2] / "catalogue" / "docs" / "maps"

# Fixed 25 km windows (EPSG:27700): centre +/- 12.5 km.
WINDOWS = {
    "MK": (472500, 225500, 497500, 250500),          # Milton Keynes
    "south_downs": (467500, 99500, 492500, 124500),  # countryside fallback
    "england": (240000, 50000, 660000, 640000),      # whole-country overview
}
WINDOW_LABEL = {"MK": "Milton Keynes", "south_downs": "South Downs",
                "england": "England"}

# Brand palette (matches the catalogue theme colours).
THEME_COLOURS = {
    "ADM": "#e9511d", "BLT": "#920f67", "COM": "#554596", "DEM": "#945f14",
    "ECN": "#dd1220", "EDU": "#6da2ed", "ENV": "#219900", "HER": "#2b242c",
    "HOU": "#8c3111", "HTH": "#005dff", "MOB": "#7a7a72", "UTL": "#991955",
}

# Preview thinning. Points/polygons are randomly sampled above the cap so the
# HTML stays small; lines are kept whole (sampling breaks a network) but
# simplified harder. Tolerance is in degrees (4326): coarser for the England
# overview window, finer for the 25 km local windows.
CAPS = {"point": 3000, "polygon": 4000, "line": 200000}
# Full-extent (England-wide) caps. Points lift to 5000 so the national spread
# reads as a distribution; polygons lift to 60000 so admin choropleths (~35k
# LSOAs / ~7k MSOAs / ~360 LADs) render every unit with no sampling holes.
CAPS_FULL = {"point": 5000, "polygon": 60000, "line": 200000}
# Polygon layers above this row estimate stay windowed (Group C) — too dense for
# one static HTML at national extent. Line layers always stay windowed. The
# ceiling sits just above LSOA grain (~35k units) so every LSOA / MSOA / ward
# choropleth renders whole (no sampling holes) while Output-Area grain (~188k)
# and dense coverage layers (built-up areas, green space, tidal water, …) fall
# back to a local window.
HEAVY_POLY_ROWS = 50_000
# At full extent, layers above this estimate are sampled server-side via
# TABLESAMPLE: an ORDER BY random() over tens of millions of rows would
# full-scan + sort the whole table (minutes per layer); TABLESAMPLE picks pages
# first, then we trim to the cap.
TABLESAMPLE_ROWS = 200_000
SAMPLE_KINDS = {"point", "polygon"}      # lines are never sampled
# ~10 m (0.0001°) is sub-pixel in a 25 km-wide preview, so simplifying this hard
# keeps the HTML small with no visible quality loss; the England overview is
# coarser still.
SIMPLIFY = {"MK": {"line": 0.00012, "other": 0.0001},
            "south_downs": {"line": 0.00012, "other": 0.0001},
            "england": {"line": 0.0008, "other": 0.001}}   # ~110 m: sub-pixel at national zoom
# GeoJSON coordinate decimal places (EPSG:4326). The default 9 (~0.1 mm) bloats
# the HTML pointlessly; 4 (~11 m) is sub-pixel at national zoom, 6 (~0.1 m) in the
# 25 km local windows.
PRECISION = {"england": 4, "MK": 6, "south_downs": 6}
# Qualitative brand hues for categorical colouring. 12 distinct hues so layers
# with up to a dozen classes (e.g. POI categories, building themes) all show;
# beyond that, or an explicit "Other" class, falls to grey.
QUAL = ["#e9511d", "#005dff", "#4bb400", "#920f67", "#ff2a8e", "#dadf50",
        "#554596", "#009476", "#c8b5e2", "#945f14", "#f2a900", "#00a3a3"]
GREY = "#9a958c"
CARTO = {"tiles": "CartoDB positron", "attr": "© OpenStreetMap, © CARTO"}

# Acronyms to upper-case wherever they appear as a whole word in a legend
# title or category label (key tidy-up: "Os named places" -> "OS named places").
ACRONYMS = {"OS", "OSM", "ONS", "NHS", "GP", "POI", "VOA", "NDR", "IMD", "LSOA",
            "MSOA", "OA", "LAD", "GVA", "OHID", "DFT", "DFE", "DESNZ", "MHCLG",
            "GEODS", "WWCT", "UK", "EV", "SSSI", "SAC", "SPA", "HMLR"}


def prettify_acronyms(text: str) -> str:
    """Upper-case known acronyms appearing as whole words in ``text``."""
    return re.sub(r"[A-Za-z]+",
                  lambda m: m.group(0).upper() if m.group(0).upper() in ACRONYMS
                  else m.group(0), text)

CONNINFO = None


def conninfo() -> str:
    e = dotenv_values(ENV)
    parts = [f"host={e['PG_HOST']}", f"port={e['PG_PORT']}",
             f"dbname={e['PG_DATABASE']}", f"user={e['PG_USER']}"]
    if e.get("PG_PASSWORD"):
        parts.append(f"password={e['PG_PASSWORD']}")
    return " ".join(parts)


def _tint(hex_colour: str, amount: float = 0.85) -> str:
    """Blend a hex colour toward white by ``amount`` (0..1) for the ramp's low end."""
    r, g, b = (int(hex_colour[i:i + 2], 16) for i in (1, 3, 5))
    r = int(r + (255 - r) * amount)
    g = int(g + (255 - g) * amount)
    b = int(b + (255 - b) * amount)
    return f"#{r:02x}{g:02x}{b:02x}"


def window_bounds_4326(cur, key, bbox=None):
    x0, y0, x1, y1 = bbox or WINDOWS[key]
    cur.execute(
        "SELECT ST_XMin(g), ST_YMin(g), ST_XMax(g), ST_YMax(g) FROM "
        "(SELECT ST_Transform(ST_MakeEnvelope(%s,%s,%s,%s,27700),4326) g) s",
        (x0, y0, x1, y1))
    xmin, ymin, xmax, ymax = cur.fetchone()
    return (ymin, xmin, ymax, xmax)  # south, west, north, east


def kind_of(gtype):
    """Map a geometry_columns type string to point / line / polygon."""
    g = (gtype or "").upper()
    if "POINT" in g:
        return "point"
    if "LINE" in g:
        return "line"
    return "polygon"


def fetch_features(cur, table, colour_by, label, window_key, kind,
                   bbox=None, where=None, est_rows=0):
    """Return (features, total_in_window, sampled?).

    Dense point/polygon layers are randomly sampled to the per-kind cap so the
    preview HTML stays small; lines are kept whole. Geometry is simplified at a
    window-dependent tolerance. At full England extent dense layers are sampled
    server-side via TABLESAMPLE and the total uses the planner row estimate, to
    avoid scanning + sorting tens of millions of rows.
    """
    x0, y0, x1, y1 = bbox or WINDOWS[window_key]
    env = f"ST_MakeEnvelope({x0},{y0},{x1},{y1},27700)"
    val = colour_by if colour_by else "NULL"
    lbl = label if label else "NULL"
    extra = f" AND ({where})" if where else ""   # per-layer row filter
    full = window_key == "england"
    cap = (CAPS_FULL if full else CAPS)[kind]
    # Full-extent counts span the whole dataset; an exact count(*) over tens of
    # millions of rows is a needless scan — use the planner's row estimate.
    if full and est_rows:
        total = int(est_rows)
    else:
        cur.execute(f"SELECT count(*) FROM {SCHEMA}.{table} "
                    f"WHERE geom && {env} AND ST_Intersects(geom, {env}){extra}")
        total = cur.fetchone()[0]
    # Server-side sampling for dense full-extent layers (page-level, fast); else
    # ORDER BY random() over the (already small) windowed set.
    tablesample = full and kind in SAMPLE_KINDS and total > TABLESAMPLE_ROWS
    if tablesample:
        pct = min(100.0, 100.0 * cap * 5.0 / max(total, 1))  # over-sample ~5x, then trim
        src = f"{SCHEMA}.{table} TABLESAMPLE SYSTEM ({pct:.4f})"
        sampled = True
    else:
        src = f"{SCHEMA}.{table}"
        sampled = kind in SAMPLE_KINDS and total > cap
    order = "ORDER BY random() " if sampled else ""
    limit = cap if sampled else CAPS["line"]
    tol = SIMPLIFY[window_key]["line" if kind == "line" else "other"]
    prec = PRECISION.get(window_key, 6)
    cur.execute(
        f"""SELECT {val} AS v, {lbl} AS lbl,
                   ST_AsGeoJSON(ST_SimplifyPreserveTopology(
                       ST_Transform(geom,4326), {tol}), {prec}) AS gj
            FROM {src}
            WHERE geom && {env} AND ST_Intersects(geom, {env}){extra}
            {order}LIMIT {limit}""")
    feats = []
    for v, lab, gj in cur.fetchall():
        if not gj:
            continue
        feats.append({"type": "Feature",
                      "geometry": json.loads(gj),
                      "properties": {"value": v, "label": lab}})
    return feats, total, sampled


def legend_html(title, items):
    rows = "".join(
        f'<div style="display:flex;align-items:center;gap:6px;margin:2px 0;">'
        f'<span style="width:14px;height:14px;background:{c};border:1px solid #00000022;'
        f'display:inline-block;border-radius:2px;"></span>'
        f'<span>{lab}</span></div>'
        for lab, c in items)
    return (
        '<div style="position:fixed;bottom:22px;right:12px;z-index:9999;'
        'background:#f1eedf;color:#2b242c;padding:8px 11px;border:1px solid #d9d3c4;'
        'border-radius:6px;font:12px/1.3 -apple-system,Segoe UI,sans-serif;'
        'max-width:240px;box-shadow:0 1px 4px #0003;">'
        f'<div style="font-weight:700;margin-bottom:4px;">{title}</div>{rows}</div>')


def _fmt_num(x):
    """Compact human number for a legend tick (1.2M, 34k, 72, 8.4)."""
    ax = abs(x)
    if ax >= 1e6:
        return f"{x / 1e6:.1f}M"
    if ax >= 1e4:
        return f"{x / 1e3:.0f}k"
    if ax >= 100:
        return f"{x:.0f}"
    return f"{int(x)}" if float(x).is_integer() else f"{x:.1f}"


def legend_html_sequential(title, low, high, vmin, vmax):
    """Vertical gradient legend for sequential layers.

    Replaces branca's horizontal colorbar (which a full re-render overwrites)
    with a self-contained vertical bar in the same brand box as the categorical
    key, high value at the top.
    """
    grad = f"linear-gradient(to top, {low}, {high})"
    mid = (vmin + vmax) / 2
    return (
        '<div style="position:fixed;bottom:22px;right:12px;z-index:9999;'
        'background:#f1eedf;color:#2b242c;padding:8px 11px;border:1px solid #d9d3c4;'
        'border-radius:6px;font:12px/1.3 -apple-system,Segoe UI,sans-serif;'
        'box-shadow:0 1px 4px #0003;">'
        f'<div style="font-weight:700;margin-bottom:5px;">{title}</div>'
        '<div style="display:flex;gap:7px;align-items:stretch;">'
        f'<div style="width:14px;height:120px;background:{grad};'
        'border:1px solid #00000022;border-radius:2px;"></div>'
        '<div style="display:flex;flex-direction:column;justify-content:space-between;'
        'height:120px;">'
        f'<span>{_fmt_num(vmax)}</span><span>{_fmt_num(mid)}</span>'
        f'<span>{_fmt_num(vmin)}</span></div></div></div>')


def render(cur, spec):
    table, theme = spec["table"], spec["theme"]
    colour_by, ctype = spec.get("colour_by"), spec["ctype"]
    title = prettify_acronyms(spec["legend_title"])
    win = spec["window"]
    label, label_title = spec.get("label"), spec.get("label_title", "Name")
    fill_op = spec.get("fill_opacity", 0.6)
    line_weight = spec.get("line_weight", 2.6)   # line layers; per-layer override
    outline = spec.get("outline", "#ffffff")     # polygon stroke; default white
    bbox = spec.get("bbox")
    kind = kind_of(spec.get("gtype"))
    feats, total, sampled = fetch_features(
        cur, table, colour_by, label, win, kind, bbox, spec.get("where"),
        spec.get("est_rows", 0))
    if not feats:
        log.warning("  %s — no features in %s window, skipped", table, win)
        return False
    base = THEME_COLOURS.get(theme, "#444")
    south, west, north, east = window_bounds_4326(cur, win, bbox)

    fmap = folium.Map(location=[(south + north) / 2, (west + east) / 2],
                      tiles=None, control_scale=True, zoom_start=12,
                      prefer_canvas=True)  # canvas render: smooth pan/zoom for 10k+ features
    folium.TileLayer(tiles=CARTO["tiles"], attr=CARTO["attr"], control=False).add_to(fmap)
    # Remove the browser's default focus outline (the "black square" drawn
    # around an SVG feature when clicked).
    fmap.get_root().header.add_child(Element(
        "<style>.leaflet-interactive:focus{outline:none;}"
        "path.leaflet-interactive:focus{outline:none;}</style>"))

    # --- colour assignment + legend ---
    colormap = None
    cat_map = {}
    if ctype == "categorical":
        cats = sorted({f["properties"]["value"] for f in feats
                       if f["properties"]["value"] not in (None, "")})
        legend_items, grey_used, pi = [], False, 0
        for c in cats:
            label = prettify_acronyms(str(c))
            if str(c).lower().startswith("other") or pi >= len(QUAL):
                cat_map[c], grey_used = GREY, True       # 'Other' + overflow -> grey
            else:
                cat_map[c] = QUAL[pi]; pi += 1
                legend_items.append((label, cat_map[c]))
        if grey_used:
            legend_items.append(("Other", GREY))
        fmap.get_root().html.add_child(Element(legend_html(title, legend_items)))
    elif ctype == "sequential":
        vals = [f["properties"]["value"] for f in feats
                if isinstance(f["properties"]["value"], (int, float))]
        vmin, vmax = (min(vals), max(vals)) if vals else (0, 1)
        if vmin == vmax:
            vmax = vmin + 1
        low = _tint(base)
        colormap = cm.LinearColormap([low, base], vmin=vmin, vmax=vmax)
        # Custom vertical legend instead of branca's horizontal colorbar (which a
        # full re-render overwrites). colormap is still used to colour features.
        fmap.get_root().html.add_child(Element(
            legend_html_sequential(title, low, base, vmin, vmax)))
    else:  # single
        fmap.get_root().html.add_child(Element(legend_html(title, [(title, base)])))

    def style(feature):
        v = feature["properties"]["value"]
        null_seq = False
        if ctype == "categorical":
            c = cat_map.get(v, GREY)
        elif ctype == "sequential":
            if isinstance(v, (int, float)):
                c = colormap(v)
            else:                       # no data -> white void (not grey)
                c, null_seq = "#ffffff", True
        else:
            c = base
        if kind == "line":
            return {"color": c, "weight": line_weight, "opacity": 0.9}
        if kind == "point":
            return {"fillColor": c, "color": c, "fillOpacity": 0.5,
                    "weight": 0.6, "opacity": 0.6}
        fo = 0.9 if null_seq else fill_op   # white void reads solid
        return {"fillColor": c, "color": outline, "weight": 1.0, "fillOpacity": fo}

    def highlight(_feature):  # hover emphasis — outline stays white, thicker
        if kind == "line":
            return {"weight": line_weight + 1.9, "opacity": 1}
        return {"weight": 3.0, "color": "#ffffff", "fillOpacity": min(fill_op + 0.3, 0.85)}

    # tooltip: hover label (e.g. LSOA name) and/or the coloured value
    fields, aliases = [], []
    if label:
        fields.append("label"); aliases.append(label_title)
    if colour_by:
        fields.append("value"); aliases.append(title)
    tooltip = (folium.GeoJsonTooltip(fields=fields, aliases=aliases, sticky=True)
               if fields else None)

    gj_kwargs = dict(style_function=style, highlight_function=highlight, tooltip=tooltip)
    if kind == "point":
        gj_kwargs["marker"] = folium.CircleMarker(radius=4, fill=True)
    folium.GeoJson({"type": "FeatureCollection", "features": feats},
                   name=table, **gj_kwargs).add_to(fmap)

    fmap.fit_bounds([[south, west], [north, east]])
    # caption (top-left) — layer name only (no location); note any dense-layer sample
    note = (f' · sample of {len(feats):,} of {total:,}' if sampled
            else '')
    cap = (f'<div style="position:fixed;top:10px;left:10px;z-index:9999;'
           f'background:#2b242c;color:#fff;padding:4px 9px;border-radius:5px;'
           f'font:12px -apple-system,Segoe UI,sans-serif;">{table}'
           f'<span style="opacity:.7;">{note}</span></div>')
    fmap.get_root().html.add_child(Element(cap))

    OUT.mkdir(parents=True, exist_ok=True)
    fmap.save(str(OUT / f"{table}.html"))
    log.info("  %-52s %-11s %-11s %6d feats%s", table, win, ctype, len(feats),
             f"  (sampled of {total:,})" if sampled else "")
    return True


# --- pilot manifest (16 layers; expand to all later) ----------------------
PILOT = [
    {"table": "adm_ons_lsoa_boundary_2021", "theme": "ADM", "window": "MK",
     "colour_by": None, "ctype": "single", "legend_title": "LSOA 2021 boundary",
     "label": "lsoa21nm", "label_title": "LSOA", "fill_opacity": 0.12},
    {"table": "adm_ons_postcode_centroid_feb2026", "theme": "ADM", "window": "MK",
     "colour_by": None, "ctype": "single", "legend_title": "Postcode centroid"},
    {"table": "dem_mhclg_lsoa_imd_2025", "theme": "DEM", "window": "MK",
     "colour_by": "imd_decile", "ctype": "sequential", "legend_title": "IMD decile (1 = most deprived)"},
    {"table": "dem_ons_lsoa_accommodation_type_2021", "theme": "DEM", "window": "MK",
     # dominant single type (largest share) -> 4 clean categories, not the
     # messy compound 'dominant group' column
     "colour_by": ("CASE GREATEST(detached_perc, semi_detached_perc, terraced_perc, "
                   "in_a_purpose_built_block_of_flats_or_tenement_perc) "
                   "WHEN detached_perc THEN 'Detached' "
                   "WHEN semi_detached_perc THEN 'Semi-detached' "
                   "WHEN terraced_perc THEN 'Terraced' "
                   "WHEN in_a_purpose_built_block_of_flats_or_tenement_perc THEN 'Flats' END"),
     "ctype": "categorical", "legend_title": "Dominant accommodation type"},
    {"table": "ecn_ons_lad_gross_value_added_2023", "theme": "ECN", "window": "MK",
     "colour_by": "gva_2023", "ctype": "sequential", "legend_title": "GVA 2023 (£m)",
     "bbox": (452500, 205500, 517500, 270500)},  # ±32.5km → 17 LADs (coarse grain)
    {"table": "ecn_voa_lsoa_business_floorspace_2023", "theme": "ECN", "window": "MK",
     "colour_by": "floorspace_all_2023", "ctype": "sequential",
     "legend_title": "Business floorspace 2023 (m²)"},
    {"table": "env_naturalengland_sssi_apr2026", "theme": "ENV", "window": "MK",
     "colour_by": None, "ctype": "single", "legend_title": "SSSI",
     # ±29.5 km around MK → ~120 sites; transparent fill, green outline
     "bbox": (455500, 208500, 514500, 267500), "outline": "#219900",
     "fill_opacity": 0.15},
    {"table": "env_ons_national_park_may2026", "theme": "ENV", "window": "england",
     "colour_by": None, "ctype": "single", "legend_title": "National Park"},
    {"table": "her_historicengland_listed_building_points_may2026", "theme": "HER", "window": "MK",
     "colour_by": "grade", "ctype": "categorical", "legend_title": "Listed building grade"},
    {"table": "her_historicengland_conservation_areas_jul2025", "theme": "HER", "window": "MK",
     "colour_by": None, "ctype": "single", "legend_title": "Conservation area",
     # drop Historic England's placeholder polygons (whole-authority fills
     # named 'No data available for publication by HE')
     "where": "name <> 'No data available for publication by HE'"},
    {"table": "blt_ons_built_up_areas_dec2024", "theme": "BLT", "window": "MK",
     "colour_by": None, "ctype": "single", "legend_title": "Built up area"},
    {"table": "blt_geods_poi_sep2024", "theme": "BLT", "window": "MK",
     # 1,836 raw GeoDS categories reduced to 12 broad classes (approved 2026-06-02)
     "colour_by": (
         "CASE "
         "WHEN main_category IS NULL THEN 'Other' "
         "WHEN main_category ~* 'school|preschool|kindergarten|education|college|university|tutor|nursery' THEN 'Education' "
         "WHEN main_category ~* 'hospital|pharmac|dentist|doctor|medical|health|clinic|optician|physician|naturopath|chiropract|veterinar|nursing|therapy|hospice' THEN 'Health & Medical' "
         "WHEN main_category ~* 'hotel|motel|hostel|accommodation|bed_and_breakfast|guest|lodging|resort|retirement_home|caravan|campground' THEN 'Accommodation' "
         "WHEN main_category ~* 'restaurant|cafe|coffee|pub|bar$|_bar|bakery|fast_food|food|pizza|diner|brewery|bistro|eatery|deli|takeaway|fish_and_chips|brasserie|grill|steakhouse' THEN 'Food & Drink' "
         "WHEN main_category ~* 'beauty|salon|barber|hairdress|nail|spa|tattoo|tanning|pet_groom|massage' THEN 'Beauty & Personal care' "
         "WHEN main_category ~* 'automotive|car_dealer|car_repair|taxi|mechanic|tyre|petrol|fuel|car_wash|parking|shipping|courier|motorcycle|auto_|logistics' THEN 'Automotive & Transport' "
         "WHEN main_category ~* 'contractor|electric|plumb|construction|landscap|engineer|roofing|builder|carpenter|painter|hvac|handyman|industrial_equipment|welding|flooring' THEN 'Trades & Construction' "
         "WHEN main_category ~* 'bank|financ|insurance|account|real_estate|mortgage|investment|currency|loan|credit_union|legal|lawyer|solicitor|attorney|notary|professional_services|business_management|marketing|advertis|consult|it_service|information_technology|software|web_design|recruit|staffing|estate_agent' THEN 'Professional & Financial' "
         "WHEN main_category ~* 'gym|fitness|sport|active_life|stadium|arena|recreation|arts_and_entertainment|cinema|theatre|theater|museum|gallery|night_club|nightlife|bowling|golf|leisure|amusement|park|playground|arts_and_crafts|travel|tour|landmark|historic|monument|attraction' THEN 'Sport, Leisure & Culture' "
         "WHEN main_category ~* 'church|cathedral|mosque|temple|synagogue|worship|religi|community|charity|non_profit|social_service|government|library|post_office|civic|public_service|funeral|cemetery' THEN 'Community & Religion' "
         "WHEN main_category ~* 'shop|store|retail|supermarket|grocery|market|mall|boutique|clothing|furniture|jewel|florist|flower|hardware|convenience|book|electronics|cosmetic|gift' THEN 'Shops & Retail' "
         "ELSE 'Other' END"),
     "ctype": "categorical", "legend_title": "POI category"},
    {"table": "blt_geods_retail_centre_2022", "theme": "BLT", "window": "MK",
     "colour_by": None, "ctype": "single", "legend_title": "Retail centre",
     # zoomed out to show more centres (±40 km around MK)
     "bbox": (445000, 198000, 525000, 278000)},
    {"table": "blt_os_functional_sites_oct2024", "theme": "BLT", "window": "MK",
     # 30 (mostly compound) classifications reduced to 3 (approved 2026-06-02)
     "colour_by": (
         "CASE "
         "WHEN classification ILIKE '%Education%' THEN 'Education' "
         "WHEN classification IN ('Medical Care Accommodation','Hospital','Hospice') THEN 'Health & Medical' "
         "ELSE 'Transport' END"),
     "ctype": "categorical", "legend_title": "Site type"},
    {"table": "blt_os_important_buildings", "theme": "BLT", "window": "MK",
     "colour_by": "building_theme", "ctype": "categorical", "legend_title": "Building theme"},
    {"table": "blt_os_named_places", "theme": "BLT", "window": "MK",
     "colour_by": "classification", "ctype": "categorical", "legend_title": "Named place type"},
    {"table": "com_sportengland_active_places_facilities", "theme": "COM", "window": "MK",
     "colour_by": "facility_type", "ctype": "categorical", "legend_title": "Facility type"},
    {"table": "edu_dfe_school_may2026", "theme": "EDU", "window": "MK",
     "colour_by": "phase_of_education_name", "ctype": "categorical", "legend_title": "Phase of education"},
    {"table": "hth_ohid_msoa_life_expectancy_2023", "theme": "HTH", "window": "MK",
     "colour_by": "male_life_expectancy", "ctype": "sequential",
     "legend_title": "Male life expectancy (years)"},
    {"table": "mob_os_open_roads_apr2025", "theme": "MOB", "window": "MK",
     "colour_by": "road_classification", "ctype": "categorical", "legend_title": "Road classification",
     "line_weight": 1.3},  # halved from the 2.6 default
    {"table": "utl_nationalgrid_over_head_line", "theme": "UTL", "window": "MK",
     "colour_by": None, "ctype": "single", "legend_title": "Overhead transmission line",
     # ±18.5 km around MK → ~50 lines
     "bbox": (466500, 219500, 503500, 256500)},
    {"table": "hou_hmlandregistry_house_price_paid_jun2026", "theme": "HOU", "window": "MK",
     "colour_by": "price", "ctype": "sequential", "legend_title": "Price paid (£)",
     "label": "concat_ws(', ', street, town_city)", "label_title": "Address"},
]


# hover-name field per layer (table -> (column, alias)); applied if not already set
LABELS = {
    "adm_ons_postcode_centroid_feb2026": ("pcds", "Postcode"),
    "dem_mhclg_lsoa_imd_2025": ("lsoa21nm", "LSOA"),
    "dem_ons_lsoa_accommodation_type_2021": ("lsoa21nm", "LSOA"),
    "ecn_ons_lad_gross_value_added_2023": ("lad24nm", "Local authority"),
    "ecn_voa_lsoa_business_floorspace_2023": ("lsoa21nm", "LSOA"),
    "env_naturalengland_sssi_apr2026": ("name", "SSSI"),
    "env_ons_national_park_may2026": ("name", "National Park"),
    "her_historicengland_listed_building_points_may2026": ("name", "Listed building"),
    "her_historicengland_conservation_areas_jul2025": ("name", "Conservation area"),
    "blt_ons_built_up_areas_dec2024": ("bua24nm", "Built up area"),
    "com_sportengland_active_places_facilities": ("site_name", "Facility"),
    "edu_dfe_school_may2026": ("establishment_name", "School"),
    "hth_ohid_msoa_life_expectancy_2023": ("msoa21nm", "MSOA"),
    "mob_os_open_roads_apr2025": ("name_1", "Road"),
    "utl_nationalgrid_over_head_line": ("route_asse", "Route"),
}
for _s in PILOT:
    if _s["table"] in LABELS and "label" not in _s:
        _s["label"], _s["label_title"] = LABELS[_s["table"]]


# --- full-schema rollout ---------------------------------------------------
def read_layers(cur):
    """Every base table in the schema: theme, geometry type, column names."""
    cur.execute(
        """SELECT c.relname,
                  upper(split_part(c.relname,'_',1)) AS theme,
                  (SELECT type FROM geometry_columns g
                   WHERE g.f_table_schema=%s AND g.f_table_name=c.relname LIMIT 1) AS gtype,
                  c.reltuples::bigint AS est_rows
           FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace
           WHERE n.nspname=%s AND c.relkind='r'
           ORDER BY theme, c.relname""", (SCHEMA, SCHEMA))
    layers = [{"table": r[0], "theme": r[1], "gtype": r[2], "est_rows": r[3]}
              for r in cur.fetchall()]
    for lyr in layers:
        cur.execute("SELECT a.attname FROM pg_attribute a "
                    f"WHERE a.attrelid='{SCHEMA}.{lyr['table']}'::regclass "
                    "AND a.attnum>0 AND NOT a.attisdropped ORDER BY a.attnum")
        lyr["columns"] = [r[0] for r in cur.fetchall()]
    return layers


def humanise_title(table):
    """Legend title for an auto layer: drop the theme prefix and trailing date."""
    toks = table.split("_")[1:]
    if toks and re.fullmatch(r"[a-z]{0,4}\d{4}", toks[-1]):
        toks = toks[:-1]
    text = " ".join(toks)
    text = (text[:1].upper() + text[1:]) if text else table
    return prettify_acronyms(text)


def detect_label(columns):
    """Pick a hover-name column from a layer's columns (None if nothing fits)."""
    cols = set(columns)
    for c in ("name", "name_1"):
        if c in cols:
            return c, "Name"
    for c in columns:                       # ONS name fields: lsoa21nm, lad24nm…
        if c.endswith("nm"):
            return c, "Name"
    for c in ("pcds", "postcode"):
        if c in cols:
            return c, "Postcode"
    for c in columns:
        if c.endswith("name") or c.endswith("_name"):
            return c, "Name"
    return None, "Name"


def pick_window(cur, table, bbox=None):
    """First window (MK → South Downs) with any data; England overview otherwise."""
    for w in ("MK", "south_downs"):
        x0, y0, x1, y1 = WINDOWS[w]
        env = f"ST_MakeEnvelope({x0},{y0},{x1},{y1},27700)"
        cur.execute(f"SELECT 1 FROM {SCHEMA}.{table} "
                    f"WHERE geom && {env} AND ST_Intersects(geom,{env}) LIMIT 1")
        if cur.fetchone():
            return w
    return "england"


def build_specs(cur):
    """Curated pilot specs as overrides; single-colour previews for the rest."""
    curated = {s["table"]: s for s in PILOT}
    specs = []
    for lyr in read_layers(cur):
        if lyr["table"] in curated:
            spec = dict(curated[lyr["table"]])
        else:
            lbl, lbl_title = detect_label(lyr["columns"])
            spec = {"table": lyr["table"], "theme": lyr["theme"],
                    "colour_by": None, "ctype": "single",
                    "legend_title": humanise_title(lyr["table"])}
            if lbl:
                spec["label"], spec["label_title"] = lbl, lbl_title
        spec["gtype"] = lyr["gtype"]
        spec["est_rows"] = lyr.get("est_rows", 0)
        kind = kind_of(lyr["gtype"])
        heavy = kind == "line" or (kind == "polygon"
                                   and spec["est_rows"] > HEAVY_POLY_ROWS)
        # Render at full England extent when it earns its file size:
        #   * points — cheap (~1 MB sampled) and the national spread is the point;
        #   * non-heavy polygons that are actually coloured (a real choropleth).
        # A single-colour polygon at national extent is a uniform fill — no
        # information and ~16 MB for LSOA grain — so those stay windowed; they
        # promote to full extent automatically once a colour-by is assigned.
        full = kind == "point" or (kind == "polygon" and not heavy
                                   and spec.get("colour_by"))
        if full:
            spec["window"] = "england"
            spec.pop("bbox", None)
        elif spec.get("window"):
            pass                       # respect a curated window / bbox
        else:
            spec["window"] = pick_window(cur, lyr["table"], spec.get("bbox"))
        specs.append(spec)
    return specs


def main() -> None:
    with psycopg.connect(conninfo()) as conn, conn.cursor() as cur:
        specs = build_specs(cur)
        log.info("Rendering %d layer maps to %s", len(specs), OUT)
        ok = 0
        for spec in specs:
            try:
                ok += render(cur, spec)
            except Exception as exc:  # keep going; report the failure
                log.warning("  %s — FAILED: %s", spec["table"], exc)
        log.info("Done: %d/%d rendered.", ok, len(specs))


if __name__ == "__main__":
    main()
