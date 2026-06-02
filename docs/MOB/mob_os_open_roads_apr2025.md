# Ordnance Survey OS Open Roads - road network for Great Britain, April 2025

`mob_os_open_roads_apr2025`

<a href="http://localhost:7800/?layer=uk_baseline.mob_os_open_roads_apr2025" target="_blank" rel="noopener">Open in the Dashboard &#8599;</a> <span style="opacity:.6;font-size:.85em;">(start your local Dashboard first)</span>

**SOURCE**

- Ordnance Survey (OS), OS Open Roads product.

**DOCUMENTATION**

- OS Open Roads : https://www.ordnancesurvey.co.uk/products/os-open-roads

**DEFINITIONS**

- "A structured link-and-node network, which represents the central alignment of all classified and unclassified roads in Great Britain." (Ordnance Survey, OS Open Roads)

**SCOPE**

- Great Britain. 4,207,717 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type LineString.

**LICENCE**

- OS OpenData Licence (incorporates Open Government Licence v3.0; attribution "Contains OS data (c) Crown copyright and database right" required).


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `id` | `character varying` | Source field; OS feature identifier. |
| `fictitious` | `boolean` | Source field "fictitious"; flag for fictitious (connector) links. |
| `road_classification` | `character varying` | Source field "road_classification"; road classification. Observed values: "Unclassified", "Unknown", "Not Classified", "Classified Unnumbered", "A Road", "B Road", "Motorway". |
| `road_function` | `character varying` | Source field "road_function"; road function. Observed values: "Local Road", "Restricted Local Access Road", "Minor Road", "A Road", "B Road", "Secondary Access Road", "Local Access Road", "Motorway". |
| `form_of_way` | `character varying` | Source field "form_of_way"; physical form of the road (e.g. single carriageway, dual carriageway, roundabout, slip road). |
| `road_classification_number` | `character varying` | Source field "road_classification_number"; road number (e.g. "M1", "A40"). |
| `name_1` | `character varying` | Source field "name_1"; primary road name. |
| `name_1_lang` | `character varying` | Source field "name_1_lang"; language of name_1. |
| `name_2` | `character varying` | Source field "name_2"; alternative road name. |
| `name_2_lang` | `character varying` | Source field "name_2_lang"; language of name_2. |
| `road_structure` | `character varying` | Source field "road_structure"; structural form (e.g. bridge, tunnel) where applicable. |
| `length` | `double precision` | Source field "length"; road link length as published. |
| `length_uom` | `character varying` | Source field "length_uom"; unit of measure for length (e.g. "m"). |
| `loop` | `boolean` | Source field "loop"; flag for loop links. |
| `primary_route` | `boolean` | Source field "primary_route"; flag for primary routes. |
| `trunk_road` | `boolean` | Source field "trunk_road"; flag for trunk roads. |
| `start_node` | `character varying` | Source field "start_node"; network start node identifier. |
| `end_node` | `character varying` | Source field "end_node"; network end node identifier. |
| `road_number_toid` | `character varying` | Source field "road_number_toid"; OS TOID of the associated road number. |
| `road_name_toid` | `character varying` | Source field "road_name_toid"; OS TOID of the associated road name. |
| `fid_original` | `integer` | ArcGIS source identifier preserved at load. |
| `lad22nm` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD name. |
| `lad22cd` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD GSS code. |
| `wd21nm` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward name. |
| `wd21cd` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward GSS code. |
| `geom` | `geometry(LineString,27700)` | LineString in EPSG:27700. Road centreline geometry. |
| `length_m` | `double precision` | Length in metres. |
| `fid` | `bigint` |  |
