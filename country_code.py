from pygal_maps_world.i18n import COUNTRIES
from pygal_maps_world.i18n import ASIA, AFRICA, ANTARTICA,NORTH_AMERICA, SOUTH_AMERICA, OCEANIA, EUROPE

def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if country_name in name:
            return code

continents = {
    "Asia": ASIA,
    "Africa": AFRICA,
    "Antarctica": ANTARTICA,
    "Oceania": OCEANIA,
    "Europe" : EUROPE,
    "North_America": NORTH_AMERICA,
    "South_America": SOUTH_AMERICA,
}

def get_continent(country_code):
    for continent_name, countries in continents.items():
        if country_code in countries:
            return continent_name
        else:
            continue

