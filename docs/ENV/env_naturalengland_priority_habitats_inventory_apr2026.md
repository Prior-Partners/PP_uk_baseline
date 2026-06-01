# Natural England Priority Habitats Inventory (England), April 2026

`env_naturalengland_priority_habitats_inventory_apr2026`

**SOURCE**

- Natural England, via the NE Open Data Hub. Priority Habitats Inventory (England) dataset.

**DOCUMENTATION**

- NE Open Data Hub : https://naturalengland-defra.opendata.arcgis.com/
- data.gov.uk PHI  : https://www.data.gov.uk/dataset/4b6ddab7-6c0f-4407-946e-d6499f19fcde/priority-habitats-inventory-england

**DEFINITIONS**

- "The Priority Habitat Inventory is a spatial dataset that maps priority habitats identified in the UK Biodiversity Action Plan" - habitats "listed as being of principal importance for the purpose of conserving or enhancing biodiversity, under Section 41 of the Natural Environment and Rural Communities Act (2006)." (data.gov.uk, Priority Habitats Inventory (England), Natural England)

**SCOPE**

- England. 814,471 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type MultiPolygon.

**LICENCE**

- Open Government Licence v3.0. © Natural England.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid_original` | `integer` | Original feature id preserved at load. |
| `mainhabs` | `character varying` | Source field "mainhabs"; main habitat. Observed values include "Deciduous woodland", "Coastal and floodplain grazing marsh", "Traditional orchard". |
| `habcodes` | `character varying` | Source field "habcodes"; habitat code(s). |
| `featdesc` | `character varying` | Source field "featdesc"; feature description. |
| `featcodes` | `character varying` | Source field "featcodes"; feature code(s). |
| `otherclass` | `character varying` | Source field "otherclass"; other classification. |
| `addhabs` | `character varying` | Source field "addhabs"; additional habitats present. |
| `primsource` | `character varying` | Source field "primsource"; primary source dataset (e.g. "National Forest Inventory 2023 (DWOOD)"). |
| `areaha` | `double precision` | Source field "areaha"; area as published by Natural England. Unit: "hectares". |
| `version` | `character varying` | Source field "version"; source version. Observed value: "Sep_25". |
| `uid` | `character varying` | Source field "uid"; unique feature identifier. |
| `globalid` | `character varying` | Source field "GlobalID"; ArcGIS GlobalID GUID. |
| `lad25cd` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD GSS code. |
| `lad25nm` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD name. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. Priority habitat polygon geometry. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `rgn22cd` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `text` | Internal categorisation: Spatial Development Strategy (SDS) area where the polygon falls. Blank or NULL where outside any SDS area. |
| `layer` | `character(100)` | Source field "layer"; fixed-string source-layer annotation. Single observed value: "Priority Habitats". |
