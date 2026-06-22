# MHCLG Local plan boundary, January 2026

<p class="layer-short">Local Plan Boundary</p>

`adm_mhclg_local_plan_boundary_jan2026`

<img src="../../maps/adm_mhclg_local_plan_boundary_jan2026.png" alt="Styling preview of adm_mhclg_local_plan_boundary_jan2026" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Ministry of Housing, Communities and Local Government (MHCLG), published via Planning Data (planning.data.gov.uk).

**DOCUMENTATION**

- Dataset page : https://www.planning.data.gov.uk/dataset/local-plan-boundary
- Field specification : https://digital-land.github.io/specification/dataset/local-plan-boundary

**DEFINITIONS**

- Local plan boundary is the development plan area prepared by a local planning authority.

**SCOPE**

- England only.
- 575 polygon rows representing 364 distinct upstream entity IDs across 363 local planning authorities.

**CRS**

- EPSG:27700 (British National Grid / BNG).

**LICENCE**

- Open Government Licence v3.0.

**DATA QUALITY CAVEATS**

- The upstream geometry is multipolygon; the loader exploded each multipolygon into single-part Polygon rows. One entity can occupy many rows (entity 4211319 has 53 parts).

**UPDATE REQUIRED**

- New data found from data source on 18 March 2026. Current data is 9 January 2026. An update is scheduled in the next turn.

**LOADED INTO uk_baseline**

- Loaded by PNC, January 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `id` | `integer` |  |
| `geom` | `geometry(Polygon,27700)` | Source field "geometry" (multipolygon per upstream spec; exploded to Polygon at load); EPSG:27700. |
| `fid` | `bigint` |  |
| `dataset` | `character varying` | Source field "dataset"; constant value "local-plan-boundary". |
| `end_date` | `character varying` | Source field "end-date"; date the boundary was retired upstream (blank if still active). All rows currently active in this load. |
| `entity` | `character varying` | Source field "entity"; numeric ID assigned by Planning Data; 364 distinct entities in this load. |
| `entry_date` | `date` | Source field "entry-date"; date this row was first published in the upstream Planning Data dataset. |
| `name` | `character varying` | Source field "name"; human-readable name of the local-plan area (e.g. "London Borough of Camden"). |
| `organisation_entity` | `character varying` | Source field "organisation-entity"; numeric ID of the publishing organisation. |
| `prefix` | `character varying` | Source field "prefix"; constant value "local-plan-boundary" (mirrors dataset). |
| `quality` | `character varying` | Source field "quality"; upstream data-quality tag (e.g. "authoritative"). |
| `reference` | `character varying` | Source field "reference"; alphanumeric identifier (often matches the LPA GSS code, e.g. "E60000188"). |
| `start_date` | `character varying` | Source field "start-date"; date the boundary became effective upstream (often blank). |
| `typology` | `character varying` | Source field "typology"; upstream taxonomy class. Constant "geography" for this dataset. |
| `organisations` | `character varying` | Source field "organisations"; ":"-delimited list of upstream organisation slugs (e.g. "local-authority:CMD"). |
| `local_planning_authorities` | `character varying` | Source field "local-planning-authorities"; LPA reference(s). |
