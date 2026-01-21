import pygal

from pygal_maps_world.maps import World
import json
from country_code import get_country_code, get_continent

worldmap = World()

file = "country-by-population.json"
worldmap.title = "Countries Population"

continents = {
        "Asia" : {},
        "Africa" : {},
        "Antarctica" : {},
        "Oceania" : {},
        "Europe" : {},
        "North_America" : {},
        "South_America" : {}        
    }


with open(file) as jsonF:
    data = json.load(jsonF)

for dict_data in data:
    country_name = dict_data["country"]
    population = int(dict_data["population"])
    country_code = get_country_code(country_name)
    if not country_code:
        continue

    continent = get_continent(country_code)
    if not continent:
        continue

    continents[continent][country_code] = population

for continent, data in continents.items():
    worldmap.add(continent, data)

worldmap.render_to_file("Population.svg")