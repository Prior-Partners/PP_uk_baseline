# ONS Business Register and Employment Survey (BRES) employment by 18 broad industry groups, LSOA 2021 boundary, Prior + Partners edition, 2024

<p class="layer-short">BRES Employment - LSOA, 2024, broad groups (P+P)</p>

`ecn_ons_lsoa_business_register_employment_pp_2024`

**SOURCE**

- Office for National Statistics (ONS), distributed via the Nomis dataset Business Register and Employment Survey open access. Pulled from the Nomis application programming interface by Prior + Partners, 27 August 2026 (dual independent pulls verified identical; audit report in the project folder). Measure: Employment, count.
- Prior + Partners processing, 27 August 2026: rows limited to England and Wales; the long-format Nomis extract pivoted to one row per area with one column per broad industry group; a derived motor-wholesale-retail sum column added. No published value altered.

**DOCUMENTATION**

- Nomis dataset page : https://www.nomisweb.co.uk/datasets/newbres6pub
- ONS BRES methodology : https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/methodologies/businessregisterandemploymentsurveybres
- Nomis rounding article : https://www.nomisweb.co.uk/articles/1103.aspx

**DEFINITIONS**

- "Employees: people aged 16 or over paid directly through the employer's payroll (full-time, part-time or on a training scheme) on the survey reference date." (ONS BRES QMI)
- "Working owners: business owners (sole traders, sole proprietors and partners) who take a share of the profits rather than being paid a wage through the payroll." (ONS BRES QMI)
- Employment is the sum of Employees plus Working owners (ONS BRES QMI).
- Employment is broken down by the 18 Nomis broad industry groups over SIC2007.

**SCOPE**

- England and Wales. Lower Layer Super Output Area (LSOA) 2021; 35,672 rows. Survey year 2024.

**CRS**

- EPSG:27700 (British National Grid); source data is non-spatial, geometry joined from the boundary layer named on the geom column.

**LICENCE**

- Open Government Licence v3.0 (OGL v3.0).

**DATA QUALITY CAVEATS**

- Values carry Nomis rounding, which varies by estimate.
- Total columns are Nomis-published and independently rounded; the sector columns may not sum to the total.
- Do not aggregate the Lower Layer Super Output Area rows to district: the district table carries its own Nomis-published figures under a different rounding regime.
- ONS notice: geographical misreporting affects 2015-2024 outputs for the local authorities of Hillingdon and Hounslow and certain areas within them; ONS will revise the provisional 2024 tables in October 2026 and will not revise earlier years.
- Wales and the Isles of Scilly carry a county but no Spatial Development Strategy area.
- 9 geometries repaired on 23 September 2026 to meet the geometry validity rules: Stockport 006C (E01005866), Bristol 027B (E01014674), Thurrock 001C (E01015946), Dorset 008C (E01020541), Colchester 021C (E01021733), Wyre Forest 007C (E01032465), Swale 007G (E01032655), North Somerset 026D (E01032668), Chichester 012H (E01035327). Each outline touched itself at a single point, enclosing a void as part of the outer boundary; the void is now drawn as a separate hole. Areas are unchanged.

**ENRICHMENT**

- sds_name / sds_group - Spatial Development Strategy area and devolution status, a Prior + Partners categorisation over MHCLG English devolution policy, joined at enrichment via uk_baseline.adm_ons_lsoa_boundary_2021.
- msoa21hclnm - House of Commons Library readable MSOA name. Open Parliament Licence.

**LOADED INTO uk_baseline**

- Loaded by PNC, 28 August 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `lsoa21cd` | `character varying(9)` | Source field `GEOGRAPHY_CODE`. |
| `lsoa21nm` | `character varying(255)` | Source field `GEOGRAPHY_NAME`. |
| `jobs24_agri_forestry_fishing` | `integer` | Unit: "Persons". Broad industry group 1: Agriculture, forestry & fishing (A). Source field `OBS_VALUE`. |
| `jobs24_mining_utilities` | `integer` | Unit: "Persons". Broad industry group 2: Mining, quarrying & utilities (B, D and E). Source field `OBS_VALUE`. |
| `jobs24_manufacturing` | `integer` | Unit: "Persons". Broad industry group 3: Manufacturing (C). Source field `OBS_VALUE`. |
| `jobs24_construction` | `integer` | Unit: "Persons". Broad industry group 4: Construction (F). Source field `OBS_VALUE`. |
| `jobs24_motor_trades` | `integer` | Unit: "Persons". Broad industry group 5: Motor trades (Part G). Source field `OBS_VALUE`. |
| `jobs24_wholesale` | `integer` | Unit: "Persons". Broad industry group 6: Wholesale (Part G). Source field `OBS_VALUE`. |
| `jobs24_retail` | `integer` | Unit: "Persons". Broad industry group 7: Retail (Part G). Source field `OBS_VALUE`. |
| `jobs24_transport_storage` | `integer` | Unit: "Persons". Broad industry group 8: Transport & storage (inc postal) (H). Source field `OBS_VALUE`. |
| `jobs24_accomm_food_svcs` | `integer` | Unit: "Persons". Broad industry group 9: Accommodation & food services (I). Source field `OBS_VALUE`. |
| `jobs24_info_comms` | `integer` | Unit: "Persons". Broad industry group 10: Information & communication (J). Source field `OBS_VALUE`. |
| `jobs24_finance_insurance` | `integer` | Unit: "Persons". Broad industry group 11: Financial & insurance (K). Source field `OBS_VALUE`. |
| `jobs24_property` | `integer` | Unit: "Persons". Broad industry group 12: Property (L). Source field `OBS_VALUE`. |
| `jobs24_prof_sci_tech` | `integer` | Unit: "Persons". Broad industry group 13: Professional, scientific & technical (M). Source field `OBS_VALUE`. |
| `jobs24_business_admin_support` | `integer` | Unit: "Persons". Broad industry group 14: Business administration & support services (N). Source field `OBS_VALUE`. |
| `jobs24_public_admin_defence` | `integer` | Unit: "Persons". Broad industry group 15: Public administration & defence (O). Source field `OBS_VALUE`. |
| `jobs24_education` | `integer` | Unit: "Persons". Broad industry group 16: Education (P). Source field `OBS_VALUE`. |
| `jobs24_health` | `integer` | Unit: "Persons". Broad industry group 17: Health (Q). Source field `OBS_VALUE`. |
| `jobs24_arts_ent_other` | `integer` | Unit: "Persons". Broad industry group 18: Arts, entertainment, recreation & other services (R, S, T and U). Source field `OBS_VALUE`. |
| `jobs24_motor_wholesale_retail` | `integer` | Derived, approved 27 August 2026: sum of the Motor trades, Wholesale and Retail broad group columns. |
| `jobs24_total` | `integer` | Unit: "Persons". Nomis-published total employment; independently rounded, so the sector columns may not sum to it. Source field `OBS_VALUE`. |
| `geom` | `geometry(MultiPolygon,27700)` | Geometry from uk_baseline.adm_ons_lsoa_boundary_2021. |
| `fid` | `integer` |  |
| `msoa21cd` | `text` | Middle Layer Super Output Area (MSOA) 2021 code of the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at enrichment on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021. Open Government Licence v3.0. |
| `msoa21nm` | `text` | Official Office for National Statistics MSOA 2021 name of the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at enrichment on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021. Open Government Licence v3.0. |
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name of the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at enrichment on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021. Open Parliament Licence. |
| `lad22cd` | `text` | Local Authority District 2022 code (2021 LAD geography) of the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at enrichment on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021. Open Government Licence v3.0. |
| `lad22nm` | `text` | Local Authority District 2022 name (2021 LAD geography) of the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at enrichment on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021. Open Government Licence v3.0. |
| `lad25cd` | `text` | Local Authority District 2025 code (current administering authority) of the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at enrichment on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021. Open Government Licence v3.0. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority) of the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at enrichment on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021. Open Government Licence v3.0. |
| `ctyua25cd` | `text` | County or unitary authority code at 1 April 2025 of the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at enrichment on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021. Open Government Licence v3.0. |
| `ctyua25nm` | `text` | County or unitary authority name at 1 April 2025 of the row's Lower Layer Super Output Area (LSOA); LSOAs nest wholly within MSOAs. Joined at enrichment on lsoa21cd via uk_baseline.adm_ons_lsoa_boundary_2021. Open Government Licence v3.0. |
| `sds_name` | `text` | Spatial Development Strategy (SDS) area, a Prior + Partners categorisation over Ministry of Housing, Communities and Local Government (MHCLG) English devolution policy. Joined at enrichment via uk_baseline.adm_ons_lsoa_boundary_2021. Open Government Licence v3.0. |
| `sds_group` | `text` | Devolution status of the Spatial Development Strategy area: Existing Devolution Footprints, Devolution Priority Programme, Other Proposed Geographies or Remaining Areas. Joined at enrichment via uk_baseline.adm_ons_lsoa_boundary_2021. Open Government Licence v3.0. |
