# `utl_defra_permitted_waste_authorised_landfill`

Defra - Department for Environment, Food and Rural Affairs — Environment Agency Permitted Waste Sites, Authorised Landfill Site Boundaries (England).

**SOURCE**

- Environment Agency (EA), part of the Department for Environment, Food and Rural Affairs (Defra). Permitted Waste Sites - Authorised Landfill Site Boundaries dataset.

**DOCUMENTATION**

- EA dataset record : https://environment.data.gov.uk/dataset/692eaecf-d465-11e4-ac2e-f0def148f590

**DEFINITIONS**

- "The Permitted Waste Sites - Authorised Landfill Site Boundaries is a polygon dataset that contains the boundaries of landfill sites that are currently authorised by the Environment Agency under Environmental Permitting Regulations." (Environment Agency)

**SCOPE**

- England. 2,406 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type Polygon.

**LICENCE**

- Open Government Licence v3.0. © Environment Agency.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `lic_admin` | `character varying` | Source field "lic_admin"; Environment Agency licensing administration area. |
| `lic_nmbr` | `character varying` | Source field "lic_nmbr"; licence number. |
| `lic_ippcr` | `character varying` | Source field "lic_ippcr"; Integrated Pollution Prevention and Control (IPPC) reference. |
| `lic_wml` | `double precision` | Source field "lic_wml"; Waste Management Licence number. |
| `cust_nmbr` | `character varying` | Source field "cust_nmbr"; customer number. |
| `status` | `character varying` | Source field "status"; permit status. Observed values: "Closure", "Issued", "Effective", "Expired", "Part Suspended". |
| `lic_ltype` | `character varying` | Source field "lic_ltype"; licence type code (e.g. "A05", "L05", "5.2 A(1) a)"). |
| `lic_name` | `character varying` | Source field "lic_name"; licence holder name. |
| `lic_site` | `character varying` | Source field "lic_site"; licensed site reference (name truncated from the source shapefile). |
| `site_name` | `character varying` | Source field "site_name"; site name. |
| `site_build` | `character varying` | Source field "site_build"; site address — building. |
| `site_strt` | `character varying` | Source field "site_strt"; site address — street. |
| `site_area` | `character varying` | Source field "site_area"; site address — area / locality. |
| `site_town` | `character varying` | Source field "site_town"; site address — town. |
| `site_cnty` | `character varying` | Source field "site_cnty"; site address — county. |
| `site_pcode` | `character varying` | Source field "site_pcode"; site postcode. |
| `type_desc` | `character varying` | Source field "type_desc"; permit type description (e.g. "A04: Household, Commercial & Industrial Waste Landfill"). |
| `ngr` | `character varying` | Source field "ngr"; National Grid Reference. |
| `ctroid_x` | `integer` | Source field "ctroid_x"; centroid easting. Unit: metres (EPSG:27700). |
| `ctroid_y` | `integer` | Source field "ctroid_y"; centroid northing. Unit: metres (EPSG:27700). |
| `area` | `character varying` | Source field "area"; site area as published. |
| `date_issue` | `timestamp without time zone` | Source field "date_issue"; permit issue date. |
| `lic_epr` | `character varying` | Source field "lic_epr"; Environmental Permitting Regulations (EPR) permit reference. |
| `gdb_geomattr_data` | `character varying` | Source field "gdb_geomattr_data"; ArcGIS geodatabase legacy geometry-attribute storage. |
| `id_original` | `character varying` | Original feature id preserved at load. |
| `lad22nm` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD name. |
| `lad22cd` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD GSS code. |
| `wd21nm` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward name. |
| `wd21cd` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward GSS code. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `geom` | `geometry(Polygon,27700)` | Polygon in EPSG:27700. Authorised landfill site boundary. |
