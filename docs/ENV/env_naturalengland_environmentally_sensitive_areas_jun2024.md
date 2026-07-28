# Natural England Environmentally Sensitive Areas (ESA) for England, June 2024

<p class="layer-short">Environmentally Sensitive Areas</p>

`env_naturalengland_environmentally_sensitive_areas_jun2024`

<img src="../../maps/env_naturalengland_environmentally_sensitive_areas_jun2024.png" alt="Styling preview of env_naturalengland_environmentally_sensitive_areas_jun2024" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Natural England, via the NE Open Data Hub. Environmentally Sensitive Areas (England) dataset.

**DOCUMENTATION**

- NE Open Data Hub : https://naturalengland-defra.opendata.arcgis.com/

**DEFINITIONS**

- Environmentally Sensitive Areas (ESAs) are areas of particularly high landscape, wildlife or historic value where, from 1987, farmers were offered incentive payments to adopt agricultural practices that safeguard and enhance them. The scheme is now closed to new applicants. (data.gov.uk, Environmentally Sensitive Areas (England), Natural England)

**SCOPE**

- England. 12,669 rows (multiple polygon rows per ESA).

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type Polygon.

**LICENCE**

- Open Government Licence v3.0. © Natural England.

**DATA QUALITY CAVEATS**

- Geography keys are NULL on 754 of 12,669 rows, measured 28 July 2026: 659 fall inside an England or Wales district and could carry one, so their keys are a gap rather than an absence; 92 are residual fragments left by the MSOA split, each under 100 sqm or 10 m; 3 fall outside every district — offshore, inter-tidal, or beyond Great Britain.
- County and Spatial Development Strategy columns are England and Wales only; rows elsewhere carry no county or SDS. Wales and the Isles of Scilly carry a county but no SDS. Rows with no Local Authority District code are NULL in all four columns.

**ENRICHMENT**

- `sds_name` / `sds_group` — Spatial Development Strategy area and devolution status, a Prior + Partners categorisation over Ministry of Housing, Communities and Local Government (MHCLG) English devolution policy, joined at load on the row's Local Authority District 2025 code via uk.ref_lad25_ctyua25_sds_lu_jul2026.
- Geometry split to one row per source feature per MSOA (2021).
- Each row carries that MSOA's `msoa21cd`, `msoa21nm`, `msoa21hclnm`, `lad22cd`, `lad22nm`, `lad25cd`, `lad25nm`.
- The source feature's original primary key is preserved as `source_fid`; `gid` is a fresh surrogate primary key.
- Geometry outside every MSOA (offshore, estuarine, or beyond the coastline) is kept as rows with NULL geography columns, so the layer holds the complete source geometry.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `source_fid` | `bigint` | Primary key of the source feature in the pre-split layer uk.env_naturalengland_environmentally_sensitive_areas_jun2024__pre (non-unique here: a feature spanning N MSOAs has N rows). |
| `objectid` | `bigint` | Source feature identifier (Esri OBJECTID), repeated across a feature's per-MSOA split rows (matches `fid_original`). Not a domain key — use `gid`. |
| `ref_code` | `character varying` | Source field `ref_code`; ESA short code — e.g. "BR" (Broads), "SR" (Suffolk River Valleys), "LD" (Lake District). |
| `name` | `character varying` | Source field `name`; Environmentally Sensitive Area name (e.g. "BROADS", "LAKE DISTRICT"). |
| `measure` | `double precision` | Source field `measure`; area as recorded in the source. Unit: hectares. |
| `desig_date` | `character varying` | Source field `desig_date`; designation year (e.g. "1987"). |
| `hotlink` | `character varying` | Source field `hotlink`; URL of the (archived) Natural England ESA scheme page. |
| `fid_original` | `integer` | Original source feature identifier, preserved at load (matches `objectid`). |
| `wd21nm` | `character varying` | Electoral Ward 2021 name assigned to the feature. |
| `wd21cd` | `character varying` | Electoral Ward 2021 code assigned to the feature. |
| `fid` | `bigint` | Loader surrogate row identifier. Not a stable key — use `gid`. |
| `area_ha` | `double precision` | Area of this row's geometry in hectares. |
| `msoa21cd` | `character varying` | Middle Layer Super Output Area (MSOA) 2021 code of this piece. Open Government Licence v3.0. |
| `msoa21nm` | `character varying` | Official ONS MSOA 2021 name of this piece. Open Government Licence v3.0. |
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name of this piece. Open Parliament Licence. |
| `lad22cd` | `text` | Local Authority District 2022 code (2021 LAD geography, anchored to the MSOA 2021 name scoping), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad22nm` | `text` | Local Authority District 2022 name (2021 LAD geography), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25cd` | `text` | Local Authority District 2025 code (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `geom` | `geometry(MultiPolygon,27700)` | Environmentally Sensitive Area polygon geometry in EPSG:27700 (British National Grid); one part per MSOA (2021) after the split. |
| `gid` | `bigint` | Surrogate primary key, added at the MSOA split (see ENRICHMENT). |
| `ctyua25cd` | `text` | County or unitary authority code at 1 April 2025. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `ctyua25nm` | `text` | County or unitary authority name at 1 April 2025. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `sds_name` | `text` | Spatial Development Strategy (SDS) area, a Prior + Partners categorisation over Ministry of Housing, Communities and Local Government (MHCLG) English devolution policy. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `sds_group` | `text` | Devolution status of the Spatial Development Strategy area: Existing Devolution Footprints, Devolution Priority Programme, Other Proposed Geographies or Remaining Areas. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
