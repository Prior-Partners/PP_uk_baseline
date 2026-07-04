# Department for Transport (DfT) Bus Open Data Service (BODS) bus route polylines, Great Britain

`mob_dft_bods_bus_routes`

<img src="../../maps/mob_dft_bods_bus_routes.png" alt="Styling preview of mob_dft_bods_bus_routes" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Bus Open Data Service (BODS), Department for Transport (DfT). Per-row provenance in feed_source: "bods_gtfs_all" (national GTFS bundle) and "txc_fallback" (per-operator TransXChange datasets).

**DOCUMENTATION**

- Bus Open Data Service      : https://www.bus-data.dft.gov.uk/
- Find and use bus open data : https://www.gov.uk/guidance/find-and-use-bus-open-data
- GTFS schedule reference    : https://gtfs.org/documentation/schedule/reference/

**DEFINITIONS**

- "The Bus Open Data Service (BODS) provides bus timetable, vehicle location and fares data for every local bus service in England." (Department for Transport, Bus Open Data Service)

**SCOPE**

- Great Britain. 13,953 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type LineString.

**LICENCE**

- Open Government Licence v3.0.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.

MSOA SPLIT (added 4 July 2026)

- Geometry split to one row per (source feature x MSOA 2021). Each row carries that MSOA's msoa21cd / msoa21nm / msoa21hclnm and best-fit lad22 / lad25. The source feature's original primary key is preserved as `source_fid`; `gid` is a fresh surrogate primary key. Geometry outside every MSOA (offshore or outside England & Wales) is retained as rows with NULL geography columns, so the layer holds the complete source geometry.
- Route lines that traverse the same street more than once (out-and-back loops) are stored once per MSOA piece after the split: repeated linework within a route is merged by the geometric overlay, so summed piece length is about 1.4% below the pre-split total while every street a route uses remains fully represented. The pre-split encoding, with repeated traversals, is uk.mob_dft_bods_bus_routes__preswap_jul04.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `source_fid` | `integer` | Primary key of the source feature in the pre-split layer uk.mob_dft_bods_bus_routes__preswap_jul04 (non-unique here: a feature spanning N MSOAs has N rows). |
| `route_id` | `character varying(100)` |  |
| `gtfs_route_id` | `character varying(100)` |  |
| `gtfs_shape_id` | `character varying(100)` |  |
| `line_name` | `character varying(100)` |  |
| `route_long_name` | `character varying(500)` |  |
| `agency_id` | `character varying(50)` |  |
| `agency_name` | `character varying(500)` |  |
| `agency_noc` | `character varying(20)` |  |
| `stops_served` | `jsonb` |  |
| `stop_count` | `integer` |  |
| `geom_source` | `character varying(50)` |  |
| `total_distance_metres` | `numeric` |  |
| `route_class` | `character varying(20)` |  |
| `feed_source` | `character varying(50)` |  |
| `feed_loaded_at` | `timestamp without time zone` |  |
| `msoa21cd` | `character varying` | Middle Layer Super Output Area (MSOA) 2021 code of this piece. Open Government Licence v3.0. |
| `msoa21nm` | `character varying` | Official ONS MSOA 2021 name of this piece. Open Government Licence v3.0. |
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name of this piece. Open Parliament Licence. |
| `lad22cd` | `text` | Local Authority District 2022 code (2021 LAD geography, anchored to the MSOA 2021 name scoping), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad22nm` | `text` | Local Authority District 2022 name (2021 LAD geography), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25cd` | `text` | Local Authority District 2025 code (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `geom` | `geometry(MultiLineString,27700)` |  |
| `gid` | `bigint` |  |
