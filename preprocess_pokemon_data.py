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
