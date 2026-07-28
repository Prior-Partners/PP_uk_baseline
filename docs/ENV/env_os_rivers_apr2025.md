# Ordnance Survey OS Open Rivers — watercourse network for Great Britain, April 2025

<p class="layer-short">Open Rivers</p>

`env_os_rivers_apr2025`

<img src="../../maps/env_os_rivers_apr2025.png" alt="Styling preview of env_os_rivers_apr2025" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Ordnance Survey (OS), OS Open Rivers product.

**DOCUMENTATION**

- OS Open Rivers : https://www.ordnancesurvey.co.uk/products/os-open-rivers

**DEFINITIONS**

- "An open dataset of the high-level view of watercourses in Great Britain." (OS Open Rivers product page)

**SCOPE**

- Great Britain. 570,566 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type LineString.

**LICENCE**

- OS OpenData Licence (incorporates Open Government Licence v3.0; attribution "Contains OS data © Crown copyright and database right" required).

**DATA QUALITY CAVEATS**

- The row count counts split pieces, not source features: this layer was split by Middle Layer Super Output Area, so it holds one row per feature per MSOA piece, plus whole and remainder rows to keep 100% of the source geometry. 666,380 rows represent 570,566 source features, measured 28 July 2026. `source_fid` identifies the originating feature.
- Geography keys are NULL on 157,469 of 666,380 rows, measured 28 July 2026: 18,424 fall inside an England or Wales district and could carry one, so their keys are a gap rather than an absence; 3,844 are residual fragments left by the MSOA split, each under 100 sqm or 10 m; 134,711 are in Scotland or Northern Ireland, outside the England and Wales lookup; 490 fall outside every district — offshore, inter-tidal, or beyond Great Britain.
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
| `source_fid` | `bigint` | Primary key of the source feature in the pre-split layer uk.env_os_rivers_apr2025__preswap_jul04 (non-unique here: a feature spanning N MSOAs has N rows). |
| `name1` | `character varying` | Source field `name1`; watercourse name (e.g. "River Avon"; "None" where unnamed). |
| `identifier` | `character varying` | Source field `identifier`; OS feature identifier (TOID). |
| `startnode` | `character varying` | Source field `startnode`; identifier of the start node of the reach. |
| `endnode` | `character varying` | Source field `endnode`; identifier of the end node of the reach. |
| `form` | `character varying` | Source field `form`; watercourse form (e.g. inland river, tidal river, canal). |
| `flow` | `character varying` | Source field `flow`; direction of flow along the reach. |
| `fictitious` | `character varying` | Source field `fictitious`; flag for fictitious (non-physical) links that complete the network. |
| `length` | `bigint` | Source field `length`; reach length as recorded in the source. Unit: metres. |
| `name2` | `character varying` | Source field `name2`; alternative / Welsh name (e.g. "Afon Hafren"; "None" where none). |
| `fid_original` | `integer` | Original source feature identifier, preserved at load. |
| `wd21nm` | `character varying` | Electoral Ward 2021 name assigned to the feature. |
| `wd21cd` | `character varying` | Electoral Ward 2021 code assigned to the feature. |
| `length_m` | `double precision` | Length of this row's line geometry in metres. |
| `msoa21cd` | `character varying` | Middle Layer Super Output Area (MSOA) 2021 code of this piece. Open Government Licence v3.0. |
| `msoa21nm` | `character varying` | Official ONS MSOA 2021 name of this piece. Open Government Licence v3.0. |
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name of this piece. Open Parliament Licence. |
| `lad22cd` | `text` | Local Authority District 2022 code (2021 LAD geography, anchored to the MSOA 2021 name scoping), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad22nm` | `text` | Local Authority District 2022 name (2021 LAD geography), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25cd` | `text` | Local Authority District 2025 code (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `geom` | `geometry(MultiLineString,27700)` | OS Open Rivers watercourse line geometry in EPSG:27700 (British National Grid); one part per MSOA (2021) after the split. |
| `gid` | `bigint` | Surrogate primary key, added at the MSOA split (see ENRICHMENT). |
| `ctyua25cd` | `text` | County or unitary authority code at 1 April 2025. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `ctyua25nm` | `text` | County or unitary authority name at 1 April 2025. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `sds_name` | `text` | Spatial Development Strategy (SDS) area, a Prior + Partners categorisation over Ministry of Housing, Communities and Local Government (MHCLG) English devolution policy. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `sds_group` | `text` | Devolution status of the Spatial Development Strategy area: Existing Devolution Footprints, Devolution Priority Programme, Other Proposed Geographies or Remaining Areas. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
