from pico2d import *

class GamePage:
    def __init__(self, game):
        self.mGame = game

    def __del__(self):
        pass

    def initialize(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def processInput(self, key):
        if key.type == SDL_QUIT:
            self.mGame.quit()
        elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            self.mGame.popPage()