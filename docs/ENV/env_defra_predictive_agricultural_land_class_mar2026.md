# Defra - Department for Environment, Food and Rural Affairs Predictive Agricultural Land Classification (ALC) for England, March 2026

<p class="layer-short">Predictive Agricultural Land</p>

`env_defra_predictive_agricultural_land_class_mar2026`

<img src="../../maps/env_defra_predictive_agricultural_land_class_mar2026.png" alt="Styling preview of env_defra_predictive_agricultural_land_class_mar2026" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Department for Environment, Food and Rural Affairs (Defra). Predictive ALC product.

**DOCUMENTATION**

- ALC concept guidance : https://www.gov.uk/government/publications/agricultural-land-classification-of-england-and-wales/agricultural-land-classification-of-england-and-wales

**DEFINITIONS**

- "Agricultural Land Classification (ALC) provides a method for assessing the quality of farmland to enable informed choices to be made about its future use within the planning system." (Defra ALC guidance)

**SCOPE**

- England. 953,652 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid).

**LICENCE**

- Open Government Licence v3.0. © Defra.

**DATA QUALITY CAVEATS**

- Predictive / modelled: every grade (1, 2, 3a, 3b, 4, 5, NA, U) is a prediction of likely ALC, not a field survey. Use for screening; confirm with a site survey for planning decisions.
- RELATED: for the authoritative surveyed classification (Natural England, grades 1–5), see uk_baseline.env_naturalengland_agricultural_land_class_nov2024.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.

MSOA SPLIT (added 3 July 2026)

- Geometry split to one row per (source feature x MSOA 2021). Each row carries that MSOA's msoa21cd / msoa21nm / msoa21hclnm and best-fit lad22 / lad25. The source feature's original primary key is preserved as `source_fid`; `gid` is a fresh surrogate primary key. Features with no MSOA overlap (offshore or outside England & Wales) are kept whole with NULL geography columns.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `source_fid` | `bigint` | Primary key of the source feature in the pre-split layer uk.env_defra_predictive_agricultural_land_class_mar2026__preswap_j (non-unique here: a feature spanning N MSOAs has N rows). |
| `id` | `integer` |  |
| `fid_original` | `bigint` |  |
| `alcgrade` | `bigint` |  |
| `alc` | `character varying(2)` |  |
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
