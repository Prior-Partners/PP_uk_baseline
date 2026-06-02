# Ordnance Survey OS Open Greenspace — Access Points for Great Britain, April 2025

`env_os_green_space_access_points_apr2025`

<a href="http://localhost:7800/?layer=uk_baseline.env_os_green_space_access_points_apr2025" target="_blank" rel="noopener">Open in the Dashboard &#8599;</a> <span style="opacity:.6;font-size:.85em;">(start your local Dashboard first)</span>

**SOURCE**

- Ordnance Survey (OS), OS Open Greenspace product (Access Points layer).

**DOCUMENTATION**

- OS Open Greenspace : https://www.ordnancesurvey.co.uk/products/os-open-greenspace

**DEFINITIONS**

- "access points for entering and exiting urban and rural green spaces." (OS Open Greenspace product page)

**SCOPE**

- Great Britain. 342,351 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type Point.

**LICENCE**

- OS OpenData Licence (incorporates Open Government Licence v3.0; attribution "Contains OS data © Crown copyright and database right" required).

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `id` | `character varying` | Source field "id"; OS source feature identifier. |
| `accesstype` | `character varying` | Source field "accesstype"; access type. Observed values: "Pedestrian", "Motor Vehicle And Pedestrian", "Motor Vehicle". |
| `reftogsite` | `character varying` | Source field "reftogsite"; reference to the parent greenspace site id. |
| `fid_original` | `integer` | Original feature id preserved at load. |
| `lad22nm` | `character varying` | Joined at load from ONS LSOA->LAD 2022 lookup; 2022 LAD name. |
| `lad22cd` | `character varying` | Joined at load from ONS LSOA->LAD 2022 lookup; 2022 LAD GSS code. |
| `wd21nm` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward name. |
| `wd21cd` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward GSS code. |
| `geom` | `geometry(Point,27700)` | Point in EPSG:27700. Greenspace access point. |
| `fid` | `bigint` |  |
