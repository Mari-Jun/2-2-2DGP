from pico2d import *
import gameframework
import boyactor

class GamePage:
    def __init__(self, game):
        self.mGame = game

    def __del__(self):
        del self.mBoyActor

    def initialize(self):
        self.load()

    def load(self):
        self.mBoyActor = boyactor.BoyActor(self.mGame)

    def update(self):
        pass

    def draw(self):
        pass

    def processInput(self, key):
        if key.type == SDL_QUIT:
            self.mGame.quit()
        elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            self.mGame.popPage()

def create(game):
    page = GamePage(game)
    return page

if __name__ == '__main__':
    gameframework.run_main()