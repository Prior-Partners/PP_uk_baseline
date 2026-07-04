# Ordnance Survey OS Open Roads - road network for Great Britain, April 2025

<p class="layer-short">Open Roads</p>

`mob_os_open_roads_apr2025`

<img src="../../maps/mob_os_open_roads_apr2025.png" alt="Styling preview of mob_os_open_roads_apr2025" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Ordnance Survey (OS), OS Open Roads product.

**DOCUMENTATION**

- OS Open Roads : https://www.ordnancesurvey.co.uk/products/os-open-roads

**DEFINITIONS**

- "A structured link-and-node network, which represents the central alignment of all classified and unclassified roads in Great Britain." (Ordnance Survey, OS Open Roads)

**SCOPE**

- Great Britain. 4,207,717 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type LineString.

**LICENCE**

- OS OpenData Licence (incorporates Open Government Licence v3.0; attribution "Contains OS data (c) Crown copyright and database right" required).

MSOA SPLIT (added 4 July 2026)

- Geometry split to one row per (source feature x MSOA 2021). Each row carries that MSOA's msoa21cd / msoa21nm / msoa21hclnm and best-fit lad22 / lad25. The source feature's original primary key is preserved as `source_fid`; `gid` is a fresh surrogate primary key. Geometry outside every MSOA (offshore or outside England & Wales) is retained as rows with NULL geography columns, so the layer holds the complete source geometry.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `source_fid` | `bigint` | Primary key of the source feature in the pre-split layer uk.mob_os_open_roads_apr2025__preswap_jul04 (non-unique here: a feature spanning N MSOAs has N rows). |
| `id` | `character varying` |  |
| `fictitious` | `boolean` |  |
| `road_classification` | `character varying` |  |
| `road_function` | `character varying` |  |
| `form_of_way` | `character varying` |  |
| `road_classification_number` | `character varying` |  |
| `name_1` | `character varying` |  |
| `name_1_lang` | `character varying` |  |
| `name_2` | `character varying` |  |
| `name_2_lang` | `character varying` |  |
| `road_structure` | `character varying` |  |
| `length` | `double precision` |  |
| `length_uom` | `character varying` |  |
| `loop` | `boolean` |  |
| `primary_route` | `boolean` |  |
| `trunk_road` | `boolean` |  |
| `start_node` | `character varying` |  |
| `end_node` | `character varying` |  |
| `road_number_toid` | `character varying` |  |
| `road_name_toid` | `character varying` |  |
| `fid_original` | `integer` |  |
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
