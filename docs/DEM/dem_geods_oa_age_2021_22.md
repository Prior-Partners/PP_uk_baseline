# Geographic Data Service (GeoDS) Unified UK Census 2021/2022, Age, United Kingdom small-area extent, March 2026

<p class="layer-short">Census 2021/22 Age (UK)</p>

`dem_geods_oa_age_2021_22`

**SOURCE**

- Geographic Data Service (GeoDS), Smart Data Research UK. Unified UK Census Data (2021/2), topic table uk007a from variable_tables_csv.zip (published 19 February 2026, last modified 3 March 2026). Harmonised by GeoDS from Office for National Statistics (ONS), National Records of Scotland (NRS) and Northern Ireland Statistics and Research Agency (NISRA) census outputs. All 19 source columns copied as published; nothing derived or filtered. Columns carry readable names from the GeoDS labels (see SCOPE); the GeoDS identifier is recorded in every column comment.

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
- Counts only; `total` (GeoDS uk007a001) is the table total. No percentages are supplied by the publisher and none were computed.
- Column names are readable forms of the GeoDS labels, signed off by the data manager on 2 September 2026; each column comment names the GeoDS source identifier. Mapping: scripts/unified_census/column_names.py.
- Sibling of the other 24 GeoDS Unified UK Census tables named dem_geods_oa_*_2021_22.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry from uk_baseline.adm_ons_oa_boundaries_dec2021 (England and Wales, Output Area 2021), uk_baseline.adm_nrs_oa_boundary_2022 (Scotland, Output Area 2022) and uk_baseline.adm_nisra_dz_boundary_2021 (Northern Ireland, Data Zone 2021), joined at load on the row's code.

**LICENCE**

- Open Government Licence v3.0. Attribution: "The data for this research have been provided by the Geographic Data Service (geods.ac.uk), a Smart Data Research UK Investment: ES/Z504464/1. These were created as part of an ESRC Census data opportunity grant - ES/Z50273X/1. Contains data from: ONS, NRS, NISRA"

**DATA QUALITY CAVEATS**

- "The Scottish census was conducted one year later than the rest of the UK (2022 vs 2021), which may introduce temporal differences in some variables." (GeoDS dataset page)
- "The data are compiled from the official census releases of the three UK statistical agencies, each of which applies its own disclosure control and data quality procedures." (GeoDS dataset page)
- Northern Ireland geometry was reprojected from Irish Grid with about 3 m accuracy; see uk_baseline.adm_nisra_dz_boundary_2021.
- 9 Scottish polygons (S00136407, S00136544, S00138851, S00142130, S00148144, S00162192, S00176070, S00177785, S00181661) were published with a ring touching itself at one vertex and were repaired on 2 September 2026 with the data manager's approval; no change in area.

**LOADED INTO uk_baseline**

- Loaded by PNC, 2 September 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid` | `integer` |  |
| `oa` | `character varying(9)` | Source field `OA`; small-area code: "OA21CD (England/Wales), OA22CD (Scotland), DZ21CD (Northern Ireland)" (GeoDS). Northern Ireland Data Zones are labelled OA by the publisher. |
| `total` | `integer` | Source field `uk007a001`; "Age: Total". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `aged_4_and_under` | `integer` | Source field `uk007a002`; "Age: Aged 4 years and under". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `aged_5_to_9` | `integer` | Source field `uk007a003`; "Age: Aged 5 to 9 years". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `aged_10_to_14` | `integer` | Source field `uk007a004`; "Age: Aged 10 to 14 years". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `aged_15_to_19` | `integer` | Source field `uk007a005`; "Age: Aged 15 to 19 years". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `aged_20_to_24` | `integer` | Source field `uk007a006`; "Age: Aged 20 to 24 years". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `aged_25_to_29` | `integer` | Source field `uk007a007`; "Age: Aged 25 to 29 years". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `aged_30_to_34` | `integer` | Source field `uk007a008`; "Age: Aged 30 to 34 years". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `aged_35_to_39` | `integer` | Source field `uk007a009`; "Age: Aged 35 to 39 years". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `aged_40_to_44` | `integer` | Source field `uk007a010`; "Age: Aged 40 to 44 years". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `aged_45_to_49` | `integer` | Source field `uk007a011`; "Age: Aged 45 to 49 years". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `aged_50_to_54` | `integer` | Source field `uk007a012`; "Age: Aged 50 to 54 years". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `aged_55_to_59` | `integer` | Source field `uk007a013`; "Age: Aged 55 to 59 years". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `aged_60_to_64` | `integer` | Source field `uk007a014`; "Age: Aged 60 to 64 years". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `aged_65_to_69` | `integer` | Source field `uk007a015`; "Age: Aged 65 to 69 years". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `aged_70_to_74` | `integer` | Source field `uk007a016`; "Age: Aged 70 to 74 years". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `aged_75_to_79` | `integer` | Source field `uk007a017`; "Age: Aged 75 to 79 years". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `aged_80_to_84` | `integer` | Source field `uk007a018`; "Age: Aged 80 to 84 years". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `aged_85_and_over` | `integer` | Source field `uk007a019`; "Age: Aged 85 years and over". Unit: "Person". Column renamed from the GeoDS identifier on 2 September 2026 (data manager sign-off). |
| `geom` | `geometry(MultiPolygon,27700)` | Geometry from uk_baseline.adm_ons_oa_boundaries_dec2021 (England and Wales, Output Area 2021), uk_baseline.adm_nrs_oa_boundary_2022 (Scotland, Output Area 2022) and uk_baseline.adm_nisra_dz_boundary_2021 (Northern Ireland, Data Zone 2021), joined at load on the row's code. |
