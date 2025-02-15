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

    def pokemonFilterName(self, text):
        text = str(text)
        text = self.onlyAlphabets(text)
        words = text.split()
        name = words[0]
        return name

    def getWeaknesses(self, name):
        name = name.lower()
        types = self.getTypes(name)
        for t in types:
            # TODO : Find "weak-to" in dict and add elements of list to "self.weaknesses"
            pass

    def getTypes(self, name):
        if name in self.db["pokemon-forms"]:
            typeA = self.db["pokemon-forms"][name]["type1"]
            typeB = self.db["pokemon-forms"][name]["type2"]
            return [typeA, typeB]
        else:
            return []

    def getData(self):
        try:
            data = self.buffer.get()
            # data = self.buffer.get_nowait()
        except:
            data = None
        return data

    def endPokedex(self):
        self.pkdex_state.clear()
        self.dex_thread.join()
        self.stream_state.clear()
        self.dex_stream.join()

def pokemonNameExtract(enabled, buffer, interval):
        qs = QuickScreen()
        qs.setWindow("Pokemon New Emerald")
        qs.initCapture()
        tess.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

        # Opponent Pokemon Name Crop
        x, y, width, height = 50, 150, 350, 100

        while enabled.is_set():
            frame = qs.getFrame()
            if frame is not None:
                text = tess.image_to_string(frame[y:y+height, x:x+width])
                try:
                    buffer.put_nowait(text)
                except queue.Full:
                    try:
                        buffer.get_nowait()
                        buffer.put_nowait(text)
                    except queue.Empty:
                        pass
            else:
                return None
            time.sleep(interval)

        qs.closeCapture()
    
# # TEST EXAMPLE
# if __name__ == '__main__':
#     SP = SimplePokedex()

#     # SP.pokemonNameExtractInit()
#     # print(SP.pokemonNameExtract())
#     # SP.qs.closeCapture()

#     SP.startPokedexProcess()
#     SP.startPokedexThread()
#     time.sleep(6)
#     SP.endPokedex()

