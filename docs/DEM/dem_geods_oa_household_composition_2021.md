# Geographic Data Service (GeoDS) Unified UK Census 2021/2022, Household composition, United Kingdom small-area extent, March 2026

<p class="layer-short">Census 2021 Household composition (UK)</p>

`dem_geods_oa_household_composition_2021`

**SOURCE**

- Geographic Data Service (GeoDS), Smart Data Research UK. Unified UK Census Data (2021/2), topic table uk003 from variable_tables_csv.zip (published 19 February 2026, last modified 3 March 2026). Harmonised by GeoDS from Office for National Statistics (ONS), National Records of Scotland (NRS) and Northern Ireland Statistics and Research Agency (NISRA) census outputs. All 14 source columns copied as published under their source variable identifiers; nothing derived, renamed or filtered.

**DOCUMENTATION**

- Dataset page : https://data.geods.ac.uk/dataset/unified-uk-census-data
- Method paper (Goodwin and Singleton) : https://doi.org/10.1177/23998083261429563
- Source code : https://github.com/GeographicDataService/unified-uk-census-2021-22
- Variable Metadata and Table Notes files : shipped with the download; local copy on the P: source folder 260902_GeoDS_Unified UK Census 2021-22.

**DEFINITIONS**

- "The Unified UK Census Dataset (2021/2022) is a harmonised, small-area dataset that brings together census data from the three UK census agencies -- ONS (England & Wales), NRS (Scotland), and NISRA (Northern Ireland) -- into a single, comparable release." (GeoDS dataset page)
- "The dataset available for download contains the counts for all 190 variables plus 25 table totals (215 variables in total) across each of the 239,023 small-area geographies. Data Zones are relabelled as "OA" in the dataset for consistency." (GeoDS dataset page)
- Table unit: "Household". Population scope: "All Households". (GeoDS Table Notes)
- Census Day: "21 March 2021 for England, Wales, and Northern Ireland, and 20 March 2022 for Scotland." (GeoDS dataset page)

**SCOPE**

- United Kingdom. 239,023 rows, one per small area: England 178,605; Wales 10,275; Scotland 46,363; Northern Ireland 3,780. Codes are Output Area 2021 (E00, W00), Output Area 2022 (S00) and Data Zone 2021 (N20).
- Counts only; uk003001 is the table total. No percentages are supplied by the publisher and none were computed.
- Sibling of the other 24 GeoDS Unified UK Census tables named dem_geods_oa_*_2021.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry from uk_baseline.adm_ons_oa_boundaries_dec2021 (England and Wales, Output Area 2021), uk_baseline.adm_nrs_oa_boundary_2022 (Scotland, Output Area 2022) and uk_baseline.adm_nisra_dz_boundary_2021 (Northern Ireland, Data Zone 2021), joined at load on the row's code.

**LICENCE**

- Open Government Licence v3.0. Attribution: "The data for this research have been provided by the Geographic Data Service (geods.ac.uk), a Smart Data Research UK Investment: ES/Z504464/1. These were created as part of an ESRC Census data opportunity grant - ES/Z50273X/1. Contains data from: ONS, NRS, NISRA"

**DATA QUALITY CAVEATS**

- "The Scottish census was conducted one year later than the rest of the UK (2022 vs 2021), which may introduce temporal differences in some variables." (GeoDS dataset page)
- "The data are compiled from the official census releases of the three UK statistical agencies, each of which applies its own disclosure control and data quality procedures." (GeoDS dataset page)
- Harmonisation notes for this table (GeoDS Table Notes, verbatim): "1. Due to disclosure control the full granularity table is not available for Northern Ireland. The available table combines married couples and cohabiting couples into a single category. "The Single Family: All over 66" and "Single Family: Other categories" are also combined. These variables were therefore combined for the other nations when producing the unified table. 2. Scotland distinguishes families with one child and families with two or more child, as these variables are not available for the other nations they are excluded from the unified table."
- Northern Ireland geometry was reprojected from Irish Grid with about 3 m accuracy; see uk_baseline.adm_nisra_dz_boundary_2021.

**LOADED INTO uk_baseline**

- Loaded by PNC, 2 September 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid` | `integer` |  |
| `oa` | `character varying(9)` | Source field `OA`; small-area code: "OA21CD (England/Wales), OA22CD (Scotland), DZ21CD (Northern Ireland)" (GeoDS). Northern Ireland Data Zones are labelled OA by the publisher. |
| `uk003001` | `integer` | Source field `uk003001`; "Household composition: Total". Unit: "Household". |
| `uk003002` | `integer` | Source field `uk003002`; "Household composition: One person household". Unit: "Household". |
| `uk003003` | `integer` | Source field `uk003003`; "Household composition: One person household: Aged 66 years and over". Unit: "Household". |
| `uk003004` | `integer` | Source field `uk003004`; "Household composition: One person household: Other". Unit: "Household". |
| `uk003005` | `integer` | Source field `uk003005`; "Household composition: Single family household". Unit: "Household". |
| `uk003006` | `integer` | Source field `uk003006`; "Household composition:  Single family household: Couple family household". Unit: "Household". |
| `uk003007` | `integer` | Source field `uk003007`; "Household composition:  Single family household: Couple family household: No children". Unit: "Household". |
| `uk003008` | `integer` | Source field `uk003008`; "Household composition:  Single family household: Couple family household: Dependent children". Unit: "Household". |
| `uk003009` | `integer` | Source field `uk003009`; "Household composition:  Single family household: Couple family household: All children non-dependent". Unit: "Household". |
| `uk003010` | `integer` | Source field `uk003010`; "Household composition: Single family household: Lone parent family". Unit: "Household". |
| `uk003011` | `integer` | Source field `uk003011`; "Household composition: Single family household: Lone parent family: With dependent children". Unit: "Household". |
| `uk003012` | `integer` | Source field `uk003012`; "Household composition: Single family household: Lone parent family: All children non-dependent". Unit: "Household". |
| `uk003013` | `integer` | Source field `uk003013`; "Household composition: Single family household: Other single family household (including All aged 66 years and over)". Unit: "Household". |
| `uk003014` | `integer` | Source field `uk003014`; "Household composition: Other household types". Unit: "Household". |
| `geom` | `geometry(MultiPolygon,27700)` | Geometry from uk_baseline.adm_ons_oa_boundaries_dec2021 (England and Wales, Output Area 2021), uk_baseline.adm_nrs_oa_boundary_2022 (Scotland, Output Area 2022) and uk_baseline.adm_nisra_dz_boundary_2021 (Northern Ireland, Data Zone 2021), joined at load on the row's code. |
