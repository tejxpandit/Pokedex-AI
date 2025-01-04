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
