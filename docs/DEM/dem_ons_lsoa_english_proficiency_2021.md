# ONS Census 2021 English-language proficiency at Lower-layer Super Output Area (LSOA) 2021

`dem_ons_lsoa_english_proficiency_2021`

**SOURCE**

- Office for National Statistics (ONS), Census 2021, England and Wales. Table TS029 "Proficiency in English". Reference date 21 March 2021. Loaded via an earlier Prior + Partners pass.

**DOCUMENTATION**

- ONS dataset (TS029) : https://www.ons.gov.uk/datasets/TS029/editions/2021/versions/1
- ONS Census 2021 landing page : https://www.ons.gov.uk/census/2021

**DEFINITIONS**

- "How well people whose main language is not English (English or Welsh in Wales) speak English. The categories are: Main language is English (English or Welsh in Wales); Main language is not English (English or Welsh in Wales): can speak English very well; can speak English well; cannot speak English well; cannot speak English." (ONS Census 2021 Proficiency in English variable)
- Asked of usual residents aged 3 years and over.

**SCOPE**

- England and Wales. LSOA 2021 boundary; 35,672 distinct lsoa21cd.
- Base population: usual residents aged 3 years and over.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Open Government Licence v3.0.

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
| `main_language_english_count` | `bigint` | Source field; count of "main language english" in LSOA usual residents aged 3+. |
| `main_language_not_english_can_speak_english_very_well_count` | `bigint` | Source field; count of "main language not english can speak english very well" in LSOA usual residents aged 3+. |
| `main_language_not_english_can_speak_english_well_count` | `bigint` | Source field; count of "main language not english can speak english well" in LSOA usual residents aged 3+. |
| `main_language_not_english_cannot_speak_english_well_count` | `bigint` | Source field; count of "main language not english cannot speak english well" in LSOA usual residents aged 3+. |
| `main_language_not_english_cannot_speak_english_count` | `bigint` | Source field; count of "main language not english cannot speak english" in LSOA usual residents aged 3+. |
| `main_language_english_perc` | `double precision` | Source field; percentage of "main language english" in LSOA usual residents aged 3+. Unit: "percent (0 to 100)". |
| `main_language_not_english_can_speak_english_very_well_perc` | `double precision` | Source field; percentage of "main language not english can speak english very well" in LSOA usual residents aged 3+. Unit: "percent (0 to 100)". |
| `main_language_not_english_can_speak_english_well_perc` | `double precision` | Source field; percentage of "main language not english can speak english well" in LSOA usual residents aged 3+. Unit: "percent (0 to 100)". |
| `main_language_not_english_cannot_speak_english_well_perc` | `double precision` | Source field; percentage of "main language not english cannot speak english well" in LSOA usual residents aged 3+. Unit: "percent (0 to 100)". |
| `main_language_not_english_cannot_speak_english_perc` | `double precision` | Source field; percentage of "main language not english cannot speak english" in LSOA usual residents aged 3+. Unit: "percent (0 to 100)". |
| `dominant_english_proficiency_group` | `text` | Derived during an earlier Prior + Partners loading pass; label of the modal category for this LSOA. |
| `wd22cd` | `character varying` | Joined at load from ONS LSOA->Ward lookup; 2022 Ward GSS code. |
| `wd22nm` | `character varying` | Joined at load from ONS LSOA->Ward lookup; 2022 Ward name. |
| `fid` | `bigint` |  |
