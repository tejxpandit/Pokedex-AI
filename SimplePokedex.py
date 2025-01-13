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

    def pokedexApp(self):
        dpg.add_window(label="Pokedex", tag="pokedex_window")
        dpg.add_text("", label="Pokemon Name : ", tag="pokemon_name", parent="pokedex_window", show_label=True)
        dpg.add_text("", label="Type A : ", tag="pokemon_type1", parent="pokedex_window", show_label=True)
        dpg.add_text("", label="Type B : ", tag="pokemon_type2", parent="pokedex_window", show_label=True)
        dpg.add_text("Weaknesses :", parent="pokedex_window")
        dpg.add_listbox(self.weaknesses, parent="pokedex_window", tag="pokemon_weaknesses")
    
    def startPokedexProcess(self):
        self.dex_stream = mp.Process(target=pokemonNameExtract, args=(self.stream_state, self.buffer, self.polling_interval, ))
        self.dex_stream.start()

    def startPokedexThread(self):
        self.dex_thread = threading.Thread(target=self.pokedexThread, args=(self.pkdex_state,))
        self.dex_thread.start()

    def pokedexThread(self, pkdex_state):
        while pkdex_state.is_set():
            text = self.getData()
            if text is not None:
                try:
                    name = self.pokemonFilterName(text)
                except:
                    name = ""
                dpg.set_value("pokemon_name", str(name))
                print(name)
            time.sleep(1)
    
    def onlyAlphabets(self, text):
        return re.sub(r'[^a-zA-Z\s]', '', text)
