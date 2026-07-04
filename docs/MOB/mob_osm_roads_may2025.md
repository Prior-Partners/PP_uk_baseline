# OpenStreetMap roads for Great Britain, May 2025

<p class="layer-short">Roads</p>

`mob_osm_roads_may2025`

<img src="../../maps/mob_osm_roads_may2025.png" alt="Styling preview of mob_osm_roads_may2025" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- OpenStreetMap contributors, distributed as a roads extract (Geofabrik). The fclass road categories derive from OpenStreetMap highway tags.

**DOCUMENTATION**

- OpenStreetMap       : https://www.openstreetmap.org/about
- Geofabrik downloads : https://download.geofabrik.de/

**DEFINITIONS**

- OpenStreetMap is "the project that creates and distributes free geographic data for the world." (OpenStreetMap Wiki)

**SCOPE**

- Great Britain. 6,431,723 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type LineString.

**LICENCE**

- Open Database Licence (ODbL). (c) OpenStreetMap contributors.

MSOA SPLIT (added 4 July 2026)

- Geometry split to one row per (source feature x MSOA 2021). Each row carries that MSOA's msoa21cd / msoa21nm / msoa21hclnm and best-fit lad22 / lad25. The source feature's original primary key is preserved as `source_fid`; `gid` is a fresh surrogate primary key. Geometry outside every MSOA (offshore or outside England & Wales) is retained as rows with NULL geography columns, so the layer holds the complete source geometry.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `source_fid` | `bigint` | Primary key of the source feature in the pre-split layer uk.mob_osm_roads_may2025__preswap_jul04 (non-unique here: a feature spanning N MSOAs has N rows). |
| `osm_id` | `character varying(12)` |  |
| `code` | `integer` |  |
| `fclass` | `character varying(28)` |  |
| `name` | `character varying(100)` |  |
| `ref` | `character varying(20)` |  |
| `oneway` | `character varying(1)` |  |
| `maxspeed` | `integer` |  |
| `layer` | `bigint` |  |
| `bridge` | `character varying(1)` |  |
| `tunnel` | `character varying(1)` |  |
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
