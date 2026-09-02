# Geographic Data Service (GeoDS) Unified UK Census 2021/2022, Ethnic group, United Kingdom small-area extent, March 2026

<p class="layer-short">Census 2021 Ethnic group (UK)</p>

`dem_geods_oa_ethnic_group_2021`

**SOURCE**

- Geographic Data Service (GeoDS), Smart Data Research UK. Unified UK Census Data (2021/2), topic table uk021 from variable_tables_csv.zip (published 19 February 2026, last modified 3 March 2026). Harmonised by GeoDS from Office for National Statistics (ONS), National Records of Scotland (NRS) and Northern Ireland Statistics and Research Agency (NISRA) census outputs. All 13 source columns copied as published under their source variable identifiers; nothing derived, renamed or filtered.

**DOCUMENTATION**

- Dataset page : https://data.geods.ac.uk/dataset/unified-uk-census-data
- Method paper (Goodwin and Singleton) : https://doi.org/10.1177/23998083261429563
- Source code : https://github.com/GeographicDataService/unified-uk-census-2021-22
- Variable Metadata and Table Notes files : shipped with the download; local copy on the P: source folder 260902_GeoDS_Unified UK Census 2021-22.

**DEFINITIONS**

- "The Unified UK Census Dataset (2021/2022) is a harmonised, small-area dataset that brings together census data from the three UK census agencies -- ONS (England & Wales), NRS (Scotland), and NISRA (Northern Ireland) -- into a single, comparable release." (GeoDS dataset page)
- "The dataset available for download contains the counts for all 190 variables plus 25 table totals (215 variables in total) across each of the 239,023 small-area geographies. Data Zones are relabelled as "OA" in the dataset for consistency." (GeoDS dataset page)
- Table unit: "Person". Population scope: "All Persons". (GeoDS Table Notes)
- Census Day: "21 March 2021 for England, Wales, and Northern Ireland, and 20 March 2022 for Scotland." (GeoDS dataset page)

**SCOPE**

- United Kingdom. 239,023 rows, one per small area: England 178,605; Wales 10,275; Scotland 46,363; Northern Ireland 3,780. Codes are Output Area 2021 (E00, W00), Output Area 2022 (S00) and Data Zone 2021 (N20).
- Counts only; uk021001 is the table total. No percentages are supplied by the publisher and none were computed.
- Sibling of the other 24 GeoDS Unified UK Census tables named dem_geods_oa_*_2021.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry from uk_baseline.adm_ons_oa_boundaries_dec2021 (England and Wales, Output Area 2021), uk_baseline.adm_nrs_oa_boundary_2022 (Scotland, Output Area 2022) and uk_baseline.adm_nisra_dz_boundary_2021 (Northern Ireland, Data Zone 2021), joined at load on the row's code.

**LICENCE**

- Open Government Licence v3.0. Attribution: "The data for this research have been provided by the Geographic Data Service (geods.ac.uk), a Smart Data Research UK Investment: ES/Z504464/1. These were created as part of an ESRC Census data opportunity grant - ES/Z50273X/1. Contains data from: ONS, NRS, NISRA"

**DATA QUALITY CAVEATS**

- "The Scottish census was conducted one year later than the rest of the UK (2022 vs 2021), which may introduce temporal differences in some variables." (GeoDS dataset page)
- "The data are compiled from the official census releases of the three UK statistical agencies, each of which applies its own disclosure control and data quality procedures." (GeoDS dataset page)
- Harmonisation notes for this table (GeoDS Table Notes, verbatim): "1. The Northern Irish questionnaire differed slightly from the rest of the nations - of note is that "Gypsy or Irish Traveller" and "Roma" were not considered subdivisions of "White" as they are for the remaining nations. Due to these differences subdivisions of "White" are not available in the unified tables.  2. The subdivisions of "Asian" ethnicity differ in the Northern Ireland table in two ways. No variable is provided for Bangladeshi, this variable is included in the unified table with all counts for Northern Ireland being set to zero. An additional variable for the Filipino ethnic group is available, this variable is aggregated into the "Other Asian" variable in the combined table. 3. Northern Ireland Table Ethnic Group - 5 Categories is not used as the aggregations are different from the rest of the UK, ie "Arab" is considered part of the "Asian" aggregation. The Northern Ireland aggregations are instead created by combining variables."
- Northern Ireland geometry was reprojected from Irish Grid with about 3 m accuracy; see uk_baseline.adm_nisra_dz_boundary_2021.

**LOADED INTO uk_baseline**

- Loaded by PNC, 2 September 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid` | `integer` |  |
| `oa` | `character varying(9)` | Source field `OA`; small-area code: "OA21CD (England/Wales), OA22CD (Scotland), DZ21CD (Northern Ireland)" (GeoDS). Northern Ireland Data Zones are labelled OA by the publisher. |
| `uk021001` | `integer` | Source field `uk021001`; "Ethnic group: Total: All usual residents". Unit: "Person". |
| `uk021002` | `integer` | Source field `uk021002`; "Ethnic group: Asian". Unit: "Person". |
| `uk021003` | `integer` | Source field `uk021003`; "Ethnic group: Asian: Bangladeshi". Unit: "Person". |
| `uk021004` | `integer` | Source field `uk021004`; "Ethnic group: Asian: Chinese". Unit: "Person". |
| `uk021005` | `integer` | Source field `uk021005`; "Ethnic group: Asian: Indian". Unit: "Person". |
| `uk021006` | `integer` | Source field `uk021006`; "Ethnic group: Asian: Pakistani". Unit: "Person". |
| `uk021007` | `integer` | Source field `uk021007`; "Ethnic group: Asian: Other Asian". Unit: "Person". |
| `uk021008` | `integer` | Source field `uk021008`; "Ethnic group: Black, Caribbean or African". Unit: "Person". |
| `uk021009` | `integer` | Source field `uk021009`; "Ethnic group: Mixed or Multiple ethnic groups". Unit: "Person". |
| `uk021010` | `integer` | Source field `uk021010`; "Ethnic group: White". Unit: "Person". |
| `uk021011` | `integer` | Source field `uk021011`; "Ethnic group: Other ethnic group". Unit: "Person". |
| `uk021012` | `integer` | Source field `uk021012`; "Ethnic group: Other ethnic group: Arab". Unit: "Person". |
| `uk021013` | `integer` | Source field `uk021013`; "Ethnic group: Other ethnic group: Any other ethnic group". Unit: "Person". |
| `geom` | `geometry(MultiPolygon,27700)` | Geometry from uk_baseline.adm_ons_oa_boundaries_dec2021 (England and Wales, Output Area 2021), uk_baseline.adm_nrs_oa_boundary_2022 (Scotland, Output Area 2022) and uk_baseline.adm_nisra_dz_boundary_2021 (Northern Ireland, Data Zone 2021), joined at load on the row's code. |
