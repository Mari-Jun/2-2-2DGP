from pico2d import *

class Selecter:

    def __init__(self, game):
        self.mGame = game
        self.load()
        self.mSelect = 0

    def __del__(self):
        del self.mImage

    def load(self):
        self.mImage = self.mGame.imageLoader.load(self.mGame.imageDir + 'titleselecter.png')

    def update(self):
        pass

    def draw(self):
        self.mImage.draw(235, 350 + self.mSelect*90)
        pass

    def processInput(self, key):
        if (key.type, key.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.mSelect > 0:
                self.mSelect -= 1
        elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.mSelect < 3:
                self.mSelect += 1