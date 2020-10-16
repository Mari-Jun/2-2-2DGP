from pico2d import *
import gameframework
import player
import map
import pausepage

class GamePage:
    def __init__(self, game):
        self.mGame = game
        self.map = None

    def __del__(self):
        self.mGame.clearActor()

    def initialize(self):
        self.load()

    def load(self):
        self.map = map.Map(self.mGame)
        dragon = player.Player(self.mGame)
        self.mGame.addActor(dragon)

    def update(self):
        self.map.update()

    def draw(self):
        self.map.draw()

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