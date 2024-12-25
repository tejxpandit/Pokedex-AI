# Project   : Pokedex AI
# File      : Preprocessing YAML Pokemon Data
# Author    : Tej Pandit
# Date      : Nov 2024

import os
import pickle
import yaml

def extractYAML(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print(f"Error reading YAML file: {e}")
            return None

# Database Parameters
src_yaml_folder = "./data/pokemon/yaml"
dst_database_folder = "./data/pokemon"
database_name = "pokemon.db"

# Convert YAML Files into Unified Python Dict
pokemon = {}
for filename in os.listdir(src_yaml_folder):
    if filename.endswith(".yaml") or filename.endswith(".yml"):
        data_type = filename.split(".")[0]
        # print(data_type)
        file_path = os.path.join(src_yaml_folder, filename)
        data = extractYAML(file_path)
        if data:
            pokemon[data_type] = data

# Save as Pickle Dict Object (Database)
file_path = os.path.join(dst_database_folder, database_name)
with open(file_path, 'wb') as file:
    pickle.dump(pokemon, file)

# Load Pickle Dict Object (Database)
file_path = os.path.join(dst_database_folder, database_name)
with open(file_path, 'rb') as file:
    pokemonDB = pickle.load(file)

# print(pokemonDB)