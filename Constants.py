import math

# Percentage of population required to feed total population
FARMER_POPULATION_PERCENTAGE = 0.9 
AVERAGE_FARMER_FAMILY_SIZE = 5

# Buckets of Grain per Acre Planted
AVERAGE_GRAIN_PLANTED_PER_ACRE = 2.4 
GRAIN_BUCKET_QUANTITY_LBS = 55

# Percentage of grain harvest that will spoil or be contaminated, based on harvest after taxes
GRAIN_SPOILAGE_PER_HARVEST = 0.2

ACRES_PER_SQUARE_MILE = 640

# Number of grain buckets required
GRAIN_CONSUMPTION_PER_NON_FARMER = 10
GRAIN_CONSUMPTION_PER_FARMING_FAMILY = 40 

# Access to fisheries and salt lowers grain requirements to support population
FISH_AND_SALT_MODIFIER = 0.7 

# Measured in miles from city or town
LAND_SUPPLY_RANGE = 15 
LAND_SUPPLY_ZONE = LAND_SUPPLY_RANGE**2 * math.pi * ACRES_PER_SQUARE_MILE


# Granary reserve is a percentage cut the final receiving city takes from incoming grain shipments
# prior to being sold on open market.  The reserve helps the city prepare for natural disasters, famine, or conflict.
GRANARY_RESERVE = 0.15

# Logistics Spillage
# OVERLAND accounts for loading/unloading and spills during travel
GRAIN_OVERLAND_SPILLAGE_PER_MILE = 0.002
# WATER HANDLING spillage mainly occurs during loading and unloading with minimum recovery availble,
# this APPLIES EACH time grain is loaded in one river/coastal city and unloaded in another city
GRAIN_WATER_HANDLING_SPILLAGE = 0.04
# GRAIN OPEN SEA spiilage accounts for grain lost to storms, scuttling. and piracy
GRAIN_OPEN_SEA_SPILLAGE = 0.06
