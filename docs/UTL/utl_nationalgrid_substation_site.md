# `utl_nationalgrid_substation_site`

National Grid Electricity Transmission - substation sites, England and Wales.

**SOURCE**

- National Grid Electricity Transmission. High-voltage transmission substation site assets.

**DOCUMENTATION**

- National Grid Electricity Transmission : https://www.nationalgrid.com/electricity-transmission

**DEFINITIONS**

- Substations connect sources of electricity generation to the transmission network and onward to the distribution system that reaches homes and businesses; this layer represents National Grid substation sites. (National Grid)

**SCOPE**

- England and Wales. 505 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type Polygon.

**LICENCE**

- © National Grid. Licence - confirm with National Grid before re-publication.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `substation` | `character varying(100)` | Source field "substation"; substation name. |
| `operating_` | `character varying(100)` | Source field "operating_"; operating voltage (name truncated). |
| `action_dtt` | `date` | Source field "action_dtt"; action date (name truncated). |
| `status` | `character varying(1)` | Source field "status"; source status code. Observed values: "C", "P", "E". |
| `substati_1` | `character varying(200)` | Source field "substati_1"; secondary substation name (name truncated). |
| `owner_flag` | `character varying(1)` | Source field "owner_flag"; ownership flag. |
| `gdo_gid` | `numeric` | Source field "gdo_gid"; source feature identifier. |
| `id_original` | `integer` | Original feature id preserved at load. |
| `lad22nm` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD name. |
| `lad22cd` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD GSS code. |
| `wd21nm` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward name. |
| `wd21cd` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward GSS code. |
| `geom` | `geometry(Polygon,27700)` | Polygon in EPSG:27700. Substation site boundary. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
