# `dem_ons_lsoa_household_population_2021`

ONS Census 2021 household population / usual residents at Lower-layer Super Output Area (LSOA) 2021.

**SOURCE**

- Office for National Statistics (ONS), Census 2021, England and Wales. Primary source table TS001 "Number of usual residents in households and communal establishments", augmented with related cross-tabs (likely from TS001a / TS001b / TS003 variants and possibly TS006 area-population-density). Reference date 21 March 2021. Loaded via an earlier Prior + Partners pass; the exact combination of source tables not recorded.

**DOCUMENTATION**

- ONS dataset (TS001) : https://www.ons.gov.uk/datasets/TS001/editions/2021/versions/3
- ONS Census 2021 landing page : https://www.ons.gov.uk/census/2021

**DEFINITIONS**

- "The number of usual residents living in households or in communal establishments. A communal establishment is an establishment providing managed full-time or part-time supervision of residential accommodation (e.g. care home, prison, hostel, boarding school)." (ONS Census 2021 Resident type variable)
- "Census Day was 21 March 2021. The information collected in the census reflects the population of England and Wales on that day." (ONS Census 2021 landing page)

**SCOPE**

- England and Wales. LSOA 2021 boundary; 35,672 distinct lsoa21cd.
- Base populations: all usual residents AND households (depending on the column — see column comments).

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid).

**LICENCE**

- Open Government Licence v3.0.

**DATA QUALITY CAVEATS**

- The 173-column shape combines multiple Census 2021 cross-tabs. The exact source-table-per-column mapping was not recorded by the earlier load; some columns may be derived (sums of category sub-groups). Treat aggregate sums with care — confirm column groupings against ONS source tables before use.
- Base population varies per column (some columns count all usual residents, others count households). Each column comment names its base.

**LOADED INTO uk_baseline**

- Data: Census Day 21 March 2021.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `lsoa21cd_original` | `text` | Added during an earlier Prior + Partners loading pass. Original LSOA 2021 code as carried in the upstream file. Duplicates lsoa21cd in this table; kept for traceability. |
| `lsoa21nm` | `text` | Source field "LSOA21NM"; human-readable LSOA 2021 name. |
| `msoa21cd` | `text` | Joined at load from ONS LSOA->MSOA lookup; 2021 MSOA GSS code. |
| `msoa21nm` | `text` | Joined at load from ONS LSOA->MSOA lookup; 2021 MSOA name. |
| `wd22cd` | `text` | Joined at load from ONS LSOA->Ward lookup; 2022 Ward GSS code. |
| `wd22nm` | `text` | Joined at load from ONS LSOA->Ward lookup; 2022 Ward name. |
| `lad22cd` | `text` | Joined at load from ONS LSOA->LAD lookup; 2022 LAD GSS code. |
| `lad22nm` | `text` | Joined at load from ONS LSOA->LAD lookup; 2022 LAD name. |
| `rgn22cd` | `text` | Joined at load from ONS LSOA->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LSOA->Region lookup; 2022 Region name. |
| `data_source` | `text` | Added during an earlier Prior + Partners loading pass. Fixed-string annotation; same value every row. |
| `data_resolution` | `text` | Added during an earlier Prior + Partners loading pass. Fixed-string annotation; same value every row. |
| `data_time_period` | `timestamp without time zone` | Added during an earlier Prior + Partners loading pass. Fixed annotation; same value every row. |
| `data_web_link` | `text` | Added during an earlier Prior + Partners loading pass. Fixed annotation; URL to the ONS dataset page. |
| `mid_2011_population_count` | `bigint` | Source field; count of "mid 2011 population" in LSOA usual residents. |
| `mid_2016_population_count` | `bigint` | Source field; count of "mid 2016 population" in LSOA usual residents. |
| `mid_2021_population_count` | `bigint` | Source field; count of "mid 2021 population" in LSOA usual residents. |
| `2021_total_population_count` | `bigint` | Source field; count of "2021 total population" in LSOA usual residents. |
| `mid_2011_people_per_ha` | `double precision` | Added during an earlier Prior + Partners loading pass. Derived population density for the LSOA in mid-2011: ONS Mid-2011 population estimate / area_ha. Unit: "persons per hectare". |
| `mid_2016_people_per_ha` | `double precision` | Added during an earlier Prior + Partners loading pass. Derived population density for the LSOA in mid-2016: ONS Mid-2016 population estimate / area_ha. Unit: "persons per hectare". |
| `mid_2021_people_per_ha` | `double precision` | Added during an earlier Prior + Partners loading pass. Derived population density for the LSOA in mid-2021: ONS Mid-2021 population estimate / area_ha. Unit: "persons per hectare". |
| `change_in_population_2021_10yr` | `bigint` | Added during an earlier Prior + Partners loading pass. Change in LSOA population over the last 10 years to 2021 (2021 ONS estimate - 2011 ONS estimate). Unit: "persons". |
| `change_in_population_2021_5yr` | `bigint` | Added during an earlier Prior + Partners loading pass. Change in LSOA population over the last 5 years to 2021 (2021 ONS estimate - 2016 ONS estimate). Unit: "persons". |
| `change_in_population_density_2021_10yr_change` | `double precision` | Added during an earlier Prior + Partners loading pass. Change in LSOA population density over the last 10 years to 2021. Unit: "persons per hectare". |
| `change_in_population_density_2021_5yr_change` | `double precision` | Added during an earlier Prior + Partners loading pass. Change in LSOA population density over the last 5 years to 2021. Unit: "persons per hectare". |
| `2021_households_count` | `bigint` | Source field; count of "2021 households" in LSOA usual residents. |
| `2021_households_per_ha` | `double precision` | Added during an earlier Prior + Partners loading pass. Derived households density for the LSOA: total households / area_ha. Unit: "households per hectare". Column name is digit-led. |
| `2021_female_population_count` | `bigint` | Source field; count of "2021 female population" in LSOA usual residents. |
| `2021_male_population_count` | `bigint` | Source field; count of "2021 male population" in LSOA usual residents. |
| `2021_female_population_perc` | `double precision` | Source field; percentage of "2021 female population" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `2021_male_population_perc` | `double precision` | Source field; percentage of "2021 male population" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_2_years_and_under_count` | `bigint` | Source field; count of "aged 2 years and under" in LSOA usual residents. |
| `aged_3_to_4_years_count` | `bigint` | Source field; count of "aged 3 to 4 years" in LSOA usual residents. |
| `aged_5_to_7_years_count` | `bigint` | Source field; count of "aged 5 to 7 years" in LSOA usual residents. |
| `aged_8_to_9_years_count` | `bigint` | Source field; count of "aged 8 to 9 years" in LSOA usual residents. |
| `aged_10_to_14_years_count` | `bigint` | Source field; count of "aged 10 to 14 years" in LSOA usual residents. |
| `aged_15_years_count` | `bigint` | Source field; count of "aged 15 years" in LSOA usual residents. |
| `aged_16_to_17_years_count` | `bigint` | Source field; count of "aged 16 to 17 years" in LSOA usual residents. |
| `aged_18_to_19_years_count` | `bigint` | Source field; count of "aged 18 to 19 years" in LSOA usual residents. |
| `aged_20_to_24_years_count` | `bigint` | Source field; count of "aged 20 to 24 years" in LSOA usual residents. |
| `aged_25_to_29_years_count` | `bigint` | Source field; count of "aged 25 to 29 years" in LSOA usual residents. |
| `aged_30_to_34_years_count` | `bigint` | Source field; count of "aged 30 to 34 years" in LSOA usual residents. |
| `aged_35_to_39_years_count` | `bigint` | Source field; count of "aged 35 to 39 years" in LSOA usual residents. |
| `aged_40_to_44_years_count` | `bigint` | Source field; count of "aged 40 to 44 years" in LSOA usual residents. |
| `aged_45_to_49_years_count` | `bigint` | Source field; count of "aged 45 to 49 years" in LSOA usual residents. |
| `aged_50_to_54_years_count` | `bigint` | Source field; count of "aged 50 to 54 years" in LSOA usual residents. |
| `aged_55_to_59_years_count` | `bigint` | Source field; count of "aged 55 to 59 years" in LSOA usual residents. |
| `aged_60_to_64_years_count` | `bigint` | Source field; count of "aged 60 to 64 years" in LSOA usual residents. |
| `aged_65_years_count` | `bigint` | Source field; count of "aged 65 years" in LSOA usual residents. |
| `aged_66_to_69_years_count` | `bigint` | Source field; count of "aged 66 to 69 years" in LSOA usual residents. |
| `aged_70_to_74_years_count` | `bigint` | Source field; count of "aged 70 to 74 years" in LSOA usual residents. |
| `aged_75_to_79_years_count` | `bigint` | Source field; count of "aged 75 to 79 years" in LSOA usual residents. |
| `aged_80_to_84_years_count` | `bigint` | Source field; count of "aged 80 to 84 years" in LSOA usual residents. |
| `aged_85_years_and_over_count` | `bigint` | Source field; count of "aged 85 years and over" in LSOA usual residents. |
| `aged_2_years_and_under_perc` | `double precision` | Source field; percentage of "aged 2 years and under" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_3_to_4_years_perc` | `double precision` | Source field; percentage of "aged 3 to 4 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_5_to_7_years_perc` | `double precision` | Source field; percentage of "aged 5 to 7 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_8_to_9_years_perc` | `double precision` | Source field; percentage of "aged 8 to 9 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_10_to_14_years_perc` | `double precision` | Source field; percentage of "aged 10 to 14 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_15_years_perc` | `double precision` | Source field; percentage of "aged 15 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_16_to_17_years_perc` | `double precision` | Source field; percentage of "aged 16 to 17 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_18_to_19_years_perc` | `double precision` | Source field; percentage of "aged 18 to 19 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_20_to_24_years_perc` | `double precision` | Source field; percentage of "aged 20 to 24 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_25_to_29_years_perc` | `double precision` | Source field; percentage of "aged 25 to 29 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_30_to_34_years_perc` | `double precision` | Source field; percentage of "aged 30 to 34 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_35_to_39_years_perc` | `double precision` | Source field; percentage of "aged 35 to 39 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_40_to_44_years_perc` | `double precision` | Source field; percentage of "aged 40 to 44 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_45_to_49_years_perc` | `double precision` | Source field; percentage of "aged 45 to 49 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_50_to_54_years_perc` | `double precision` | Source field; percentage of "aged 50 to 54 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_55_to_59_years_perc` | `double precision` | Source field; percentage of "aged 55 to 59 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_60_to_64_years_perc` | `double precision` | Source field; percentage of "aged 60 to 64 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_65_years_perc` | `double precision` | Source field; percentage of "aged 65 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_66_to_69_years_perc` | `double precision` | Source field; percentage of "aged 66 to 69 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_70_to_74_years_perc` | `double precision` | Source field; percentage of "aged 70 to 74 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_75_to_79_years_perc` | `double precision` | Source field; percentage of "aged 75 to 79 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_80_to_84_years_perc` | `double precision` | Source field; percentage of "aged 80 to 84 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_85_years_and_over_perc` | `double precision` | Source field; percentage of "aged 85 years and over" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_2_years_and_under_female_count` | `bigint` | Source field; count of "aged 2 years and under female" in LSOA usual residents. |
| `aged_3_to_4_years_female_count` | `bigint` | Source field; count of "aged 3 to 4 years female" in LSOA usual residents. |
| `aged_5_to_7_years_female_count` | `bigint` | Source field; count of "aged 5 to 7 years female" in LSOA usual residents. |
| `aged_8_to_9_years_female_count` | `bigint` | Source field; count of "aged 8 to 9 years female" in LSOA usual residents. |
| `aged_10_to_14_years_female_count` | `bigint` | Source field; count of "aged 10 to 14 years female" in LSOA usual residents. |
| `aged_15_years_female_count` | `bigint` | Source field; count of "aged 15 years female" in LSOA usual residents. |
| `aged_16_to_17_years_female_count` | `bigint` | Source field; count of "aged 16 to 17 years female" in LSOA usual residents. |
| `aged_18_to_19_years_female_count` | `bigint` | Source field; count of "aged 18 to 19 years female" in LSOA usual residents. |
| `aged_20_to_24_years_female_count` | `bigint` | Source field; count of "aged 20 to 24 years female" in LSOA usual residents. |
| `aged_25_to_29_years_female_count` | `bigint` | Source field; count of "aged 25 to 29 years female" in LSOA usual residents. |
| `aged_30_to_34_years_female_count` | `bigint` | Source field; count of "aged 30 to 34 years female" in LSOA usual residents. |
| `aged_35_to_39_years_female_count` | `bigint` | Source field; count of "aged 35 to 39 years female" in LSOA usual residents. |
| `aged_40_to_44_years_female_count` | `bigint` | Source field; count of "aged 40 to 44 years female" in LSOA usual residents. |
| `aged_45_to_49_years_female_count` | `bigint` | Source field; count of "aged 45 to 49 years female" in LSOA usual residents. |
| `aged_50_to_54_years_female_count` | `bigint` | Source field; count of "aged 50 to 54 years female" in LSOA usual residents. |
| `aged_55_to_59_years_female_count` | `bigint` | Source field; count of "aged 55 to 59 years female" in LSOA usual residents. |
| `aged_60_to_64_years_female_count` | `bigint` | Source field; count of "aged 60 to 64 years female" in LSOA usual residents. |
| `aged_65_years_female_count` | `bigint` | Source field; count of "aged 65 years female" in LSOA usual residents. |
| `aged_66_to_69_years_female_count` | `bigint` | Source field; count of "aged 66 to 69 years female" in LSOA usual residents. |
| `aged_70_to_74_years_female_count` | `bigint` | Source field; count of "aged 70 to 74 years female" in LSOA usual residents. |
| `aged_75_to_79_years_female_count` | `bigint` | Source field; count of "aged 75 to 79 years female" in LSOA usual residents. |
| `aged_80_to_84_years_female_count` | `bigint` | Source field; count of "aged 80 to 84 years female" in LSOA usual residents. |
| `aged_85_years_and_over_female_count` | `bigint` | Source field; count of "aged 85 years and over female" in LSOA usual residents. |
| `aged_2_years_and_under_female_perc` | `double precision` | Source field; percentage of "aged 2 years and under female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_3_to_4_years_female_perc` | `double precision` | Source field; percentage of "aged 3 to 4 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_5_to_7_years_female_perc` | `double precision` | Source field; percentage of "aged 5 to 7 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_8_to_9_years_female_perc` | `double precision` | Source field; percentage of "aged 8 to 9 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_10_to_14_years_female_perc` | `double precision` | Source field; percentage of "aged 10 to 14 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_15_years_female_perc` | `double precision` | Source field; percentage of "aged 15 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_16_to_17_years_female_perc` | `double precision` | Source field; percentage of "aged 16 to 17 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_18_to_19_years_female_perc` | `double precision` | Source field; percentage of "aged 18 to 19 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_20_to_24_years_female_perc` | `double precision` | Source field; percentage of "aged 20 to 24 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_25_to_29_years_female_perc` | `double precision` | Source field; percentage of "aged 25 to 29 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_30_to_34_years_female_perc` | `double precision` | Source field; percentage of "aged 30 to 34 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_35_to_39_years_female_perc` | `double precision` | Source field; percentage of "aged 35 to 39 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_40_to_44_years_female_perc` | `double precision` | Source field; percentage of "aged 40 to 44 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_45_to_49_years_female_perc` | `double precision` | Source field; percentage of "aged 45 to 49 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_50_to_54_years_female_perc` | `double precision` | Source field; percentage of "aged 50 to 54 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_55_to_59_years_female_perc` | `double precision` | Source field; percentage of "aged 55 to 59 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_60_to_64_years_female_perc` | `double precision` | Source field; percentage of "aged 60 to 64 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_65_years_female_perc` | `double precision` | Source field; percentage of "aged 65 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_66_to_69_years_female_perc` | `double precision` | Source field; percentage of "aged 66 to 69 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_70_to_74_years_female_perc` | `double precision` | Source field; percentage of "aged 70 to 74 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_75_to_79_years_female_perc` | `double precision` | Source field; percentage of "aged 75 to 79 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_80_to_84_years_female_perc` | `double precision` | Source field; percentage of "aged 80 to 84 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_85_years_and_over_female_perc` | `double precision` | Source field; percentage of "aged 85 years and over female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_2_years_and_under_male_count` | `bigint` | Source field; count of "aged 2 years and under male" in LSOA usual residents. |
| `aged_3_to_4_years_male_count` | `bigint` | Source field; count of "aged 3 to 4 years male" in LSOA usual residents. |
| `aged_5_to_7_years_male_count` | `bigint` | Source field; count of "aged 5 to 7 years male" in LSOA usual residents. |
| `aged_8_to_9_years_male_count` | `bigint` | Source field; count of "aged 8 to 9 years male" in LSOA usual residents. |
| `aged_10_to_14_years_male_count` | `bigint` | Source field; count of "aged 10 to 14 years male" in LSOA usual residents. |
| `aged_15_years_male_count` | `bigint` | Source field; count of "aged 15 years male" in LSOA usual residents. |
| `aged_16_to_17_years_male_count` | `bigint` | Source field; count of "aged 16 to 17 years male" in LSOA usual residents. |
| `aged_18_to_19_years_male_count` | `bigint` | Source field; count of "aged 18 to 19 years male" in LSOA usual residents. |
| `aged_20_to_24_years_male_count` | `bigint` | Source field; count of "aged 20 to 24 years male" in LSOA usual residents. |
| `aged_25_to_29_years_male_count` | `bigint` | Source field; count of "aged 25 to 29 years male" in LSOA usual residents. |
| `aged_30_to_34_years_male_count` | `bigint` | Source field; count of "aged 30 to 34 years male" in LSOA usual residents. |
| `aged_35_to_39_years_male_count` | `bigint` | Source field; count of "aged 35 to 39 years male" in LSOA usual residents. |
| `aged_40_to_44_years_male_count` | `bigint` | Source field; count of "aged 40 to 44 years male" in LSOA usual residents. |
| `aged_45_to_49_years_male_count` | `bigint` | Source field; count of "aged 45 to 49 years male" in LSOA usual residents. |
| `aged_50_to_54_years_male_count` | `bigint` | Source field; count of "aged 50 to 54 years male" in LSOA usual residents. |
| `aged_55_to_59_years_male_count` | `bigint` | Source field; count of "aged 55 to 59 years male" in LSOA usual residents. |
| `aged_60_to_64_years_male_count` | `bigint` | Source field; count of "aged 60 to 64 years male" in LSOA usual residents. |
| `aged_65_years_male_count` | `bigint` | Source field; count of "aged 65 years male" in LSOA usual residents. |
| `aged_66_to_69_years_male_count` | `bigint` | Source field; count of "aged 66 to 69 years male" in LSOA usual residents. |
| `aged_70_to_74_years_male_count` | `bigint` | Source field; count of "aged 70 to 74 years male" in LSOA usual residents. |
| `aged_75_to_79_years_male_count` | `bigint` | Source field; count of "aged 75 to 79 years male" in LSOA usual residents. |
| `aged_80_to_84_years_male_count` | `bigint` | Source field; count of "aged 80 to 84 years male" in LSOA usual residents. |
| `aged_85_years_and_over_male_count` | `bigint` | Source field; count of "aged 85 years and over male" in LSOA usual residents. |
| `aged_2_years_and_under_male_perc` | `double precision` | Source field; percentage of "aged 2 years and under male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_3_to_4_years_male_perc` | `double precision` | Source field; percentage of "aged 3 to 4 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_5_to_7_years_male_perc` | `double precision` | Source field; percentage of "aged 5 to 7 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_8_to_9_years_male_perc` | `double precision` | Source field; percentage of "aged 8 to 9 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_10_to_14_years_male_perc` | `double precision` | Source field; percentage of "aged 10 to 14 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_15_years_male_perc` | `double precision` | Source field; percentage of "aged 15 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_16_to_17_years_male_perc` | `double precision` | Source field; percentage of "aged 16 to 17 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_18_to_19_years_male_perc` | `double precision` | Source field; percentage of "aged 18 to 19 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_20_to_24_years_male_perc` | `double precision` | Source field; percentage of "aged 20 to 24 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_25_to_29_years_male_perc` | `double precision` | Source field; percentage of "aged 25 to 29 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_30_to_34_years_male_perc` | `double precision` | Source field; percentage of "aged 30 to 34 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_35_to_39_years_male_perc` | `double precision` | Source field; percentage of "aged 35 to 39 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_40_to_44_years_male_perc` | `double precision` | Source field; percentage of "aged 40 to 44 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_45_to_49_years_male_perc` | `double precision` | Source field; percentage of "aged 45 to 49 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_50_to_54_years_male_perc` | `double precision` | Source field; percentage of "aged 50 to 54 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_55_to_59_years_male_perc` | `double precision` | Source field; percentage of "aged 55 to 59 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_60_to_64_years_male_perc` | `double precision` | Source field; percentage of "aged 60 to 64 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_65_years_male_perc` | `double precision` | Source field; percentage of "aged 65 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_66_to_69_years_male_perc` | `double precision` | Source field; percentage of "aged 66 to 69 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_70_to_74_years_male_perc` | `double precision` | Source field; percentage of "aged 70 to 74 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_75_to_79_years_male_perc` | `double precision` | Source field; percentage of "aged 75 to 79 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_80_to_84_years_male_perc` | `double precision` | Source field; percentage of "aged 80 to 84 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_85_years_and_over_male_perc` | `double precision` | Source field; percentage of "aged 85 years and over male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `dominant_sex` | `text` | Added during an earlier Prior + Partners loading pass. Label of the modal sex group for the LSOA. |
| `dominant_age_group` | `text` | Derived during an earlier Prior + Partners loading pass; label of the modal category for this LSOA. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. Boundary geometry joined at load. |
| `fid` | `bigint` |  |
