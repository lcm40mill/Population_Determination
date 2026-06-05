import math
import Constants
from soils import *

#set up all functions to isolate one zone type, then create a list of zone types present and iterate functions through that list

def total_arable_land_zone(land_zone, river_zone, coast_zone):
    return land_zone + river_zone + coast_zone

# Calculates total arable land supply along river path, multiply land range by 2 to account for both sides of the river 
def find_river_zone(river_navigable_length):
    return river_navigable_length * 2 * Constants.LAND_SUPPLY_RANGE * Constants.ACRES_PER_SQUARE_MILE

# Not sure if this maths the math I want
def find_coast_zone(coastline):
    return coastline * Constants.LAND_SUPPLY_RANGE * Constants.ACRES_PER_SQUARE_MILE

# Determines if urban diet can be supplemented with aquatic resources, requires fish/seafood and salt for curing
def find_urban_grain_req_mod(fish, salt):
    urban_grain_req_mod = 1
    if fish and salt:
        urban_grain_req_mod = Constants.FISH_AND_SALT_MODIFIER
    return urban_grain_req_mod

# Determines the rough percentage of arable land in a given zone type,
# the flatter and more naturally irrigated the more land can be used for agriculture    
def find_zone_arable_percentage(zone_type, arable_land, tech = []):
    percent_arable = Soil_Dict[zone_type]["arable"]
    if zone_type == 3 and "heavy plow" in tech:
        percent_arable += Tech_Dict["heavy plow"]["arable"]
    if zone_type == 5 and "terracing" in tech:
        percent_arable += Tech_Dict["terracing"]["arable"]
    return arable_land * percent_arable

def calculate_farming_family_population(agrc_footprint, plot_size):
    return math.floor(agrc_footprint / plot_size)

def percentage_of_population_are_farming(tech = []):
    farming_population_percentage = Constants.FARMER_POPULATION_PERCENTAGE
    if "automills" in tech:
        farming_population_percentage = Tech_Dict["automills"]["farmers"]
    
    return farming_population_percentage

# There is a nicer way to do this for inputs but works for now as long as input is recognized
def crop_rotation_system(system = []):
    return Field_Sys_Dict[system]

def find_yield__mod(zone_type, tech = []):
    zone_mod = Soil_Dict[zone_type]["Yield"]
    tech_yield_mod = 0
    
    if zone_type == 4:
        if "irrigation" in tech or "better crops" in tech:
            zone_mod = Soil_Dict[2]["Yield"]
    if zone_type == 5 and "better crops" in tech:
        zone_mod = Soil_Dict[2]["Yield"]
    if "livestock" in tech:
        tech_yield_mod += 1

    yield_mod = zone_mod + tech_yield_mod

    return yield_mod

def gross_grain_harvest(farm_plot_count, field_size, field_system, yield_modifier):
    gross_harvest = farm_plot_count * field_size * field_system * Constants.AVERAGE_GRAIN_PLANTED_PER_ACRE * yield_modifier
    return gross_harvest

def determine_capitol_taxes(gross_harvest, capitol_tax):
    return gross_harvest * (capitol_tax)

def determine_religious_tithe(gross_harvest, religious_tithe):
    return gross_harvest * (religious_tithe)

def determine_toll(toll_rate, grain_cargo):
    return grain_cargo * toll_rate

def total_tolls(grain_cargo, tolls = []):
    total_toll = 0
    for t in tolls:
        total_toll += determine_toll(Grain_Toll_Dict[t]["toll"], grain_cargo)
    return total_toll

def grain_spillage_from_travel(grain_cargo, land_miles, travel_river = False, travel_coastal = False):
    spill_rate = land_miles * Constants.GRAIN_OVERLAND_SPILLAGE_PER_MILE
    if travel_coastal:
        spill_rate += Constants.GRAIN_OPEN_SEA_SPILLAGE
    if travel_river:
        spill_rate += Constants.GRAIN_WATER_HANDLING_SPILLAGE
    return grain_cargo * spill_rate

def city_is_final_destination(grain_cargo, final = False):
    if final:
        grain_cargo *= (1 - Constants.GRANARY_RESERVE)
    return grain_cargo