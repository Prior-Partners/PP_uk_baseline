# Ordnance Survey OS OpenMap Local - Electricity Transmission Lines for Great Britain

`utl_os_electricity_transmission_line`

<iframe src="../maps/utl_os_electricity_transmission_line.html" title="Interactive preview map of utl_os_electricity_transmission_line" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../maps/utl_os_electricity_transmission_line.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

**SOURCE**

- Ordnance Survey (OS), OS OpenMap Local product.

**DOCUMENTATION**

- OS OpenMap Local                 : https://www.ordnancesurvey.co.uk/products/os-open-map-local
- ElectricityTransmissionLine spec : https://docs.os.uk/os-downloads/products/maps-and-imagery-portfolio/os-openmap-local/os-openmap-local-technical-specification/feature-types/electricitytransmissionline

**DEFINITIONS**

- "Cables used to supply electricity that are suspended between pylons." (OS OpenMap Local Technical Specification, ElectricityTransmissionLine)

**SCOPE**

- Great Britain. 11,831 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type LineString.

**LICENCE**

- OS OpenData Licence (incorporates Open Government Licence v3.0; attribution "Contains OS data (c) Crown copyright and database right" required).


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `feature_code` | `integer` | Source field "feature_code"; OS feature code (15102). |
| `id_original` | `character varying` | Original feature id preserved at load. |
| `lad22nm` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD name. |
| `lad22cd` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD GSS code. |
| `wd21nm` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward name. |
| `wd21cd` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward GSS code. |
| `geom` | `geometry(LineString,27700)` | LineString in EPSG:27700. Electricity transmission line. |
| `length_m` | `double precision` | Length in metres. |
| `fid` | `bigint` |  |
