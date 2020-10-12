from pico2d import *

class TitlePage:
    def __init__(self, game):
        self.mGame = game

    def __del__(self):
        del self.mImage

    def initialize(self):
        self.mImage = self.mGame.imageLoader.load('../Asset/Image/title.png')

    def update(self):
        pass

    def draw(self):
        self.mImage.draw(400, 300)

    def processInput(self, key):
        if key.type == SDL_QUIT:
            self.mGame.quit()
        elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            self.mGame.quit()

