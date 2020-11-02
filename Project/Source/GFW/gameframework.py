import time
from pico2d import *
from GFW import imageloader

canvasWidth = 800
canvasHeight = 650

class Game:
    def __init__(self):
        self.running = False
        self.pageStack = None
        self.frameInterval = 0.01
        self.deltaTime = 0.0
        self.imageDir = 'Asset/Image/'
        self.imageLoader = imageloader.ImageLoader()

    def quit(self):
        self.running = False

    def run(self, page):
        self.running = True

        self.pageStack = [page]

        open_canvas(canvasWidth, canvasHeight)

        page.initialize()

        beforeTime = time.time()

        while self.running:
            # set delta time
            nowTime = time.time()
            self.deltaTime = nowTime - beforeTime
            beforeTime = nowTime;

            # Game input (event handling)
            self.processInput()

            # Game update (logic)
            self.update()

            # Game draw (rendering)
            self.draw()

            delay(self.frameInterval)

        while len(self.pageStack) > 0:
            del self.pageStack[-1]

        close_canvas()

    def processInput(self):
        input = get_events()
        for key in input:
            self.pageStack[-1].processInput(key)

    def update(self):
        self.pageStack[-1].update()

    def draw(self):
        clear_canvas()
        self.pageStack[-1].draw()
        update_canvas()

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

def run_main():
    import sys
    main_module = sys.modules['__main__']
    game = Game()
    page = main_module.create(game)
    game.run(page)
