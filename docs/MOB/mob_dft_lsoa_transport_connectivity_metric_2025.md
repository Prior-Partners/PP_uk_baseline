# Department for Transport (DfT) transport connectivity metric, Lower layer Super Output Area (LSOA) scores, England & Wales, September 2025

<p class="layer-short">Transport Connectivity 2025 (LSOA)</p>

`mob_dft_lsoa_transport_connectivity_metric_2025`

**SOURCE**

- Department for Transport (DfT). Transport connectivity metric, workbook "Connectivity metrics 2025" (connectivity_metrics_2025.ods, 68,164,574 bytes), sheet LSOA, published 29 September 2025. All 35 score columns copied as published; nothing derived or filtered. Columns carry short readable names; the source header is recorded in every column comment.

**DOCUMENTATION**

- Publication page : https://www.gov.uk/government/publications/transport-connectivity-metric
- Methodology      : https://www.gov.uk/government/publications/transport-connectivity-metric/transport-connectivity-metric
- Data file        : https://assets.publishing.service.gov.uk/media/68c966fc07d9e92bc5517b80/connectivity_metrics_2025.ods
- Metadata         : Metadata sheet inside the workbook (definitions of modes, purposes and scores)

**DEFINITIONS**

- "The metric defines connectivity as someone’s ability to get where they want to go. It measures opportunity to travel to various destinations, weighted by people’s overall proclivity to take those options." (DfT publication page)
- "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet)
- Scores are scaled so that the starting location (Output Area centroid) with the best score in England and Wales receives 100 and every other area a score relative to it; a score of 50 is half as connected as the best location (DfT methodology).
- "The public transport mode is defined as trips that involve combinations of 2 or more of the following: walking, bus, rail, light rail, underground and ferry." (DfT methodology)
- Overall scores: "a true overall score is calculated across all modes, purposes and times of day, excluding driving, to represent sustainable modes of transportation." (DfT methodology) The overall score weights public transport about 52%, walking 40% and cycling 8% (DfT methodology).
- "In this report, where scores are presented at the LSOA/LA level, these consist of population-weighted averages across all OAs within the LSOA/LA." (DfT methodology)
- "A cut-off point has been set for a maximum travel time of 60 minutes." (DfT methodology)

**SCOPE**

- England and Wales. 35,672 rows, one per Lower layer Super Output Area (LSOA) 2021 (England 33,755; Wales 1,917): every Lower layer Super Output Area (LSOA) in uk_baseline.adm_ons_lsoa_boundary_2021.
- Reference period October to December 2024 (DfT workbook Metadata sheet). Destination data are a mix of Q4 2024 and Q1 2025, except jobs, which use 2023 provisional Business Register and Employment Survey (BRES) figures (DfT methodology).

**CRS**

- EPSG:27700 (British National Grid). The source sheet has no geometry; geometry is copied from uk_baseline.adm_ons_lsoa_boundary_2021 by matching `LSOA21CD` to lsoa21cd. No reprojection.

**LICENCE**

- Open Government Licence v3.0 (DfT publication page). The workbook's own Metadata sheet leaves its licence field as TBA.

**DATA QUALITY CAVEATS**

- County and Spatial Development Strategy columns are England and Wales only; rows elsewhere carry no county or SDS. Wales and the Isles of Scilly carry a county but no SDS. Rows with no Local Authority District code are NULL in all four columns.
- Released as Experimental Statistics (DfT workbook Metadata sheet); the methodology calls these results provisional.
- Scores are relative to the best-connected location in England and Wales, not travel times or counts. The workbook's usage notes say scores should be interpreted relative to other areas and that different transport modes should not be directly compared.
- For public transport the employment column is headed Business (public transport) in the source, where the other modes say Employment. It is carried under the publisher's label as business_public_transport; DfT does not explain the difference.
- 331 score cells across 8 columns are exactly 0 (289 of them in Healthcare (walking)). The publisher does not state what a score of 0 represents; the values are loaded as published.
- Geography keys (MSOA 2021, LAD 2022, LAD 2025, county) filled on all 35,672 rows, measured 23 September 2026 (exact join on `lsoa21cd`). The SDS columns are NULL on 1,918 rows by design: 1,917 in Wales and 1 in the Isles of Scilly.

**ENRICHMENT**

- `sds_name` / `sds_group` — Spatial Development Strategy area and devolution status, a Prior + Partners categorisation over Ministry of Housing, Communities and Local Government (MHCLG) English devolution policy, joined at load on the row's Local Authority District 2025 code via uk.ref_lad25_ctyua25_sds_lu_jul2026.
- `msoa21hclnm` — House of Commons Library readable MSOA name, joined at load on lsoa21cd via the ONS 2021 output-area hierarchy (uk_baseline.adm_ons_msoa_boundary_2021). Open Parliament Licence.

**NOT IN THIS DATASET**

- The workbook's Region sheet (nine English regions and Wales) is not loaded: uk_baseline holds no region boundary.
- The workbook Metadata sheet defines deciles, but the published sheets carry scores only.
- The 100-metre grid scores behind the DfT Connectivity Tool, and scores by time of day, are not published in this workbook.

**LOADED INTO uk_baseline**

- Loaded by PNC, 23 September 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `gid` | `integer` |  |
| `lsoa21cd` | `character varying(9)` | Source field `LSOA21CD`; Lower layer Super Output Area (LSOA) 2021 code. |
| `employment_walking` | `double precision` | Source field `Employment (walking)`; purpose employment: jobs, from 2023 provisional Business Register and Employment Survey (BRES) figures; mode "walking: Travel by foot". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `education_walking` | `double precision` | Source field `Education (walking)`; purpose "education: Travel to schools and educational facilities"; mode "walking: Travel by foot". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `healthcare_walking` | `double precision` | Source field `Healthcare (walking)`; purpose "health: Travel to healthcare facilities"; mode "walking: Travel by foot". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `leisure_walking` | `double precision` | Source field `Leisure and Community (walking)`; purpose "leisure and community : Travel to entertainment and public activity venues"; mode "walking: Travel by foot". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `shopping_walking` | `double precision` | Source field `Shopping (walking)`; purpose "shopping: Travel to retail locations"; mode "walking: Travel by foot". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `residential_walking` | `double precision` | Source field `Residential (walking)`; purpose "residential: Travel to residential addresses for social purposes"; mode "walking: Travel by foot". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `overall_walking` | `double precision` | Source field `Overall (walking)`; purpose overall: all purposes combined; mode "walking: Travel by foot". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `employment_cycling` | `double precision` | Source field `Employment (cycling)`; purpose employment: jobs, from 2023 provisional Business Register and Employment Survey (BRES) figures; mode "cycling: Bicycle transport". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `education_cycling` | `double precision` | Source field `Education (cycling)`; purpose "education: Travel to schools and educational facilities"; mode "cycling: Bicycle transport". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `healthcare_cycling` | `double precision` | Source field `Healthcare (cycling)`; purpose "health: Travel to healthcare facilities"; mode "cycling: Bicycle transport". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `leisure_cycling` | `double precision` | Source field `Leisure and Community (cycling)`; purpose "leisure and community : Travel to entertainment and public activity venues"; mode "cycling: Bicycle transport". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `shopping_cycling` | `double precision` | Source field `Shopping (cycling)`; purpose "shopping: Travel to retail locations"; mode "cycling: Bicycle transport". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `residential_cycling` | `double precision` | Source field `Residential (cycling)`; purpose "residential: Travel to residential addresses for social purposes"; mode "cycling: Bicycle transport". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `overall_cycling` | `double precision` | Source field `Overall (cycling)`; purpose overall: all purposes combined; mode "cycling: Bicycle transport". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `business_public_transport` | `double precision` | Source field `Business (public transport)`; purpose headed Business in the source where the other modes say Employment; DfT does not explain the difference; mode "public transport: Bus, train, and other public transport services". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `education_public_transport` | `double precision` | Source field `Education (public transport)`; purpose "education: Travel to schools and educational facilities"; mode "public transport: Bus, train, and other public transport services". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `healthcare_public_transport` | `double precision` | Source field `Healthcare (public transport)`; purpose "health: Travel to healthcare facilities"; mode "public transport: Bus, train, and other public transport services". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `leisure_public_transport` | `double precision` | Source field `Leisure and Community (public transport)`; purpose "leisure and community : Travel to entertainment and public activity venues"; mode "public transport: Bus, train, and other public transport services". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `shopping_public_transport` | `double precision` | Source field `Shopping (public transport)`; purpose "shopping: Travel to retail locations"; mode "public transport: Bus, train, and other public transport services". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `residential_public_transport` | `double precision` | Source field `Residential (public transport)`; purpose "residential: Travel to residential addresses for social purposes"; mode "public transport: Bus, train, and other public transport services". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `overall_public_transport` | `double precision` | Source field `Overall (public transport)`; purpose overall: all purposes combined; mode "public transport: Bus, train, and other public transport services". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `employment_driving` | `double precision` | Source field `Employment (driving)`; purpose employment: jobs, from 2023 provisional Business Register and Employment Survey (BRES) figures; mode "car: Private car transport". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `education_driving` | `double precision` | Source field `Education (driving)`; purpose "education: Travel to schools and educational facilities"; mode "car: Private car transport". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `healthcare_driving` | `double precision` | Source field `Healthcare (driving)`; purpose "health: Travel to healthcare facilities"; mode "car: Private car transport". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `leisure_driving` | `double precision` | Source field `Leisure and Community (driving)`; purpose "leisure and community : Travel to entertainment and public activity venues"; mode "car: Private car transport". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `shopping_driving` | `double precision` | Source field `Shopping (driving)`; purpose "shopping: Travel to retail locations"; mode "car: Private car transport". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `residential_driving` | `double precision` | Source field `Residential (driving)`; purpose "residential: Travel to residential addresses for social purposes"; mode "car: Private car transport". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `overall_driving` | `double precision` | Source field `Overall (driving)`; purpose overall: all purposes combined; mode "car: Private car transport". Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `employment_overall` | `double precision` | Source field `Employment (overall)`; purpose employment: jobs, from 2023 provisional Business Register and Employment Survey (BRES) figures; mode overall: walking, cycling and public transport combined, driving excluded. Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `education_overall` | `double precision` | Source field `Education (overall)`; purpose "education: Travel to schools and educational facilities"; mode overall: walking, cycling and public transport combined, driving excluded. Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `healthcare_overall` | `double precision` | Source field `Healthcare (overall)`; purpose "health: Travel to healthcare facilities"; mode overall: walking, cycling and public transport combined, driving excluded. Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `leisure_overall` | `double precision` | Source field `Leisure and Community (overall)`; purpose "leisure and community : Travel to entertainment and public activity venues"; mode overall: walking, cycling and public transport combined, driving excluded. Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `shopping_overall` | `double precision` | Source field `Shopping (overall)`; purpose "shopping: Travel to retail locations"; mode overall: walking, cycling and public transport combined, driving excluded. Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `residential_overall` | `double precision` | Source field `Residential (overall)`; purpose "residential: Travel to residential addresses for social purposes"; mode overall: walking, cycling and public transport combined, driving excluded. Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `overall` | `double precision` | Source field `Overall`; purpose overall: all purposes combined; mode overall: walking, cycling and public transport combined, driving excluded. Unit: "connectivity scores range from 0 to 100, where 100 represents the highest level of connectivity." (DfT workbook Metadata sheet) |
| `geom` | `geometry(MultiPolygon,27700)` | Geometry from uk_baseline.adm_ons_lsoa_boundary_2021, matched on `LSOA21CD`. |
| `msoa21cd` | `text` | Middle Layer Super Output Area (MSOA) 2021 code of the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at load on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021, then uk_baseline.adm_ons_msoa_boundary_2021. Open Government Licence v3.0. |
| `msoa21nm` | `text` | Official Office for National Statistics MSOA 2021 name of the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at load on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021, then uk_baseline.adm_ons_msoa_boundary_2021. Open Government Licence v3.0. |
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name of the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at load on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021, then uk_baseline.adm_ons_msoa_boundary_2021, which carries the House of Commons Library name. Open Parliament Licence. |
| `lad22cd` | `text` | Local Authority District 2022 code (2021 LAD geography, anchored to the MSOA 2021 name scoping), best-fit assigned from the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at load on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021, then uk_baseline.adm_ons_msoa_boundary_2021. Open Government Licence v3.0. |
| `lad22nm` | `text` | Local Authority District 2022 name (2021 LAD geography), best-fit assigned from the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at load on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021, then uk_baseline.adm_ons_msoa_boundary_2021. Open Government Licence v3.0. |
| `lad25cd` | `text` | Local Authority District 2025 code (current administering authority), best-fit assigned from the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at load on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021, then uk_baseline.adm_ons_msoa_boundary_2021. Open Government Licence v3.0. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority), best-fit assigned from the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at load on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021, then uk_baseline.adm_ons_msoa_boundary_2021. Open Government Licence v3.0. |
| `ctyua25cd` | `text` | County or unitary authority code at 1 April 2025. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `ctyua25nm` | `text` | County or unitary authority name at 1 April 2025. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `sds_name` | `text` | Spatial Development Strategy (SDS) area, a Prior + Partners categorisation over Ministry of Housing, Communities and Local Government (MHCLG) English devolution policy. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `sds_group` | `text` | Devolution status of the Spatial Development Strategy area: Existing Devolution Footprints, Devolution Priority Programme, Other Proposed Geographies or Remaining Areas. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
