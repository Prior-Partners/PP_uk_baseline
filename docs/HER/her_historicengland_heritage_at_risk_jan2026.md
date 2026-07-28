# Historic England Heritage at Risk Register (England), January 2026

<p class="layer-short">Heritage at risk</p>

`her_historicengland_heritage_at_risk_jan2026`

<img src="../../maps/her_historicengland_heritage_at_risk_jan2026.png" alt="Styling preview of her_historicengland_heritage_at_risk_jan2026" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

Published via planning.data.gov.uk (digital-land).

**SOURCE**

- Historic England, Heritage at Risk programme; distributed via planning.data.gov.uk (digital-land).

**DOCUMENTATION**

- Heritage at Risk                      : https://historicengland.org.uk/advice/heritage-at-risk/
- Heritage at Risk selection criteria   : https://historicengland.org.uk/listing/heritage-at-risk/search-register/selection-criteria/
- planning.data.gov.uk heritage-at-risk : https://www.planning.data.gov.uk/dataset/heritage-at-risk

**DEFINITIONS**

- "The Heritage at Risk Register includes buildings, places of worship, monuments, parks and gardens, conservation areas, battlefields and wreck sites that are listed and have been assessed and found to be at risk." (gov.uk, Heritage at Risk)

**SCOPE**

- England. 5,598 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type MultiPolygon.

**LICENCE**

- Open Government Licence v3.0. © Historic England.

**DATA QUALITY CAVEATS**

- The row count counts split pieces, not source features: this layer was split by Middle Layer Super Output Area, so it holds one row per feature per MSOA piece, plus whole and remainder rows to keep 100% of the source geometry. 6,614 rows represent 5,598 source features, measured 28 July 2026. `source_fid` identifies the originating feature.
- Geography keys are NULL on 145 of 6,614 rows, measured 28 July 2026: 130 fall inside an England or Wales district and could carry one, so their keys are a gap rather than an absence; 15 are residual fragments left by the MSOA split, each under 100 sqm or 10 m.
- County and Spatial Development Strategy columns are England and Wales only; rows elsewhere carry no county or SDS. Wales and the Isles of Scilly carry a county but no SDS. Rows with no Local Authority District code are NULL in all four columns.

**ENRICHMENT**

- `sds_name` / `sds_group` — Spatial Development Strategy area and devolution status, a Prior + Partners categorisation over Ministry of Housing, Communities and Local Government (MHCLG) English devolution policy, joined at load on the row's Local Authority District 2025 code via uk.ref_lad25_ctyua25_sds_lu_jul2026.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.

MSOA SPLIT (added 3 July 2026)

- Geometry split to one row per (source feature x MSOA 2021). Each row carries that MSOA's msoa21cd / msoa21nm / msoa21hclnm and best-fit lad22 / lad25. The source feature's original primary key is preserved as `source_fid`; `gid` is a fresh surrogate primary key. Features with no MSOA overlap (offshore or outside England & Wales) are kept whole with NULL geography columns.
- Keep-everything (3 July 2026): geometry outside every MSOA — offshore, estuarine, or beyond the generalised coastline — is retained as rows with NULL geography columns (source_fid links the parts), so the layer holds the complete source geometry.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `source_fid` | `bigint` | Primary key of the source feature in the pre-split layer uk.her_historicengland_heritage_at_risk_jan2026__preswap_jul03 (non-unique here: a feature spanning N MSOAs has N rows). |
| `fid_original` | `integer` |  |
| `dataset` | `character varying` |  |
| `end_date` | `character varying` |  |
| `entity` | `character varying` |  |
| `entry_date` | `date` |  |
| `name` | `character varying` |  |
| `organisation_entity` | `character varying` |  |
| `prefix` | `character varying` |  |
| `quality` | `character varying` |  |
| `reference` | `character varying` |  |
| `start_date` | `character varying` |  |
| `typology` | `character varying` |  |
| `documentation_url` | `character varying` |  |
| `rgn22cd` | `character varying` |  |
| `rgn22nm` | `character varying` |  |
| `area_ha` | `double precision` |  |
| `msoa21cd` | `character varying` | Middle Layer Super Output Area (MSOA) 2021 code of this piece. Open Government Licence v3.0. |
| `msoa21nm` | `character varying` | Official ONS MSOA 2021 name of this piece. Open Government Licence v3.0. |
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name of this piece. Open Parliament Licence. |
| `lad22cd` | `text` | Local Authority District 2022 code (2021 LAD geography, anchored to the MSOA 2021 name scoping), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad22nm` | `text` | Local Authority District 2022 name (2021 LAD geography), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25cd` | `text` | Local Authority District 2025 code (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `geom` | `geometry(MultiPolygon,27700)` |  |
| `gid` | `bigint` |  |
| `ctyua25cd` | `text` | County or unitary authority code at 1 April 2025. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `ctyua25nm` | `text` | County or unitary authority name at 1 April 2025. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `sds_name` | `text` | Spatial Development Strategy (SDS) area, a Prior + Partners categorisation over Ministry of Housing, Communities and Local Government (MHCLG) English devolution policy. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `sds_group` | `text` | Devolution status of the Spatial Development Strategy area: Existing Devolution Footprints, Devolution Priority Programme, Other Proposed Geographies or Remaining Areas. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
