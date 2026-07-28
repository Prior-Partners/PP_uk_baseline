# GeoDS UK Points of Interest, September 2024

<p class="layer-short">POI</p>

`blt_geods_poi_sep2024`

<img src="../../maps/blt_geods_poi_sep2024.png" alt="Styling preview of blt_geods_poi_sep2024" loading="lazy" style="width:100%;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;">

**SOURCE**

- Geographic Data Service (GeoDS, formerly Consumer Data Research Centre / CDRC).
- Upstream POI provider: Overture Maps Foundation; POIs contributed by Meta and Microsoft.
- Census-key columns (lsoa21cd, lad22cd/nm, wd21cd/nm) and (easting, northing) are derived at our load (see ENRICHMENT below), not from the GeoDS file.

**DOCUMENTATION**

- GeoDS dataset page : https://data.geods.ac.uk/dataset/point-of-interest-data-for-the-united-kingdom
- Overture Maps schema : https://docs.overturemaps.org/
- H3 spatial index reference : https://h3geo.org/docs/
- Validation paper : Ballantyne & Berragan (2024), Environment and Planning B 51(8)

**DEFINITIONS**

- "This dataset contains Point of Interest (POI) data for the United Kingdom, obtained from the Overture Maps Foundation." (GeoDS dataset page)

**SCOPE**

- United Kingdom (country = "GB", ISO 3166-1 alpha-2 code for the UK).
- 2,455,987 POIs.

**CRS**

- EPSG:27700 (British National Grid / BNG). Reprojected at load from upstream WGS84.

**LICENCE**

- Community Database License Agreement - Permissive v2 (CDLA-Permissive v2).

**DATA QUALITY CAVEATS**

- Geography keys are NULL on 2 of 2,455,987 rows, measured 28 July 2026: 2 fall outside every district — offshore, inter-tidal, or beyond Great Britain.
- A further 205,887 rows carry a Scottish or Northern Irish district code, so they hold a district but no county or Spatial Development Strategy — the lookup covers England and Wales only.
- County and Spatial Development Strategy columns are England and Wales only; rows elsewhere carry no county or SDS. Wales and the Isles of Scilly carry a county but no SDS. Rows with no Local Authority District code are NULL in all four columns.

**ENRICHMENT**

- `sds_name` / `sds_group` — Spatial Development Strategy area and devolution status, a Prior + Partners categorisation over Ministry of Housing, Communities and Local Government (MHCLG) English devolution policy, joined at load on the row's Local Authority District 2025 code via uk.ref_lad25_ctyua25_sds_lu_jul2026.
- easting, northing : derived from lat/long at load.
- lsoa21cd : spatial intersect with ONS 2021 LSOA boundaries.
- lad22cd, lad22nm : spatial intersect with ONS 2022 LAD boundaries.
- wd21cd, wd21nm : spatial intersect with ONS 2021 Ward boundaries.

**UPDATE REQUIRED**

- GeoDS released V1.1 of this dataset on 2026-05-07. This load is the September 2024 Overture release; refresh planned.

**LOADED INTO uk_baseline**

- Loaded September 2024.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `primary_name` | `character varying` | Source field "primary_name"; canonical display name of the POI (Overture schema). May be NULL for incompletely-attributed POIs. |
| `main_category` | `character varying` | Source field "main_category"; top-level Overture POI category (e.g. "education", "religious_organization"). |
| `alternate_category` | `character varying` | Source field "alternate_category"; secondary Overture categories, pipe-delimited (e.g. "shopping\|pet_store"). NULL when only the main category is set. |
| `address` | `character varying` | Source field "address"; street address as recorded upstream. |
| `locality` | `character varying` | Source field "locality"; town or city as recorded upstream. |
| `postcode` | `character varying` | Source field "postcode"; UK postcode. |
| `region` | `character varying` | Source field "region"; country region code (e.g. "ENG", "SCO", "WAL", "NIR"). |
| `country` | `character varying` | Source field "country"; ISO 3166-1 alpha-2 country code (constant "GB" for this UK subset). |
| `source` | `character varying` | Source field "source"; upstream POI provider — typically "meta" or "microsoft". See quality caveat in table comment regarding Microsoft-sourced POIs. |
| `source_record_id` | `character varying` | Source field "source_record_id"; POI identifier in the upstream provider system. |
| `lat` | `double precision` | Source field "lat"; latitude of POI. Unit: "degrees". |
| `long` | `double precision` | Source field "long"; longitude of POI. Unit: "degrees". |
| `h3_15` | `character varying` | Source field "h3_15"; Uber H3 hierarchical spatial index at resolution 15 (~0.9 m^2 per cell, finest level). 15-character hexadecimal. |
| `easting` | `double precision` | British National Grid easting of POI derived at load from lat/long. Unit: "metres". |
| `northing` | `double precision` | British National Grid northing of POI derived at load from lat/long. Unit: "metres". |
| `lsoa21cd` | `character varying` | Joined at load from spatial intersection with ONS 2021 LSOA boundaries; LSOA GSS code. |
| `id_original` | `character varying` | Internal POI identifier preserved at load (concatenation of H3 cell and a source-specific hash). |
| `lad22nm` | `character varying` | Local Authority District 2022 name (2021 LAD geography). Assigned at load by point-in-polygon location against uk_baseline.adm_ons_lad_boundary_may2022. Open Government Licence v3.0. |
| `lad22cd` | `character varying` | Local Authority District 2022 code (2021 LAD geography, anchored to the MSOA 2021 name scoping). Assigned at load by point-in-polygon location against uk_baseline.adm_ons_lad_boundary_may2022. Open Government Licence v3.0. |
| `wd21nm` | `character varying` | Joined at load from spatial intersection with ONS 2021 Ward boundaries; Ward name. |
| `wd21cd` | `character varying` | Joined at load from spatial intersection with ONS 2021 Ward boundaries; Ward GSS code. |
| `geom` | `geometry(Point,27700)` | Source field "geometry" reprojected from EPSG:4326 to EPSG:27700; Point. |
| `fid` | `bigint` |  |
| `msoa21cd` | `text` | Middle Layer Super Output Area (MSOA) 2021 code. Assigned at load by point-in-polygon location against uk_baseline.adm_ons_msoa_boundary_2021. Open Government Licence v3.0. |
| `msoa21nm` | `text` | Official ONS Middle Layer Super Output Area 2021 name. Assigned at load via the point's 2021 MSOA (point-in-polygon against uk_baseline.adm_ons_msoa_boundary_2021). Open Government Licence v3.0. |
| `msoa21hclnm` | `text` | House of Commons Library readable MSOA name. Assigned at load via the point's 2021 MSOA (point-in-polygon against uk_baseline.adm_ons_msoa_boundary_2021, which carries the House of Commons Library name). Open Parliament Licence. |
| `lad25cd` | `text` | Local Authority District 2025 code (current administering authority). Assigned at load by point-in-polygon location against uk_baseline.adm_ons_lad_boundary_may2025. Open Government Licence v3.0. |
| `lad25nm` | `text` | Local Authority District 2025 name (current administering authority). Assigned at load by point-in-polygon location against uk_baseline.adm_ons_lad_boundary_may2025. Open Government Licence v3.0. |
| `ctyua25cd` | `text` | County or unitary authority code at 1 April 2025. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `ctyua25nm` | `text` | County or unitary authority name at 1 April 2025. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `sds_name` | `text` | Spatial Development Strategy (SDS) area, a Prior + Partners categorisation over Ministry of Housing, Communities and Local Government (MHCLG) English devolution policy. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
| `sds_group` | `text` | Devolution status of the Spatial Development Strategy area: Existing Devolution Footprints, Devolution Priority Programme, Other Proposed Geographies or Remaining Areas. Joined at load via uk.ref_lad25_ctyua25_sds_lu_jul2026 on the row's Local Authority District 2025 code. Open Government Licence v3.0. |
