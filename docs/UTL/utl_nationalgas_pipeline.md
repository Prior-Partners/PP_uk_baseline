# `utl_nationalgas_pipeline`

National Gas - National Transmission System (NTS) gas transmission pipelines, Great Britain.

**SOURCE**

- National Gas (formerly National Grid Gas). National Transmission System pipeline network.

**DOCUMENTATION**

- National Gas network and assets : https://www.nationalgas.com/our-businesses/our-network-and-assets

**DEFINITIONS**

- National Gas Transmission owns and operates Britain's National Transmission System (NTS) for gas; the NTS consists of nearly 5,000 miles of high-pressure steel pipes and more than 500 above-ground installations. (National Gas)

**SCOPE**

- Great Britain. 3,175 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type Polygon.

**LICENCE**

- © National Gas. Licence - confirm with National Gas before re-publication.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `actualinte` | `double precision` | Source field "actualinte"; attribute carried from source (name truncated). |
| `owner` | `character varying(3)` | Source field "owner"; pipeline owner. Observed value: "NGT" (National Gas Transmission). |
| `pipegrade` | `character varying(15)` | Source field "pipegrade"; steel pipe grade (e.g. "X60", "X52", "X80", "L555"). |
| `inserviced` | `date` | Source field "inserviced"; in-service date (name truncated). |
| `pipe_name` | `character varying(100)` | Source field "pipe_name"; pipeline name. |
| `featureid` | `double precision` | Source field "featureid"; source feature identifier. |
| `shape_leng` | `double precision` | Source field "Shape_Length"; legacy ArcGIS shape length. |
| `id_original` | `integer` | Original feature id preserved at load. |
| `lad22nm` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD name. |
| `lad22cd` | `character varying` | Joined at load from ONS LAD 2022 lookup; 2022 LAD GSS code. |
| `wd21nm` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward name. |
| `wd21cd` | `character varying` | Joined at load from ONS Ward 2021 lookup; 2021 Ward GSS code. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `geom` | `geometry(Polygon,27700)` | Polygon in EPSG:27700. Gas transmission pipeline corridor. |
| `gid` | `bigint` |  |
