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

    def idle(self):
        time.sleep(1)

    def setInitFunction(self, func):
        self.initfunc = func

    def setDataFunction(self, func):
        self.datafunc = func
    
    def setBufferFunction(self, func):
        self.func = func

    def setBuffersize(self, buffer_size):
        self.buffer = mp.Queue(maxsize=buffer_size)

    def setTimeInterval(self, time_interval):
        self.time_interval = time_interval

    def enableLogging(self):
        self.logging = True

    def disableLogging(self):
        self.logging = False

    def begin(self):
        self.enabled.set()
        self.process = mp.Process(target=self.func, args=(self.enabled, self.buffer, self.initfunc, self.datafunc, self.time_interval, self.logging, ))
        self.process.start()

    def pause(self):
        self.enabled.clear()

    def unpause(self):
        self.enabled.set()
    
    def end(self):
        self.enabled.clear()
        self.process.terminate()
        self.process.join()

    def getData(self):
        try:
            data = self.buffer.get_nowait()
        except:
            data = None
        return data

    def data_loop(self, enabled, buffer, initfunc, datafunc, time_interval, logging):
        initfunc()
        while True:
            if enabled.is_set():
                data = datafunc()
