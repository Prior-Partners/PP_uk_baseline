r"""Build per-layer STATIC preview snapshots + the shared styles contract.

Input/output CRS: reads EPSG:27700, renders in EPSG:4326 (Leaflet). Data layer:
catalogue map generation.

Each layer is styled with folium / Leaflet (CartoDB Positron basemap, brand
colours, GeoJSON style_function, legend/key), framed at a per-layer readable
extent, saved as HTML, then screenshotted to a static PNG (headless Chrome via
selenium) at catalogue/docs/maps/<table>.png. The catalogue embeds the PNG; the
"Open in the Dashboard" link points at the interactive, full-extent Dashboard
(Stream 1) — this catalogue no longer hosts the interactive map itself.

The per-layer styling decided here is the source of truth: it is written to the
shared styles JSON (STYLES_JSON) that the Dashboard reads, so both look identical.
Run `python build_maps.py` for all layers, or `python build_maps.py ADM BLT` to
(re)style named themes as they are approved.
"""
from __future__ import annotations

import json
import logging
import math
import os
import re
from decimal import Decimal
from pathlib import Path

import branca.colormap as cm
import folium
import psycopg
from branca.element import Element
from dotenv import dotenv_values
from pyproj import Transformer

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger(__name__)

# Override with the UK_BASELINE_ENV environment variable for portability.
ENV = Path(os.environ.get(
    "UK_BASELINE_ENV",
    r"C:\Users\po.nienchen\OneDrive - priorpartners.com"
    r"\Documents\05_Code_Scripts\data_import\Natural_England\.env"))
SCHEMA = "uk_baseline"
OUT = Path(__file__).resolve().parents[2] / "catalogue" / "docs" / "maps"

# Fixed 25 km windows (EPSG:27700): centre +/- 12.5 km.
WINDOWS = {
    "MK": (472500, 225500, 497500, 250500),          # Milton Keynes
    "south_downs": (467500, 99500, 492500, 124500),  # countryside fallback
    "england": (240000, 50000, 660000, 640000),      # whole-country overview
}
WINDOW_LABEL = {"MK": "Milton Keynes", "south_downs": "South Downs",
                "england": "England"}
MK_CENTRE_BNG = (485000, 238000)       # Milton Keynes centre
BHAM_CENTRE_BNG = (407000, 287000)     # Birmingham centre (denser sample for some BLT)
LONDON_CENTRE_BNG = (531000, 180000)   # central London (some layers are London-only)
WMIDS_CENTRE_BNG = (403000, 293000)    # West Midlands (Birmingham + Black Country — densest ECN enterprise-zone cluster)
SOLENT_CENTRE_BNG = (452000, 97000)    # the Solent (coastal — for tidal-water, which is empty inland)
FENS_CENTRE_BNG = (540000, 288000)     # the Fens NE of Peterborough — extensive flood coverage (for flood layers)
SOUTH_COAST_CENTRE_BNG = (399000, 80000)  # south coast + Channel — for protected wrecks (offshore, all along the coast)
PEAK_DISTRICT_BNG = (410000, 380000)   # densest published public-rights-of-way network (for PRoW)
# Layers that read best as a local cover-the-frame view: table substring ->
# (centre_bng, zoom). Fine admin grains and detail layers that vanish or become
# an unreadable scatter at national extent.
LOCAL_VIEWS = {
    "lsoa_boundary": (MK_CENTRE_BNG, 12), "oa_boundaries": (MK_CENTRE_BNG, 13),
    "ward_boundary": (MK_CENTRE_BNG, 11), "postcode_centroid": (MK_CENTRE_BNG, 12),
    "geods_poi": (MK_CENTRE_BNG, 13), "named_places": (MK_CENTRE_BNG, 13),
    "functional_sites": (BHAM_CENTRE_BNG, 12),      # Birmingham — cleaner than MK
    "important_buildings": (BHAM_CENTRE_BNG, 13),   # Birmingham — far denser
    "geods_retail_centre": (BHAM_CENTRE_BNG, 12),
    "built_up_areas": (BHAM_CENTRE_BNG, 11),
    "green_space_sport": (BHAM_CENTRE_BNG, 12),      # COM — detail, blank nationally
    "active_places": (BHAM_CENTRE_BNG, 12),
    "oa_household_residents": (BHAM_CENTRE_BNG, 13),  # DEM — Output-Area grain, too fine nationally
    "msoa_income": (BHAM_CENTRE_BNG, 11),             # DEM — MSOA, zoom to a local area
    "foodretail_accessibility": (LONDON_CENTRE_BNG, 11),  # ECN — London-only hex grid
    "enterprise_zone": (WMIDS_CENTRE_BNG, 11),       # ECN — sub-pixel nationally; frame the densest cluster
    # ENV dense small-feature single-colour layers — sub-pixel & blank nationally.
    "os_surface_water": (BHAM_CENTRE_BNG, 11), "os_woodland": (BHAM_CENTRE_BNG, 11),
    "historic_landfill": (BHAM_CENTRE_BNG, 11),
    "os_tidal_water": (SOLENT_CENTRE_BNG, 10),       # coastal — Birmingham is inland (no tidal water)
    "flood_zone": (FENS_CENTRE_BNG, 10),             # all 3 flood layers — Birmingham barely floods
    "listed_building_polygons": (LONDON_CENTRE_BNG, 14),  # HER — footprints, dense in central London
    "protected_wrecks": (SOUTH_COAST_CENTRE_BNG, 7),  # HER — 9 offshore wrecks span Cornwall→Dover (need a wide frame)
    "house_price_paid": (LONDON_CENTRE_BNG, 12),     # HOU — 31M points; intra-London price gradient (avoids national scan)
    "public_right_of_way": (PEAK_DISTRICT_BNG, 10),  # MOB — dense path network; framed on the Peak District
    # MOB roads: large-regional view (Midlands motorway hub) so the major network is
    # connected and the width-by-class hierarchy reads (national sampling fragments it).
    "os_open_roads": (BHAM_CENTRE_BNG, 9), "osm_roads": (BHAM_CENTRE_BNG, 9),
}

# Sequential colour ramps (stops listed vmin -> vmax). Estimated from the owner's
# brand colour-wheel images; tweak hexes here.
RAMP_IMD = ["#6d1250", "#d81e7f", "#ed1c24", "#f7901e"]   # decile 1 dark -> 10 orange (dark = deprived)
RAMP_FUEL = ["#79d3a6", "#2ba6e0", "#1666c8", "#15206b"]  # low mint -> high navy (dark = poorer)
RAMP_AHAH = ["#e6b8d8", "#6d1250"]                        # low light -> high dark (dark = less healthy)
RAMP_CAR = ["#d4efe6", "#0b6e5e"]                         # soft teal (dark = more no-car)
RAMP_SEQ = ["#efe3cf", "#945f14"]                         # neutral DEM-brown, low light -> high dark
RAMP_SEQ_R = ["#945f14", "#efe3cf"]                       # inverted (dark = low %, i.e. more diverse)
RAMP_ORANGE = ["#fde4cf", "#e0631c"]                      # light -> orange (dark = more)
RAMP_BLUE = ["#d6e2ff", "#0050e6"]                        # light -> blue (dark = more)
RAMP_PINK_R = ["#c2185b", "#fbd0e4"]                      # dark -> light pink (dark = low %, inverted)

RAMP_BLUEGREEN = ["#d6f2ea", "#0e7a6b"]                   # light -> teal (dark = more)
RAMP_YELLOW_R = ["#caa300", "#fff7c2"]                    # gold -> pale yellow (dark = low %, inverted)
RAMP_GREEN_R = ["#1b5e20", "#dcedc8"]                     # dark green -> pale (dark = low %, inverted)
RAMP_DARKRED = ["#fcdcd6", "#7a0a12"]                     # light -> dark red (dark = more)
RAMP_PURPLE = ["#e7ddf2", "#5b2d8c"]                      # light lavender -> deep purple (dark = more)
RAMP_GREEN = ["#dcedc8", "#1b5e20"]                       # light -> dark green (dark = more)

# ECN colouring plan (owner-approved). Table substring -> spec overrides.
# Employment layers (business_register_employment) are handled separately in
# build_specs (total employment = sum of the SIC industry count columns).
ECN_PLAN = {
    "gross_value_added": dict(colour_by="gva_2023", ctype="sequential", ramp=RAMP_GREEN,
                              scale="quantile", legend_title="GVA 2023"),
    "business_floorspace": dict(colour_by="floorspace_all_2023", ctype="sequential",
                                ramp=RAMP_BLUE, scale="quantile",
                                legend_title="Business floorspace 2023 (m²)"),
    "stock_properties": dict(colour_by="count_all_2025", ctype="sequential", ramp=RAMP_PURPLE,
                             scale="quantile", legend_title="Commercial properties 2025"),
    "housing_affordability_ratio": dict(colour_by="medratio_2025", ctype="sequential",
                                        ramp=RAMP_DARKRED,
                                        legend_title="Affordability ratio 2025 (price ÷ income)"),
    "foodretail_accessibility": dict(colour_by="travel_time_friday_18", ctype="sequential",
                                     ramp=RAMP_ORANGE,
                                     legend_title="Travel time to food retail, Fri 18:00 (min)"),
    # 535 small scattered multipolygons (avg ~360 m across) → sub-pixel at national
    # extent. Framed on the densest cluster (West Midlands, via LOCAL_VIEWS) and given
    # a red outline + solid red fill so even the smallest sites read clearly.
    "enterprise_zone": dict(colour_by=None, ctype="single", colour="#dd1220",
                            outline="#dd1220", outline_weight=1.5, fill_opacity=0.85,
                            legend_title="Enterprise zone site"),
}


def _greatest_case(items):
    """CASE picking the label of the largest expression; COALESCE so every row
    gets a value (no gaps), with an 'Other' fallback for all-null/zero rows."""
    exprs = [(f"COALESCE({e}, 0)" if e[0] != "(" else e, lab) for e, lab in items]
    return ("CASE GREATEST(" + ", ".join(e for e, _ in exprs) + ") "
            + " ".join(f"WHEN {e} THEN '{lab}'" for e, lab in exprs) + " ELSE 'Other' END")


# Dominant household size: largest of the per-size counts (cols are oddly named —
# digits / spaces — so quote them). Replaces the messy dominant_household_size_group.
_HSIZE_CASE = _greatest_case([
    ('"1 person in household_count"', "1 person"),
    ('"2_people_in_household_count"', "2 people"),
    ('"3_people_in_household_count"', "3 people"),
    ('"4_people_in_household_count"', "4 people"),
    ('"5_people_in_household_count"', "5 people"),
    ('"6_people_in_household_count"', "6 people"),
    ('"7_people_in_household_count"', "7 people"),
    ('"8_or_more_people_in_household_count"', "8+ people"),
])

# Dominant industry by the standard 8 ONS broad groups, so 2011 and 2021 match.
# 2021 has these natively (int8); 2011 (21 detailed text counts) is summed to them.
_IND_GROUPS = ["Agriculture, energy & water", "Manufacturing", "Construction",
               "Distribution, hotels & restaurants", "Transport & communication",
               "Finance, real estate, professional & admin",
               "Public admin, education & health", "Other"]
_IND2011_MAP = {
    "Agriculture, energy & water": ["agriculture_forestry_fishing", "mining_quarrying",
                                    "electricity_gas_steam_aircon_supply", "water_waste_sewerage"],
    "Manufacturing": ["manufacturing"],
    "Construction": ["construction"],
    "Distribution, hotels & restaurants": ["wholesale_retail_motor_repair",
                                           "accommodation_food_service"],
    "Transport & communication": ["transport_storage", "information_communication"],
    "Finance, real estate, professional & admin": ["financial_insurance", "real_estate",
                                                   "professional_scientific_technical",
                                                   "admin_support_service"],
    "Public admin, education & health": ["public_admin_defence_social_security",
                                         "education", "health_social_work"],
    "Other": ["arts_entertainment_recreation", "other_service",
              "activities_of_household_employers_goods_services", "extraterritorial_orgs"],
}
_IND_CASE = _greatest_case([   # 2011 counts are text → cast to numeric
    ("(" + " + ".join(f"COALESCE(NULLIF({c}_count,'')::numeric, 0)" for c in _IND2011_MAP[lab]) + ")", lab)
    for lab in _IND_GROUPS])
_IND2021_COLS = {  # native 2021 group counts (int8)
    "Agriculture, energy & water": "agriculture_energy_and_water_count",
    "Manufacturing": "manufacturinge_count", "Construction": "construction_count",
    "Distribution, hotels & restaurants": "distribution_hotels_and_restaurants_count",
    "Transport & communication": "transport_and_communication_count",
    "Finance, real estate, professional & admin": "finance_realestate_prof_admin_activity_count",
    "Public admin, education & health": "public_administration_education_health_count",
    "Other": "other_industries_count",
}
_IND2021_CASE = _greatest_case([(_IND2021_COLS[lab], lab) for lab in _IND_GROUPS])

# Explicit DEM colouring plan (owner-approved). Table substring -> spec overrides.
DEM_PLAN = {
    "imd_2025": dict(colour_by="imd_decile", ctype="sequential", ramp=RAMP_IMD,
                     legend_title="IMD 2025 decile (1 = most deprived)"),
    "imd_2019": dict(colour_by="index_of_multiple_deprivation_decile", ctype="sequential",
                     ramp=RAMP_IMD, legend_title="IMD 2019 decile (1 = most deprived)"),
    "fuel_poverty": dict(colour_by="fuel_poor_households_perc", ctype="sequential",
                         ramp=RAMP_FUEL, legend_title="Fuel-poor households (%)"),
    "access_healthy_assets": dict(colour_by="ahah_pct", ctype="sequential", ramp=RAMP_AHAH,
                                  legend_title="AHAH percentile (higher = less healthy)"),
    "car_availability": dict(colour_by='"No cars or vans in household _perc"', ctype="sequential",
                             ramp=RAMP_CAR, legend_title="No car/van households (%)"),
    "students_2011": dict(colour_by="total_students_count", ctype="sequential", ramp=RAMP_PURPLE,
                          legend_title="Total students"),
    "students_2021": dict(colour_by="total_students", ctype="sequential", ramp=RAMP_PURPLE,
                          legend_title="Total students"),
    "msoa_income_2011": dict(colour_by="total_annual_income", ctype="sequential", ramp=RAMP_DARKRED,
                             legend_title="Total annual income (£)"),
    "oa_household_residents": dict(colour_by="total_residents", ctype="sequential", ramp=RAMP_BLUE,
                                   legend_title="Total residents"),
    "national_identity": dict(colour_by="british_only_identity_perc", ctype="sequential",
                              ramp=RAMP_YELLOW_R, legend_title="British-only identity (%)"),
    "passport_held": dict(colour_by="united_kingdom_perc", ctype="sequential", ramp=RAMP_GREEN_R,
                          legend_title="UK passport (%)"),
    "household_population": dict(colour_by="mid_2021_people_per_ha", ctype="sequential",
                                ramp=RAMP_BLUEGREEN, legend_title="Population density (people/ha)"),
    "age_alternate_bands": dict(
        colour_by="aged_65_to_69_years_perc + aged_70_to_79_years_perc + aged_80_and_above_years_perc",
        ctype="sequential", ramp=RAMP_ORANGE, legend_title="Aged 65 and over (%)"),
    "lsoa_education": dict(colour_by="level_4_qualifications_or_above_perc", ctype="sequential",
                           ramp=RAMP_BLUE, legend_title="Level 4+ qualifications (%)"),
    "housing_tenure": dict(colour_by="dominant_housing_tenure_group", ctype="categorical",
                           legend_title="Dominant housing tenure"),
    "household_composition": dict(colour_by="dominant_household_composition_group",
                                  ctype="categorical", legend_title="Dominant household composition"),
    "household_size": dict(colour_by=_HSIZE_CASE, ctype="categorical",
                           legend_title="Dominant household size"),
    "industry_occupation_2021": dict(
        colour_by=_IND2021_CASE, ctype="categorical", legend_title="Dominant industry",
        note=("In 2021, 'Public admin, education & health' is the largest sector in "
              "~83% of LSOAs (vs 40% in 2011), so this dominant-sector map is "
              "largely one colour — the concentration is real, not a styling artefact.")),
    "industry_occupation_2011": dict(colour_by=_IND_CASE, ctype="categorical",
                                     legend_title="Dominant industry"),
    "english_proficiency": dict(colour_by="main_language_english_perc", ctype="sequential",
                                ramp=RAMP_PINK_R, legend_title="Main language English (%)"),
    "religion": dict(colour_by="dominant_relegious_group", ctype="categorical",
                     legend_title="Dominant religious group"),
    "ethnicity": dict(colour_by="dominant_ethnic_group", ctype="categorical",
                      legend_title="Dominant ethnic group"),
    "street_crime": dict(colour_by="crime_type", ctype="categorical", legend_title="Crime type"),
    "stop_search": dict(colour_by="object_of_search", ctype="categorical",
                        legend_title="Object of search"),
}

# Brand palette (matches the catalogue theme colours).
THEME_COLOURS = {
    "ADM": "#e9511d", "BLT": "#920f67", "COM": "#554596", "DEM": "#945f14",
    "ECN": "#dd1220", "EDU": "#6da2ed", "ENV": "#219900", "HER": "#2b242c",
    "HOU": "#8c3111", "HTH": "#005dff", "MOB": "#7a7a72", "UTL": "#991955",
}

# Preview thinning. Points/polygons are randomly sampled above the cap so the
# HTML stays small; lines are kept whole (sampling breaks a network) but
# simplified harder. Tolerance is in degrees (4326): coarser for the England
# overview window, finer for the 25 km local windows.
CAPS = {"point": 3000, "polygon": 4000, "line": 200000}   # local-window caps (legacy)
# Full-extent (England-wide) caps. Every layer renders nationally; dense layers
# are sampled to keep each HTML manageable. Coloured polygons (choropleths) keep
# enough units for the pattern to read (LSOA ~35k renders whole); single-colour
# polygons need only a national distribution sketch; lines are sampled too (a
# preview, so the broken network is acceptable — the caption notes the sample).
CAPS_FULL = {"point": 5000, "line": 30000,
             "polygon_colour": 60000, "polygon_single": 15000}
NONE_LIMIT = 1_000_000     # effective "no limit" for whole-layer renders (total <= cap)
# Above this estimate, sample server-side via TABLESAMPLE: an ORDER BY random()
# over tens of millions of rows would full-scan + sort the whole table (minutes
# per layer); TABLESAMPLE picks pages first, then we trim to the cap.
TABLESAMPLE_ROWS = 200_000
SAMPLE_KINDS = {"point", "polygon", "line"}   # at full extent, all kinds may sample
# ~10 m (0.0001°) is sub-pixel in a 25 km-wide preview, so simplifying this hard
# keeps the HTML small with no visible quality loss; the England overview is
# coarser still.
SIMPLIFY = {"MK": {"line": 0.00012, "other": 0.0001},
            "south_downs": {"line": 0.00012, "other": 0.0001},
            # national tolerances (~110-165 m, sub-pixel at country zoom): coloured
            # polygons keep more fidelity than single-colour extent-only fills.
            "england": {"line": 0.001, "polygon_colour": 0.001,
                        "polygon_single": 0.0015}}
# GeoJSON coordinate decimal places (EPSG:4326). The default 9 (~0.1 mm) bloats
# the HTML pointlessly; 4 (~11 m) is sub-pixel at national zoom, 6 (~0.1 m) in the
# 25 km local windows.
PRECISION = {"england": 4, "MK": 6, "south_downs": 6}
# Qualitative brand hues for categorical colouring. 12 distinct hues so layers
# with up to a dozen classes (e.g. POI categories, building themes) all show;
# beyond that, or an explicit "Other" class, falls to grey.
QUAL = ["#e9511d", "#005dff", "#4bb400", "#920f67", "#ff2a8e", "#dadf50",
        "#554596", "#009476", "#c8b5e2", "#945f14", "#f2a900", "#00a3a3"]
GREY = "#9a958c"
# Green->teal ramp (lime to dark teal), for layers a spec pins via "palette".
GREENS = ["#9cca3c", "#5cb82d", "#229a45", "#0c9472", "#0b8a8a", "#0a6b6b"]
CARTO = {"tiles": "CartoDB positron", "attr": "© OpenStreetMap, © CARTO"}

# Ofsted overall effectiveness — ordinal, semantic green (Outstanding) -> red
# (Inadequate); 'Not Judged' and unrated/null fall to grey. Used via cat_colours.
OFSTED_COLOURS = {
    "Outstanding": "#0b6e2e",            # dark green
    "Good": "#79c44d",                   # green
    "Requires Improvement": "#f2a900",   # amber
    "Inadequate": "#d62d20",             # red
    "Not Judged": GREY,
}

# School phase — Primary/Secondary as the clear dominant pair, the middle-deemed
# phases as related lighter shades, and 'Not applicable' (non-phase establishments,
# ~23%) greyed so it recedes instead of dominating with a loud hue.
PHASE_COLOURS = {
    "Primary": "#005dff",                 # blue
    "Secondary": "#e9511d",               # orange
    "Middle deemed primary": "#6da2ed",   # light blue (relates to Primary)
    "Middle deemed secondary": "#f2a900", # amber (relates to Secondary)
    "Nursery": "#4bb400",                 # green
    "16 plus": "#920f67",                 # plum
    "All-through": "#00a3a3",             # teal
    "Not applicable": GREY,
}

# EDU colouring plan (owner-approved). Table substring -> spec overrides. The
# all-schools layer is coloured by phase (level); the primary/secondary subsets are
# coloured by Ofsted rating (phase is ~uniform there).
EDU_PLAN = {
    "primary_school": dict(colour_by="ofsted_overall_rate", ctype="categorical",
                           cat_colours=OFSTED_COLOURS, legend_title="Ofsted rating",
                           label="establishment_name", label_title="School"),
    "secondary_school": dict(colour_by="ofsted_overall_rate", ctype="categorical",
                             cat_colours=OFSTED_COLOURS, legend_title="Ofsted rating",
                             label="establishment_name", label_title="School"),
    "dfe_school": dict(colour_by="phase_of_education_name", ctype="categorical",
                       cat_colours=PHASE_COLOURS, legend_title="Phase of education",
                       label="establishment_name", label_title="School"),
}

# --- ENV palettes & plan ---------------------------------------------------
WATER_BLUE = "#3a86c8"
TIDAL_BLUE = "#2c6a9e"
WOOD_GREEN = "#2e7d32"
LANDFILL_BROWN = "#7a6a53"
# Graduated-point ramp: a near-white low end vanishes on the basemap for small
# points, so start saturated (visible orange -> dark brown).
BROWNFIELD_RAMP = ["#fdae6b", "#7f2704"]

# OS rivers `form`, relabelled to readable text via CASE.
RIVER_FORM_COLOURS = {"Inland river": "#2b7bba", "Tidal river": "#5bb8c4",
                      "Lake": "#1f5f8b", "Canal": "#b06a2c"}
_RIVER_FORM_CASE = ("CASE form WHEN 'inlandRiver' THEN 'Inland river' "
                    "WHEN 'tidalRiver' THEN 'Tidal river' WHEN 'lake' THEN 'Lake' "
                    "WHEN 'canal' THEN 'Canal' END")

# Ancient woodland status: ASNW (semi-natural) darkest, PAWS (plantation) mid, AWP pale.
AW_STATUS_COLOURS = {"ASNW": "#1b5e20", "PAWS": "#7cb342", "AWP": "#c5e1a5"}
# Flood zone: FZ3 (higher risk) darker than FZ2.
FLOOD_ZONE_COLOURS = {"FZ2": "#9ecae1", "FZ3": "#2171b5"}
FLOOD_SOURCE_COLOURS = {"river": "#2171b5", "sea": "#41b6c4",
                        "river and sea": "#5e4fa2", "unknown": GREY}

# Agricultural Land Classification — ordinal best (Grade 1, dark green) -> poor
# (Grade 5, brown); urban / non-agricultural / exclusion greyed. Both agri layers
# map to these labels (the predictive layer's `alc` codes relabelled via CASE).
ALC_COLOURS = {"Grade 1": "#1a9850", "Grade 2": "#66bd63", "Grade 3": "#a6d96a",
               "Grade 3a": "#a6d96a", "Grade 3b": "#cfe08a", "Grade 4": "#fdae61",
               "Grade 5": "#a6611a", "Urban": GREY, "Non Agricultural": GREY,
               "Exclusion": GREY}
_ALC_PRED_CASE = ("CASE alc WHEN '1' THEN 'Grade 1' WHEN '2' THEN 'Grade 2' "
                  "WHEN '3a' THEN 'Grade 3a' WHEN '3b' THEN 'Grade 3b' "
                  "WHEN '4' THEN 'Grade 4' WHEN '5' THEN 'Grade 5' "
                  "WHEN 'NA' THEN 'Non Agricultural' WHEN 'U' THEN 'Urban' END")

# Priority Habitats — 83 `mainhabs` types rolled up into 8 broad classes.
HABITAT_GROUP_COLOURS = {"Woodland": "#1b5e20", "Grassland & meadow": "#9acd32",
                         "Heathland": "#9c5fb0", "Wetland, fen & bog": "#2c7fb8",
                         "Coastal": "#c9a227", "Moorland": "#8d6e63",
                         "Traditional orchard": "#e377c2", "Other": GREY}
_HABITAT_CASE = (
    "CASE "
    "WHEN mainhabs ILIKE '%woodland%' THEN 'Woodland' "
    "WHEN mainhabs ILIKE '%orchard%' THEN 'Traditional orchard' "
    "WHEN mainhabs ILIKE '%heath%' THEN 'Heathland' "
    "WHEN mainhabs ILIKE '%grazing marsh%' THEN 'Wetland, fen & bog' "
    "WHEN mainhabs ILIKE '%saltmarsh%' OR mainhabs ILIKE '%mudflat%' "
    "OR mainhabs ILIKE '%sand dune%' OR mainhabs ILIKE '%shingle%' "
    "OR mainhabs ILIKE '%maritime%' OR mainhabs ILIKE '%lagoon%' "
    "OR mainhabs ILIKE '%coastal%' THEN 'Coastal' "
    "WHEN mainhabs ILIKE '%bog%' OR mainhabs ILIKE '%fen%' "
    "OR mainhabs ILIKE '%reedbed%' OR mainhabs ILIKE '%marsh%' "
    "OR mainhabs ILIKE '%flush%' OR mainhabs ILIKE '%swamp%' "
    "OR mainhabs ILIKE '%pond%' OR mainhabs ILIKE '%lake%' "
    "OR mainhabs ILIKE '%saline%' THEN 'Wetland, fen & bog' "
    "WHEN mainhabs ILIKE '%moorland%' THEN 'Moorland' "
    "WHEN mainhabs ILIKE '%grassland%' OR mainhabs ILIKE '%meadow%' "
    "OR mainhabs ILIKE '%pasture%' OR mainhabs ILIKE '%limestone pavement%' "
    "OR mainhabs ILIKE '%calaminarian%' OR mainhabs ILIKE '%moor grass%' "
    "THEN 'Grassland & meadow' "
    "ELSE 'Other' END")

# ENV protected-area designations: uniform semi-transparent green fill + darker
# green outline, national (owner-approved 2 Jun 2026). Applied to any ENV polygon
# whose table matches one of these and has no ENV_PLAN colour-by override.
ENV_DESIGNATIONS = ("sssi", "special_areas_conservation", "special_protection_areas",
                    "ramsar", "national_nature_reserves", "local_nature_reserves",
                    "aonb", "country_parks", "environmentally_sensitive_areas",
                    "heathland", "national_park", "green_belt")
ENV_DESIGNATION_STYLE = dict(colour="#219900", fill_opacity=0.45,
                             outline="#0b6e2e", outline_weight=0.8)

# ENV colouring plan (owner-approved). Table substring -> spec overrides. Layers
# not matched here AND in ENV_DESIGNATIONS get the uniform designation style.
ENV_PLAN = {
    # water (blue)
    "os_rivers": dict(colour_by=_RIVER_FORM_CASE, ctype="categorical",
                      cat_colours=RIVER_FORM_COLOURS, legend_title="Watercourse type",
                      line_weight=1.1),
    "os_surface_water": dict(colour_by=None, ctype="single", colour=WATER_BLUE,
                             legend_title="Surface water"),
    "os_tidal_water": dict(colour_by=None, ctype="single", colour=TIDAL_BLUE,
                           legend_title="Tidal water"),
    # woodland (green)
    "os_woodland": dict(colour_by=None, ctype="single", colour=WOOD_GREEN,
                        legend_title="Woodland"),
    "ancient_woodland": dict(colour_by="status", ctype="categorical",
                             cat_colours=AW_STATUS_COLOURS,
                             legend_title="Ancient woodland status"),
    # flood (blue, by zone / source)
    # Flood is a near-continuous coverage layer: random sampling leaves big gaps,
    # so dissolve (ST_Union) all polygons per zone inside the viewport into one
    # merged geometry — solid extent, no gaps. Border = fill so zones read clean.
    "flood_zone_jan2025": dict(colour_by="flood_zone", ctype="categorical",
                               cat_colours=FLOOD_ZONE_COLOURS, legend_title="Flood zone",
                               dissolve=True, outline_match_fill=True, fill_opacity=0.8),
    "flood_zones_2_3": dict(colour_by="flood_zone", ctype="categorical",
                            cat_colours=FLOOD_ZONE_COLOURS, legend_title="Flood zone",
                            dissolve=True, outline_match_fill=True, fill_opacity=0.8),
    "flood_zones_plus": dict(colour_by="flood_source", ctype="categorical",
                             cat_colours=FLOOD_SOURCE_COLOURS, legend_title="Flood source",
                             dissolve=True, outline_match_fill=True, fill_opacity=0.8),
    # agricultural land (ordinal grade)
    "predictive_agricultural_land": dict(colour_by=_ALC_PRED_CASE, ctype="categorical",
                                         cat_colours=ALC_COLOURS,
                                         legend_title="Agricultural land grade"),
    "agri_land_nov2024": dict(colour_by="alc_grade", ctype="categorical",
                              cat_colours=ALC_COLOURS,
                              legend_title="Agricultural land grade"),
    # green space & access
    "green_space_apr2025": dict(colour_by='"function"', ctype="categorical",
                                legend_title="Green space function"),
    "green_space_access_points": dict(colour_by="accesstype", ctype="categorical",
                                      legend_title="Access type"),
    "access_to_public_parks": dict(
        colour_by="average_distance_to_nearest_park_public_garden_or_playing_field",
        ctype="sequential", ramp=RAMP_DARKRED, scale="quantile",
        legend_title="Distance to nearest park (m)"),
    "rivertrust_msoa": dict(colour_by="gb_sp_perc", ctype="sequential",
                            ramp=RAMP_GREEN, scale="quantile",
                            legend_title="Accessible green/blue space (%)"),
    # habitats & other
    "priority_habitats": dict(colour_by=_HABITAT_CASE, ctype="categorical",
                              cat_colours=HABITAT_GROUP_COLOURS,
                              legend_title="Broad habitat"),
    "historic_landfill": dict(colour_by=None, ctype="single", colour=LANDFILL_BROWN,
                              legend_title="Historic landfill site"),
    "brownfield_land": dict(colour_by="NULLIF(hectares,'')::numeric", ctype="sequential",
                            ramp=BROWNFIELD_RAMP, scale="quantile",
                            legend_title="Brownfield site area (ha)"),
}

# --- HER palettes & plan ---------------------------------------------------
# Listed-building / parks-and-gardens grade — ordinal importance: Grade I (rarest,
# most important) darkest -> Grade II (commonest) lightest.
HER_GRADE_COLOURS = {"I": "#6d1250", "II*": "#b54a9a", "II": "#d9a3c7"}

# HER designations: uniform dark-plum (theme colour) semi-transparent fill + outline.
HER_DESIGNATIONS = ("battlefields", "conservation_areas", "heritage_at_risk",
                    "national_trust_land", "scheduled_monuments", "world_heritage_sites",
                    "always_open", "limited_access", "protected_wrecks")
HER_DESIGNATION_STYLE = dict(colour="#2b242c", fill_opacity=0.4,
                             outline="#2b242c", outline_weight=0.8)

# HER colouring plan (owner-approved). Table substring -> spec overrides. Layers not
# matched here AND in HER_DESIGNATIONS get the uniform designation style.
HER_PLAN = {
    "listed_building_points": dict(colour_by="grade", ctype="categorical",
                                   cat_colours=HER_GRADE_COLOURS,
                                   legend_title="Listed building grade",
                                   label="name", label_title="Listed building"),
    "listed_building_polygons": dict(colour_by="grade", ctype="categorical",
                                     cat_colours=HER_GRADE_COLOURS,
                                     legend_title="Listed building grade",
                                     label="name", label_title="Listed building"),
    # Registered parks & gardens are small park-sized polygons — sub-pixel and
    # blank at national extent, so colour each polygon's border to match its grade
    # fill (outline_match_fill) with a visible weight so they read as graded specks.
    "parks_gardens": dict(colour_by="grade", ctype="categorical",
                          cat_colours=HER_GRADE_COLOURS,
                          legend_title="Registered park/garden grade",
                          label="name", label_title="Park/garden",
                          outline_match_fill=True, outline_weight=1.8, fill_opacity=0.85),
    # 9 small offshore wrecks — most fall outside the national land bbox, so frame
    # on the south coast (via LOCAL_VIEWS) with a visible speck style.
    "protected_wrecks": dict(colour_by=None, ctype="single", colour="#2b242c",
                             outline="#2b242c", outline_weight=2.6, fill_opacity=0.9,
                             legend_title="Protected wreck",
                             label="name", label_title="Wreck"),
}

# --- HOU plan --------------------------------------------------------------
# Single layer: HM Land Registry price paid (31M points). Price is extremely
# skewed (£100 -> £154M) so quantile; framed on London (intra-city price gradient,
# and avoids a national scan of 31M rows).
HOU_PLAN = {
    "house_price_paid": dict(colour_by="price", ctype="sequential", ramp=RAMP_DARKRED,
                             scale="quantile", legend_title="Price paid (£)",
                             label="concat_ws(', ', street, town_city)", label_title="Address"),
}

# --- HTH plan --------------------------------------------------------------
# OHID MSOA health choropleths + two NHS point layers. Per-indicator intuitive
# ramps; skewed indicators (mortality, GP list size) use quantile.
# Life expectancy: dark = LOW (worse), teal (high) -> navy (low), per owner's scheme.
RAMP_LIFE_EXP = ["#2a1c6e", "#1c3fcb", "#33a8d8", "#45c4b0"]   # vmin (low/dark) -> vmax (high/teal)
HTH_PLAN = {
    # MSOA choropleths (national; MSOA ~7k is coarse enough to read)
    "life_expectancy": dict(colour_by="male_life_expectancy", ctype="sequential",
                            ramp=RAMP_LIFE_EXP, legend_title="Male life expectancy (years)"),
    # Value is a ratio to expected (100 = national average), not a true %. Reuse the
    # life-expectancy teal->navy scheme but reversed so dark = high = worse (consistent
    # with life expectancy where dark = low = worse).
    "mortality_rate": dict(colour_by="deaths_from_all_causes_all_ages_under_75_years_perc",
                           ctype="sequential", ramp=RAMP_LIFE_EXP[::-1], scale="quantile",
                           legend_title="Under-75 mortality ratio — >100 worse, <100 better than average"),
    "childhood_obesity": dict(colour_by="year_6_prevalence_of_obesity_perc", ctype="sequential",
                              ramp=RAMP_ORANGE, legend_title="Year 6 obesity (%)"),
    "long_term_disability": dict(colour_by="limiting_long_term_illness_or_disability_perc",
                                 ctype="sequential", ramp=RAMP_PURPLE,
                                 legend_title="Limiting long-term illness or disability (%)"),
    "unemployment": dict(colour_by="unemployment_perc", ctype="sequential", ramp=RAMP_BLUE,
                         scale="quantile", legend_title="Unemployment (%)"),
    # NHS point layers (national)
    "nhs_facility": dict(colour_by="organisation_type", ctype="categorical",
                         legend_title="NHS facility type",
                         label="organisation_name", label_title="Facility"),
    "nhs_gp": dict(colour_by="total_patients", ctype="sequential", ramp=RAMP_BLUE,
                   scale="quantile", legend_title="Registered patients",
                   label="practice_name", label_title="GP practice"),
}

# --- MOB plan --------------------------------------------------------------
# Roads: single grey, WIDTH encodes class (Motorway thick -> B thin); the preview
# shows only the major tier (the Dashboard reveals minor classes on zoom-in).
ROAD_GREY = "#6b6b6b"
RAIL_PURPLE = "#7b3fa0"
BUS_AMBER = "#e0850b"
OS_ROAD_WEIGHTS = {"Motorway": 3.4, "A Road": 2.1, "B Road": 1.1}
OSM_ROAD_WEIGHTS = {"Motorway": 3.4, "Trunk": 2.4, "Primary": 1.3}
_OSM_ROAD_CASE = ("CASE WHEN fclass IN ('motorway','motorway_link') THEN 'Motorway' "
                  "WHEN fclass IN ('trunk','trunk_link') THEN 'Trunk' "
                  "WHEN fclass IN ('primary','primary_link') THEN 'Primary' END")
NCN_COLOURS = {"NCN": "#1a9850", "RCN": "#7cc043", "LINK": "#c8b5e2"}  # national / regional / link
_PROW_CASE = ("CASE prow_type_norm WHEN 'footpath' THEN 'Footpath' "
              "WHEN 'bridleway' THEN 'Bridleway' WHEN 'boat' THEN 'BOAT' "
              "WHEN 'restricted_byway' THEN 'Restricted byway' "
              "WHEN 'cycle_track' THEN 'Cycle track' ELSE 'Other' END")

MOB_PLAN = {
    # Roads — grey, width by class; preview filtered to the major tier (national).
    "os_open_roads": dict(colour_by="road_classification", ctype="categorical",
        colour=ROAD_GREY, weight_by=OS_ROAD_WEIGHTS, cap=40000,
        where="road_classification IN ('Motorway','A Road','B Road')",
        legend_title="Road classification", label="name_1", label_title="Road"),
    "osm_roads": dict(colour_by=_OSM_ROAD_CASE, ctype="categorical",
        colour=ROAD_GREY, weight_by=OSM_ROAD_WEIGHTS, cap=40000,
        where="fclass IN ('motorway','motorway_link','trunk','trunk_link','primary','primary_link')",
        legend_title="Road class (OSM)", label="name", label_title="Road"),
    # Rail — purple; tracks solid, tunnels dashed (per owner's scheme).
    "railway_tracks": dict(colour_by=None, ctype="single", colour=RAIL_PURPLE,
        line_weight=1.4, legend_title="Railway track"),
    "railway_tunnels": dict(colour_by=None, ctype="single", colour=RAIL_PURPLE,
        line_weight=1.4, legend_title="Railway tunnel"),
    "railway_stations": dict(colour_by=None, ctype="single", colour=RAIL_PURPLE,
        legend_title="Railway station"),
    # Cycle / bus
    "national_cycle_network": dict(colour_by="routetype", ctype="categorical",
        cat_colours=NCN_COLOURS, line_weight=1.5, legend_title="Cycle network"),
    "bus_routes": dict(colour_by="route_class", ctype="categorical",
        where="route_class IN ('local','regional')",   # local + regional only (hide intercity + coach)
        line_weight=1.0, legend_title="Bus route class"),
    "bus_stops": dict(colour_by=None, ctype="single", colour=BUS_AMBER,
        legend_title="Bus stop"),
    # PRoW — flood-zone strategy: framed on the densest area (Peak District) at a
    # raised cap, coloured by type (no natural major/minor hierarchy).
    "public_right_of_way": dict(colour_by=_PROW_CASE, ctype="categorical",
        line_weight=1.2, cap=30000, legend_title="Right of way type"),
}

# Acronyms to upper-case wherever they appear as a whole word in a legend
# title or category label (key tidy-up: "Os named places" -> "OS named places").
ACRONYMS = {"OS", "OSM", "ONS", "NHS", "GP", "POI", "VOA", "NDR", "IMD", "LSOA",
            "MSOA", "OA", "LAD", "GVA", "OHID", "DFT", "DFE", "DESNZ", "MHCLG",
            "GEODS", "WWCT", "UK", "EV", "SSSI", "SAC", "SPA", "HMLR"}


def prettify_acronyms(text: str) -> str:
    """Upper-case known acronyms appearing as whole words in ``text``."""
    return re.sub(r"[A-Za-z]+",
                  lambda m: m.group(0).upper() if m.group(0).upper() in ACRONYMS
                  else m.group(0), text)

CONNINFO = None


def conninfo() -> str:
    e = dotenv_values(ENV)
    parts = [f"host={e['PG_HOST']}", f"port={e['PG_PORT']}",
             f"dbname={e['PG_DATABASE']}", f"user={e['PG_USER']}"]
    if e.get("PG_PASSWORD"):
        parts.append(f"password={e['PG_PASSWORD']}")
    return " ".join(parts)


def _tint(hex_colour: str, amount: float = 0.85) -> str:
    """Blend a hex colour toward white by ``amount`` (0..1) for the ramp's low end."""
    r, g, b = (int(hex_colour[i:i + 2], 16) for i in (1, 3, 5))
    r = int(r + (255 - r) * amount)
    g = int(g + (255 - g) * amount)
    b = int(b + (255 - b) * amount)
    return f"#{r:02x}{g:02x}{b:02x}"


def window_bounds_4326(cur, key, bbox=None):
    x0, y0, x1, y1 = bbox or WINDOWS[key]
    cur.execute(
        "SELECT ST_XMin(g), ST_YMin(g), ST_XMax(g), ST_YMax(g) FROM "
        "(SELECT ST_Transform(ST_MakeEnvelope(%s,%s,%s,%s,27700),4326) g) s",
        (x0, y0, x1, y1))
    xmin, ymin, xmax, ymax = cur.fetchone()
    return (ymin, xmin, ymax, xmax)  # south, west, north, east


def kind_of(gtype):
    """Map a geometry_columns type string to point / line / polygon."""
    g = (gtype or "").upper()
    if "POINT" in g:
        return "point"
    if "LINE" in g:
        return "line"
    return "polygon"


def geojson_bounds(feats):
    """(south, west, north, east) enclosing all feature coords, or None.

    Lets the map fit to the actual data extent so the layer fills the frame
    rather than floating inside the window box.
    """
    xs, ys = [], []

    def walk(coords):
        if not coords:
            return
        if isinstance(coords[0], (int, float)):
            xs.append(coords[0]); ys.append(coords[1])
        else:
            for c in coords:
                walk(c)

    for f in feats:
        walk(f["geometry"].get("coordinates"))
    if not xs:
        return None
    return (min(ys), min(xs), max(ys), max(xs))


# Output frame (must match the screenshot window size) so a fixed-zoom "view"
# fetches exactly what the PNG shows.
FRAME = (1000, 720)
_BNG_WGS = Transformer.from_crs("EPSG:27700", "EPSG:4326", always_xy=True)
_BNG_3857 = Transformer.from_crs("EPSG:27700", "EPSG:3857", always_xy=True)
_3857_BNG = Transformer.from_crs("EPSG:3857", "EPSG:27700", always_xy=True)
_WGS_3857 = Transformer.from_crs("EPSG:4326", "EPSG:3857", always_xy=True)


def fit_zoom(south, west, north, east, frame=FRAME, margin=1.10):
    """Web-Mercator zoom that fits a 4326 bbox into ``frame``. Used to set the map's
    initial zoom so the extent is correct even when Leaflet's fitBounds is prevented
    from running (a folium tooltip-on-markers JS error can halt the page script
    before fitBounds — without this the map stays at the default zoom)."""
    xw, ys = _WGS_3857.transform(west, south)
    xe, yn = _WGS_3857.transform(east, north)
    res = max(abs(xe - xw) * margin / frame[0], abs(yn - ys) * margin / frame[1], 1e-6)
    return max(2, min(18, int(math.log2(156543.03392804097 / res))))


def viewport_bng(center_bng, zoom, frame=FRAME):
    """BNG bbox + (lon, lat) centre for what a frame-sized Leaflet map shows at
    ``zoom`` centred on ``center_bng``. Used to *cover* the viewport: fetch this
    bbox and set the map to this centre/zoom (no fit_bounds), so contiguous
    layers fill the frame edge-to-edge and overflow off-screen.
    """
    e, n = center_bng
    lon, lat = _BNG_WGS.transform(e, n)
    cx, cy = _BNG_3857.transform(e, n)
    res = 156543.03392804097 / (2 ** zoom)        # 3857 metres per pixel
    margin = 1.08                                 # over-fetch so edges never gap
    hw, hh = frame[0] / 2 * res * margin, frame[1] / 2 * res * margin
    x0, y0 = _3857_BNG.transform(cx - hw, cy - hh)
    x1, y1 = _3857_BNG.transform(cx + hw, cy + hh)
    return (x0, y0, x1, y1), (lon, lat)


def fetch_features(cur, table, colour_by, label, window_key, kind,
                   bbox=None, where=None, est_rows=0, cap_override=None, dissolve=False):
    """Return (features, total_in_window, sampled?).

    Dense point/polygon layers are randomly sampled to the per-kind cap so the
    preview HTML stays small; lines are kept whole. Geometry is simplified at a
    window-dependent tolerance. At full England extent dense layers are sampled
    server-side via TABLESAMPLE and the total uses the planner row estimate, to
    avoid scanning + sorting tens of millions of rows.
    """
    x0, y0, x1, y1 = bbox or WINDOWS[window_key]
    env = f"ST_MakeEnvelope({x0},{y0},{x1},{y1},27700)"
    val = colour_by if colour_by else "NULL"
    lbl = label if label else "NULL"
    extra = f" AND ({where})" if where else ""   # per-layer row filter
    full = window_key == "england"
    coloured = bool(colour_by)
    if full:
        if kind == "polygon":
            cap = CAPS_FULL["polygon_colour" if coloured else "polygon_single"]
            tol = SIMPLIFY["england"]["polygon_colour" if coloured else "polygon_single"]
        else:
            cap = CAPS_FULL[kind]
            tol = SIMPLIFY["england"]["line" if kind == "line" else "polygon_single"]
    else:
        cap = CAPS[kind]
        tol = SIMPLIFY[window_key]["line" if kind == "line" else "other"]
    if cap_override:                     # per-layer cap (dense coverage layers)
        cap = cap_override
    # Dissolve mode: near-continuous coverage layers (e.g. flood zones) look
    # gap-ridden when randomly sampled. Instead union all polygons per colour-by
    # category inside the viewport into one merged geometry — no sampling, no
    # gaps, and far fewer vertices. Pre-simplify each polygon (sub-pixel) so the
    # union is cheap.
    if dissolve:
        prec = PRECISION.get(window_key, 6)
        cur.execute(
            f"""SELECT {val} AS v, NULL AS lbl,
                       ST_AsGeoJSON(ST_SimplifyPreserveTopology(
                           ST_Transform(
                               ST_Union(ST_MakeValid(ST_SnapToGrid(geom, 10))), 4326),
                           {tol}), {prec}) AS gj
                FROM {SCHEMA}.{table}
                WHERE geom && {env} AND ST_Intersects(geom, {env}){extra}
                GROUP BY {val}""")
        feats = []
        for v, lab, gj in cur.fetchall():
            if not gj:
                continue
            if isinstance(v, Decimal):
                v = float(v)
            feats.append({"type": "Feature", "geometry": json.loads(gj),
                          "properties": {"value": v, "label": lab}})
        return feats, 0, False
    # Full-extent counts span the whole dataset; an exact count(*) over tens of
    # millions of rows is a needless scan — use the planner's row estimate.
    if full and est_rows:
        total = int(est_rows)
    else:
        cur.execute(f"SELECT count(*) FROM {SCHEMA}.{table} "
                    f"WHERE geom && {env} AND ST_Intersects(geom, {env}){extra}")
        total = cur.fetchone()[0]
    # Lines are normally kept whole locally, but a dense regional line layer with an
    # explicit cap (roads, PRoW) must be sampled or the browser can't render it.
    sample_kinds = (SAMPLE_KINDS if full
                    else {"point", "polygon", "line"} if cap_override
                    else {"point", "polygon"})
    # Server-side sampling for dense layers; else ORDER BY random() over the
    # (already small) set. Use BERNOULLI (true per-row random), NOT SYSTEM: SYSTEM
    # samples disk pages, so a table stored in spatial order yields a clustered
    # regional blob instead of a national spread (e.g. listed buildings).
    tablesample = full and kind in sample_kinds and total > TABLESAMPLE_ROWS
    if tablesample:
        pct = min(100.0, 100.0 * cap * 5.0 / max(total, 1))  # over-sample ~5x, then trim
        src = f"{SCHEMA}.{table} TABLESAMPLE BERNOULLI ({pct:.4f})"
        sampled = True
    else:
        src = f"{SCHEMA}.{table}"
        sampled = kind in sample_kinds and total > cap
    order = "ORDER BY random() " if sampled else ""
    limit = cap if sampled else NONE_LIMIT
    prec = PRECISION.get(window_key, 6)
    cur.execute(
        f"""SELECT {val} AS v, {lbl} AS lbl,
                   ST_AsGeoJSON(ST_SimplifyPreserveTopology(
                       ST_Transform(geom,4326), {tol}), {prec}) AS gj
            FROM {src}
            WHERE geom && {env} AND ST_Intersects(geom, {env}){extra}
            {order}LIMIT {limit}""")
    feats = []
    for v, lab, gj in cur.fetchall():
        if not gj:
            continue
        # numeric columns come back as Decimal; sequential colouring tests
        # isinstance(v, (int, float)), which Decimal fails -> coerce so the
        # value reads as numeric (else every feature falls to the white "no data"
        # branch and the layer renders blank).
        if isinstance(v, Decimal):
            v = float(v)
        feats.append({"type": "Feature",
                      "geometry": json.loads(gj),
                      "properties": {"value": v, "label": lab}})
    return feats, total, sampled


def legend_html(title, items):
    rows = "".join(
        f'<div style="display:flex;align-items:center;gap:6px;margin:2px 0;">'
        f'<span style="width:14px;height:14px;background:{c};border:1px solid #00000022;'
        f'display:inline-block;border-radius:2px;"></span>'
        f'<span>{lab}</span></div>'
        for lab, c in items)
    return (
        '<div style="position:fixed;bottom:22px;right:12px;z-index:9999;'
        'background:#f1eedf;color:#2b242c;padding:8px 11px;border:1px solid #d9d3c4;'
        'border-radius:6px;font:12px/1.3 -apple-system,Segoe UI,sans-serif;'
        'max-width:240px;box-shadow:0 1px 4px #0003;">'
        f'<div style="font-weight:700;margin-bottom:4px;">{title}</div>{rows}</div>')


def legend_html_line_weights(title, items, colour):
    """Legend for a single-colour line layer styled by WIDTH (e.g. roads: Motorway
    thick -> B thin). ``items`` is [(label, weight)] in display order."""
    rows = "".join(
        f'<div style="display:flex;align-items:center;gap:6px;margin:3px 0;">'
        f'<span style="width:26px;border-top:{max(1, round(w))}px solid {colour};'
        f'display:inline-block;"></span><span>{lab}</span></div>'
        for lab, w in items)
    return (
        '<div style="position:fixed;bottom:22px;right:12px;z-index:9999;'
        'background:#f1eedf;color:#2b242c;padding:8px 11px;border:1px solid #d9d3c4;'
        'border-radius:6px;font:12px/1.3 -apple-system,Segoe UI,sans-serif;'
        'max-width:240px;box-shadow:0 1px 4px #0003;">'
        f'<div style="font-weight:700;margin-bottom:4px;">{title}</div>{rows}</div>')


def quantile_step(ramp, vals, n=6):
    """StepColormap with equal-count (quantile) classes whose colours are spread
    evenly across ``ramp`` by class RANK, not by value position.

    branca's own ``to_step(method="quantiles")`` colours each class by where its
    break sits on the linear value axis ``[min, max]``. For heavily skewed data
    (GVA, floorspace, property stock, employment — median ≪ max) every lower
    quantile edge sits near 0 on that axis, so the bottom classes all collapse to
    the lightest shade and only the top class reads dark. Spreading the colours by
    class rank instead gives the n classes the n evenly-spaced shades of the ramp,
    so the whole gradient is visible.
    """
    svals = sorted(v for v in vals if isinstance(v, (int, float)))

    def pct(p):                                # linear-interpolated percentile
        if not svals:
            return 0.0
        k = p / 100.0 * (len(svals) - 1)
        lo = int(k)
        hi = min(lo + 1, len(svals) - 1)
        return svals[lo] + (svals[hi] - svals[lo]) * (k - lo)

    # quantile edges (n+1), then dedupe ties so the index is strictly increasing
    # (zero-heavy / very skewed data can repeat an edge).
    breaks = []
    for b in (pct(100.0 * i / n) for i in range(n + 1)):
        if not breaks or b > breaks[-1]:
            breaks.append(b)
    if len(breaks) < 2:                        # degenerate (all values equal)
        breaks = [svals[0], svals[0] + 1] if svals else [0, 1]
    k = len(breaks) - 1                         # class count after dedupe
    ramp_cm = cm.LinearColormap(ramp, vmin=0, vmax=1)
    colours = ([ramp_cm.rgb_hex_str(0.5)] if k == 1
               else [ramp_cm.rgb_hex_str(i / (k - 1)) for i in range(k)])
    return cm.StepColormap(colours, index=breaks, vmin=breaks[0], vmax=breaks[-1])


def legend_html_steps(title, step):
    """Discrete legend for a quantile StepColormap — one swatch per class with its
    value range, highest class at top (reuses the categorical legend box)."""
    idx = list(step.index)
    items = [(f"{_fmt_num(idx[i])}–{_fmt_num(idx[i + 1])}",
              step.rgb_hex_str((idx[i] + idx[i + 1]) / 2))
             for i in range(len(idx) - 1)]
    return legend_html(title, items[::-1])


def _fmt_num(x):
    """Compact human number for a legend tick (1.2M, 34k, 72, 8.4)."""
    ax = abs(x)
    if ax >= 1e6:
        return f"{x / 1e6:.1f}M"
    if ax >= 1e4:
        return f"{x / 1e3:.0f}k"
    if ax >= 100:
        return f"{x:.0f}"
    return f"{int(x)}" if float(x).is_integer() else f"{x:.1f}"


def legend_html_sequential(title, ramp, vmin, vmax):
    """Vertical gradient legend for sequential layers.

    Replaces branca's horizontal colorbar (which a full re-render overwrites)
    with a self-contained vertical bar in the same brand box as the categorical
    key, high value at the top. ``ramp`` is the list of stops (vmin -> vmax).
    """
    grad = "linear-gradient(to top, " + ", ".join(ramp) + ")"
    mid = (vmin + vmax) / 2
    return (
        '<div style="position:fixed;bottom:22px;right:12px;z-index:9999;'
        'background:#f1eedf;color:#2b242c;padding:8px 11px;border:1px solid #d9d3c4;'
        'border-radius:6px;font:12px/1.3 -apple-system,Segoe UI,sans-serif;'
        'box-shadow:0 1px 4px #0003;">'
        f'<div style="font-weight:700;margin-bottom:5px;">{title}</div>'
        '<div style="display:flex;gap:7px;align-items:stretch;">'
        f'<div style="width:14px;height:120px;background:{grad};'
        'border:1px solid #00000022;border-radius:2px;"></div>'
        '<div style="display:flex;flex-direction:column;justify-content:space-between;'
        'height:120px;">'
        f'<span>{_fmt_num(vmax)}</span><span>{_fmt_num(mid)}</span>'
        f'<span>{_fmt_num(vmin)}</span></div></div></div>')


def render(cur, spec):
    table, theme = spec["table"], spec["theme"]
    colour_by, ctype = spec.get("colour_by"), spec["ctype"]
    title = prettify_acronyms(spec["legend_title"])
    win = spec["window"]
    label, label_title = spec.get("label"), spec.get("label_title", "Name")
    fill_op = spec.get("fill_opacity", 0.6)
    line_weight = spec.get("line_weight", 2.6)   # line layers; per-layer override
    weight_for = spec.get("weight_by")           # line layers: per-class width (roads)
    dash = spec.get("dash", False)               # line layers: dashed (e.g. rail tunnels)
    outline = spec.get("outline", "#ffffff")     # polygon stroke; default white
    outline_weight = spec.get("outline_weight", 1.0)   # polygon stroke width; ADM bumped +50%
    outline_match = spec.get("outline_match_fill", False)  # stroke = fill colour (coverage layers merge)
    kind = kind_of(spec.get("gtype"))
    # A "view" (fixed centre + zoom) covers the frame: fetch exactly the visible
    # bbox and pin the map there (no fit_bounds). Otherwise fetch the window/bbox.
    view = spec.get("view")
    if view:
        bbox, (view_lon, view_lat) = viewport_bng(view["center_bng"], view["zoom"])
    else:
        bbox = spec.get("bbox")
    feats, total, sampled = fetch_features(
        cur, table, colour_by, label, win, kind, bbox, spec.get("where"),
        spec.get("est_rows", 0), spec.get("cap"), spec.get("dissolve"))
    if not feats:
        log.warning("  %s — no features in %s window, skipped", table, win)
        return False
    base = spec.get("colour", THEME_COLOURS.get(theme, "#444"))  # per-layer shade override
    if view:
        fmap = folium.Map(location=[view_lat, view_lon], tiles=None,
                          control_scale=True, zoom_start=view["zoom"],
                          zoom_control=False, prefer_canvas=True)
    else:
        # Fit to the data extent so the layer fills the frame; fall back to the
        # window box only if bounds can't be derived. Set zoom_start to the computed
        # fit-zoom so the extent is right even if Leaflet's fitBounds is prevented.
        south, west, north, east = (geojson_bounds(feats)
                                    or window_bounds_4326(cur, win, bbox))
        fmap = folium.Map(location=[(south + north) / 2, (west + east) / 2],
                          tiles=None, control_scale=True,
                          zoom_start=fit_zoom(south, west, north, east),
                          zoom_control=False, prefer_canvas=True)  # static snapshot
    folium.TileLayer(tiles=CARTO["tiles"], attr=CARTO["attr"], control=False).add_to(fmap)
    # Remove the browser's default focus outline (the "black square" drawn
    # around an SVG feature when clicked).
    fmap.get_root().header.add_child(Element(
        "<style>.leaflet-interactive:focus{outline:none;}"
        "path.leaflet-interactive:focus{outline:none;}</style>"))

    # --- colour assignment + legend ---
    colormap = None
    cat_map = {}
    vmin = vmax = None
    qbreaks = None
    if ctype == "categorical":
        cat_colours = spec.get("cat_colours")            # explicit value->hex (ordinal scales)
        weight_by = spec.get("weight_by")                # line layers: width encodes the class
        cats = sorted({f["properties"]["value"] for f in feats
                       if f["properties"]["value"] not in (None, "")})
        if weight_by:
            # Single-colour line layer styled by WIDTH (e.g. roads grey, Motorway
            # thick -> B thin). All classes share one colour; weight encodes the class.
            road_colour = spec.get("colour", "#6b6b6b")
            for v in cats:
                cat_map[v] = road_colour
            items = [(prettify_acronyms(str(v)), weight_by[v])
                     for v in weight_by if v in cats]   # legend in weight_by order
            fmap.get_root().html.add_child(
                Element(legend_html_line_weights(title, items, road_colour)))
        elif cat_colours:
            # Explicit semantic mapping (e.g. Ofsted rating green->red). Legend
            # follows the spec's value order; any unlisted value falls to grey.
            legend_items = []
            for v, col in cat_colours.items():
                if v in cats:
                    cat_map[v] = col
                    legend_items.append((prettify_acronyms(str(v)), col))
            leftover = [v for v in cats if v not in cat_map]
            for v in leftover:
                cat_map[v] = GREY
            if leftover:
                legend_items.append(("Other", GREY))
            fmap.get_root().html.add_child(Element(legend_html(title, legend_items)))
        else:
            palette = spec.get("palette", QUAL)          # per-layer palette override
            legend_items, grey_used, pi = [], False, 0
            for c in cats:
                label = prettify_acronyms(str(c))
                # only the literal 'Other' bucket greys (not e.g. 'Other Sports Facility')
                if str(c).strip().lower() == "other" or pi >= len(palette):
                    cat_map[c], grey_used = GREY, True    # 'Other' + overflow -> grey
                else:
                    cat_map[c] = palette[pi]; pi += 1
                    legend_items.append((label, cat_map[c]))
            if grey_used:
                legend_items.append(("Other", GREY))
            fmap.get_root().html.add_child(Element(legend_html(title, legend_items)))
    elif ctype == "sequential":
        vals = [f["properties"]["value"] for f in feats
                if isinstance(f["properties"]["value"], (int, float))]
        vmin, vmax = (min(vals), max(vals)) if vals else (0, 1)
        if vmin == vmax:
            vmax = vmin + 1
        ramp = spec.get("ramp") or [_tint(base), base]
        lin = cm.LinearColormap(ramp, vmin=vmin, vmax=vmax)
        # Skewed magnitudes (GVA, floorspace, employment…) wash out under a linear
        # ramp; `scale="quantile"` switches to equal-count classes so the spatial
        # pattern reads. Otherwise a continuous linear ramp + gradient legend.
        if spec.get("scale") == "quantile" and len(set(vals)) > 6:
            colormap = quantile_step(ramp, vals, n=6)
            qbreaks = list(colormap.index)
            fmap.get_root().html.add_child(Element(legend_html_steps(title, colormap)))
        else:
            colormap = lin
            fmap.get_root().html.add_child(Element(
                legend_html_sequential(title, ramp, vmin, vmax)))
    else:  # single
        fmap.get_root().html.add_child(Element(legend_html(title, [(title, base)])))

    def style(feature):
        v = feature["properties"]["value"]
        null_seq = False
        if ctype == "categorical":
            c = cat_map.get(v, GREY)
        elif ctype == "sequential":
            if isinstance(v, (int, float)):
                c = colormap(v)
            else:                       # no data -> white void (not grey)
                c, null_seq = "#ffffff", True
        else:
            c = base
        if kind == "line":
            w = weight_for.get(v, line_weight) if weight_for else line_weight
            st = {"color": c, "weight": w, "opacity": 0.9}
            if dash:
                st["dashArray"] = "5,5"
            return st
        if kind == "point":
            return {"fillColor": c, "color": c, "fillOpacity": 0.5,
                    "weight": 0.6, "opacity": 0.6}
        # 'Other' bucket (grey) on any polygon layer: grey + transparent so it
        # recedes behind the named categories.
        if ctype == "categorical" and c == GREY:
            return {"fillColor": GREY, "color": GREY, "weight": 0.6,
                    "fillOpacity": 0.18}
        fo = 0.9 if null_seq else fill_op   # white void reads solid
        if outline_match:                   # border = fill colour: coverage layers merge
            return {"fillColor": c, "color": c, "weight": outline_weight, "fillOpacity": fo}
        return {"fillColor": c, "color": outline, "weight": outline_weight, "fillOpacity": fo}

    def highlight(_feature):  # hover emphasis — outline stays white, thicker
        if kind == "line":
            return {"weight": line_weight + 1.9, "opacity": 1}
        return {"weight": 3.0, "color": "#ffffff", "fillOpacity": min(fill_op + 0.3, 0.85)}

    # tooltip: hover label (e.g. LSOA name) and/or the coloured value
    fields, aliases = [], []
    if label:
        fields.append("label"); aliases.append(label_title)
    if colour_by:
        fields.append("value"); aliases.append(title)
    tooltip = (folium.GeoJsonTooltip(fields=fields, aliases=aliases, sticky=True)
               if fields else None)

    gj_kwargs = dict(style_function=style, highlight_function=highlight, tooltip=tooltip)
    if kind == "point":
        gj_kwargs["marker"] = folium.CircleMarker(radius=4, fill=True)
    folium.GeoJson({"type": "FeatureCollection", "features": feats},
                   name=table, **gj_kwargs).add_to(fmap)

    if not view:                       # view maps are pinned to centre+zoom
        fmap.fit_bounds([[south, west], [north, east]], padding=(6, 6))
    # caption (top-left) — layer name only (no location); note any dense-layer sample
    note = (f' · sample of {len(feats):,} of {total:,}' if sampled
            else '')
    cap = (f'<div style="position:fixed;top:10px;left:10px;z-index:9999;'
           f'background:#2b242c;color:#fff;padding:4px 9px;border-radius:5px;'
           f'font:12px -apple-system,Segoe UI,sans-serif;">{table}'
           f'<span style="opacity:.7;">{note}</span></div>')
    fmap.get_root().html.add_child(Element(cap))

    OUT.mkdir(parents=True, exist_ok=True)
    fmap.save(str(OUT / f"{table}.html"))
    log.info("  %-52s %-11s %-11s %6d feats%s", table, win, ctype, len(feats),
             f"  (sampled of {total:,})" if sampled else "")
    # Return the computed style so the styles JSON carries the EXACT colours /
    # domain the preview used (so the Dashboard matches the Beta).
    return {"cat_map": cat_map, "vmin": vmin, "vmax": vmax, "base": base,
            "breaks": qbreaks, "n": len(feats), "total": total, "sampled": sampled}


# --- pilot manifest (16 layers; expand to all later) ----------------------
PILOT = [
    {"table": "adm_ons_lsoa_boundary_2021", "theme": "ADM", "window": "MK",
     "colour_by": None, "ctype": "single", "legend_title": "LSOA 2021 boundary",
     "label": "lsoa21nm", "label_title": "LSOA", "fill_opacity": 0.12},
    {"table": "adm_ons_postcode_centroid_feb2026", "theme": "ADM", "window": "MK",
     "colour_by": None, "ctype": "single", "legend_title": "Postcode centroid"},
    {"table": "dem_mhclg_lsoa_imd_2025", "theme": "DEM", "window": "MK",
     "colour_by": "imd_decile", "ctype": "sequential", "legend_title": "IMD decile (1 = most deprived)"},
    {"table": "dem_ons_lsoa_accommodation_type_2021", "theme": "DEM", "window": "MK",
     # dominant single type (largest share) -> 4 clean categories, not the
     # messy compound 'dominant group' column
     "colour_by": ("CASE GREATEST(detached_perc, semi_detached_perc, terraced_perc, "
                   "in_a_purpose_built_block_of_flats_or_tenement_perc) "
                   "WHEN detached_perc THEN 'Detached' "
                   "WHEN semi_detached_perc THEN 'Semi-detached' "
                   "WHEN terraced_perc THEN 'Terraced' "
                   "WHEN in_a_purpose_built_block_of_flats_or_tenement_perc THEN 'Flats' END"),
     "ctype": "categorical", "legend_title": "Dominant accommodation type"},
    {"table": "ecn_ons_lad_gross_value_added_2023", "theme": "ECN", "window": "MK",
     "colour_by": "gva_2023", "ctype": "sequential", "legend_title": "GVA 2023 (£m)",
     "bbox": (452500, 205500, 517500, 270500)},  # ±32.5km → 17 LADs (coarse grain)
    {"table": "ecn_voa_lsoa_business_floorspace_2023", "theme": "ECN", "window": "MK",
     "colour_by": "floorspace_all_2023", "ctype": "sequential",
     "legend_title": "Business floorspace 2023 (m²)"},
    {"table": "env_naturalengland_sssi_apr2026", "theme": "ENV", "window": "MK",
     "colour_by": None, "ctype": "single", "legend_title": "SSSI",
     # ±29.5 km around MK → ~120 sites; transparent fill, green outline
     "bbox": (455500, 208500, 514500, 267500), "outline": "#219900",
     "fill_opacity": 0.15},
    {"table": "env_ons_national_park_may2026", "theme": "ENV", "window": "england",
     "colour_by": None, "ctype": "single", "legend_title": "National Park"},
    {"table": "her_historicengland_listed_building_points_may2026", "theme": "HER", "window": "MK",
     "colour_by": "grade", "ctype": "categorical", "legend_title": "Listed building grade"},
    {"table": "her_historicengland_conservation_areas_jul2025", "theme": "HER", "window": "MK",
     "colour_by": None, "ctype": "single", "legend_title": "Conservation area",
     # drop Historic England's placeholder polygons (whole-authority fills
     # named 'No data available for publication by HE')
     "where": "name <> 'No data available for publication by HE'"},
    {"table": "blt_ons_built_up_areas_dec2024", "theme": "BLT", "window": "MK",
     "colour_by": None, "ctype": "single", "legend_title": "Built up area",
     "colour": "#c887b3"},   # lighter BLT-magenta tint (per owner)
    {"table": "blt_geods_poi_sep2024", "theme": "BLT", "window": "MK",
     # 1,836 raw GeoDS categories reduced to 12 broad classes (approved 2026-06-02)
     "colour_by": (
         "CASE "
         "WHEN main_category IS NULL THEN 'Other' "
         "WHEN main_category ~* 'school|preschool|kindergarten|education|college|university|tutor|nursery' THEN 'Education' "
         "WHEN main_category ~* 'hospital|pharmac|dentist|doctor|medical|health|clinic|optician|physician|naturopath|chiropract|veterinar|nursing|therapy|hospice' THEN 'Health & Medical' "
         "WHEN main_category ~* 'hotel|motel|hostel|accommodation|bed_and_breakfast|guest|lodging|resort|retirement_home|caravan|campground' THEN 'Accommodation' "
         "WHEN main_category ~* 'restaurant|cafe|coffee|pub|bar$|_bar|bakery|fast_food|food|pizza|diner|brewery|bistro|eatery|deli|takeaway|fish_and_chips|brasserie|grill|steakhouse' THEN 'Food & Drink' "
         "WHEN main_category ~* 'beauty|salon|barber|hairdress|nail|spa|tattoo|tanning|pet_groom|massage' THEN 'Beauty & Personal care' "
         "WHEN main_category ~* 'automotive|car_dealer|car_repair|taxi|mechanic|tyre|petrol|fuel|car_wash|parking|shipping|courier|motorcycle|auto_|logistics' THEN 'Automotive & Transport' "
         "WHEN main_category ~* 'contractor|electric|plumb|construction|landscap|engineer|roofing|builder|carpenter|painter|hvac|handyman|industrial_equipment|welding|flooring' THEN 'Trades & Construction' "
         "WHEN main_category ~* 'bank|financ|insurance|account|real_estate|mortgage|investment|currency|loan|credit_union|legal|lawyer|solicitor|attorney|notary|professional_services|business_management|marketing|advertis|consult|it_service|information_technology|software|web_design|recruit|staffing|estate_agent' THEN 'Professional & Financial' "
         "WHEN main_category ~* 'gym|fitness|sport|active_life|stadium|arena|recreation|arts_and_entertainment|cinema|theatre|theater|museum|gallery|night_club|nightlife|bowling|golf|leisure|amusement|park|playground|arts_and_crafts|travel|tour|landmark|historic|monument|attraction' THEN 'Sport, Leisure & Culture' "
         "WHEN main_category ~* 'church|cathedral|mosque|temple|synagogue|worship|religi|community|charity|non_profit|social_service|government|library|post_office|civic|public_service|funeral|cemetery' THEN 'Community & Religion' "
         "WHEN main_category ~* 'shop|store|retail|supermarket|grocery|market|mall|boutique|clothing|furniture|jewel|florist|flower|hardware|convenience|book|electronics|cosmetic|gift' THEN 'Shops & Retail' "
         "ELSE 'Other' END"),
     "ctype": "categorical", "legend_title": "POI category"},
    {"table": "blt_geods_retail_centre_2022", "theme": "BLT", "window": "MK",
     "colour_by": None, "ctype": "single", "legend_title": "Retail centre",
     "colour": "#e1241c"},   # brand red (per owner image), not the BLT magenta
    {"table": "blt_os_functional_sites_oct2024", "theme": "BLT", "window": "MK",
     # 30 (mostly compound) classifications reduced to 3 (approved 2026-06-02)
     # Transport is now explicit; anything unmatched falls to a grey 'Other'
     # bucket rather than being mislabelled Transport.
     "colour_by": (
         "CASE "
         "WHEN classification ILIKE '%Education%' THEN 'Education' "
         "WHEN classification IN ('Medical Care Accommodation','Hospital','Hospice') THEN 'Health & Medical' "
         "WHEN classification ~* 'Airfield|Airport|Helicopter|Heliport|Bus Station|Coach Station|Ferry Terminal|Port|Road User Services' THEN 'Transport' "
         "ELSE 'Other' END"),
     "ctype": "categorical", "legend_title": "Site type"},
    {"table": "blt_os_important_buildings", "theme": "BLT", "window": "MK",
     "colour_by": "building_theme", "ctype": "categorical", "legend_title": "Building theme"},
    {"table": "blt_os_named_places", "theme": "BLT", "window": "MK",
     "colour_by": "classification", "ctype": "categorical", "legend_title": "Named place type"},
    {"table": "com_sportengland_active_places_facilities", "theme": "COM", "window": "MK",
     "colour_by": "facility_type", "ctype": "categorical", "legend_title": "Facility type",
     # 4 well-separated greens (chartreuse / green / bright teal / dark teal)
     "palette": ["#b5d320", "#2e9e3f", "#00a99d", "#0b6157"]},
    {"table": "com_os_green_space_sport_activity_area", "theme": "COM", "window": "MK",
     "colour_by": "attribute", "ctype": "categorical", "legend_title": "Green space type",
     "palette": GREENS},                                        # green->teal ramp (image 1)
    {"table": "edu_dfe_school_may2026", "theme": "EDU", "window": "MK",
     "colour_by": "phase_of_education_name", "ctype": "categorical", "legend_title": "Phase of education"},
    {"table": "hth_ohid_msoa_life_expectancy_2023", "theme": "HTH", "window": "MK",
     "colour_by": "male_life_expectancy", "ctype": "sequential",
     "legend_title": "Male life expectancy (years)"},
    {"table": "mob_os_open_roads_apr2025", "theme": "MOB", "window": "MK",
     "colour_by": "road_classification", "ctype": "categorical", "legend_title": "Road classification",
     "line_weight": 1.3},  # halved from the 2.6 default
    {"table": "utl_nationalgrid_over_head_line", "theme": "UTL", "window": "MK",
     "colour_by": None, "ctype": "single", "legend_title": "Overhead transmission line",
     # ±18.5 km around MK → ~50 lines
     "bbox": (466500, 219500, 503500, 256500)},
    {"table": "hou_hmlandregistry_house_price_paid_jun2026", "theme": "HOU", "window": "MK",
     "colour_by": "price", "ctype": "sequential", "legend_title": "Price paid (£)",
     "label": "concat_ws(', ', street, town_city)", "label_title": "Address"},
]


# hover-name field per layer (table -> (column, alias)); applied if not already set
LABELS = {
    "adm_ons_postcode_centroid_feb2026": ("pcds", "Postcode"),
    "dem_mhclg_lsoa_imd_2025": ("lsoa21nm", "LSOA"),
    "dem_ons_lsoa_accommodation_type_2021": ("lsoa21nm", "LSOA"),
    "ecn_ons_lad_gross_value_added_2023": ("lad24nm", "Local authority"),
    "ecn_voa_lsoa_business_floorspace_2023": ("lsoa21nm", "LSOA"),
    "env_naturalengland_sssi_apr2026": ("name", "SSSI"),
    "env_ons_national_park_may2026": ("name", "National Park"),
    "her_historicengland_listed_building_points_may2026": ("name", "Listed building"),
    "her_historicengland_conservation_areas_jul2025": ("name", "Conservation area"),
    "blt_ons_built_up_areas_dec2024": ("bua24nm", "Built up area"),
    "com_sportengland_active_places_facilities": ("site_name", "Facility"),
    "edu_dfe_school_may2026": ("establishment_name", "School"),
    "hth_ohid_msoa_life_expectancy_2023": ("msoa21nm", "MSOA"),
    "mob_os_open_roads_apr2025": ("name_1", "Road"),
    "utl_nationalgrid_over_head_line": ("route_asse", "Route"),
}
for _s in PILOT:
    if _s["table"] in LABELS and "label" not in _s:
        _s["label"], _s["label_title"] = LABELS[_s["table"]]


# --- full-schema rollout ---------------------------------------------------
def read_layers(cur):
    """Every base table in the schema: theme, geometry type, column names."""
    cur.execute(
        """SELECT c.relname,
                  upper(split_part(c.relname,'_',1)) AS theme,
                  (SELECT type FROM geometry_columns g
                   WHERE g.f_table_schema=%s AND g.f_table_name=c.relname LIMIT 1) AS gtype,
                  c.reltuples::bigint AS est_rows
           FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace
           WHERE n.nspname=%s AND c.relkind='r'
           ORDER BY theme, c.relname""", (SCHEMA, SCHEMA))
    layers = [{"table": r[0], "theme": r[1], "gtype": r[2], "est_rows": r[3]}
              for r in cur.fetchall()]
    for lyr in layers:
        cur.execute("SELECT a.attname FROM pg_attribute a "
                    f"WHERE a.attrelid='{SCHEMA}.{lyr['table']}'::regclass "
                    "AND a.attnum>0 AND NOT a.attisdropped ORDER BY a.attnum")
        lyr["columns"] = [r[0] for r in cur.fetchall()]
    return layers


def humanise_title(table):
    """Legend title for an auto layer: drop the theme prefix and trailing date."""
    toks = table.split("_")[1:]
    if toks and re.fullmatch(r"[a-z]{0,4}\d{4}", toks[-1]):
        toks = toks[:-1]
    text = " ".join(toks)
    text = (text[:1].upper() + text[1:]) if text else table
    return prettify_acronyms(text)


def detect_label(columns):
    """Pick a hover-name column from a layer's columns (None if nothing fits)."""
    cols = set(columns)
    for c in ("name", "name_1"):
        if c in cols:
            return c, "Name"
    for c in columns:                       # ONS name fields: lsoa21nm, lad24nm…
        if c.endswith("nm"):
            return c, "Name"
    for c in ("pcds", "postcode"):
        if c in cols:
            return c, "Postcode"
    for c in columns:
        if c.endswith("name") or c.endswith("_name"):
            return c, "Name"
    return None, "Name"


def pick_window(cur, table, bbox=None):
    """First window (MK → South Downs) with any data; England overview otherwise."""
    for w in ("MK", "south_downs"):
        x0, y0, x1, y1 = WINDOWS[w]
        env = f"ST_MakeEnvelope({x0},{y0},{x1},{y1},27700)"
        cur.execute(f"SELECT 1 FROM {SCHEMA}.{table} "
                    f"WHERE geom && {env} AND ST_Intersects(geom,{env}) LIMIT 1")
        if cur.fetchone():
            return w
    return "england"


def build_specs(cur):
    """Curated pilot specs as overrides; single-colour previews for the rest."""
    curated = {s["table"]: s for s in PILOT}
    specs = []
    for lyr in read_layers(cur):
        if lyr["table"] in curated:
            spec = dict(curated[lyr["table"]])
        else:
            lbl, lbl_title = detect_label(lyr["columns"])
            spec = {"table": lyr["table"], "theme": lyr["theme"],
                    "colour_by": None, "ctype": "single",
                    "legend_title": humanise_title(lyr["table"])}
            if lbl:
                spec["label"], spec["label_title"] = lbl, lbl_title
        spec["gtype"] = lyr["gtype"]
        spec["est_rows"] = lyr.get("est_rows", 0)
        kind = kind_of(lyr["gtype"])
        # DEM explicit colouring plan (owner-approved): apply the first matching
        # DEM_PLAN entry. (LSOA-scale choropleths get a local view below.)
        if lyr["theme"] == "DEM":
            for key, ov in DEM_PLAN.items():
                if key in lyr["table"]:
                    spec.update(ov)
                    break
        # EDU plan: primary/secondary subsets coloured by Ofsted rating; the
        # all-schools layer keeps its PILOT phase colouring (no matching key).
        if lyr["theme"] == "EDU":
            for key, ov in EDU_PLAN.items():
                if key in lyr["table"]:
                    spec.update(ov)
                    break
        # ENV plan: per-layer colour-by (water/woodland/flood/agri/green space/
        # habitats); designation polygons not matched here get the uniform green
        # designation style.
        if lyr["theme"] == "ENV":
            matched = False
            for key, ov in ENV_PLAN.items():
                if key in lyr["table"]:
                    spec.update(ov)
                    matched = True
                    break
            if (not matched and kind == "polygon"
                    and any(d in lyr["table"] for d in ENV_DESIGNATIONS)):
                spec.update(ENV_DESIGNATION_STYLE)
        # HER plan: grade-based layers coloured by listing grade; designation
        # polygons not matched get the uniform dark-plum designation style.
        if lyr["theme"] == "HER":
            matched = False
            for key, ov in HER_PLAN.items():
                if key in lyr["table"]:
                    spec.update(ov)
                    matched = True
                    break
            if (not matched and kind == "polygon"
                    and any(d in lyr["table"] for d in HER_DESIGNATIONS)):
                spec.update(HER_DESIGNATION_STYLE)
        # HOU plan: house price paid (framed on London via LOCAL_VIEWS).
        if lyr["theme"] == "HOU":
            for key, ov in HOU_PLAN.items():
                if key in lyr["table"]:
                    spec.update(ov)
                    break
        # HTH plan: OHID MSOA choropleths + NHS point layers.
        if lyr["theme"] == "HTH":
            for key, ov in HTH_PLAN.items():
                if key in lyr["table"]:
                    spec.update(ov)
                    break
        # MOB plan: road hierarchy (grey, width by class), rail (solid/dashed),
        # cycle / bus, PRoW (Peak District via LOCAL_VIEWS).
        if lyr["theme"] == "MOB":
            for key, ov in MOB_PLAN.items():
                if key in lyr["table"]:
                    spec.update(ov)
                    break
        # ECN plan: overrides for the headline layers; employment layers get
        # total employment = sum of their SIC industry count columns.
        if lyr["theme"] == "ECN":
            for key, ov in ECN_PLAN.items():
                if key in lyr["table"]:
                    spec.update(ov)
                    break
            if "business_register_employment" in lyr["table"]:
                ind = [c for c in lyr["columns"]
                       if c not in ("fid", "id", "geom", "area_ha")
                       and not re.search(r"(cd|nm)$", c)
                       and not c.startswith("data_") and "boundary" not in c]
                spec["colour_by"] = "(" + " + ".join(f'COALESCE("{c}",0)' for c in ind) + ")"
                spec["ctype"], spec["ramp"] = "sequential", RAMP_BLUEGREEN
                spec["scale"] = "quantile"     # employment is skewed → equal-count classes
                spec["legend_title"] = "Total employment"
        # Default extent: full England, tuned per layer/theme as the styling is
        # approved (the previews are static snapshots, so the frame is chosen for
        # readability — not an interactive viewport).
        spec["window"] = "england"
        spec.pop("bbox", None)
        # ADM boundary polygons: transparent fill + theme-colour outline. LAD /
        # ward / LSOA boundaries at 1.95 (+50%); MSOA lighter (-50% => 0.98) as
        # its denser mesh reads better thin. Fine/dense grains (LSOA, Output Area,
        # ward) and postcode points use a local extent; nationally they collapse
        # to a solid block.
        if lyr["theme"] == "ADM" and kind == "polygon":
            spec["fill_opacity"] = 0.0
            spec["outline"] = THEME_COLOURS.get("ADM", "#e9511d")
            spec["outline_weight"] = (0.49 if "msoa_boundary" in lyr["table"]
                                      else 1.95)
        # Local cover-the-frame view (fixed MK centre + zoom, no fit_bounds) for
        # fine grains / detail layers that don't read at national extent.
        for key, (center, zoom) in LOCAL_VIEWS.items():
            if key in lyr["table"]:
                spec["window"] = "MK"      # local simplify / precision / caps
                spec["view"] = {"center_bng": center, "zoom": zoom}
                break
        # Fine-grained choropleths (LSOA scale, ~35k units) are illegible as a
        # static national PNG — units are sub-pixel. Show them at a Birmingham
        # local cover view so the colour-by reads; the national pattern is the
        # Dashboard's interactive job. Coarse grains (LAD/MSOA) stay national.
        if (kind == "polygon" and spec.get("colour_by")
                and spec["est_rows"] > 20000 and not spec.get("view")):
            spec["window"] = "MK"
            spec["view"] = {"center_bng": BHAM_CENTRE_BNG, "zoom": 11}
        specs.append(spec)
    return specs


# --- static snapshot + shared styles contract -----------------------------
# Shared per-layer style file: this script WRITES it, the Dashboard READS it.
# Neutral location (sibling of the tileserver folder), overridable for testing.
STYLES_JSON = Path(os.environ.get(
    "UK_BASELINE_STYLES",
    r"P:\0_Practice\10_Data management resources\XX_Working\uk_baseline_styles.json"))


def new_driver(size=FRAME):
    """Headless Chrome for screenshotting the folium HTML to PNG."""
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    opts = Options()
    for a in ("--headless=new", f"--window-size={size[0]},{size[1]}",
              "--hide-scrollbars", "--force-device-scale-factor=1", "--no-sandbox"):
        opts.add_argument(a)
    return webdriver.Chrome(options=opts)


def snapshot(driver, table, delay=4.0):
    """Save a static PNG of the rendered map (basemap tiles need a moment), then
    drop the intermediate HTML — the catalogue ships only the PNG."""
    import time
    html = OUT / f"{table}.html"
    driver.get(html.resolve().as_uri())
    time.sleep(delay)
    driver.save_screenshot(str(OUT / f"{table}.png"))
    html.unlink(missing_ok=True)


def style_entry(spec, comp):
    """Build the shared-contract style dict for one layer from its rendered style."""
    kind = kind_of(spec.get("gtype"))
    e = {"colour_by": spec.get("colour_by"), "ctype": spec["ctype"],
         "legend_title": prettify_acronyms(spec["legend_title"])}
    if spec["ctype"] == "categorical":
        # exact value->colour map the preview used (incl. the grey 'Other')
        e["categories"] = [{"value": str(v), "colour": c}
                           for v, c in comp["cat_map"].items()]
    elif spec["ctype"] == "sequential":
        e["ramp"] = spec.get("ramp") or [_tint(comp["base"]), comp["base"]]
        e["domain"] = [comp["vmin"], comp["vmax"]]
        if spec.get("scale") == "quantile" and comp.get("breaks"):
            e["scale"], e["breaks"] = "quantile", comp["breaks"]
    else:                                       # single
        e["colour"] = spec.get("outline") if spec.get("fill_opacity") == 0.0 \
            else comp["base"]
    if kind == "polygon":
        e["fill_opacity"] = spec.get("fill_opacity", 0.6)
        e["line_weight"] = spec.get("outline_weight", 1.0)
    elif kind == "line":
        e["line_weight"] = spec.get("line_weight", 2.6)
    else:                                       # point
        e["point_radius"] = 4
    e["extent"] = spec.get("extent")            # 4326 [w,s,e,n]; None = full layer
    if spec.get("note"):                        # layer-info caveat for the Dashboard
        e["note"] = spec["note"]
    return e


def write_styles(entries):
    """Merge style entries into the shared JSON, preserving its other content."""
    if STYLES_JSON.exists():
        data = json.loads(STYLES_JSON.read_text(encoding="utf-8"))
    else:
        data = {"version": 1, "layers": {}}
    data.setdefault("layers", {}).update(entries)
    STYLES_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False),
                           encoding="utf-8")


def main() -> None:
    import sys
    args = sys.argv[1:]                                  # themes (ADM) or table substrings
    themes, subs = {a.upper() for a in args}, [a.lower() for a in args]

    def keep(s):
        return (not args) or s["theme"] in themes or any(x in s["table"] for x in subs)

    with psycopg.connect(conninfo()) as conn, conn.cursor() as cur:
        specs = [s for s in build_specs(cur) if keep(s)]
        log.info("Rendering %d layer maps to %s%s", len(specs), OUT,
                 f" ({', '.join(args)})" if args else "")
        try:
            driver = new_driver()
        except Exception as exc:                 # render HTML even if no browser
            driver = None
            log.warning("No Chrome driver (%s) — HTML only, no PNG snapshots", exc)
        ok, entries = 0, {}
        for spec in specs:
            try:
                comp = render(cur, spec)
                if comp:
                    ok += 1
                    if driver:
                        snapshot(driver, spec["table"])
                    entries[spec["table"]] = style_entry(spec, comp)
            except Exception as exc:             # keep going; report the failure
                log.warning("  %s — FAILED: %s", spec["table"], exc)
        if driver:
            driver.quit()
    if entries:
        write_styles(entries)
        log.info("Wrote %d style entries to %s", len(entries), STYLES_JSON)
    log.info("Done: %d/%d rendered.", ok, len(specs))


if __name__ == "__main__":
    main()
