# Ordnance Survey OS Open Greenspace for Great Britain, April 2025

`env_os_green_space_apr2025`

<img src="../../maps/env_os_green_space_apr2025.png" alt="Styling preview of env_os_green_space_apr2025" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Ordnance Survey (OS), OS Open Greenspace product.

**DOCUMENTATION**

- OS Open Greenspace : https://www.ordnancesurvey.co.uk/products/os-open-greenspace

**DEFINITIONS**

- "Information about publicly accessible urban green spaces across Great Britain. It includes parks, sports facilities and other recreational areas." (OS Open Greenspace product page)

**SCOPE**

- Great Britain. 196,619 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type MultiPolygon.

**LICENCE**

- OS OpenData Licence (incorporates Open Government Licence v3.0; attribution "Contains OS data © Crown copyright and database right" required).

**DATA QUALITY CAVEATS**

- The row count counts split pieces, not source features: this layer was split by Middle Layer Super Output Area, so it holds one row per feature per MSOA piece, plus whole and remainder rows to keep 100% of the source geometry. 215,806 rows represent 196,619 source features, measured 28 July 2026. `source_fid` identifies the originating feature.
- Geography keys are NULL on 22,325 of 215,806 rows, measured 28 July 2026: 244 fall inside an England or Wales district and could carry one, so their keys are a gap rather than an absence; 163 are residual fragments left by the MSOA split, each under 100 sqm or 10 m; 21,918 are in Scotland or Northern Ireland, outside the England and Wales lookup.
- County and Spatial Development Strategy columns are England and Wales only; rows elsewhere carry no county or SDS. Wales and the Isles of Scilly carry a county but no SDS. Rows with no Local Authority District code are NULL in all four columns.

**ENRICHMENT**

- `sds_name` / `sds_group` — Spatial Development Strategy area and devolution status, a Prior + Partners categorisation over Ministry of Housing, Communities and Local Government (MHCLG) English devolution policy, joined at load on the row's Local Authority District 2025 code via uk.ref_lad25_ctyua25_sds_lu_jul2026.
- Geometry split to one row per source feature per MSOA (2021).
- Each row carries that MSOA's `msoa21cd`, `msoa21nm`, `msoa21hclnm`, `lad22cd`, `lad22nm`, `lad25cd`, `lad25nm`.
- The source feature's original primary key is preserved as `source_fid`; `gid` is a fresh surrogate primary key.
- Features with no MSOA overlap (offshore or outside England & Wales) are kept whole, with NULL geography columns.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `source_fid` | `bigint` | Primary key of the source feature in the pre-split layer uk.env_os_green_space_apr2025__preswap_jul03 (non-unique here: a feature spanning N MSOAs has N rows). |
| `id` | `character varying` | Source field `id`; OS feature identifier (TOID). |
| `function` | `character varying` | Source field `function`; OS Open Greenspace function (site type). |
| `distname1` | `character varying` | Source field `distname1`; distinctive name 1 (site name; "None" where unnamed). |
| `distname2` | `character varying` | Source field `distname2`; distinctive name 2 (secondary name; "None" where none). |
| `distname3` | `character varying` | Source field `distname3`; distinctive name 3 (rarely populated). |
| `distname4` | `character varying` | Source field `distname4`; distinctive name 4 (rarely populated). |
| `fid_original` | `bigint` | Original source feature identifier, preserved at load. |
| `rgn22cd` | `character varying` | Region 2022 GSS code (nine English regions), assigned via the ONS Region lookup. Open Government Licence v3.0. |
| `rgn22nm` | `character varying` | Region 2022 name, assigned via the ONS Region lookup. Open Government Licence v3.0. |
| `area_ha` | `double precision` | Area of this row's geometry in hectares. |
| `msoa21cd` | `character varying` | Middle Layer Super Output Area (MSOA) 2021 code of this piece. Open Government Licence v3.0. |
| `msoa21nm` | `character varying` | Official ONS MSOA 2021 name of this piece. Open Government Licence v3.0. |
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name of this piece. Open Parliament Licence. |
| `lad22cd` | `text` | Local Authority District 2022 code (2021 LAD geography, anchored to the MSOA 2021 name scoping), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad22nm` | `text` | Local Authority District 2022 name (2021 LAD geography), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25cd` | `text` | Local Authority District 2025 code (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `geom` | `geometry(MultiPolygon,27700)` | OS Open Greenspace polygon geometry in EPSG:27700 (British National Grid); one part per MSOA (2021) after the split. |
| `gid` | `bigint` | Surrogate primary key, added at the MSOA split (see ENRICHMENT). |
| `ctyua25cd` | `text` | County or unitary authority code at 1 April 2025. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `ctyua25nm` | `text` | County or unitary authority name at 1 April 2025. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `sds_name` | `text` | Spatial Development Strategy (SDS) area, a Prior + Partners categorisation over Ministry of Housing, Communities and Local Government (MHCLG) English devolution policy. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `sds_group` | `text` | Devolution status of the Spatial Development Strategy area: Existing Devolution Footprints, Devolution Priority Programme, Other Proposed Geographies or Remaining Areas. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
