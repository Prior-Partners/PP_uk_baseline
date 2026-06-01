# Natural England Lowland Heathland Extent and Potential (England), October 2018

`env_naturalengland_heathland_oct2018`

<iframe src="../../maps/env_naturalengland_heathland_oct2018.html" title="Interactive preview map of env_naturalengland_heathland_oct2018" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../../maps/env_naturalengland_heathland_oct2018.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

**SOURCE**

- Natural England. Lowland Heathland Extent and Potential dataset.

**DOCUMENTATION**

- NE Open Data Hub : https://naturalengland-defra.opendata.arcgis.com/

**SCOPE**

- England. 3,763 rows. Mix of "Extent" (3,211) and "Potential" (552) features — filter on the type column to separate them.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid).

**LICENCE**

- Open Government Licence v3.0. © Natural England.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid_original` | `integer` | Original feature id preserved at load. |
| `sitename` | `character varying` | Source field "sitename"; heathland site name. |
| `area` | `character varying` | Source field "area"; named locality / area (e.g. "Breckland", "Kennet Valley"). NOT a numeric area — see areahectar. |
| `county` | `character varying` | Source field "county"; county name. |
| `areahectar` | `double precision` | Source field "areahectar"; site area. Unit: "hectares". |
| `sssi` | `character varying` | Source field "sssi"; flag for overlap with a Site of Special Scientific Interest (SSSI). Observed values: "Y", "N", blank, NULL. |
| `sssiname` | `character varying` | Source field "sssiname"; name of the overlapping SSSI where applicable. |
| `type` | `character varying` | Source field "type"; feature type. Observed values: "Extent", "Potential". |
| `lad25cd` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD GSS code. |
| `lad25nm` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD name. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. Heathland polygon geometry. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `rgn22cd` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `text` | Internal categorisation: Spatial Development Strategy (SDS) area where the polygon falls. Blank or NULL where outside any SDS area. |
| `layer` | `character(100)` | Source field "layer"; fixed-string source-layer annotation. Single observed value: "Historic Environment Action Plan". |
