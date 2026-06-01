# ONS Census 2021 students at Lower-layer Super Output Area (LSOA) 2021

`dem_ons_lsoa_students_2021`

<iframe src="../maps/dem_ons_lsoa_students_2021.html" title="Interactive preview map of dem_ons_lsoa_students_2021" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../maps/dem_ons_lsoa_students_2021.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

**SOURCE**

- Office for National Statistics (ONS), Census 2021, England and Wales. Primary source table TS068 (schoolchildren and full-time students), augmented with student-related cross-tabs from TS062 (NS-SEC) and TS067 (qualifications). Reference date 21 March 2021. Loaded via an earlier Prior + Partners pass; exact source combination not recorded.

**DOCUMENTATION**

- ONS Census 2021 student variable info : https://www.ons.gov.uk/census/planningforcensus2021/censusdesign/studentscensus2021
- ONS dataset (TS068) : https://www.ons.gov.uk/datasets/TS068/editions/2021/versions/1
- ONS Census 2021 landing page : https://www.ons.gov.uk/census/2021

**DEFINITIONS**

- "A student is a person who is in full-time education, or who is enrolled on a course at any educational establishment in the UK. Students are usually counted at their term-time address." (ONS Census 2021 Schoolchildren and students variable)
- "Higher-education students were counted at their term-time address, even if they were not at that address on Census Day." (ONS Census 2021 student counting design page)

**SCOPE**

- England and Wales. LSOA 2021 boundary; 35,672 distinct lsoa21cd.
- Base population: schoolchildren and full-time students; some columns subset further by age band or accommodation type.

**CRS**

- EPSG:27700. Open Government Licence v3.0.

**DATA QUALITY CAVEATS**

- Students are counted at their term-time address. This means university towns / cities show artificially high student counts in term time; home addresses show artificially low counts. Use this layer for term-time demographic analysis, not for home-residence analysis.

**LOADED INTO uk_baseline**

- Data: Census Day 21 March 2021.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `FID` | `bigint` |  |
| `lsoa21cd` | `text` | Source field "LSOA21CD"; ONS GSS 9-character LSOA 2021 code. |
| `lsoa21nm` | `text` | Source field "LSOA21NM"; human-readable LSOA 2021 name. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. Boundary geometry joined at load. |
| `msoa21cd` | `text` | Joined at load from ONS LSOA->MSOA lookup; 2021 MSOA GSS code. |
| `msoa21nm` | `text` | Joined at load from ONS LSOA->MSOA lookup; 2021 MSOA name. |
| `lad22cd` | `text` | Joined at load from ONS LSOA->LAD lookup; 2022 LAD GSS code. |
| `lad22nm` | `text` | Joined at load from ONS LSOA->LAD lookup; 2022 LAD name. |
| `rgn22cd` | `text` | Joined at load from ONS LSOA->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LSOA->Region lookup; 2022 Region name. |
| `data_source` | `text` | Added during an earlier Prior + Partners loading pass. Fixed-string annotation; same value every row. |
| `data_resolution` | `text` | Added during an earlier Prior + Partners loading pass. Fixed-string annotation; same value every row. |
| `data_time_period` | `timestamp without time zone` | Added during an earlier Prior + Partners loading pass. Fixed annotation; same value every row. |
| `data_web_link` | `text` | Added during an earlier Prior + Partners loading pass. Fixed annotation; URL to the ONS dataset page. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Unit: hectares. Stale if geometry is later edited. |
| `total_students` | `bigint` | Source field; total schoolchildren and full-time students recorded in the LSOA at Census 2021 (term-time address basis). |
| `age_4_under_count` | `bigint` | Source field; count of "age 4 under" in LSOA schoolchildren and full-time students. |
| `age_5_15_count` | `bigint` | Source field; count of "age 5 15" in LSOA schoolchildren and full-time students. |
| `age_16_17_count` | `bigint` | Source field; count of "age 16 17" in LSOA schoolchildren and full-time students. |
| `age_18_20_count` | `bigint` | Source field; count of "age 18 20" in LSOA schoolchildren and full-time students. |
| `age_21_24_count` | `bigint` | Source field; count of "age 21 24" in LSOA schoolchildren and full-time students. |
| `age_25_29_count` | `bigint` | Source field; count of "age 25 29" in LSOA schoolchildren and full-time students. |
| `age_30_over_count` | `bigint` | Source field; count of "age 30 over" in LSOA schoolchildren and full-time students. |
| `age_4_under_perc` | `double precision` | Source field; percentage of "age 4 under" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `age_5_15_perc` | `double precision` | Source field; percentage of "age 5 15" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `age_16_17_perc` | `double precision` | Source field; percentage of "age 16 17" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `age_18_20_perc` | `double precision` | Source field; percentage of "age 18 20" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `age_21_24_perc` | `double precision` | Source field; percentage of "age 21 24" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `age_25_29_perc` | `double precision` | Source field; percentage of "age 25 29" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `age_30_over_perc` | `double precision` | Source field; percentage of "age 30 over" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_with_parents_count` | `bigint` | Source field; count of "living with parents" in LSOA schoolchildren and full-time students. |
| `living_in_communal_establishment_uni_count` | `bigint` | Source field; count of "living in communal establishment uni" in LSOA schoolchildren and full-time students. |
| `living_in_communal_establishment_other_count` | `bigint` | Source field; count of "living in communal establishment other" in LSOA schoolchildren and full-time students. |
| `living_in_all_student_household_count` | `bigint` | Source field; count of "living in all student household" in LSOA schoolchildren and full-time students. |
| `living_alone_count` | `bigint` | Source field; count of "living alone" in LSOA schoolchildren and full-time students. |
| `living_in_other_household_count` | `bigint` | Source field; count of "living in other household" in LSOA schoolchildren and full-time students. |
| `living_with_parents_perc` | `double precision` | Source field; percentage of "living with parents" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_communal_establishment_uni_perc` | `double precision` | Source field; percentage of "living in communal establishment uni" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_communal_establishment_other_perc` | `double precision` | Source field; percentage of "living in communal establishment other" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_all_student_household_perc` | `double precision` | Source field; percentage of "living in all student household" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_alone_perc` | `double precision` | Source field; percentage of "living alone" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_other_household_perc` | `double precision` | Source field; percentage of "living in other household" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_with_parents_age_4_under_count` | `bigint` | Source field; count of "living with parents age 4 under" in LSOA schoolchildren and full-time students. |
| `living_with_parents_age_5_15_count` | `bigint` | Source field; count of "living with parents age 5 15" in LSOA schoolchildren and full-time students. |
| `living_with_parents_age_16_17_count` | `bigint` | Source field; count of "living with parents age 16 17" in LSOA schoolchildren and full-time students. |
| `living_with_parents_age_18_20_count` | `bigint` | Source field; count of "living with parents age 18 20" in LSOA schoolchildren and full-time students. |
| `living_with_parents_age_21_24_count` | `bigint` | Source field; count of "living with parents age 21 24" in LSOA schoolchildren and full-time students. |
| `living_with_parents_age_25_29_count` | `bigint` | Source field; count of "living with parents age 25 29" in LSOA schoolchildren and full-time students. |
| `living_with_parents_age_30_over_count` | `bigint` | Source field; count of "living with parents age 30 over" in LSOA schoolchildren and full-time students. |
| `living_with_parents_age_4_under_perc` | `double precision` | Source field; percentage of "living with parents age 4 under" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_with_parents_age_5_15_perc` | `double precision` | Source field; percentage of "living with parents age 5 15" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_with_parents_age_16_17_perc` | `double precision` | Source field; percentage of "living with parents age 16 17" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_with_parents_age_18_20_perc` | `double precision` | Source field; percentage of "living with parents age 18 20" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_with_parents_age_21_24_perc` | `double precision` | Source field; percentage of "living with parents age 21 24" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_with_parents_age_25_29_perc` | `double precision` | Source field; percentage of "living with parents age 25 29" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_with_parents_age_30_over_perc` | `double precision` | Source field; percentage of "living with parents age 30 over" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_communal_establishment_uni_age_4_under_count` | `bigint` | Source field; count of "living in communal establishment uni age 4 under" in LSOA schoolchildren and full-time students. |
| `living_in_communal_establishment_uni_age_5_15_count` | `bigint` | Source field; count of "living in communal establishment uni age 5 15" in LSOA schoolchildren and full-time students. |
| `living_in_communal_establishment_uni_age_16_17_count` | `bigint` | Source field; count of "living in communal establishment uni age 16 17" in LSOA schoolchildren and full-time students. |
| `living_in_communal_establishment_uni_age_18_20_count` | `bigint` | Source field; count of "living in communal establishment uni age 18 20" in LSOA schoolchildren and full-time students. |
| `living_in_communal_establishment_uni_age_21_24_count` | `bigint` | Source field; count of "living in communal establishment uni age 21 24" in LSOA schoolchildren and full-time students. |
| `living_in_communal_establishment_uni_age_25_29_count` | `bigint` | Source field; count of "living in communal establishment uni age 25 29" in LSOA schoolchildren and full-time students. |
| `living_in_communal_establishment_uni_age_30_over_count` | `bigint` | Source field; count of "living in communal establishment uni age 30 over" in LSOA schoolchildren and full-time students. |
| `living_in_communal_establishment_uni_age_4_under_perc` | `double precision` | Source field; percentage of "living in communal establishment uni age 4 under" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_communal_establishment_uni_age_5_15_perc` | `double precision` | Source field; percentage of "living in communal establishment uni age 5 15" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_communal_establishment_uni_age_16_17_perc` | `double precision` | Source field; percentage of "living in communal establishment uni age 16 17" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_communal_establishment_uni_age_18_20_perc` | `double precision` | Source field; percentage of "living in communal establishment uni age 18 20" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_communal_establishment_uni_age_21_24_perc` | `double precision` | Source field; percentage of "living in communal establishment uni age 21 24" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_communal_establishment_uni_age_25_29_perc` | `double precision` | Source field; percentage of "living in communal establishment uni age 25 29" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_communal_establishment_uni_age_30_over_perc` | `double precision` | Source field; percentage of "living in communal establishment uni age 30 over" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_communal_establishment_other_age_4_under_count` | `bigint` | Source field; count of "living in communal establishment other age 4 under" in LSOA schoolchildren and full-time students. |
| `living_in_communal_establishment_other_age_5_15_count` | `bigint` | Source field; count of "living in communal establishment other age 5 15" in LSOA schoolchildren and full-time students. |
| `living_in_communal_establishment_other_age_16_17_count` | `bigint` | Source field; count of "living in communal establishment other age 16 17" in LSOA schoolchildren and full-time students. |
| `living_in_communal_establishment_other_age_18_20_count` | `bigint` | Source field; count of "living in communal establishment other age 18 20" in LSOA schoolchildren and full-time students. |
| `living_in_communal_establishment_other_age_21_24_count` | `bigint` | Source field; count of "living in communal establishment other age 21 24" in LSOA schoolchildren and full-time students. |
| `living_in_communal_establishment_other_age_25_29_count` | `bigint` | Source field; count of "living in communal establishment other age 25 29" in LSOA schoolchildren and full-time students. |
| `living_in_communal_establishment_other_age_30_over_count` | `bigint` | Source field; count of "living in communal establishment other age 30 over" in LSOA schoolchildren and full-time students. |
| `living_in_communal_establishment_other_age_4_under_perc` | `double precision` | Source field; percentage of "living in communal establishment other age 4 under" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_communal_establishment_other_age_5_15_perc` | `double precision` | Source field; percentage of "living in communal establishment other age 5 15" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_communal_establishment_other_age_16_17_perc` | `double precision` | Source field; percentage of "living in communal establishment other age 16 17" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_communal_establishment_other_age_18_20_perc` | `double precision` | Source field; percentage of "living in communal establishment other age 18 20" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_communal_establishment_other_age_21_24_perc` | `double precision` | Source field; percentage of "living in communal establishment other age 21 24" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_communal_establishment_other_age_25_29_perc` | `double precision` | Source field; percentage of "living in communal establishment other age 25 29" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_communal_establishment_other_age_30_over_perc` | `double precision` | Source field; percentage of "living in communal establishment other age 30 over" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_all_student_household_age_4_under_count` | `bigint` | Source field; count of "living in all student household age 4 under" in LSOA schoolchildren and full-time students. |
| `living_in_all_student_household_age_5_15_count` | `bigint` | Source field; count of "living in all student household age 5 15" in LSOA schoolchildren and full-time students. |
| `living_in_all_student_household_age_16_17_count` | `bigint` | Source field; count of "living in all student household age 16 17" in LSOA schoolchildren and full-time students. |
| `living_in_all_student_household_age_18_20_count` | `bigint` | Source field; count of "living in all student household age 18 20" in LSOA schoolchildren and full-time students. |
| `living_in_all_student_household_age_21_24_count` | `bigint` | Source field; count of "living in all student household age 21 24" in LSOA schoolchildren and full-time students. |
| `living_in_all_student_household_age_25_29_count` | `bigint` | Source field; count of "living in all student household age 25 29" in LSOA schoolchildren and full-time students. |
| `living_in_all_student_household_age_30_over_count` | `bigint` | Source field; count of "living in all student household age 30 over" in LSOA schoolchildren and full-time students. |
| `living_in_all_student_household_age_4_under_perc` | `double precision` | Source field; percentage of "living in all student household age 4 under" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_all_student_household_age_5_15_perc` | `double precision` | Source field; percentage of "living in all student household age 5 15" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_all_student_household_age_16_17_perc` | `double precision` | Source field; percentage of "living in all student household age 16 17" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_all_student_household_age_18_20_perc` | `double precision` | Source field; percentage of "living in all student household age 18 20" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_all_student_household_age_21_24_perc` | `double precision` | Source field; percentage of "living in all student household age 21 24" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_all_student_household_age_25_29_perc` | `double precision` | Source field; percentage of "living in all student household age 25 29" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_all_student_household_age_30_over_perc` | `double precision` | Source field; percentage of "living in all student household age 30 over" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_alone_age_4_under_count` | `bigint` | Source field; count of "living alone age 4 under" in LSOA schoolchildren and full-time students. |
| `living_alone_age_5_15_count` | `bigint` | Source field; count of "living alone age 5 15" in LSOA schoolchildren and full-time students. |
| `living_alone_age_16_17_count` | `bigint` | Source field; count of "living alone age 16 17" in LSOA schoolchildren and full-time students. |
| `living_alone_age_18_20_count` | `bigint` | Source field; count of "living alone age 18 20" in LSOA schoolchildren and full-time students. |
| `living_alone_age_21_24_count` | `bigint` | Source field; count of "living alone age 21 24" in LSOA schoolchildren and full-time students. |
| `living_alone_age_25_29_count` | `bigint` | Source field; count of "living alone age 25 29" in LSOA schoolchildren and full-time students. |
| `living_alone_age_30_over_count` | `bigint` | Source field; count of "living alone age 30 over" in LSOA schoolchildren and full-time students. |
| `living_alone_age_4_under_perc` | `double precision` | Source field; percentage of "living alone age 4 under" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_alone_age_5_15_perc` | `double precision` | Source field; percentage of "living alone age 5 15" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_alone_age_16_17_perc` | `double precision` | Source field; percentage of "living alone age 16 17" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_alone_age_18_20_perc` | `double precision` | Source field; percentage of "living alone age 18 20" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_alone_age_21_24_perc` | `double precision` | Source field; percentage of "living alone age 21 24" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_alone_age_25_29_perc` | `double precision` | Source field; percentage of "living alone age 25 29" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_alone_age_30_over_perc` | `double precision` | Source field; percentage of "living alone age 30 over" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_other_household_age_4_under_count` | `bigint` | Source field; count of "living in other household age 4 under" in LSOA schoolchildren and full-time students. |
| `living_in_other_household_age_5_15_count` | `bigint` | Source field; count of "living in other household age 5 15" in LSOA schoolchildren and full-time students. |
| `living_in_other_household_age_16_17_count` | `bigint` | Source field; count of "living in other household age 16 17" in LSOA schoolchildren and full-time students. |
| `living_in_other_household_age_18_20_count` | `bigint` | Source field; count of "living in other household age 18 20" in LSOA schoolchildren and full-time students. |
| `living_in_other_household_age_21_24_count` | `bigint` | Source field; count of "living in other household age 21 24" in LSOA schoolchildren and full-time students. |
| `living_in_other_household_age_25_29_count` | `bigint` | Source field; count of "living in other household age 25 29" in LSOA schoolchildren and full-time students. |
| `living_in_other_household_age_30_over_count` | `bigint` | Source field; count of "living in other household age 30 over" in LSOA schoolchildren and full-time students. |
| `living_in_other_household_age_4_under_perc` | `double precision` | Source field; percentage of "living in other household age 4 under" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_other_household_age_5_15_perc` | `double precision` | Source field; percentage of "living in other household age 5 15" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_other_household_age_16_17_perc` | `double precision` | Source field; percentage of "living in other household age 16 17" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_other_household_age_18_20_perc` | `double precision` | Source field; percentage of "living in other household age 18 20" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_other_household_age_21_24_perc` | `double precision` | Source field; percentage of "living in other household age 21 24" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_other_household_age_25_29_perc` | `double precision` | Source field; percentage of "living in other household age 25 29" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `living_in_other_household_age_30_over_perc` | `double precision` | Source field; percentage of "living in other household age 30 over" in LSOA schoolchildren and full-time students. Unit: "percent (0 to 100)". |
| `dominant_student_age_group` | `text` | Derived during an earlier Prior + Partners loading pass; label of the modal category for this LSOA. |
| `dominant_student_household_group` | `text` | Derived during an earlier Prior + Partners loading pass; label of the modal category for this LSOA. |
| `wd22cd` | `character varying` | Joined at load from ONS LSOA->Ward lookup; 2022 Ward GSS code. |
| `wd22nm` | `character varying` | Joined at load from ONS LSOA->Ward lookup; 2022 Ward name. |
| `fid` | `bigint` |  |
