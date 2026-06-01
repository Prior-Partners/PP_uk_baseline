# Department for Transport (DfT) Bus Open Data Service (BODS) bus stop points, Great Britain

`mob_dft_bods_bus_stops`

<iframe src="../maps/mob_dft_bods_bus_stops.html" title="Interactive preview map of mob_dft_bods_bus_stops" loading="lazy" style="width:100%;height:480px;border:1px solid #d9d3c4;border-radius:8px;margin:6px 0 4px;"></iframe>

<a href="../maps/mob_dft_bods_bus_stops.html" target="_blank" rel="noopener">Open the map in a new tab &#8599;</a>

**SOURCE**

- Bus Open Data Service (BODS), Department for Transport (DfT). atco_code is the National Public Transport Access Node (NaPTAN) identifier from the BODS GTFS stops; routes_served is derived by reverse-lookup from uk_baseline.mob_bus_routes.

**DOCUMENTATION**

- Bus Open Data Service          : https://www.bus-data.dft.gov.uk/
- NaPTAN                         : https://beta-naptan.dft.gov.uk/
- NaPTAN guide for data managers : https://www.gov.uk/government/publications/national-public-transport-access-node-schema/naptan-guide-for-data-managers

**DEFINITIONS**

- NaPTAN "lists all public transport access points in Great Britain, including bus, rail, tram, metro, underground, air and ferry services." (data.gov.uk, NaPTAN)
- ATCO code structure: "The first 3 numbers denotes the authority responsible for the stop. The fourth character is a 0 (zero). The remaining characters to a maximum of 8 are alpha-numeric determined locally." (Department for Transport, NaPTAN guide for data managers)

**SCOPE**

- Great Britain. 315,952 rows.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid). Geometry type Point.

**LICENCE**

- Open Government Licence v3.0.

**LOADED INTO uk_baseline**

- Loaded by PNC, May 2026.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `id` | `integer` | Surrogate row identifier. |
| `atco_code` | `character varying(50)` | Source field; NaPTAN ATCO code - the National Public Transport Access Node identifier for the stop. |
| `naptan_code` | `character varying(50)` | Source field; short NaPTAN (SMS) code. |
| `stop_name` | `character varying(500)` | Source field; stop name. |
| `platform_code` | `character varying(50)` | Source field; platform / stand code where applicable. |
| `routes_served` | `jsonb` | Routes serving this stop (derived by reverse-lookup from mob_bus_routes). |
| `route_count` | `integer` | Number of routes serving this stop. |
| `easting` | `numeric` | Stop easting. Unit: metres (EPSG:27700). |
| `northing` | `numeric` | Stop northing. Unit: metres (EPSG:27700). |
| `geom` | `geometry(Point,27700)` | Point in EPSG:27700. Bus stop point. |
| `feed_source` | `character varying(50)` | Feed provenance. Observed values: "bods_gtfs_all", "txc_fallback". |
| `feed_loaded_at` | `timestamp without time zone` | Timestamp the source feed was loaded. |
