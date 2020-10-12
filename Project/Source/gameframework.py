import time
import imageloader
from pico2d import *

class Game:
    def __init__(self):
        self.running = False
        self.pageStack = None
        self.frameInterval = 0.01
        self.deltaTime = 0.0
        self.imageLoader = imageloader.ImageLoader()

    def quit(self):
        self.running = False

    def run(self, page):
        self.running = True

        self.pageStack = [page]

        open_canvas()

        page.initialize()

        beforeTime = time.time()

        while self.running:
            # set delta time
            nowTime = time.time()
            self.deltaTime = nowTime - beforeTime
            beforeTime = nowTime;

            # Game input (event handling)
            input = get_events()
            for key in input:
                self.pageStack[-1].processInput(key)

            # Game update (logic)
            self.pageStack[-1].update()

            # Game draw (rendering)
            clear_canvas()
            self.pageStack[-1].draw()
            update_canvas()

            delay(self.frameInterval)

        while len(self.pageStack) > 0:
            del self.pageStack[-1]

        close_canvas()

    def changePage(self, page):
        if len(self.pageStack) > 0:
            del self.pageStack[-1]
        self.pageStack.append(page)
        page.initialize()

    def pushPage(self, page):
        self.pageStack.append(page)
        page.initialize()

    def popPage(self):
        if len(self.pageStack) == 1:
            quit()
        elif len(self.pageStack) > 1:
            del self.pageStack[-1]
            self.pageStack.pop()
