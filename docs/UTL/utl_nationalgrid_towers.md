# `utl_nationalgrid_towers`

National Grid Electricity Transmission - transmission towers (pylons), England and Wales.

**SOURCE**

- National Grid Electricity Transmission. High-voltage transmission tower (pylon) assets.

**DOCUMENTATION**

- National Grid Electricity Transmission : https://www.nationalgrid.com/electricity-transmission

**DEFINITIONS**

- Transmission towers (pylons) are the steel lattice structures that carry National Grid high-voltage overhead lines. (National Grid)

**SCOPE**

- England and Wales. 21,965 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type Point.

**LICENCE**

- © National Grid. Licence - confirm with National Grid before re-publication.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `tower_asse` | `character varying(12)` | Source field "tower_asse"; tower asset reference (name truncated). |
| `action_dtt` | `date` | Source field "action_dtt"; action date (name truncated). |
| `status` | `character varying(1)` | Source field "status"; source status code. |
| `line_serie` | `character varying(200)` | Source field "line_serie"; line series (name truncated). |
| `tower_cons` | `character varying(30)` | Source field "tower_cons"; tower construction type. Observed values: "D", "D30", "D60", "D10". |
| `year_of_in` | `integer` | Source field "year_of_in"; year installed (name truncated). |
| `tower_heig` | `double precision` | Source field "tower_heig"; tower height (name truncated). |
| `gdo_gid` | `numeric` | Source field "gdo_gid"; source feature identifier. |
| `id_original` | `integer` | Original feature id preserved at load. |
| `lad22nm` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD name. |
| `lad22cd` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD GSS code. |
| `wd21nm` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward name. |
| `wd21cd` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward GSS code. |
| `geom` | `geometry(Point,27700)` | Point in EPSG:27700. Transmission tower (pylon) point. |
| `fid` | `bigint` |  |
