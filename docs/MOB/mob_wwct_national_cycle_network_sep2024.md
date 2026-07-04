# National Cycle Network (NCN) for the United Kingdom, September 2024

<p class="layer-short">National Cycle Network</p>

`mob_wwct_national_cycle_network_sep2024`

<img src="../../maps/mob_wwct_national_cycle_network_sep2024.png" alt="Styling preview of mob_wwct_national_cycle_network_sep2024" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Sustrans (now Walk Wheel Cycle Trust). National Cycle Network dataset, distributed via the Sustrans open-data hub.

**DOCUMENTATION**

- Sustrans open data     : https://data-sustrans-uk.opendata.arcgis.com/
- National Cycle Network : https://www.walkwheelcycletrust.org.uk/national-cycle-network/

**DEFINITIONS**

- The National Cycle Network is "a UK-wide network of signed paths and routes for walking, wheeling, cycling and exploring outdoors, brought to you by Walk Wheel Cycle Trust." (Walk Wheel Cycle Trust, National Cycle Network)

**SCOPE**

- United Kingdom. 46,248 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type LineString.

**LICENCE**

- Open Government Licence v3.0 (confirm with Sustrans / Walk Wheel Cycle Trust before re-publication).

MSOA SPLIT (added 4 July 2026)

- Geometry split to one row per (source feature x MSOA 2021). Each row carries that MSOA's msoa21cd / msoa21nm / msoa21hclnm and best-fit lad22 / lad25. The source feature's original primary key is preserved as `source_fid`; `gid` is a fresh surrogate primary key. Geometry outside every MSOA (offshore or outside England & Wales) is retained as rows with NULL geography columns, so the layer holds the complete source geometry.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `source_fid` | `bigint` | Primary key of the source feature in the pre-split layer uk.mob_wwct_national_cycle_network_sep2024__preswap_jul04 (non-unique here: a feature spanning N MSOAs has N rows). |
| `desc_` | `character varying(200)` |  |
| `greenway` | `character varying(3)` |  |
| `routetype` | `character varying(4)` |  |
| `routeno` | `integer` |  |
| `linkno` | `integer` |  |
| `routecat` | `character varying(19)` |  |
| `openstatus` | `character varying(23)` |  |
| `surface` | `character varying(13)` |  |
| `quality` | `character varying(10)` |  |
| `lighting` | `character varying(7)` |  |
| `roadclass` | `character varying(32)` |  |
| `globalid` | `character varying(38)` |  |
| `segmentid` | `integer` |  |
| `id_original` | `integer` |  |
| `wd21nm` | `character varying` |  |
| `wd21cd` | `character varying` |  |
| `length_m` | `double precision` |  |
| `msoa21cd` | `character varying` | Middle Layer Super Output Area (MSOA) 2021 code of this piece. Open Government Licence v3.0. |
| `msoa21nm` | `character varying` | Official ONS MSOA 2021 name of this piece. Open Government Licence v3.0. |
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name of this piece. Open Parliament Licence. |
| `lad22cd` | `text` | Local Authority District 2022 code (2021 LAD geography, anchored to the MSOA 2021 name scoping), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad22nm` | `text` | Local Authority District 2022 name (2021 LAD geography), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25cd` | `text` | Local Authority District 2025 code (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `geom` | `geometry(MultiLineString,27700)` |  |
| `gid` | `bigint` |  |
