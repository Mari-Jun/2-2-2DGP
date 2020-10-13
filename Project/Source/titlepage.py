from pico2d import *
import gameframework
import gamepage
import selecter


class TitlePage:
    def __init__(self, game):
        self.mGame = game

    def __del__(self):
        del self.mBKImage

    def initialize(self):
        self.load()

    def load(self):
        self.mBKImage = self.mGame.imageLoader.load(self.mGame.imageDir + 'title.png')
        self.mSelecter = selecter.Selecter(self.mGame)

    def update(self):
        pass

    def draw(self):
        self.mBKImage.draw(400, 350)
        self.mSelecter.draw()

    def processInput(self, key):
        if key.type == SDL_QUIT:
            self.mGame.quit()
        elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            self.mGame.quit()
        elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_SPACE):
            self.mGame.pushPage(gamepage.GamePage(self.mGame))

        self.mSelecter.processInput(key)

def create(game):
    page = TitlePage(game)
    return page

if __name__ == '__main__':
    gameframework.run_main()