# Ordnance Survey OS OpenMap Local - Railway Tunnels for Great Britain

`mob_os_railway_tunnels`

<a href="http://localhost:7800/?layer=uk_baseline.mob_os_railway_tunnels" target="_blank" rel="noopener">Open in the Dashboard &#8599;</a> <span style="opacity:.6;font-size:.85em;">(start your local Dashboard first)</span>

**SOURCE**

- Ordnance Survey (OS), OS OpenMap Local product.

**DOCUMENTATION**

- OS OpenMap Local   : https://www.ordnancesurvey.co.uk/products/os-open-map-local
- RailwayTunnel spec : https://docs.os.uk/os-downloads/products/maps-and-imagery-portfolio/os-openmap-local/os-openmap-local-technical-specification/feature-types/railwaytunnel

**DEFINITIONS**

- "Railway tunnels are represented as approximate centrelines of the railway that runs through the tunnel." (OS OpenMap Local Technical Specification, RailwayTunnel)

**SCOPE**

- Great Britain. 2,755 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type LineString.

**LICENCE**

- OS OpenData Licence (incorporates Open Government Licence v3.0; attribution required).


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `id` | `character varying` | Source field; OS feature identifier. |
| `feature_code` | `bigint` | Source field "feature_code"; OS feature code (15303). |
| `fid_original` | `integer` | ArcGIS source identifier preserved at load. |
| `lad22nm` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD name. |
| `lad22cd` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD GSS code. |
| `wd21nm` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward name. |
| `wd21cd` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward GSS code. |
| `geom` | `geometry(LineString,27700)` | LineString in EPSG:27700. Railway tunnel centreline. |
| `length_m` | `double precision` | Length in metres. |
| `fid` | `bigint` |  |
