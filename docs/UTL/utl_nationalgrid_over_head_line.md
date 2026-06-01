# National Grid Electricity Transmission - overhead lines, England and Wales

`utl_nationalgrid_over_head_line`

<iframe src="../../maps/utl_nationalgrid_over_head_line.html" title="Interactive preview map of utl_nationalgrid_over_head_line" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../../maps/utl_nationalgrid_over_head_line.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

**SOURCE**

- National Grid Electricity Transmission. High-voltage transmission overhead line assets.

**DOCUMENTATION**

- National Grid Electricity Transmission : https://www.nationalgrid.com/electricity-transmission

**DEFINITIONS**

- An overhead transmission line transmits power from the generating source into the national grid network, and on to substations that provide power to homes and businesses. (National Grid)

**SCOPE**

- England and Wales. 3,780 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type LineString.

**LICENCE**

- © National Grid. Licence - confirm with National Grid before re-publication.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `gdo_gid` | `numeric` | Source field "gdo_gid"; source feature identifier. |
| `route_asse` | `character varying(12)` | Source field "route_asse"; route asset reference (name truncated). |
| `towers_in` | `character varying(40)` | Source field "towers_in"; towers on the route (name truncated). |
| `action_dtt` | `date` | Source field "action_dtt"; action date (name truncated). |
| `status` | `character varying(1)` | Source field "status"; source status code. Observed values: "C", "E". |
| `operating_` | `character varying(18)` | Source field "operating_"; operating voltage in kV. Observed values: "400", "275", "132", "33", "25". |
| `circuit1` | `character varying(200)` | Source field "circuit1"; first circuit identifier. |
| `circuit2` | `character varying(200)` | Source field "circuit2"; second circuit identifier. |
| `id_original` | `integer` | Original feature id preserved at load. |
| `lad22nm` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD name. |
| `lad22cd` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD GSS code. |
| `wd21nm` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward name. |
| `wd21cd` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward GSS code. |
| `geom` | `geometry(LineString,27700)` | LineString in EPSG:27700. Overhead transmission line route. |
| `length_m` | `double precision` | Length in metres. |
| `fid` | `bigint` |  |
