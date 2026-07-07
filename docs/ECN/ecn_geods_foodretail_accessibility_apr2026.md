# GeoDS London Nighttime Access to Food Retail Options, April 2026

<p class="layer-short">London Nighttime Access to Food Retail</p>

`ecn_geods_foodretail_accessibility_apr2026`

<img src="../../maps/ecn_geods_foodretail_accessibility_apr2026.png" alt="Styling preview of ecn_geods_foodretail_accessibility_apr2026" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Geographic Data Service (GeoDS), Smart Data Research UK (SDR UK): University College London (UCL), University of Liverpool, University of Oxford, University of Edinburgh.
- Dataset created Jan 2026; last updated by publisher Apr 2026.
- Underlying analysis: Iliev, M., Cheshire, J., & Law, S. (2026). "Revealing the geography of food (in)accessibility for nighttime workers in the Greater London Area." Urban Studies, 0(0).

**DOCUMENTATION**

- Catalogue page : https://data.geods.ac.uk/dataset/london-nighttime-access-to-food-retail-options
- Source files : hex_foodretail_accessibility.gpkg, hex_food_variable_dictionary.csv, hex_food_data_summary.csv, food_travel_time_allhex.csv

**DEFINITIONS**

- Hex_ID: "Unique cell ID of bespoke BT hexagonal grid" (hex_food_variable_dictionary.csv)
- travel_time_xxxx_yy: "Travel-time to the closest open food retail outlet on day xxxx (Friday or Saturday) at yy (hour of the day)" (hex_food_variable_dictionary.csv)
- Unit: "reports travel times (in minutes) to the nearest open food retail outlet across Greater London, measured on a granular hexagonal grid (350-metre edge-to-edge)" (catalogue page)
- Reporting intervals: "Daytime accessibility (6:00 a.m.–6:00 p.m.), included for comparative purposes, is reported in 3-hour intervals, while nighttime accessibility (6:00 p.m.–6:00 a.m. the following day) is reported at hourly intervals." (catalogue page)
- Missing values: "Missing values (NA) are assigned to hexagons that are either inaccessible (i.e., contain no road network) or have travel times exceeding 60 minutes, which is our maximum travel-time threshold." (catalogue page)
- Retail outlets in scope: Supermarkets, Grocers, Greengrocers & Fruitsellers, Convenience Stores. 8,337 outlets analysed. (catalogue page)
- General Transit Feed Specification (GTFS) schedules used: 1-2 March 2024. Multimodal routing combines walking, waiting and transfer times. (catalogue page)

**SCOPE**

- Greater London Authority (GLA) area; outlet capture extends to outlets within 2,000 metres of the GLA boundary.
- 15,041 hexagonal cells, 350-metre spacing.
- Temporal coverage: Friday 06:00 to Saturday 06:00, snapshot of 1-2 March 2024.

**CRS**

- EPSG:27700 (OSGB36 / British National Grid). Native CRS as published; no reprojection at load.

**LICENCE**

- UK Open Government Licence (OGL) v3.0.

**DATA QUALITY CAVEATS**

- 2.5%-3.9% of cells are NULL per hourly snapshot, peaking in the Saturday 01:00-03:00 columns.
- Hex_ID is stored as double precision but the publisher's data summary reports type=integer. Values are well within int4 range.

**ENRICHMENT**

- msoa21cd, msoa21nm, msoa21hclnm, lad22cd, lad22nm, lad25cd, lad25nm, source_fid, gid

**LOADED INTO uk_baseline**

- Loaded by PNC, 28 May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `source_fid` | `bigint` | Primary key of the source feature in the pre-split layer uk.ecn_geods_foodretail_accessibility_apr2026__preswap_jul03 (non-unique here: a feature spanning N MSOAs has N rows). |
| `hex_id` | `double precision` | Source field "Hex_ID"; "Unique cell ID of bespoke BT hexagonal grid" (hex_food_variable_dictionary.csv). |
| `travel_time_friday_06` | `double precision` | Source field "travel_time_friday_06"; travel time to the closest open food retail outlet on Friday at 06:00. Unit: "minutes". NULL where the hexagon is inaccessible or the travel time exceeds the publisher's 60-minute maximum. |
| `travel_time_friday_09` | `double precision` | Source field "travel_time_friday_09"; travel time to the closest open food retail outlet on Friday at 09:00. Unit: "minutes". NULL where the hexagon is inaccessible or the travel time exceeds the publisher's 60-minute maximum. |
| `travel_time_friday_12` | `double precision` | Source field "travel_time_friday_12"; travel time to the closest open food retail outlet on Friday at 12:00. Unit: "minutes". NULL where the hexagon is inaccessible or the travel time exceeds the publisher's 60-minute maximum. |
| `travel_time_friday_15` | `double precision` | Source field "travel_time_friday_15"; travel time to the closest open food retail outlet on Friday at 15:00. Unit: "minutes". NULL where the hexagon is inaccessible or the travel time exceeds the publisher's 60-minute maximum. |
| `travel_time_friday_18` | `double precision` | Source field "travel_time_friday_18"; travel time to the closest open food retail outlet on Friday at 18:00. Unit: "minutes". NULL where the hexagon is inaccessible or the travel time exceeds the publisher's 60-minute maximum. |
| `travel_time_friday_19` | `double precision` | Source field "travel_time_friday_19"; travel time to the closest open food retail outlet on Friday at 19:00. Unit: "minutes". NULL where the hexagon is inaccessible or the travel time exceeds the publisher's 60-minute maximum. |
| `travel_time_friday_20` | `double precision` | Source field "travel_time_friday_20"; travel time to the closest open food retail outlet on Friday at 20:00. Unit: "minutes". NULL where the hexagon is inaccessible or the travel time exceeds the publisher's 60-minute maximum. |
| `travel_time_friday_21` | `double precision` | Source field "travel_time_friday_21"; travel time to the closest open food retail outlet on Friday at 21:00. Unit: "minutes". NULL where the hexagon is inaccessible or the travel time exceeds the publisher's 60-minute maximum. |
| `travel_time_friday_22` | `double precision` | Source field "travel_time_friday_22"; travel time to the closest open food retail outlet on Friday at 22:00. Unit: "minutes". NULL where the hexagon is inaccessible or the travel time exceeds the publisher's 60-minute maximum. |
| `travel_time_friday_23` | `double precision` | Source field "travel_time_friday_23"; travel time to the closest open food retail outlet on Friday at 23:00. Unit: "minutes". NULL where the hexagon is inaccessible or the travel time exceeds the publisher's 60-minute maximum. |
| `travel_time_saturday_00` | `double precision` | Source field "travel_time_saturday_00"; travel time to the closest open food retail outlet on Saturday at 00:00. Unit: "minutes". NULL where the hexagon is inaccessible or the travel time exceeds the publisher's 60-minute maximum. |
| `travel_time_saturday_01` | `double precision` | Source field "travel_time_saturday_01"; travel time to the closest open food retail outlet on Saturday at 01:00. Unit: "minutes". NULL where the hexagon is inaccessible or the travel time exceeds the publisher's 60-minute maximum. |
| `travel_time_saturday_02` | `double precision` | Source field "travel_time_saturday_02"; travel time to the closest open food retail outlet on Saturday at 02:00. Unit: "minutes". NULL where the hexagon is inaccessible or the travel time exceeds the publisher's 60-minute maximum. |
| `travel_time_saturday_03` | `double precision` | Source field "travel_time_saturday_03"; travel time to the closest open food retail outlet on Saturday at 03:00. Unit: "minutes". NULL where the hexagon is inaccessible or the travel time exceeds the publisher's 60-minute maximum. |
| `travel_time_saturday_04` | `double precision` | Source field "travel_time_saturday_04"; travel time to the closest open food retail outlet on Saturday at 04:00. Unit: "minutes". NULL where the hexagon is inaccessible or the travel time exceeds the publisher's 60-minute maximum. |
| `travel_time_saturday_05` | `double precision` | Source field "travel_time_saturday_05"; travel time to the closest open food retail outlet on Saturday at 05:00. Unit: "minutes". NULL where the hexagon is inaccessible or the travel time exceeds the publisher's 60-minute maximum. |
| `msoa21cd` | `character varying` | Middle Layer Super Output Area (MSOA) 2021 code of this piece. Open Government Licence v3.0. |
| `msoa21nm` | `character varying` | Official ONS MSOA 2021 name of this piece. Open Government Licence v3.0. |
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name of this piece. Open Parliament Licence. |
| `lad22cd` | `text` | Local Authority District 2022 code (2021 LAD geography, anchored to the MSOA 2021 name scoping), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad22nm` | `text` | Local Authority District 2022 name (2021 LAD geography), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25cd` | `text` | Local Authority District 2025 code (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority), best-fit from this piece's msoa21cd. Open Government Licence v3.0. |
| `geom` | `geometry(MultiPolygon,27700)` |  |
| `gid` | `bigint` |  |
