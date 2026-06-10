# Defra - Department for Environment, Food and Rural Affairs Predictive Agricultural Land Classification (ALC) for England, March 2026

`env_defra_predictive_agricultural_land_class_mar2026`

<a href="http://localhost:7800/?layer=uk_baseline.env_defra_predictive_agricultural_land_class_mar2026" target="_blank" rel="noopener">Open in the Dashboard &#8599;</a> <span style="opacity:.6;font-size:.85em;">(start your local Dashboard first)</span>

**SOURCE**

- Department for Environment, Food and Rural Affairs (Defra). Predictive ALC product.

**DOCUMENTATION**

- ALC concept guidance : https://www.gov.uk/government/publications/agricultural-land-classification-of-england-and-wales/agricultural-land-classification-of-england-and-wales

**DEFINITIONS**

- "Agricultural Land Classification (ALC) provides a method for assessing the quality of farmland to enable informed choices to be made about its future use within the planning system." (Defra ALC guidance)

**SCOPE**

- England. 953,652 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid).

**LICENCE**

- Open Government Licence v3.0. © Defra.

**DATA QUALITY CAVEATS**

- Predictive / modelled: every grade (1, 2, 3a, 3b, 4, 5, NA, U) is a prediction of likely ALC, not a field survey. Use for screening; confirm with a site survey for planning decisions.
- RELATED: for the authoritative surveyed classification (Natural England, grades 1–5), see uk_baseline.env_naturalengland_agricultural_land_class_nov2024.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `id` | `integer` | Source identifier preserved at load. |
| `fid_original` | `bigint` | Original feature id preserved at load. |
| `alcgrade` | `bigint` | Source field "alcgrade"; numeric sort key 1-8 paired with `alc`. Mapping observed: 1->"1", 2->"2", 3->"3a", 4->"3b", 5->"4", 6->"5", 7->"NA", 8->"U". |
| `alc` | `character varying(2)` | Source field "alc"; Agricultural Land Classification grade as published. Observed values: "1", "2", "3a", "3b", "4", "5", "NA", "U". |
| `lad25cd` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD GSS code. |
| `lad25nm` | `character varying` | Joined at load from ONS LAD 2025 lookup; 2025 LAD name. |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. ALC polygon geometry. |
| `area_ha` | `double precision` | Area in hectares, computed at load from the geometry. Stale if the geometry is later edited. |
| `fid` | `bigint` |  |
| `rgn22cd` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region GSS code. |
| `rgn22nm` | `text` | Joined at load from ONS LAD->Region lookup; 2022 Region name. |
| `sds_boundary` | `text` | Internal categorisation: Spatial Development Strategy (SDS) area where the polygon falls. Blank or NULL where outside any SDS area. |
