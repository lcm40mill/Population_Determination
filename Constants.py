import math

# Percentage of population required to feed total population
FARMER_POPULATION_PERCENTAGE = 0.9 
AVERAGE_FARMER_FAMILY_SIZE = 5

# Buckets of Grain per Acre Planted
AVERAGE_GRAIN_PLANTED_PER_ACRE = 2.4 
GRAIN_BUCKET_QUANTITY_LBS = 55

ACRES_PER_SQUARE_MILE = 640

# Number of grain buckets required
GRAIN_CONSUMPTION_PER_NON_FARMER = 10
GRAIN_CONSUMPTION_PER_FARMING_FAMILY = 40 

# Access to fisheries and salt lowers grain requirements to support population
FISH_AND_SALT_MODIFIER = 0.7 

# Measured in miles from city or town
LAND_SUPPLY_RANGE = 15 
LAND_SUPPLY_ZONE = LAND_SUPPLY_RANGE**2 * math.pi * ACRES_PER_SQUARE_MILE