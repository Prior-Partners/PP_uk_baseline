# National Cycle Network (NCN) for the United Kingdom, September 2024

`mob_wwct_national_cycle_network_sep2024`

**SOURCE**

- Sustrans (now Walk Wheel Cycle Trust). National Cycle Network dataset, distributed via the Sustrans open-data hub.

**DOCUMENTATION**

- Sustrans open data     : https://data-sustrans-uk.opendata.arcgis.com/
- National Cycle Network : https://www.walkwheelcycletrust.org.uk/national-cycle-network/

**DEFINITIONS**

- The National Cycle Network is "a UK-wide network of signed paths and routes for walking, wheeling, cycling and exploring outdoors, brought to you by Walk Wheel Cycle Trust." (Walk Wheel Cycle Trust, National Cycle Network)

**SCOPE**

- United Kingdom. 46,248 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type LineString.

**LICENCE**

- Open Government Licence v3.0 (confirm with Sustrans / Walk Wheel Cycle Trust before re-publication).


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `desc_` | `character varying(200)` | Source field "desc_"; route description. |
| `greenway` | `character varying(3)` | Source field "greenway"; greenway indicator. |
| `routetype` | `character varying(4)` | Source field "routetype"; route type. Observed values: "NCN" (National Cycle Network), "LINK", "RCN" (Regional Cycle Network). |
| `routeno` | `integer` | Source field "routeno"; route number. |
| `linkno` | `integer` | Source field "linkno"; link number. |
| `routecat` | `character varying(19)` | Source field "routecat"; route category. |
| `openstatus` | `character varying(23)` | Source field "openstatus"; open status. Observed values: "Open", "Temporary Closure". |
| `surface` | `character varying(13)` | Source field "surface"; surface type. |
| `quality` | `character varying(10)` | Source field "quality"; route quality. |
| `lighting` | `character varying(7)` | Source field "lighting"; lighting provision. |
| `roadclass` | `character varying(32)` | Source field "roadclass"; road class. |
| `globalid` | `character varying(38)` | Source field "GlobalID"; ArcGIS GlobalID GUID. |
| `segmentid` | `integer` | Source field "segmentid"; segment identifier. |
| `id_original` | `integer` | Original feature id preserved at load. |
| `lad22nm` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD name. |
| `lad22cd` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD GSS code. |
| `wd21nm` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward name. |
| `wd21cd` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward GSS code. |
| `geom` | `geometry(LineString,27700)` | LineString in EPSG:27700. National Cycle Network route geometry. |
| `length_m` | `double precision` | Length in metres. |
| `fid` | `bigint` |  |
