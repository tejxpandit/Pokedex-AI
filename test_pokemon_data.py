# Project   : Pokedex AI
# File      : Testing Pokemon Database
# Author    : Tej Pandit
# Date      : Nov 2024

import os
import pickle
import yaml

# Database Parameters
src_yaml_folder = "./data/pokemon/yaml"
dst_database_folder = "./data/pokemon"
database_name = "pokemon.db"

# Load Pickle Dict Object (Database)
file_path = os.path.join(dst_database_folder, database_name)
with open(file_path, 'rb') as file:
    pokemon = pickle.load(file)

# for key, value in pokemon.items() :
#     print(key)

print(pokemon["pokemon-forms"]["bulbasaur"]["type1"])