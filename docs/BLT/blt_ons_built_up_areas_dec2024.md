# ONS Built Up Areas (BUA), England & Wales extent, December 2024

`blt_ons_built_up_areas_dec2024`

<iframe src="../../maps/blt_ons_built_up_areas_dec2024.html" title="Interactive preview map of blt_ons_built_up_areas_dec2024" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../../maps/blt_ons_built_up_areas_dec2024.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

**SOURCE**

- Office for National Statistics (ONS), Open Geography Portal. Underlying boundaries derived from Ordnance Survey (OS) Open Built Up Areas product.

**DOCUMENTATION**

- Dataset page : https://open-geography-portalx-ons.hub.arcgis.com/datasets/ons::built-up-areas-december-2024-boundaries-ew-bgg-v2
- ONS digital boundaries methods : https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries

**DEFINITIONS**

- BGG boundary type: "The built up area boundaries are generalised and created using an automated approach based on a 25m grid squares (BGG) and have been created from OS Open Built Up Areas." (data.gov.uk / ONS-OS background)
- Note: ONS does not formally document BGG on its digitalboundaries page (which covers BFE/BFC/BGC/BUC). BGG is specific to the Built Up Areas product family — automated 25m-grid generalisation.

**SCOPE**

- England & Wales.
- 7,775 distinct Built Up Areas represented across 121,072 polygon rows. The upstream geometry is multipolygon; the loader exploded each multipolygon BUA into single-part Polygon rows (avg ~15.6 parts per BUA).

**CRS**

- EPSG:27700 (British National Grid / BNG).

**LICENCE**

- Open Government Licence v3.0.

**DATA QUALITY CAVEATS**

- bua24cd is NOT unique per row — 7,775 distinct BUAs are exploded across 121,072 rows.
- areahectar is the whole-BUA area (constant across all rows sharing a bua24cd). area_ha is the area of THIS polygon part only.

**ENRICHMENT**

- lad22cd, lad22nm : spatial intersect with ONS 2022 LAD boundaries.
- wd21cd, wd21nm : spatial intersect with ONS 2021 Ward boundaries.
- area_ha : derived from geom at load (area in hectares, computed from the geometry at load). Per-part area. For whole-BUA area use areahectar (constant within a bua24cd group).

**LOADED INTO uk_baseline**

- Loaded November 2024.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `objectid` | `integer` | Source field "OBJECTID"; ArcGIS surrogate from upstream. |
| `gsscode` | `character varying(10)` | Source field "GSSCode"; ONS GSS code for the BUA (mirrors bua24cd). |
| `bua24cd` | `character varying(10)` | Source field "BUA24CD"; ONS GSS code for the Built Up Area (e.g. "E63011973"). NOT unique per row - see table comment. |
| `bua24nm` | `character varying(100)` | Source field "BUA24NM"; human-readable BUA name (English). |
| `bua24nmw` | `character varying(100)` | Source field "BUA24NMW"; human-readable BUA name (Welsh, populated where applicable). |
| `geometry_a` | `double precision` | Source field "Geometry_Area"; whole-BUA area. Unit: "square metres". Constant within a bua24cd group. |
| `areahectar` | `double precision` | Source field "AreaHectares"; whole-BUA area. Unit: "hectares". Constant within a bua24cd group. |
| `globalid` | `character varying(38)` | Source field "GlobalID"; ArcGIS GUID. |
| `id_original` | `integer` | Source numeric identifier preserved at load. |
| `lad22nm` | `character varying` | Joined at load from spatial intersection with ONS 2022 LAD boundaries; LAD name. |
| `lad22cd` | `character varying` | Joined at load from spatial intersection with ONS 2022 LAD boundaries; LAD GSS code. |
| `wd21nm` | `character varying` | Joined at load from spatial intersection with ONS 2021 Ward boundaries; Ward name. |
| `wd21cd` | `character varying` | Joined at load from spatial intersection with ONS 2021 Ward boundaries; Ward GSS code. |
| `area_ha` | `double precision` | Derived at load from ST_Area(geom)/10000 - area of THIS polygon part. Unit: "hectares". For whole-BUA area use areahectar. |
| `fid` | `bigint` |  |
| `geom` | `geometry(Polygon,27700)` | Source field "geometry"; Polygon in EPSG:27700 (British National Grid). |
| `gid` | `bigint` |  |
