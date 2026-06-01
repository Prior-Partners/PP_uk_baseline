# `ecn_geods_foodretail_accessibility_apr2026`

GeoDS London Nighttime Access to Food Retail Options, April 2026.

**SOURCE**

- Geographic Data Service (GeoDS), Smart Data Research UK (SDR UK): University College London (UCL), University of Liverpool, University of Oxford, University of Edinburgh.
- Dataset created 2026-01-28; last updated by publisher 2026-04-15.
- Underlying analysis: Iliev, M., Cheshire, J., & Law, S. (2026). "Revealing the geography of food (in)accessibility for nighttime workers in the Greater London Area." Urban Studies, 0(0).

**DOCUMENTATION**

- Catalogue page : https://data.geods.ac.uk/dataset/london-nighttime-access-to-food-retail-options
- Source files : hex_foodretail_accessibility.gpkg, hex_food_variable_dictionary.csv, hex_food_data_summary.csv, food_travel_time_allhex.csv

**DEFINITIONS**

- Hex_ID: "Unique cell ID of bespoke BT hexagonal grid" (hex_food_variable_dictionary.csv)
- travel_time_xxxx_yy: "Travel-time to the closest open food retail outlet on day xxxx (Friday or Saturday) at yy (hour of the day)" (hex_food_variable_dictionary.csv)
- Retail outlets in scope: Supermarkets, Grocers, Greengrocers & Fruitsellers, Convenience Stores. 8,337 outlets analysed. (catalogue page)
- General Transit Feed Specification (GTFS) schedules used: 1-2 March 2024. Multimodal routing combines walking, waiting and transfer times. (catalogue page)

**SCOPE**

- Greater London Authority (GLA) area; outlet capture extends to outlets within 2,000 metres of the GLA boundary.
- 15,041 hexagonal cells, 350-metre spacing.
- Temporal coverage: Friday 06:00 to Saturday 06:00, snapshot week of 2024-03-01 to 2024-03-02.

**CRS**

- EPSG:27700 (OSGB36 / British National Grid). Native CRS as published; no reprojection at load.

**LICENCE**

- UK Open Government Licence (OGL) v3.0.

**DATA QUALITY CAVEATS**

- Travel-time UNIT is INFERRED as minutes. The publisher's hex_food_variable_dictionary.csv does NOT state a unit. The inference is based on the routing description on the catalogue page, the 0-60 value range, and the temporal granularity. Confirm with publisher before any unit-sensitive downstream use.
- NULL share per hourly snapshot is 2.5%-3.9% (peaking saturday_01-03). Publisher documentation does not specify whether NULL = "no outlet reachable inside the analysis cap" or "missing from analysis".
- Values appear capped at 60. Whether this is the analytical horizon or the maximum observed travel time is not documented.
- Hex_ID is stored as double precision but the publisher's data summary reports type=integer. Values are well within int4 range.

**LOADED INTO uk_baseline**

- Data published: 2026-04-15
- Imported: 2026-05-28 by PNC


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `geom` | `geometry(Polygon,27700)` | Geometry from publisher GPKG (hex_foodretail_accessibility.gpkg). EPSG:27700 (OSGB36 / British National Grid). Polygon - one 350-metre bespoke hexagonal cell per row. |
| `fid` | `bigint` |  |
| `hex_id` | `double precision` | Source field `Hex_ID`. "Unique cell ID of bespoke BT hexagonal grid" (hex_food_variable_dictionary.csv). Stored as double precision in DB; publisher data summary reports type=integer with range 10,631,211 - 12,541,266. |
| `travel_time_friday_06` | `double precision` | Source field `travel_time_friday_06`. Unit: "Travel-time to the closest open food retail outlet on day xxxx (Friday or Saturday) at yy (hour of the day)" - unit inferred as MINUTES (publisher does not state). Friday 06:00 snapshot (daytime, 3-hourly cadence). |
| `travel_time_friday_09` | `double precision` | Source field `travel_time_friday_09`. Unit: minutes (inferred; publisher does not state). Friday 09:00 snapshot (daytime, 3-hourly cadence). |
| `travel_time_friday_12` | `double precision` | Source field `travel_time_friday_12`. Unit: minutes (inferred; publisher does not state). Friday 12:00 snapshot (daytime, 3-hourly cadence). |
| `travel_time_friday_15` | `double precision` | Source field `travel_time_friday_15`. Unit: minutes (inferred; publisher does not state). Friday 15:00 snapshot (daytime, 3-hourly cadence). |
| `travel_time_friday_18` | `double precision` | Source field `travel_time_friday_18`. Unit: minutes (inferred; publisher does not state). Friday 18:00 snapshot (daytime, 3-hourly cadence). |
| `travel_time_friday_19` | `double precision` | Source field `travel_time_friday_19`. Unit: minutes (inferred; publisher does not state). Friday 19:00 snapshot (nighttime, hourly cadence). |
| `travel_time_friday_20` | `double precision` | Source field `travel_time_friday_20`. Unit: minutes (inferred; publisher does not state). Friday 20:00 snapshot (nighttime, hourly cadence). |
| `travel_time_friday_21` | `double precision` | Source field `travel_time_friday_21`. Unit: minutes (inferred; publisher does not state). Friday 21:00 snapshot (nighttime, hourly cadence). |
| `travel_time_friday_22` | `double precision` | Source field `travel_time_friday_22`. Unit: minutes (inferred; publisher does not state). Friday 22:00 snapshot (nighttime, hourly cadence). |
| `travel_time_friday_23` | `double precision` | Source field `travel_time_friday_23`. Unit: minutes (inferred; publisher does not state). Friday 23:00 snapshot (nighttime, hourly cadence). |
| `travel_time_saturday_00` | `double precision` | Source field `travel_time_saturday_00`. Unit: minutes (inferred; publisher does not state). Saturday 00:00 snapshot (nighttime, hourly cadence). |
| `travel_time_saturday_01` | `double precision` | Source field `travel_time_saturday_01`. Unit: minutes (inferred; publisher does not state). Saturday 01:00 snapshot (nighttime, hourly cadence). |
| `travel_time_saturday_02` | `double precision` | Source field `travel_time_saturday_02`. Unit: minutes (inferred; publisher does not state). Saturday 02:00 snapshot (nighttime, hourly cadence). |
| `travel_time_saturday_03` | `double precision` | Source field `travel_time_saturday_03`. Unit: minutes (inferred; publisher does not state). Saturday 03:00 snapshot (nighttime, hourly cadence). |
| `travel_time_saturday_04` | `double precision` | Source field `travel_time_saturday_04`. Unit: minutes (inferred; publisher does not state). Saturday 04:00 snapshot (nighttime, hourly cadence). |
| `travel_time_saturday_05` | `double precision` | Source field `travel_time_saturday_05`. Unit: minutes (inferred; publisher does not state). Saturday 05:00 snapshot (nighttime, hourly cadence). |
