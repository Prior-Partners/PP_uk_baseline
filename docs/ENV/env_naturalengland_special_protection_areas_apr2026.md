# Natural England Special Protection Areas (SPA) for England, April 2026

<p class="layer-short">Special Protection Areas</p>

`env_naturalengland_special_protection_areas_apr2026`

<img src="../../maps/env_naturalengland_special_protection_areas_apr2026.png" alt="Styling preview of env_naturalengland_special_protection_areas_apr2026" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Natural England, via the NE Open Data Hub (ArcGIS Online platform). Special Protection Areas (England) dataset. Designation authority: Joint Nature Conservation Committee (JNCC).

**DOCUMENTATION**

- NE Open Data Hub  : https://naturalengland-defra.opendata.arcgis.com/
- JNCC SPA overview : https://jncc.gov.uk/our-work/special-protection-areas-overview/

**DEFINITIONS**

- "Special Protection Areas (SPAs) are protected areas for birds in the UK classified under" the relevant regulations, for species "listed in Annex I of the Birds Directive (79/409/EEC as amended)." (JNCC, Special Protection Areas overview)

**SCOPE**

- England. 1,194 rows representing 88 distinct SPA sites; geometry is exploded to one polygon part per row.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type MultiPolygon.

**LICENCE**

- Open Government Licence v3.0. © Natural England.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.

MSOA SPLIT (added 3 July 2026)

- Geometry split to one row per (source feature x MSOA 2021). Each row carries that MSOA's msoa21cd / msoa21nm / msoa21hclnm and best-fit lad22 / lad25. The source feature's original primary key is preserved as `source_fid`; `gid` is a fresh surrogate primary key. Features with no MSOA overlap (offshore or outside England & Wales) are kept whole with NULL geography columns.
- Coastal note: MSOA coverage stops at the coastline (roughly Mean High Water), so split pieces retain 68.34% of the pre-split area of features that overlap an MSOA; 123 wholly marine sites are kept whole with NULL geography columns. The full pre-split extent is uk.env_naturalengland_special_protection_areas_apr2026__preswap_ju.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `source_fid` | `bigint` | Primary key of the source feature in the pre-split layer uk.env_naturalengland_special_protection_areas_apr2026__preswap_ju (non-unique here: a feature spanning N MSOAs has N rows). |
| `fid_original` | `integer` |  |
| `spa_name` | `character varying` |  |
| `spa_code` | `character varying` |  |
| `spa_area` | `double precision` |  |
| `grid_ref` | `character varying` |  |
| `easting` | `double precision` |  |
| `northing` | `double precision` |  |
| `latitude` | `character varying` |  |
| `longitude` | `character varying` |  |
| `name` | `character varying` |  |
| `status` | `character varying` |  |
| `id` | `double precision` |  |
| `file_` | `character varying` |  |
| `area` | `double precision` |  |
| `easting0` | `double precision` |  |
| `northing0` | `double precision` |  |
| `gis_date` | `character varying` |  |
| `version` | `integer` |  |
| `globalid` | `character varying` |  |
| `area_ha` | `double precision` |  |
| `rgn22cd` | `text` |  |
| `rgn22nm` | `text` |  |
| `sds_boundary` | `text` |  |
| `msoa21cd` | `character varying` | Middle Layer Super Output Area (MSOA) 2021 code of this piece. Open Government Licence v3.0. |
| `msoa21nm` | `character varying` | Official ONS MSOA 2021 name of this piece. Open Government Licence v3.0. |
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name of this piece. Open Parliament Licence. |
| `lad22cd` | `text` | Local Authority District 2022 code (2021 LAD geography, anchored to the MSOA 2021 name scoping), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad22nm` | `text` | Local Authority District 2022 name (2021 LAD geography), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25cd` | `text` | Local Authority District 2025 code (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `geom` | `geometry(MultiPolygon,27700)` |  |
| `gid` | `bigint` |  |
