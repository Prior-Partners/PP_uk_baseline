# Natural England Ancient Woodland Inventory (England), March 2026

<p class="layer-short">Ancient Woodland</p>

`env_naturalengland_ancient_woodland_mar2026`

<img src="../../maps/env_naturalengland_ancient_woodland_mar2026.png" alt="Styling preview of env_naturalengland_ancient_woodland_mar2026" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Natural England, via the NE Open Data Hub. Ancient Woodland (England) dataset.

**DOCUMENTATION**

- NE Open Data Hub          : https://naturalengland-defra.opendata.arcgis.com/
- Ancient woodland guidance : https://www.gov.uk/guidance/ancient-woodland-and-veteran-trees-protection-surveys-licences

**DEFINITIONS**

- "Ancient woodland is an area that has been wooded continuously since at least 1600AD." (data.gov.uk, Ancient Woodland (England), Natural England)

**SCOPE**

- England. 55,647 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type MultiPolygon.

**LICENCE**

- Open Government Licence v3.0. © Natural England.

**DATA QUALITY CAVEATS**

- Some areas overlap with env_naturalengland_ancient_woodland_revised_apr2026 (the revised inventory); the two datasets are not mutually exclusive.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.

MSOA SPLIT (added 3 July 2026)

- Geometry split to one row per (source feature x MSOA 2021). Each row carries that MSOA's msoa21cd / msoa21nm / msoa21hclnm and best-fit lad22 / lad25. The source feature's original primary key is preserved as `source_fid`; `gid` is a fresh surrogate primary key. Features with no MSOA overlap (offshore or outside England & Wales) are kept whole with NULL geography columns.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `source_fid` | `bigint` | Primary key of the source feature in the pre-split layer uk.env_naturalengland_ancient_woodland_mar2026__preswap_jul03 (non-unique here: a feature spanning N MSOAs has N rows). |
| `fid_original` | `integer` |  |
| `name` | `character varying` |  |
| `theme` | `character varying` |  |
| `themname` | `character varying` |  |
| `themid` | `double precision` |  |
| `status` | `character varying` |  |
| `perimeter` | `double precision` |  |
| `area` | `double precision` |  |
| `x_coord` | `integer` |  |
| `y_coord` | `integer` |  |
| `globalid` | `character varying` |  |
| `area_ha` | `double precision` |  |
| `rgn22cd` | `text` |  |
| `rgn22nm` | `text` |  |
| `sds_boundary` | `text` |  |
| `layer` | `character(100)` |  |
| `msoa21cd` | `character varying` | Middle Layer Super Output Area (MSOA) 2021 code of this piece. Open Government Licence v3.0. |
| `msoa21nm` | `character varying` | Official ONS MSOA 2021 name of this piece. Open Government Licence v3.0. |
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name of this piece. Open Parliament Licence. |
| `lad22cd` | `text` | Local Authority District 2022 code (2021 LAD geography, anchored to the MSOA 2021 name scoping), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad22nm` | `text` | Local Authority District 2022 name (2021 LAD geography), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25cd` | `text` | Local Authority District 2025 code (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `geom` | `geometry(MultiPolygon,27700)` |  |
| `gid` | `bigint` |  |
