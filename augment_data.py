# Project   : Pokedex AI
# File      : Augmenting Pokemon Database
# Author    : Tej Pandit
# Date      : Nov 2024

import os
import pickle

# Database Parameters
src_yaml_folder = "./data/pokemon/yaml"
dst_database_folder = "./data/pokemon"
database_name = "pokemon.db"

# Load Pickle Dict Object (Database)
file_path = os.path.join(dst_database_folder, database_name)
with open(file_path, 'rb') as file:
    pokemon = pickle.load(file)

# Augment Database
print(pokemon["pokemon-forms"]["bulbasaur"]["type1"])
# TODO : Make "weaknesses" dict of all "type-chart" keys as keys, iterate through all super-effectives of all types and append them to the SET of values for each key
# TODO : Add "weaknesses" to database under pokemon["type-chart"][type]["weak-to"]

# Save as Augmented Database
file_path = os.path.join(dst_database_folder, database_name)
with open(file_path, 'wb') as file:
    pickle.dump(pokemon, file)