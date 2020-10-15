from pico2d import *
import gameframework
import player
import pausepage

class GamePage:
    def __init__(self, game):
        self.mGame = game

    def __del__(self):
        self.mGame.clearActor()

    def initialize(self):
        self.load()

    def load(self):
        dragon = player.Player(self.mGame)
        self.mGame.addActor(dragon)

    def update(self):
        pass

    def draw(self):
        pass

    def processInput(self, key):
        if key.type == SDL_QUIT:
            self.mGame.quit()
        elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            self.mGame.pushPage(pausepage.PausePage(self.mGame))
            self.mGame.isPause = True

def create(game):
    page = GamePage(game)
    return page

if __name__ == '__main__':
    gameframework.run_main()