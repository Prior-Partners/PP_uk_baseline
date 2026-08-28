# ONS gross value added (GVA) per filled job 2002-2023 and total GVA 2023 at Local Authority District, Prior + Partners edition, 2023

<p class="layer-short">GVA per filled job - LAD (P+P)</p>

`ecn_ons_lad_gross_value_added_pp_2023`

**SOURCE**

- Office for National Statistics (ONS). GVA per filled job: subregional productivity Table B3, file labourproductivitylad1.xls, downloaded 27 August 2026. Total GVA: copied from uk_baseline.ecn_ons_lad_gross_value_added_2023 (ONS small area GVA estimates, loaded May 2026).
- Prior + Partners processing, 27 August 2026: Table B3 per-filled-job values carried unaltered; total gross value added copied from the small-area-derived district layer. No published value altered.

**DOCUMENTATION**

- ONS subregional productivity : https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/labourproductivity/datasets/subregionalproductivitylabourproductivityindicesbylocalauthoritydistrict
- ONS small area GVA estimates : https://www.ons.gov.uk/economy/grossvalueaddedgva/datasets/uksmallareagvaestimates

**DEFINITIONS**

- "These data are annual subnational gross value added (GVA) disaggregated to lower layer super output areas (LSOA) in England and Wales, data zones (DZ) in Scotland, and super output areas (SOA) in Northern Ireland." (ONS)

**SCOPE**

- England and Wales. 318 districts. GVA per filled job 2002-2023; total GVA 2023.

**CRS**

- EPSG:27700 (British National Grid); source data is non-spatial, geometry joined from the boundary layer named on the geom column.

**LICENCE**

- Open Government Licence v3.0 (OGL v3.0).

**DATA QUALITY CAVEATS**

- GVA per filled job values are ONS-smoothed current-price estimates.
- Total GVA is in pounds million; GVA per filled job is in pounds. The two come from different ONS publications and are not derived from each other here.
- Wales and the Isles of Scilly carry a county but no Spatial Development Strategy area.

**ENRICHMENT**

- sds_name / sds_group - Spatial Development Strategy area and devolution status, a Prior + Partners categorisation over MHCLG English devolution policy, joined at enrichment via uk_baseline.adm_ons_lad_boundary_may2024.

**LOADED INTO uk_baseline**

- Loaded by PNC, 28 August 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `ladcd` | `character varying(9)` | Source field `LAD_Code` (ONS Table B3); current Local Authority District codes with Barnsley and Sheffield on their pre-2025 codes. |
| `ladnm` | `character varying(60)` | Source field `LAD_Name`. |
| `gva_per_job_2002` | `integer` | Unit: "Pounds". Source field `Pounds_2002` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2003` | `integer` | Unit: "Pounds". Source field `Pounds_2003` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2004` | `integer` | Unit: "Pounds". Source field `Pounds_2004` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2005` | `integer` | Unit: "Pounds". Source field `Pounds_2005` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2006` | `integer` | Unit: "Pounds". Source field `Pounds_2006` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2007` | `integer` | Unit: "Pounds". Source field `Pounds_2007` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2008` | `integer` | Unit: "Pounds". Source field `Pounds_2008` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2009` | `integer` | Unit: "Pounds". Source field `Pounds_2009` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2010` | `integer` | Unit: "Pounds". Source field `Pounds_2010` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2011` | `integer` | Unit: "Pounds". Source field `Pounds_2011` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2012` | `integer` | Unit: "Pounds". Source field `Pounds_2012` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2013` | `integer` | Unit: "Pounds". Source field `Pounds_2013` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2014` | `integer` | Unit: "Pounds". Source field `Pounds_2014` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2015` | `integer` | Unit: "Pounds". Source field `Pounds_2015` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2016` | `integer` | Unit: "Pounds". Source field `Pounds_2016` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2017` | `integer` | Unit: "Pounds". Source field `Pounds_2017` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2018` | `integer` | Unit: "Pounds". Source field `Pounds_2018` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2019` | `integer` | Unit: "Pounds". Source field `Pounds_2019` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2020` | `integer` | Unit: "Pounds". Source field `Pounds_2020` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2021` | `integer` | Unit: "Pounds". Source field `Pounds_2021` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2022` | `integer` | Unit: "Pounds". Source field `Pounds_2022` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_per_job_2023` | `integer` | Unit: "Pounds". Source field `Pounds_2023` (ONS Table B3, current price smoothed gross value added (balanced) per filled job). |
| `gva_total_2023_gbp_m` | `numeric` | Unit: "pounds million" (current prices). Copied from uk_baseline.ecn_ons_lad_gross_value_added_2023 field `gva_2023`. |
| `geom` | `geometry(MultiPolygon,27700)` | Geometry from uk_baseline.adm_ons_lad_boundary_may2024. |
| `fid` | `integer` |  |
| `lad25cd` | `text` | Local Authority District 2025 code (current administering authority). Joined at enrichment via uk_baseline.adm_ons_lad_boundary_may2024 on the row's district code. Open Government Licence v3.0. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority). Joined at enrichment via uk_baseline.adm_ons_lad_boundary_may2024 on the row's district code. Open Government Licence v3.0. |
| `ctyua25cd` | `text` | County or unitary authority code at 1 April 2025. Joined at enrichment via uk_baseline.adm_ons_lad_boundary_may2024 on the row's district code. Open Government Licence v3.0. |
| `ctyua25nm` | `text` | County or unitary authority name at 1 April 2025. Joined at enrichment via uk_baseline.adm_ons_lad_boundary_may2024 on the row's district code. Open Government Licence v3.0. |
| `sds_name` | `text` | Spatial Development Strategy (SDS) area, a Prior + Partners categorisation over Ministry of Housing, Communities and Local Government (MHCLG) English devolution policy. Joined at enrichment via uk_baseline.adm_ons_lad_boundary_may2024. Open Government Licence v3.0. |
| `sds_group` | `text` | Devolution status of the Spatial Development Strategy area: Existing Devolution Footprints, Devolution Priority Programme, Other Proposed Geographies or Remaining Areas. Joined at enrichment via uk_baseline.adm_ons_lad_boundary_may2024. Open Government Licence v3.0. |
