# Yield is a multiplier applied to grain production, Plot Size is measured in acres


Soil_Dict = {
    1: {"Type": "Floodplains", "Yield": 8, "Plot Size": 15, "arable": 0.8},
    2: {"Type": "Lowlands", "Yield": 4, "Plot Size": 30, "arable": 0.6},
    3: {"Type": "Rolling Hills", "Yield": 3, "Plot Size": 30, "arable": 0.4},
    4: {"Type": "Uplands", "Yield": 2, "Plot Size": 30, "arable": 0.20},
    5: {"Type": "Mountains", "Yield": 2, "Plot Size": 30, "arable": 0.05}
}

Tech_Dict = {
    "livestock": {"Description": "Regenerates soil quality via manure spreading", "Yield": 1},
    "irrigation": {"Description": "Irrigation techniques allow for draught protection in arid and shrublands", "Yield": 4},
    "heavy plow": {"Description": "Heavy plows break clay in midland soils allowing for more arable land", "arable": 0.3},
    "terracing": {"Description": "Tremendous labor has resulted in terraced plots allowing for more arable land in mountainous regions", "arable": 0.25},
    "automills": {"Description": "Through clever engineering mills are now using the power of wind or water to reduce human workload", "farmers": 0.85},
    "better crops": {"Description": "Hardier crops have been discovered that are less reliant on good soil and weather, such as potatos and maize", "Yield": 4}
}

Field_Sys_Dict = {
    "2 Fields": 0.50,
    "3 Fields": 0.67,
    "Floodplains": 1
}

Grain_Toll_Dict = {
    1: {"type": "maintained road", "toll": 0.01},
    2: {"type": "small bridge", "toll": 0.02},
    3: {"type": "guarded road", "toll": 0.04},
    4: {"type": "major river crossing", "toll": 0.03},
    5: {"type": "polictical", "toll": 0.05}
}