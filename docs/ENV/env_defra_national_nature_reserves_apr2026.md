# Defra - Department for Environment, Food and Rural Affairs — Environment Agency National Nature Reserves (NNRs) in England, April 2026

<p class="layer-short">National Nature Reserves</p>

`env_defra_national_nature_reserves_apr2026`

<img src="../../maps/env_defra_national_nature_reserves_apr2026.png" alt="Styling preview of env_defra_national_nature_reserves_apr2026" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Natural England (designating body), distributed under the Department for Environment, Food and Rural Affairs (Defra) family. Source dataset on the Natural England Open Data Hub.

**DOCUMENTATION**

- NE Open Data Hub : https://naturalengland-defra.opendata.arcgis.com/
- NE NNR landing   : https://www.gov.uk/government/publications/national-nature-reserves-in-england
- About NNRs       : https://www.gov.uk/government/publications/national-nature-reserves-in-england/national-nature-reserves-in-england

**DEFINITIONS**

- "National Nature Reserves (NNRs) are places where wildlife comes first. They were established to protect the most significant areas of habitat and of geological formations and to provide outdoor laboratories for research." (gov.uk NNR landing page)

**SCOPE**

- England. 299 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid).

**LICENCE**

- Open Government Licence v3.0. © Natural England.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.

MSOA SPLIT (added 3 July 2026)

- Geometry split to one row per (source feature x MSOA 2021). Each row carries that MSOA's msoa21cd / msoa21nm / msoa21hclnm and best-fit lad22 / lad25. The source feature's original primary key is preserved as `source_fid`; `gid` is a fresh surrogate primary key. Features with no MSOA overlap (offshore or outside England & Wales) are kept whole with NULL geography columns.
- Coastal note: MSOA coverage stops at the coastline (roughly Mean High Water); geometry beyond it is held in rows with NULL geography columns rather than dropped.
- Keep-everything (3 July 2026): geometry outside every MSOA — offshore, estuarine, or beyond the generalised coastline — is retained as rows with NULL geography columns (source_fid links the parts), so the layer holds the complete source geometry.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `source_fid` | `bigint` | Primary key of the source feature in the pre-split layer uk.env_defra_national_nature_reserves_apr2026__preswap_jul03 (non-unique here: a feature spanning N MSOAs has N rows). |
| `fid_original` | `integer` |  |
| `hyperlink` | `character varying` |  |
| `ref_code` | `character varying` |  |
| `name` | `character varying` |  |
| `measure` | `double precision` |  |
| `label` | `character varying` |  |
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
