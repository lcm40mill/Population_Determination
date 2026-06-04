import math
import Constants
from soils import *
from arable_supply import *

# TO DO List
#   [/] == in progress
#   [x] == base function complete
#
# [x] Calculate Population and population dispersion (farmers vs urban/non-farmers)
# [x] Calculate expected gross grain harvest
# [x] Apply urban population support if population center has fish and salt
# [x] Apply tech modifiers for yield, arable land usage, and population dispersion
# [] Calculate Grain Surplus
#   [] Calculate Taxes owed on grain harvest
#       [x] Gross Taxes: (owed on the total harvest)
#           [x] Lordly Tax
#           [x] Religious Tithes
#       [] Net Taxes: (owed on whats left after Gross Taxes)
#           [/] Logistic Taxes (tolls)
#           [x] Spoilage (Not really a tax but does effect net grain supply)
#   [] Calculate grain losses:
#       [] Logistics Losses (spillage, contamination, etc...)
#       [] Next year's seed bank
#       [] Subsistence (a family needs to eat)
#   [] Total Grain surplus = Net Grain Surplus + Percentage of Lordly Tax that does not get used (~20%)
# [] Determine max urban population based off of grain surplus
#
# [] Future thoughts - Price prediction in a coinage economy:
#   [] Cost of grain purchase
#   [] Cost of grain labor
#   [] Cost of grain logistics
# stuff and things



def main():
    #Does not account for multiple zone typings, not sure if that is relevant maybe for extended river runs into an interior plains
    
    #These are going to be converted to user inputs at a later date
    river_navigable_length_upstream = 15
    coastline = 0
    zone = 2
    has_fishery = False
    has_salt = False
    field_system = "2 Fields"
    tech = ["heavy plow", "terracing", "livestock", "irrigation", "automills"]
    cap_tax = 0.2
    religious_tithe = .1

    arable_river_land = find_river_zone(river_navigable_length_upstream)
    arable_coastal_land = find_coast_zone(coastline)
    total_arable_land = total_arable_land_zone(Constants.LAND_SUPPLY_ZONE, arable_river_land, arable_coastal_land)
    useable_arable_land = round(find_zone_arable_percentage(zone, total_arable_land, tech), 2)


    urban_grain_req_mod = find_urban_grain_req_mod(has_fishery, has_salt)
    yield_mod = find_yield__mod(zone, tech)
    

    farming_families = calculate_farming_family_population(useable_arable_land, Soil_Dict[zone]["Plot Size"])
    rural_population = farming_families * Constants.AVERAGE_FARMER_FAMILY_SIZE

    max_population = rural_population // percentage_of_population_are_farming(tech)
    max_urban_population = (max_population - rural_population)  // urban_grain_req_mod

    gross_harvest = gross_grain_harvest(farming_families, Soil_Dict[zone]["Plot Size"], Field_Sys_Dict[field_system], yield_mod)
    harvest_capitol_taxes = math.floor(determine_capitol_taxes(gross_harvest, cap_tax))
    harvest_religious_tithe = math.floor(determine_religious_tithe(gross_harvest, religious_tithe))
    harvest_after_taxes = gross_harvest - harvest_capitol_taxes - harvest_religious_tithe
    spoilage = harvest_after_taxes * Constants.GRAIN_SPOILAGE_PER_HARVEST
    harvest_after_spoilage = harvest_after_taxes - spoilage



    print(f'Land utilized for agriculture is {useable_arable_land:,} acres.')
    print(f'The typical plot size in the current area is: {Soil_Dict[zone]["Plot Size"]} acres.')
    print(f'The yield modifier for grain harvest is {yield_mod}.')
    print(f'The number of farming families in the area is {farming_families:,} families, the total rural population is {rural_population:,} people.')
    print(f'The maximum urban and non-farmer population of this city is {max_urban_population:,} people')
    print(f'The gross harvest this city should expect is {gross_harvest:,} buckets of grain.')
    print(f'Gross Harvest after taxes is {harvest_after_taxes:,} buckets of grain.')
    print(f'Grain buckets left after spoilage is {harvest_after_spoilage:,}.')


main()