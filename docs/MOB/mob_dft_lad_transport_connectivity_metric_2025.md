# Department for Transport (DfT) transport connectivity metric, Local Authority District (LAD) scores, England & Wales, September 2025

<p class="layer-short">Transport Connectivity 2025 (LAD)</p>

`mob_dft_lad_transport_connectivity_metric_2025`

**SOURCE**

- Department for Transport (DfT). Transport connectivity metric, workbook "Connectivity metrics 2025" (connectivity_metrics_2025.ods, 68,164,574 bytes), sheet LAD, published 29 September 2025. All 35 score columns copied as published; nothing derived or filtered. Columns carry short readable names; the source header is recorded in every column comment.

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

- England and Wales. 331 rows, one per Local Authority District (May 2022 boundary): every English and Welsh district in uk_baseline.adm_ons_lad_boundary_may2022.
- Reference period October to December 2024 (DfT workbook Metadata sheet). Destination data are a mix of Q4 2024 and Q1 2025, except jobs, which use 2023 provisional Business Register and Employment Survey (BRES) figures (DfT methodology).

**CRS**

- EPSG:27700 (British National Grid). The source sheet has no geometry; geometry is copied from uk_baseline.adm_ons_lad_boundary_may2022 by matching the district name `LAD22NM` to lad22nm (three names aligned to the boundary's spelling, see the lad22nm column comment). No reprojection.

**LICENCE**

- Open Government Licence v3.0 (DfT publication page). The workbook's own Metadata sheet leaves its licence field as TBA.

**DATA QUALITY CAVEATS**

- Released as Experimental Statistics (DfT workbook Metadata sheet); the methodology calls these results provisional.
- Scores are relative to the best-connected location in England and Wales, not travel times or counts. The workbook's usage notes say scores should be interpreted relative to other areas and that different transport modes should not be directly compared.
- For public transport the employment column is headed Business (public transport) in the source, where the other modes say Employment. It is carried under the publisher's label as business_public_transport; DfT does not explain the difference.

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
| `lad22nm` | `character varying(36)` | Source field `LAD22NM`; three names aligned at load to the spelling in uk_baseline.adm_ons_lad_boundary_may2022 (Bristol to Bristol, City of; Herefordshire to Herefordshire, County of; Kingston upon Hull to Kingston upon Hull, City of). |
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
| `geom` | `geometry(MultiPolygon,27700)` | Geometry from uk_baseline.adm_ons_lad_boundary_may2022, England and Wales rows, matched on the district name. |
