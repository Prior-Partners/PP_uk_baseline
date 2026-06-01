# ONS Census 2021 usual residents at Output Area (OA) 2021

`dem_ons_oa_household_residents_2021`

**SOURCE**

- Office for National Statistics (ONS), Census 2021, England and Wales. Source: table TS001 "Number of usual residents in households and communal establishments" at OA grain. Reference date 21 March 2021. Loaded via an earlier Prior + Partners pass.

**DOCUMENTATION**

- ONS dataset (TS001 at OA grain) : https://www.ons.gov.uk/datasets/TS001/editions/2021/versions/3
- ONS Census 2021 landing page : https://www.ons.gov.uk/census/2021

**DEFINITIONS**

- "A usual resident is anyone who, on Census Day, was in the UK and had stayed or intended to stay in the UK for a period of 12 months or more, or had a permanent UK address and was outside the UK and intended to be outside the UK for less than 12 months." (ONS Census 2021 Demography variables)
- "The number of usual residents living in households or in communal establishments." (ONS Census 2021 Resident type variable)

**SCOPE**

- England and Wales. Output Area 2021 boundary; 188,880 OAs.
- Base population: all usual residents.

**CRS**

- EPSG:27700 (OSGB 1936 / British National Grid).

**LICENCE**

- Open Government Licence v3.0.

**DATA QUALITY CAVEATS**

- Output Area is the lowest published Census geography. Confidentiality protection (ONS "cell key perturbation") can move single residents around between cells; treat single-digit counts with care.

**LOADED INTO uk_baseline**

- Data: Census Day 21 March 2021.


## Columns

| Column | Type | Description / unit |
|---|---|---|
| `fid` | `integer` |  |
| `oa21cd` | `text` | Source field "OA21CD"; ONS GSS 9-character Output Area 2021 code. |
| `total_residents` | `integer` | Source field; count of all usual residents in the Output Area on Census Day. Unit: "persons". |
| `residents_in_household` | `integer` | Source field; count of usual residents living in households (excludes communal establishments). Unit: "persons". |
| `residents_in_communal` | `integer` | Source field; count of usual residents living in communal establishments (e.g. care home, prison, hostel). Unit: "persons". |
| `geom` | `geometry(MultiPolygon,27700)` | MultiPolygon in EPSG:27700. Boundary geometry joined at load. |
