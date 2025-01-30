# File      : Data Stream Class for Multiprocessing in Python
# Author    : Tej Pandit
# Date      : Oct 2024

import time
import queue
import multiprocessing as mp

class DataStream:
    def __init__(self):
        self.func = self.data_loop
        self.initfunc = self.idle
        self.datafunc = self.idle
        self.enabled = mp.Event()
        self.buffer = mp.Queue()
        self.process = None
        self.time_interval = 1
        self.logging = False

