import fbpy.fb as fb
import time

class Clock(object):

    def __init__(self):
        self.win = fb.Surface()
        self.cwin = fb.Surface((10,10),(600,100))
        self.win.clear()
        self.win.printxy((0.5,0.9),"fb python iface by Noisegate 2014",1)
        self.cwin.clear()
        self.win.update()
        self.cwin.update()

    def start(self):
        while True:
            self.cwin.clear()
            self.cwin.printxy((0,0),time.ctime(),2)
            self.cwin.update()
            time.sleep(1)

if __name__ == "__main__":
    myclock = Clock()
    myclock.start()

