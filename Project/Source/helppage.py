from pico2d import *
from GFW import gameframework
import selecter
from ext_pico2d import *


class HelpPage:
    def __init__(self, game):
        self.mGame = game

    def __del__(self):
        del self.mBKImage
        del self.mSelecter

    def initialize(self):
        self.load()

    def load(self):
        self.mBKImage = self.mGame.imageLoader.load(self.mGame.imageDir + 'help.png')
        self.mSelecter = selecter.Selecter(self.mGame, 0, 570, 40)
        self.font = self.mGame.fontLoader.load(self.mGame.fontDir + "ConsolaMalgun.ttf", 40)

    def update(self):
        pass

    def draw(self):
        self.mBKImage.draw(gameframework.canvasWidth / 2, gameframework.canvasHeight / 2)
        self.mSelecter.draw()
        draw_centered_text(self.font, "이동", get_canvas_width()//2, get_canvas_height()//2, 100, 0);


    def processInput(self, key):
        if key.type == SDL_QUIT:
            self.mGame.quit()
        elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_SPACE):
            self.mGame.isPause = False
            if self.mSelecter.mSelect == 0:
                self.mGame.popPage()
            elif self.mSelecter.mSelect == 1:
                self.mGame.popPage()

        self.mSelecter.processInput(key)

def create(game):
    page = HelpPage(game)
    return page

if __name__ == '__main__':
    gameframework.run_main()