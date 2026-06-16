# Ordnance Survey OS Open Rivers — watercourse network for Great Britain, April 2025

<p class="layer-short">Open Rivers</p>

`env_os_rivers_apr2025`

<img src="../../maps/env_os_rivers_apr2025.png" alt="Styling preview of env_os_rivers_apr2025" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Ordnance Survey (OS), OS Open Rivers product.

**DOCUMENTATION**

- OS Open Rivers : https://www.ordnancesurvey.co.uk/products/os-open-rivers

**DEFINITIONS**

- "An open dataset of the high-level view of watercourses in Great Britain." (OS Open Rivers product page)

**SCOPE**

- Great Britain. 570,566 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type LineString.

**LICENCE**

- OS OpenData Licence (incorporates Open Government Licence v3.0; attribution "Contains OS data © Crown copyright and database right" required).

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `name1` | `character varying` | Source field "name1"; watercourse name. |
| `identifier` | `character varying` | Source field "identifier"; OS source feature identifier. |
| `startnode` | `character varying` | Source field "startnode"; network start node identifier. |
| `endnode` | `character varying` | Source field "endnode"; network end node identifier. |
| `form` | `character varying` | Source field "form"; watercourse form. Observed values: "inlandRiver", "tidalRiver", "lake", "canal". |
| `flow` | `character varying` | Source field "flow"; flow direction. Observed values: "in direction", "in opposite direction", "unknown", "missing". |
| `fictitious` | `character varying` | Source field "fictitious"; flag for fictitious (connector) links. |
| `length` | `bigint` | Source field "length"; watercourse length as published. |
| `name2` | `character varying` | Source field "name2"; alternative watercourse name (where present). |
| `fid_original` | `integer` | Original feature id preserved at load. |
| `lad22nm` | `character varying` | Joined at load from ONS LSOA->LAD 2022 lookup; 2022 LAD name. |
| `lad22cd` | `character varying` | Joined at load from ONS LSOA->LAD 2022 lookup; 2022 LAD GSS code. |
| `wd21nm` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward name. |
| `wd21cd` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward GSS code. |
| `geom` | `geometry(LineString,27700)` | LineString in EPSG:27700. Watercourse network geometry. |
| `length_m` | `double precision` | Length in metres. |
| `fid` | `bigint` |  |
