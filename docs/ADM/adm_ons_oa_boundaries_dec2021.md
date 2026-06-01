# ONS Output Areas (OA), England & Wales extent, 2021 Census geography, December 2021

`adm_ons_oa_boundaries_dec2021`

<iframe src="../maps/adm_ons_oa_boundaries_dec2021.html" title="Interactive preview map of adm_ons_oa_boundaries_dec2021" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../maps/adm_ons_oa_boundaries_dec2021.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

**SOURCE**

- Office for National Statistics (ONS), via data.gov.uk.

**DOCUMENTATION**

- Dataset page : https://www.data.gov.uk/dataset/4d4e021d-fe98-4a0e-88e2-3ead84538537/output-areas-december-2021-boundaries-ew-bgc-v21
- Digital boundaries methods : https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries

**DEFINITIONS**

- "Generalised (20m) - clipped to the coastline (Mean High Water mark)." (ONS digitalboundaries page, definition of BGC)

**SCOPE**

- England & Wales.
- 188,880 OAs.

**CRS**

- EPSG:27700 (British National Grid / BNG).

**LICENCE**

- Open Government Licence v3.0.

**LOADED INTO uk_baseline**

- Loaded by PNC, February 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `id` | `integer` | ArcGIS source identifier preserved at load. |
| `geom` | `geometry(MultiPolygon,27700)` | Source field "geometry"; MultiPolygon in EPSG:27700. BGC = 20m generalised, clipped to Mean High Water — see table comment. |
| `fid` | `bigint` |  |
| `oa21cd` | `character varying(9)` | Source field "OA21CD"; ONS GSS 9-character OA code. |
| `lsoa21cd` | `character varying(9)` | Joined at load from ONS OA->LSOA lookup; 2021 LSOA GSS code. |
| `lsoa21nm` | `character varying(40)` | Joined at load; 2021 LSOA name (English). |
| `lsoa21nmw` | `character varying(29)` | Joined at load; 2021 LSOA name (Welsh, populated where applicable). |
| `bng_e` | `integer` | Source field "BNG_E"; OA centroid easting. Unit: "metres". |
| `bng_n` | `integer` | Source field "BNG_N"; OA centroid northing. Unit: "metres". |
| `lat` | `double precision` | Source field "LAT"; OA centroid latitude. Unit: "degrees". |
| `long` | `double precision` | Source field "LONG"; OA centroid longitude. Unit: "degrees". |
| `globalid` | `character varying(38)` | Source field "GlobalID"; ArcGIS GUID-format unique identifier. |
