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

