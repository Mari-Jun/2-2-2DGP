from pico2d import *

class Selecter:

    def __init__(self, game, max, yPos):
        self.mGame = game
        self.mImage = self.mGame.imageLoader.load(self.mGame.imageDir + 'titleselecter.png')
        self.mSelect = 0
        self.maxSelect = max
        self.yPos = yPos

    def __del__(self):
        del self.mImage

    def load(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.mImage.draw(210, self.yPos - self.mSelect*88)
        pass

    def processInput(self, key):
        if (key.type, key.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.mSelect > 0:
                self.mSelect -= 1
        elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.mSelect < self.maxSelect:
                self.mSelect += 1
