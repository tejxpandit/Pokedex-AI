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
        
    def setWindow(self, keywords):
        self.win = self.findWindow(keywords)
        if self.win:
            self.bbox = (self.win.left, self.win.top, self.win.left+self.win.width, self.win.top+self.win.height)

    def initCapture(self):
        self.cam = dxcam.create(device_idx=self.renderer, output_idx=self.monitor, region=self.bbox)

    def getFrame(self):
        return self.cam.grab()
    
    def closeCapture(self):
        try:
            self.cam.release()
        except:
            pass
        # del self.cam

# TEST EXAMPLE
if __name__ == '__main__':
    QS = QuickScreen()
    # SG.findWindow("Pokemon New Emerald")
    QS.setWindow("Pokemon New Emerald")
    QS.initCapture()
    frame = QS.getFrame()
    x, y, width, height = 50, 150, 350, 100

    from PIL import Image
    Image.fromarray(frame[y:y+height, x:x+width]).show()