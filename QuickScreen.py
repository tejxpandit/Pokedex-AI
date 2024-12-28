# Project : Quick Screen Grabber
# Author  : Tej Pandit
# Date    : Nov 2024

import dxcam
import pygetwindow as pgw

class QuickScreen:
    def __init__(self):
        self.cam = None
        self.renderer = 0
        self.monitor = 0
        self.bbox = (0,0,100,100) # left, top, right, bottom
        self.win = None

    def setVideoRenderer(self, id):
        self.renderer = id

