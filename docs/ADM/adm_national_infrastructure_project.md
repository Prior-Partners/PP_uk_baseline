# adm_national_infrastructure_project

<p class="layer-short">National Infrastructure Projects</p>

`adm_national_infrastructure_project`

<img src="../../maps/adm_national_infrastructure_project.png" alt="Styling preview of adm_national_infrastructure_project" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**DATA QUALITY CAVEATS**

- Project boundaries overlap one another, so summing area_ha across the rows in an MSOA counts shared land more than once and can exceed the MSOA's own area. Dissolve the geometry before computing a coverage share.
- County and Spatial Development Strategy columns are England and Wales only; rows elsewhere carry no county or SDS. Wales and the Isles of Scilly carry a county but no SDS. Rows with no Local Authority District code are NULL in all four columns.
- Geometry split to one row per source feature and MSOA 2021 piece on 5 August 2026. The source feature's primary key is preserved as `source_fid` and is non-unique here: a project spanning N MSOAs has N rows. `gid` is a fresh surrogate primary key. Row count 351 before the split, 2,273 after.
- `area_ha` is the whole project's area, carried unchanged onto every piece. It is NOT the area of the piece, and summing it across rows does not give a meaningful total. It was deliberately not recomputed, because that would change a published numeric value.
- 121 rows carry no MSOA or district geography. These hold the parts of a project lying outside every MSOA, which for this layer is predominantly marine: MSOA and district boundaries stop at the coast, while offshore energy projects extend well beyond it. They account for 6,109,662 ha of the 6,745,096 ha total, so most of this layer's area sits offshore and carries no geography key by construction. 116 of the 121 touch the coastline; 5 lie wholly offshore.
- Geometry is conserved at 100.000% against the pre-split layer: the split neither gained nor lost measurable area.

**ENRICHMENT**

- `sds_name` / `sds_group` — Spatial Development Strategy area and devolution status, a Prior + Partners categorisation over Ministry of Housing, Communities and Local Government (MHCLG) English devolution policy, joined at load on the row's Local Authority District 2025 code via uk.ref_lad25_ctyua25_sds_lu_jul2026.
- msoa21cd, msoa21nm, msoa21hclnm, lad22cd, lad22nm, lad25cd, lad25nm from the MSOA 2021 boundary each piece falls in; ctyua25cd, ctyua25nm, sds_name, sds_group joined from the LAD 2025 lookup.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `source_fid` | `bigint` | Primary key of the source feature in uk_baseline.adm_national_infrastructure_project (non-unique here: a feature spanning N MSOAs has N rows). |
| `case_reference` | `text` |  |
| `project_name` | `text` |  |
| `file_name` | `text` |  |
| `received_date` | `timestamp with time zone` |  |
| `area_ha` | `double precision` | Area in hectares of this row's own geometry, computed at load from the EPSG:27700 geometry. On layers split by Middle Layer Super Output Area this is the area of the piece inside its MSOA, not the area of the whole source feature. |
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
| `msoa_area_ha` | `double precision` | Area in hectares of the Middle Layer Super Output Area this row falls in, computed from uk_baseline.adm_ons_msoa_boundary_2021 — the same boundary the layer was split against. Provided as the denominator for MSOA coverage shares. NULL wherever msoa21cd is NULL. Open Government Licence v3.0. |
