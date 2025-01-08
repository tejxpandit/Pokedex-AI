# Project   : Pokedex AI
# File      : Simple Pokedex
# Author    : Tej Pandit
# Date      : Nov 2024

import time
import os
import re
import pickle
import threading
import queue
import multiprocessing as mp

import dearpygui.dearpygui as dpg
import pytesseract as tess

from QuickScreen import QuickScreen

class SimplePokedex:
    def __init__(self):
        self.db = None
        self.dex_stream = None
        self.dex_thread = None
        self.pkdex_state = threading.Event()
        self.pkdex_state.set()
        self.stream_state = mp.Event()
        self.stream_state.set()
        self.buffer = mp.Queue()
        self.qs = None
        self.polling_interval = 3

        self.weaknesses = []
        
        self.dst_database_folder = "./data/pokemon"
        self.database_name = "pokemon.db"
        self.loadPokedexDatabase()

    def loadPokedexDatabase(self):
        # Load Pickle Dict Object (Database)
        file_path = os.path.join(self.dst_database_folder, self.database_name)
        with open(file_path, 'rb') as file:
            self.db = pickle.load(file)
