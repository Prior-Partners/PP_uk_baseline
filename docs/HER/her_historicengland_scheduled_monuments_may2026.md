# Historic England Scheduled Monuments (England), May 2026

`her_historicengland_scheduled_monuments_may2026`

<iframe src="../maps/her_historicengland_scheduled_monuments_may2026.html" title="Interactive preview map of her_historicengland_scheduled_monuments_may2026" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../maps/her_historicengland_scheduled_monuments_may2026.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

**SOURCE**

- Historic England, National Heritage List for England (NHLE), Scheduled Monuments dataset.

**DOCUMENTATION**

- NHLE              : https://historicengland.org.uk/listing/the-list/
- HE data downloads : https://historicengland.org.uk/listing/the-list/data-downloads/
- Scheduled Monuments : https://historicengland.org.uk/listing/what-is-designation/scheduled-monuments/

**DEFINITIONS**

- "'Scheduling' is the selection of nationally important archaeological sites." (Historic England, Scheduled Monuments)

**SCOPE**

- England. 21,317 rows.

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
| `scheddate` | `timestamp with time zone` | Source field "SchedDate"; date the monument was scheduled. |
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
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. Scheduled monument boundary. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `rgn22cd` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `text` | Internal categorisation: Spatial Development Strategy (SDS) area where the geometry falls. Blank or NULL where outside any SDS area. |
