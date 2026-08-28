# ONS Business Register and Employment Survey (BRES) employment change 2015 to 2022 by 18 broad industry groups, LSOA 2011 boundary, Prior + Partners edition, 2022

<p class="layer-short">BRES Employment change 2015-22 - LSOA (P+P)</p>

`ecn_ons_lsoa_business_register_employment_pp_2015_2022`

**SOURCE**

- Office for National Statistics (ONS), distributed via the Nomis dataset Business Register and Employment Survey open access. Pulled from the Nomis application programming interface by Prior + Partners, 27 August 2026 (dual independent pulls verified identical; audit report in the project folder). Measure: Employment, count.
- Prior + Partners processing, 27 August 2026: rows limited to England and Wales; the long-format Nomis extract pivoted to one row per area with one column per broad industry group; a derived motor-wholesale-retail sum column added. No published value altered.
- Change columns computed by Prior + Partners as the 2022 value minus the 2015 value, per broad industry group and for the Nomis-published totals.

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

- England and Wales. Lower Layer Super Output Area (LSOA) 2011; 34,753 rows. Survey years 2015 and 2022.

**CRS**

- EPSG:27700 (British National Grid); source data is non-spatial, geometry joined from the boundary layer named on the geom column.

**LICENCE**

- Open Government Licence v3.0 (OGL v3.0).

**DATA QUALITY CAVEATS**

- BRES publishes 2015-2022 small-area data only on the LSOA 2011 boundary; 2024 data exists only on LSOA 2021. The two editions cannot be combined at LSOA level; this layer deliberately keeps the boundary its data was published on.
- Values carry Nomis rounding, which varies by estimate.
- Total columns are Nomis-published and independently rounded; the sector columns may not sum to the total.
- Do not aggregate the Lower Layer Super Output Area rows to district: the district table carries its own Nomis-published figures under a different rounding regime.
- ONS notice: geographical misreporting affects 2015-2024 outputs for the local authorities of Hillingdon and Hounslow and certain areas within them; ONS will revise the provisional 2024 tables in October 2026 and will not revise earlier years.
- The 2021-geography columns are best-fit assigned: rows on a 2011 LSOA that straddles a 2011-to-2021 boundary change are attached to their largest-overlap 2021 MSOA, so a small share of those rows' area lies outside the assigned MSOA.
- Wales and the Isles of Scilly carry a county but no Spatial Development Strategy area.

**ENRICHMENT**

- sds_name / sds_group - Spatial Development Strategy area and devolution status, a Prior + Partners categorisation over MHCLG English devolution policy, joined at enrichment via uk.ref_lad25_ctyua25_sds_lu_jul2026.
- msoa21hclnm - House of Commons Library readable MSOA name, best-fit assigned from the 2011 LSOA. Open Parliament Licence.

**LOADED INTO uk_baseline**

- Loaded by PNC, 28 August 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `lsoa11cd` | `character varying(9)` | Source field `GEOGRAPHY_CODE`. |
| `lsoa11nm` | `character varying(255)` | Source field `GEOGRAPHY_NAME`. |
| `jobs15_total` | `integer` | Unit: "Persons". Nomis-published total employment, 2015. Source field `OBS_VALUE`. |
| `jobs22_total` | `integer` | Unit: "Persons". Nomis-published total employment, 2022. Source field `OBS_VALUE`. |
| `chg1522_total` | `integer` | Unit: "Persons". Derived, approved 27 August 2026: 2022 total minus 2015 total. |
| `chg1522_agri_forestry_fishing` | `integer` | Unit: "Persons". Derived, approved 27 August 2026: 2022 minus 2015 for broad industry group 1: Agriculture, forestry & fishing (A). |
| `chg1522_mining_utilities` | `integer` | Unit: "Persons". Derived, approved 27 August 2026: 2022 minus 2015 for broad industry group 2: Mining, quarrying & utilities (B, D and E). |
| `chg1522_manufacturing` | `integer` | Unit: "Persons". Derived, approved 27 August 2026: 2022 minus 2015 for broad industry group 3: Manufacturing (C). |
| `chg1522_construction` | `integer` | Unit: "Persons". Derived, approved 27 August 2026: 2022 minus 2015 for broad industry group 4: Construction (F). |
| `chg1522_motor_trades` | `integer` | Unit: "Persons". Derived, approved 27 August 2026: 2022 minus 2015 for broad industry group 5: Motor trades (Part G). |
| `chg1522_wholesale` | `integer` | Unit: "Persons". Derived, approved 27 August 2026: 2022 minus 2015 for broad industry group 6: Wholesale (Part G). |
| `chg1522_retail` | `integer` | Unit: "Persons". Derived, approved 27 August 2026: 2022 minus 2015 for broad industry group 7: Retail (Part G). |
| `chg1522_transport_storage` | `integer` | Unit: "Persons". Derived, approved 27 August 2026: 2022 minus 2015 for broad industry group 8: Transport & storage (inc postal) (H). |
| `chg1522_accomm_food_svcs` | `integer` | Unit: "Persons". Derived, approved 27 August 2026: 2022 minus 2015 for broad industry group 9: Accommodation & food services (I). |
| `chg1522_info_comms` | `integer` | Unit: "Persons". Derived, approved 27 August 2026: 2022 minus 2015 for broad industry group 10: Information & communication (J). |
| `chg1522_finance_insurance` | `integer` | Unit: "Persons". Derived, approved 27 August 2026: 2022 minus 2015 for broad industry group 11: Financial & insurance (K). |
| `chg1522_property` | `integer` | Unit: "Persons". Derived, approved 27 August 2026: 2022 minus 2015 for broad industry group 12: Property (L). |
| `chg1522_prof_sci_tech` | `integer` | Unit: "Persons". Derived, approved 27 August 2026: 2022 minus 2015 for broad industry group 13: Professional, scientific & technical (M). |
| `chg1522_business_admin_support` | `integer` | Unit: "Persons". Derived, approved 27 August 2026: 2022 minus 2015 for broad industry group 14: Business administration & support services (N). |
| `chg1522_public_admin_defence` | `integer` | Unit: "Persons". Derived, approved 27 August 2026: 2022 minus 2015 for broad industry group 15: Public administration & defence (O). |
| `chg1522_education` | `integer` | Unit: "Persons". Derived, approved 27 August 2026: 2022 minus 2015 for broad industry group 16: Education (P). |
| `chg1522_health` | `integer` | Unit: "Persons". Derived, approved 27 August 2026: 2022 minus 2015 for broad industry group 17: Health (Q). |
| `chg1522_arts_ent_other` | `integer` | Unit: "Persons". Derived, approved 27 August 2026: 2022 minus 2015 for broad industry group 18: Arts, entertainment, recreation & other services (R, S, T and U). |
| `chg1522_motor_wholesale_retail` | `integer` | Derived, approved 27 August 2026: sum of the Motor trades, Wholesale and Retail change columns. |
| `geom` | `geometry(MultiPolygon,27700)` | Geometry from uk_baseline.adm_ons_lsoa_boundary_2011. |
| `fid` | `integer` |  |
| `msoa21cd` | `text` | Middle Layer Super Output Area (MSOA) 2021 code, best-fit assigned from the row's 2011 Lower Layer Super Output Area (LSOA) by largest-area-overlap 2021 MSOA (uk.ref_lsoa11_msoa21_bestfit_lu). Open Government Licence v3.0. |
| `msoa21nm` | `text` | Official Office for National Statistics MSOA 2021 name, best-fit assigned from the row's 2011 Lower Layer Super Output Area (LSOA) by largest-area-overlap 2021 MSOA (uk.ref_lsoa11_msoa21_bestfit_lu). Open Government Licence v3.0. |
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name, best-fit assigned from the row's 2011 Lower Layer Super Output Area (LSOA) by largest-area-overlap 2021 MSOA (uk.ref_lsoa11_msoa21_bestfit_lu). Open Parliament Licence. |
| `lad22cd` | `text` | Local Authority District 2022 code (2021 LAD geography), best-fit assigned from the row's 2011 Lower Layer Super Output Area (LSOA) by largest-area-overlap 2021 MSOA (uk.ref_lsoa11_msoa21_bestfit_lu). Open Government Licence v3.0. |
| `lad22nm` | `text` | Local Authority District 2022 name (2021 LAD geography), best-fit assigned from the row's 2011 Lower Layer Super Output Area (LSOA) by largest-area-overlap 2021 MSOA (uk.ref_lsoa11_msoa21_bestfit_lu). Open Government Licence v3.0. |
| `lad25cd` | `text` | Local Authority District 2025 code (current administering authority), best-fit assigned from the row's 2011 Lower Layer Super Output Area (LSOA) by largest-area-overlap 2021 MSOA (uk.ref_lsoa11_msoa21_bestfit_lu). Open Government Licence v3.0. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority), best-fit assigned from the row's 2011 Lower Layer Super Output Area (LSOA) by largest-area-overlap 2021 MSOA (uk.ref_lsoa11_msoa21_bestfit_lu). Open Government Licence v3.0. |
| `ctyua25cd` | `text` | County or unitary authority code at 1 April 2025. Joined at enrichment via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `ctyua25nm` | `text` | County or unitary authority name at 1 April 2025. Joined at enrichment via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `sds_name` | `text` | Spatial Development Strategy (SDS) area, a Prior + Partners categorisation over Ministry of Housing, Communities and Local Government (MHCLG) English devolution policy. Joined at enrichment via uk.ref_lad25_ctyua25_sds_lu_jul2026. Open Government Licence v3.0. |
| `sds_group` | `text` | Devolution status of the Spatial Development Strategy area: Existing Devolution Footprints, Devolution Priority Programme, Other Proposed Geographies or Remaining Areas. Joined at enrichment via uk.ref_lad25_ctyua25_sds_lu_jul2026. Open Government Licence v3.0. |
