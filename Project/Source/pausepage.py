from pico2d import *
import gameframework
import selecter


class PausePage:
    def __init__(self, game):
        self.mGame = game

    def __del__(self):
        del self.mBKImage
        del self.mSelecter

    def initialize(self):
        self.load()

    def load(self):
        self.mBKImage = self.mGame.imageLoader.load(self.mGame.imageDir + 'pause.png')
        self.mSelecter = selecter.Selecter(self.mGame, 1, 375)

    def update(self):
        pass

    def draw(self):
        self.mBKImage.draw(400, 350)
        self.mSelecter.draw()

    def processInput(self, key):
        if key.type == SDL_QUIT:
            self.mGame.quit()
        elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_SPACE):
            self.mGame.isPause = False
            if self.mSelecter.mSelect == 0:
                self.mGame.popPage()
            elif self.mSelecter.mSelect == 1:
                self.mGame.popPage()
                self.mGame.popPage()

        self.mSelecter.processInput(key)