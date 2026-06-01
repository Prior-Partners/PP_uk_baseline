# National Grid Electricity Transmission - underground cables, England and Wales

`utl_nationalgrid_cables`

<iframe src="../../maps/utl_nationalgrid_cables.html" title="Interactive preview map of utl_nationalgrid_cables" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../../maps/utl_nationalgrid_cables.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

**SOURCE**

- National Grid Electricity Transmission. High-voltage transmission underground cable assets.

**DOCUMENTATION**

- National Grid Electricity Transmission : https://www.nationalgrid.com/electricity-transmission

**DEFINITIONS**

- National Grid Electricity Transmission owns and maintains the high-voltage electricity transmission network in England and Wales; this layer represents the network's underground cable assets. (National Grid)

**SCOPE**

- England and Wales. 4,580 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type LineString.

**LICENCE**

- © National Grid. Licence - confirm with National Grid before re-publication.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `gdo_gid` | `numeric` | Source field "gdo_gid"; source feature identifier. |
| `operating_` | `bigint` | Source field "operating_"; operating voltage (name truncated). |
| `action_dtt` | `date` | Source field "action_dtt"; action date (name truncated). |
| `status` | `character varying(1)` | Source field "status"; source status code. Observed values: "C", "E", "P". |
| `cable_type` | `character varying(14)` | Source field "cable_type"; cable type. Observed values: "A/C" (alternating current), "D/C" (direct current), "DECOMMISSIONED", "CBL_UNKNOWN". |
| `comments` | `character varying(254)` | Source field "comments"; free-text comments. |
| `tunnel` | `character varying(1)` | Source field "tunnel"; tunnel indicator. |
| `owned` | `character varying(1)` | Source field "owned"; ownership flag. |
| `cable_set` | `character varying(200)` | Source field "cable_set"; cable set identifier. |
| `cable_rout` | `character varying(200)` | Source field "cable_rout"; cable route (name truncated). |
| `cable_make` | `character varying(40)` | Source field "cable_make"; cable make / manufacture (name truncated). |
| `year_of_in` | `integer` | Source field "year_of_in"; year installed (name truncated). |
| `id_original` | `integer` | Original feature id preserved at load. |
| `lad22nm` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD name. |
| `lad22cd` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD GSS code. |
| `wd21nm` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward name. |
| `wd21cd` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward GSS code. |
| `geom` | `geometry(LineString,27700)` | LineString in EPSG:27700. Underground cable route. |
| `length_m` | `double precision` | Length in metres. |
| `fid` | `bigint` |  |
