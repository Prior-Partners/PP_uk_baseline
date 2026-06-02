# ONS Census 2021 usual residents by age band at Lower-layer Super Output Area (LSOA) 2021

`dem_ons_lsoa_age_alternate_bands_2021`

<a href="http://localhost:7800/?layer=uk_baseline.dem_ons_lsoa_age_alternate_bands_2021" target="_blank" rel="noopener">Open in the Dashboard &#8599;</a> <span style="opacity:.6;font-size:.85em;">(start your local Dashboard first)</span>

**SOURCE**

- Office for National Statistics (ONS), Census 2021, England and Wales. ONS publishes age in multiple alternative bandings — single-year (TS007a), 5-year (TS007a, alternative variant), broad bands (TS007b). This table holds several of those bandings side-by-side. Reference date 21 March 2021. Loaded via an earlier Prior + Partners pass; original load pathway not recorded.

**DOCUMENTATION**

- ONS Census 2021 age variable : https://www.ons.gov.uk/census/census2021dictionary/variablesbytopic/demographyvariablescensus2021/age
- ONS dataset (TS007a) : https://www.ons.gov.uk/datasets/TS007A/editions/2021/versions/1
- ONS Census 2021 landing page : https://www.ons.gov.uk/census/2021
- NOMIS bulk download : https://www.nomisweb.co.uk/sources/census_2021

**DEFINITIONS**

- "A person's age on Census Day, 21 March 2021. Infants aged less than one year are classified as 0 years." (ONS Census 2021 Demography variables — Age)
- "A usual resident is anyone who, on Census Day, was in the UK and had stayed or intended to stay in the UK for a period of 12 months or more, or had a permanent UK address and was outside the UK and intended to be outside the UK for less than 12 months." (ONS Census 2021 Demography variables — Usual resident)

**SCOPE**

- England and Wales. LSOA 2021 boundary; 35,672 distinct lsoa21cd.
- Base population: all usual residents.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid).

**LICENCE**

- Open Government Licence v3.0.

**DATA QUALITY CAVEATS**

- The 103-column shape combines several age bandings (single-year, 5-year, broad). Be precise about which banding you sum — different bandings overlap and double-counting is easy. Confirm the column-list grouping at first use; see the column comments for which banding each column belongs to.
- The `dominant_age_*` column (if present) is a derived label from the earlier load; methodology not recorded.

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
| `mid_2011_population_count` | `bigint` | Source field; count of "mid 2011 population" in LSOA usual residents. |
| `mid_2016_population_count` | `bigint` | Source field; count of "mid 2016 population" in LSOA usual residents. |
| `mid_2021_population_count` | `bigint` | Source field; count of "mid 2021 population" in LSOA usual residents. |
| `mid_2011_people_per_ha` | `double precision` | Added during an earlier Prior + Partners loading pass. Derived population density for the LSOA in mid-2011: ONS Mid-2011 population estimate / area_ha. Unit: "persons per hectare". |
| `mid_2016_people_per_ha` | `double precision` | Added during an earlier Prior + Partners loading pass. Derived population density for the LSOA in mid-2016: ONS Mid-2016 population estimate / area_ha. Unit: "persons per hectare". |
| `mid_2021_people_per_ha` | `double precision` | Added during an earlier Prior + Partners loading pass. Derived population density for the LSOA in mid-2021: ONS Mid-2021 population estimate / area_ha. Unit: "persons per hectare". |
| `change_in_population_2021_10yr` | `bigint` | Added during an earlier Prior + Partners loading pass. Change in LSOA population over the last 10 years to 2021 (2021 ONS estimate - 2011 ONS estimate). Unit: "persons". |
| `change_in_population_2021_5yr` | `bigint` | Added during an earlier Prior + Partners loading pass. Change in LSOA population over the last 5 years to 2021 (2021 ONS estimate - 2016 ONS estimate). Unit: "persons". |
| `change_in_population_density_2021_10yr_change` | `double precision` | Added during an earlier Prior + Partners loading pass. Change in LSOA population density over the last 10 years to 2021. Unit: "persons per hectare". |
| `change_in_population_density_2021_5yr_change` | `double precision` | Added during an earlier Prior + Partners loading pass. Change in LSOA population density over the last 5 years to 2021. Unit: "persons per hectare". |
| `2021_households_count` | `bigint` | Source field; count of "2021 households" in LSOA usual residents. |
| `2021_households_per_ha` | `double precision` | Added during an earlier Prior + Partners loading pass. Derived households density for the LSOA: total households / area_ha. Unit: "households per hectare". Column name is digit-led — use double-quoted identifier in SQL. |
| `2021_total_population_count` | `bigint` | Source field; count of "2021 total population" in LSOA usual residents. |
| `2021_female_population_count` | `bigint` | Source field; count of "2021 female population" in LSOA usual residents. |
| `2021_male_population_count` | `bigint` | Source field; count of "2021 male population" in LSOA usual residents. |
| `2021_female_population_perc` | `double precision` | Source field; percentage of "2021 female population" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `2021_male_population_perc` | `double precision` | Source field; percentage of "2021 male population" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_0_to_9_years_count` | `bigint` | Source field; count of "aged 0 to 9 years" in LSOA usual residents. |
| `aged_10_to_15_years_count` | `bigint` | Source field; count of "aged 10 to 15 years" in LSOA usual residents. |
| `aged_16_to_19_years_count` | `bigint` | Source field; count of "aged 16 to 19 years" in LSOA usual residents. |
| `aged_20_to_29_years_count` | `bigint` | Source field; count of "aged 20 to 29 years" in LSOA usual residents. |
| `aged_30_to_39_years_count` | `bigint` | Source field; count of "aged 30 to 39 years" in LSOA usual residents. |
| `aged_40_to_49_years_count` | `bigint` | Source field; count of "aged 40 to 49 years" in LSOA usual residents. |
| `aged_50_to_59_years_count` | `bigint` | Source field; count of "aged 50 to 59 years" in LSOA usual residents. |
| `aged_60_to_64_years_count` | `bigint` | Source field; count of "aged 60 to 64 years" in LSOA usual residents. |
| `aged_65_to_69_years_count` | `bigint` | Source field; count of "aged 65 to 69 years" in LSOA usual residents. |
| `aged_70_to_79_years_count` | `bigint` | Source field; count of "aged 70 to 79 years" in LSOA usual residents. |
| `aged_80_and_above_years_count` | `bigint` | Source field; count of "aged 80 and above years" in LSOA usual residents. |
| `aged_0_to_9_years_perc` | `double precision` | Source field; percentage of "aged 0 to 9 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_10_to_15_years_perc` | `double precision` | Source field; percentage of "aged 10 to 15 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_16_to_19_years_perc` | `double precision` | Source field; percentage of "aged 16 to 19 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_20_to_29_years_perc` | `double precision` | Source field; percentage of "aged 20 to 29 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_30_to_39_years_perc` | `double precision` | Source field; percentage of "aged 30 to 39 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_40_to_49_years_perc` | `double precision` | Source field; percentage of "aged 40 to 49 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_50_to_59_years_perc` | `double precision` | Source field; percentage of "aged 50 to 59 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_60_to_64_years_perc` | `double precision` | Source field; percentage of "aged 60 to 64 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_65_to_69_years_perc` | `double precision` | Source field; percentage of "aged 65 to 69 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_70_to_79_years_perc` | `double precision` | Source field; percentage of "aged 70 to 79 years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_80_and_above_years_perc` | `double precision` | Source field; percentage of "aged 80 and above years" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_0_to_9_years_female_count` | `bigint` | Source field; count of "aged 0 to 9 years female" in LSOA usual residents. |
| `aged_10_to_15_years_female_count` | `bigint` | Source field; count of "aged 10 to 15 years female" in LSOA usual residents. |
| `aged_16_to_19_years_female_count` | `bigint` | Source field; count of "aged 16 to 19 years female" in LSOA usual residents. |
| `aged_20_to_29_years_female_count` | `bigint` | Source field; count of "aged 20 to 29 years female" in LSOA usual residents. |
| `aged_30_to_39_years_female_count` | `bigint` | Source field; count of "aged 30 to 39 years female" in LSOA usual residents. |
| `aged_40_to_49_years_female_count` | `bigint` | Source field; count of "aged 40 to 49 years female" in LSOA usual residents. |
| `aged_50_to_59_years_female_count` | `bigint` | Source field; count of "aged 50 to 59 years female" in LSOA usual residents. |
| `aged_60_to_64_years_female_count` | `bigint` | Source field; count of "aged 60 to 64 years female" in LSOA usual residents. |
| `aged_65_to_69_years_female_count` | `bigint` | Source field; count of "aged 65 to 69 years female" in LSOA usual residents. |
| `aged_70_to_79_years_female_count` | `bigint` | Source field; count of "aged 70 to 79 years female" in LSOA usual residents. |
| `aged_80_and_above_years_female_count` | `bigint` | Source field; count of "aged 80 and above years female" in LSOA usual residents. |
| `aged_0_to_9_years_female_perc` | `double precision` | Source field; percentage of "aged 0 to 9 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_10_to_15_years_female_perc` | `double precision` | Source field; percentage of "aged 10 to 15 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_16_to_19_years_female_perc` | `double precision` | Source field; percentage of "aged 16 to 19 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_20_to_29_years_female_perc` | `double precision` | Source field; percentage of "aged 20 to 29 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_30_to_39_years_female_perc` | `double precision` | Source field; percentage of "aged 30 to 39 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_40_to_49_years_female_perc` | `double precision` | Source field; percentage of "aged 40 to 49 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_50_to_59_years_female_perc` | `double precision` | Source field; percentage of "aged 50 to 59 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_60_to_64_years_female_perc` | `double precision` | Source field; percentage of "aged 60 to 64 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_65_to_69_years_female_perc` | `double precision` | Source field; percentage of "aged 65 to 69 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_70_to_79_years_female_perc` | `double precision` | Source field; percentage of "aged 70 to 79 years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_80_and_above_years_female_perc` | `double precision` | Source field; percentage of "aged 80 and above years female" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_0_to_9_years_male_count` | `bigint` | Source field; count of "aged 0 to 9 years male" in LSOA usual residents. |
| `aged_10_to_15_years_male_count` | `bigint` | Source field; count of "aged 10 to 15 years male" in LSOA usual residents. |
| `aged_16_to_19_years_male_count` | `bigint` | Source field; count of "aged 16 to 19 years male" in LSOA usual residents. |
| `aged_20_to_29_years_male_count` | `bigint` | Source field; count of "aged 20 to 29 years male" in LSOA usual residents. |
| `aged_30_to_39_years_male_count` | `bigint` | Source field; count of "aged 30 to 39 years male" in LSOA usual residents. |
| `aged_40_to_49_years_male_count` | `bigint` | Source field; count of "aged 40 to 49 years male" in LSOA usual residents. |
| `aged_50_to_59_years_male_count` | `bigint` | Source field; count of "aged 50 to 59 years male" in LSOA usual residents. |
| `aged_60_to_64_years_male_count` | `bigint` | Source field; count of "aged 60 to 64 years male" in LSOA usual residents. |
| `aged_65_to_69_years_male_count` | `bigint` | Source field; count of "aged 65 to 69 years male" in LSOA usual residents. |
| `aged_70_to_79_years_male_count` | `bigint` | Source field; count of "aged 70 to 79 years male" in LSOA usual residents. |
| `aged_80_and_above_years_male_count` | `bigint` | Source field; count of "aged 80 and above years male" in LSOA usual residents. |
| `aged_0_to_9_years_male_perc` | `double precision` | Source field; percentage of "aged 0 to 9 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_10_to_15_years_male_perc` | `double precision` | Source field; percentage of "aged 10 to 15 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_16_to_19_years_male_perc` | `double precision` | Source field; percentage of "aged 16 to 19 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_20_to_29_years_male_perc` | `double precision` | Source field; percentage of "aged 20 to 29 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_30_to_39_years_male_perc` | `double precision` | Source field; percentage of "aged 30 to 39 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_40_to_49_years_male_perc` | `double precision` | Source field; percentage of "aged 40 to 49 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_50_to_59_years_male_perc` | `double precision` | Source field; percentage of "aged 50 to 59 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_60_to_64_years_male_perc` | `double precision` | Source field; percentage of "aged 60 to 64 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_65_to_69_years_male_perc` | `double precision` | Source field; percentage of "aged 65 to 69 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_70_to_79_years_male_perc` | `double precision` | Source field; percentage of "aged 70 to 79 years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `aged_80_and_above_years_male_perc` | `double precision` | Source field; percentage of "aged 80 and above years male" in LSOA usual residents. Unit: "percent (0 to 100)". |
| `dominant_sex` | `text` | Added during an earlier Prior + Partners loading pass. Label of the modal sex group for the LSOA. |
| `dominant_age_group` | `text` | Derived during an earlier Prior + Partners loading pass; label of the modal category for this LSOA. |
| `wd22cd` | `character varying` | Joined at load from ONS LSOA->Ward lookup; 2022 Ward GSS code. |
| `wd22nm` | `character varying` | Joined at load from ONS LSOA->Ward lookup; 2022 Ward name. |
| `fid` | `bigint` |  |
