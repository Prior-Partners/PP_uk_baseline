# Historic England Listed Buildings (England) — polygon geometry, May 2026

<p class="layer-short">Listed Building polygons</p>

`her_historicengland_listed_building_polygons_may2026`

<img src="../../maps/her_historicengland_listed_building_polygons_may2026.png" alt="Styling preview of her_historicengland_listed_building_polygons_may2026" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Historic England, National Heritage List for England (NHLE), Listed Buildings dataset (polygon geometry).

**DOCUMENTATION**

- NHLE              : https://historicengland.org.uk/listing/the-list/
- HE data downloads : https://historicengland.org.uk/listing/the-list/data-downloads/
- Listed Buildings : https://historicengland.org.uk/listing/what-is-designation/listed-buildings/

**DEFINITIONS**

- "Listed buildings are buildings of special architectural or historic interest with legal protection." (Historic England, Listed Buildings)
- Listing grades: Grade I — buildings of exceptional interest; Grade II* — particularly important buildings of more than special interest; Grade II — buildings of special interest. (Historic England, Listed Buildings)

**SCOPE**

- England. 380,263 polygon rows representing 379,329 distinct List Entry Numbers (a small number of buildings have more than one polygon).

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type MultiPolygon.

**LICENCE**

- Open Government Licence v3.0. © Historic England.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid_original` | `integer` | ArcGIS source identifier preserved at load; not stable across Historic England re-publications. |
| `listentry` | `integer` | Source field "ListEntry"; National Heritage List for England (NHLE) List Entry Number — the canonical national identifier for the heritage asset. |
| `name` | `character varying` | Source field "Name"; heritage asset name as published on the NHLE. |
| `grade` | `character varying` | Source field "Grade"; statutory listing grade. Observed values: "I", "II*", "II". |
| `listdate` | `timestamp with time zone` | Source field "ListDate"; date first listed. |
| `amenddate` | `timestamp with time zone` | Source field "AmendDate"; date of the most recent amendment to the listing. |
| `capturescale` | `character varying` | Source field "CaptureScale"; cartographic scale at which the geometry was captured (e.g. "1:1250"). |
| `hyperlink` | `character varying` | Source field "Hyperlink"; URL of the listing page on the Historic England website. |
| `ngr` | `character varying` | Source field "NGR"; alphanumeric National Grid Reference (e.g. "SP 12345 67890"). |
| `easting` | `double precision` | Source field "Easting"; British National Grid easting. Unit: metres (EPSG:27700). |
| `northing` | `double precision` | Source field "Northing"; British National Grid northing. Unit: metres (EPSG:27700). |
| `wd25cd` | `character varying` | Joined at load from ONS Ward 2025 lookup; 2025 Ward GSS code. |
| `wd25nm` | `character varying` | Joined at load from ONS Ward 2025 lookup; 2025 Ward name. |
| `lad25cd` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD GSS code. |
| `lad25nm` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD name. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. Listed building polygon. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `rgn22cd` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `text` | Internal categorisation: Spatial Development Strategy (SDS) area where the geometry falls. Blank or NULL where outside any SDS area. |
