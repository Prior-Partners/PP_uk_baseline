# Geographic Data Service (GeoDS) Unified UK Census 2021/2022, Method of travel to workplace, United Kingdom small-area extent, March 2026

<p class="layer-short">Census 2021/22 Method of travel to workplace (UK)</p>

`dem_geods_oa_travel_to_work_2021_22`

**SOURCE**

- Geographic Data Service (GeoDS), Smart Data Research UK. Unified UK Census Data (2021/2), topic table uk061 from variable_tables_csv.zip (published 19 February 2026, last modified 3 March 2026). Harmonised by GeoDS from Office for National Statistics (ONS), National Records of Scotland (NRS) and Northern Ireland Statistics and Research Agency (NISRA) census outputs. All 11 source columns copied as published under their source variable identifiers; nothing derived, renamed or filtered.

**DOCUMENTATION**

- Dataset page : https://data.geods.ac.uk/dataset/unified-uk-census-data
- Method paper (Goodwin and Singleton) : https://doi.org/10.1177/23998083261429563
- Source code : https://github.com/GeographicDataService/unified-uk-census-2021-22
- Variable Metadata and Table Notes files : shipped with the download; local copy on the P: source folder 260902_GeoDS_Unified UK Census 2021-22.

**DEFINITIONS**

- "The Unified UK Census Dataset (2021/2022) is a harmonised, small-area dataset that brings together census data from the three UK census agencies -- ONS (England & Wales), NRS (Scotland), and NISRA (Northern Ireland) -- into a single, comparable release." (GeoDS dataset page)
- "The dataset available for download contains the counts for all 190 variables plus 25 table totals (215 variables in total) across each of the 239,023 small-area geographies. Data Zones are relabelled as "OA" in the dataset for consistency." (GeoDS dataset page)
- Table unit: "Person". Population scope: "Persons Aged 16 or over and in full time employment the week before the census. Scotland: Persons Aged 16 or over and in full time employment the week before the census (including full-time students if they gave a work address as the address they primarily travel to for work or study)". (GeoDS Table Notes)
- Census Day: "21 March 2021 for England, Wales, and Northern Ireland, and 20 March 2022 for Scotland." (GeoDS dataset page)

**SCOPE**

- United Kingdom. 239,023 rows, one per small area: England 178,605; Wales 10,275; Scotland 46,363; Northern Ireland 3,780. Codes are Output Area 2021 (E00, W00), Output Area 2022 (S00) and Data Zone 2021 (N20).
- Counts only; uk061001 is the table total. No percentages are supplied by the publisher and none were computed.
- Sibling of the other 24 GeoDS Unified UK Census tables named dem_geods_oa_*_2021_22.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry from uk_baseline.adm_ons_oa_boundaries_dec2021 (England and Wales, Output Area 2021), uk_baseline.adm_nrs_oa_boundary_2022 (Scotland, Output Area 2022) and uk_baseline.adm_nisra_dz_boundary_2021 (Northern Ireland, Data Zone 2021), joined at load on the row's code.

**LICENCE**

- Open Government Licence v3.0. Attribution: "The data for this research have been provided by the Geographic Data Service (geods.ac.uk), a Smart Data Research UK Investment: ES/Z504464/1. These were created as part of an ESRC Census data opportunity grant - ES/Z50273X/1. Contains data from: ONS, NRS, NISRA"

**DATA QUALITY CAVEATS**

- "The Scottish census was conducted one year later than the rest of the UK (2022 vs 2021), which may introduce temporal differences in some variables." (GeoDS dataset page)
- "The data are compiled from the official census releases of the three UK statistical agencies, each of which applies its own disclosure control and data quality procedures." (GeoDS dataset page)
- Harmonisation notes for this table (GeoDS Table Notes, verbatim): "1. Changes in working patterns due to the COVID-19 pandemic severely impact this variable 2. The Northern Ireland table does not contain the variable "Method of travel to workplace: Underground, metro, light rail, tram", as this form of transport is not available in Northern Ireland. The counts for this variable in the unified table are therefore set to zero for all Northern Ireland Data Zones. 3. An aggregated "Car or Van" variable is created for the unified tables, as the subdivisions of this variable differ for Northern Ireland to the rest of the censuses. 4. The variables for Scotland include those who travel for study as well as work."
- "The COVID-19 pandemic severely impacted method of travel to workplace data across all nations." (GeoDS dataset page)
- Northern Ireland geometry was reprojected from Irish Grid with about 3 m accuracy; see uk_baseline.adm_nisra_dz_boundary_2021.

**LOADED INTO uk_baseline**

- Loaded by PNC, 2 September 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid` | `integer` |  |
| `oa` | `character varying(9)` | Source field `OA`; small-area code: "OA21CD (England/Wales), OA22CD (Scotland), DZ21CD (Northern Ireland)" (GeoDS). Northern Ireland Data Zones are labelled OA by the publisher. |
| `uk061001` | `integer` | Source field `uk061001`; "Method of travel to workplace: Total: All usual residents aged 16 years and over in employment the week before the census". Unit: "Person". |
| `uk061002` | `integer` | Source field `uk061002`; "Method of travel to workplace: Work mainly at or from home". Unit: "Person". |
| `uk061003` | `integer` | Source field `uk061003`; "Method of travel to workplace: Underground, metro, light rail, tram". Unit: "Person". |
| `uk061004` | `integer` | Source field `uk061004`; "Method of travel to workplace: Train". Unit: "Person". |
| `uk061005` | `integer` | Source field `uk061005`; "Method of travel to workplace: Bus, minibus or coach". Unit: "Person". |
| `uk061006` | `integer` | Source field `uk061006`; "Method of travel to workplace: Taxi". Unit: "Person". |
| `uk061007` | `integer` | Source field `uk061007`; "Method of travel to workplace: Motorcycle, scooter or moped". Unit: "Person". |
| `uk061008` | `integer` | Source field `uk061008`; "Method of travel to workplace: Car or van". Unit: "Person". |
| `uk061009` | `integer` | Source field `uk061009`; "Method of travel to workplace: Bicycle". Unit: "Person". |
| `uk061010` | `integer` | Source field `uk061010`; "Method of travel to workplace: On foot". Unit: "Person". |
| `uk061011` | `integer` | Source field `uk061011`; "Method of travel to workplace: Other method of travel to work". Unit: "Person". |
| `geom` | `geometry(MultiPolygon,27700)` | Geometry from uk_baseline.adm_ons_oa_boundaries_dec2021 (England and Wales, Output Area 2021), uk_baseline.adm_nrs_oa_boundary_2022 (Scotland, Output Area 2022) and uk_baseline.adm_nisra_dz_boundary_2021 (Northern Ireland, Data Zone 2021), joined at load on the row's code. |
