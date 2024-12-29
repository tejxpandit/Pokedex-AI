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

    def setMonitor(self, id):
        self.monitor = id

    def findWindow(self, keywords):
        keyword_list = keywords.split()
        win_titles = pgw.getAllTitles()
        for title in win_titles:
            if all(keyword in title for keyword in keyword_list):
                # print(title)
                win = pgw.getWindowsWithTitle(title)[0]
                return win
        print("No Window Found with Keywords : \"" + keywords + "\"")
        return None
