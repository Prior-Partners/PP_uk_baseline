# `com_os_green_space_sport_activity_area`

OS Open Greenspace Sport and activity provision, polygon layer with analytical attributes.

**SOURCE**

- Ordnance Survey (OS), Open Greenspace product (base geometry; dataset column records "OS Greenspace").
- Additional analytical columns (naturalness, accessible, angst, perc_manmade, greenspacetopology, habitat, designation, typologytitle, typologycode, attribute, vxcount, orig_area) appear to be added by an upstream pipeline not yet identified - exact derivation rules to be documented when known.

**DOCUMENTATION**

- OS Open Greenspace product page : https://docs.os.uk/os-downloads/products/land-and-terrain-portfolio/os-open-greenspace
- OS Open Greenspace download : https://osdatahub.os.uk/data/downloads/open/OpenGreenspace

**DEFINITIONS**

- OS Open Greenspace: "OS Open Greenspace depicts the location and extent of spaces, such as parks and sports facilities, which are likely to be accessible to the public." (OS Open Greenspace product page)
- ANGST: Accessible Natural Greenspace Standard, a Natural England standard defining sizes/distances within which residents should be able to reach natural greenspace.

**SCOPE**

- England & Wales.
- 74,573 distinct sites (by id_original) represented across 87,983 polygon rows (avg ratio ~1.18 - most sites are single polygons; some are exploded multipolygons).

**CRS**

- EPSG:27700 (British National Grid / BNG).

**LICENCE**

- Open Government Licence v3.0 (per source OS Open Greenspace licence column value "OGL"; verify if upstream-derived analytical attributes carry an additional licence).

**DATA QUALITY CAVEATS**

- id_original is NOT strictly unique per row - 74,573 distinct values across 87,983 rows. Multipolygon sites have been exploded.
- Upstream derivation pipeline for the analytical attributes is not yet documented here; values should be cross-checked against the originating source before being used in published outputs. at load time.

**ENRICHMENT**

- lad22cd, lad22nm : spatial intersect with ONS 2022 LAD boundaries.
- wd21cd, wd21nm : spatial intersect with ONS 2021 Ward boundaries.
- area_ha : derived from geom at load (area in hectares, computed from the geometry at load).


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `objectid` | `bigint` | Source ArcGIS surrogate from upstream. |
| `dataset` | `character varying(255)` | Source field "dataset"; upstream dataset tag. Constant value "OS Greenspace" in this load. |
| `accessible` | `character varying(255)` | Source field "accessible"; Yes/No flag indicating whether the site is publicly accessible. |
| `angst` | `character varying(255)` | Source field "angst"; Yes/No flag for ANGST (Accessible Natural Greenspace Standard) eligibility. |
| `naturalness` | `integer` | Source field "naturalness"; integer score (semantics inferred - likely 1-5 scale; verify with upstream). |
| `typologytitle` | `character varying(255)` | Source field "typologytitle"; human-readable typology label (e.g. "Play Space Provision"). |
| `license` | `character varying(255)` | Source field "license"; upstream licence tag (e.g. "OGL"). |
| `greenspacetopology` | `integer` | Source field "greenspacetopology"; integer code (semantics inferred). |
| `habitat` | `integer` | Source field "habitat"; integer code (semantics inferred). |
| `designation` | `integer` | Source field "designation"; integer code (semantics inferred). |
| `attribute` | `character varying(8000)` | Source field "attribute"; free-text greenspace attribute (e.g. "Play Space"). Length 8000. |
| `typologycode` | `character varying(255)` | Source field "typologycode"; numeric typology code (e.g. "5.5"). |
| `orig_area` | `double precision` | Source field "orig_area"; upstream-recorded area. Unit: presumed "square metres" (matches shape_area values in samples). |
| `perc_manmade` | `double precision` | Source field "perc_manmade"; percentage of the polygon that is manmade. Unit: "per cent (0-100)". |
| `vxcount` | `integer` | Source field "vxcount"; vertex count of the polygon - useful for geometry-complexity analysis. |
| `shape_length` | `double precision` | Source field "shape_length"; legacy ArcGIS shape perimeter. Unit: "metres". |
| `shape_area` | `double precision` | Source field "shape_area"; legacy ArcGIS shape area. Unit: "square metres". |
| `id_original` | `integer` | Source identifier preserved at load. NOT strictly unique per row - see caveats. |
| `lad22nm` | `character varying` | Joined at load from spatial intersection with ONS 2022 LAD boundaries; LAD name. |
| `lad22cd` | `character varying` | Joined at load from spatial intersection with ONS 2022 LAD boundaries; LAD GSS code. |
| `wd21nm` | `character varying` | Joined at load from spatial intersection with ONS 2021 Ward boundaries; Ward name. |
| `wd21cd` | `character varying` | Joined at load from spatial intersection with ONS 2021 Ward boundaries; Ward GSS code. |
| `geom` | `geometry(Polygon,27700)` | Source field "geometry"; Polygon in EPSG:27700 (British National Grid). |
| `area_ha` | `double precision` | Derived at load from ST_Area(geom)/10000. Unit: "hectares". |
| `fid` | `bigint` |  |
