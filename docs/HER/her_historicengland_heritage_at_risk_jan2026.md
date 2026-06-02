# Historic England Heritage at Risk Register (England), January 2026

`her_historicengland_heritage_at_risk_jan2026`

<a href="http://localhost:7800/?layer=uk_baseline.her_historicengland_heritage_at_risk_jan2026" target="_blank" rel="noopener">Open in the Dashboard &#8599;</a> <span style="opacity:.6;font-size:.85em;">(start your local Dashboard first)</span>

Published via planning.data.gov.uk (digital-land).

**SOURCE**

- Historic England, Heritage at Risk programme; distributed via planning.data.gov.uk (digital-land).

**DOCUMENTATION**

- Heritage at Risk                      : https://historicengland.org.uk/advice/heritage-at-risk/
- Heritage at Risk selection criteria   : https://historicengland.org.uk/listing/heritage-at-risk/search-register/selection-criteria/
- planning.data.gov.uk heritage-at-risk : https://www.planning.data.gov.uk/dataset/heritage-at-risk

**DEFINITIONS**

- "The Heritage at Risk Register includes buildings, places of worship, monuments, parks and gardens, conservation areas, battlefields and wreck sites that are listed and have been assessed and found to be at risk." (gov.uk, Heritage at Risk)

**SCOPE**

- England. 5,598 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type MultiPolygon.

**LICENCE**

- Open Government Licence v3.0. © Historic England.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid_original` | `integer` | ArcGIS source identifier preserved at load. |
| `dataset` | `character varying` | Source field "dataset"; digital-land dataset slug. Observed value: "heritage-at-risk". |
| `end_date` | `character varying` | Source field "end-date"; entity end date (blank where current). |
| `entity` | `character varying` | Source field "entity"; digital-land national entity identifier. |
| `entry_date` | `date` | Source field "entry-date"; date the record entered the digital-land collection. |
| `name` | `character varying` | Source field "name"; heritage-at-risk entry name. |
| `organisation_entity` | `character varying` | Source field "organisation-entity"; digital-land entity id of the publishing organisation. |
| `prefix` | `character varying` | Source field "prefix"; digital-land dataset prefix. |
| `quality` | `character varying` | Source field "quality"; digital-land data-quality field. |
| `reference` | `character varying` | Source field "reference"; the publishing organisation's own reference. |
| `start_date` | `character varying` | Source field "start-date"; entity start date. |
| `typology` | `character varying` | Source field "typology"; digital-land typology. Observed value: "geography". |
| `documentation_url` | `character varying` | Source field "documentation-url"; URL to the heritage-at-risk record. |
| `lad25cd` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD GSS code. |
| `lad25nm` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD name. |
| `rgn22cd` | `character varying` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `character varying` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `character varying` | Internal categorisation: Spatial Development Strategy (SDS) area where the geometry falls. Blank or NULL where outside any SDS area. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. Heritage at Risk entry geometry. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
