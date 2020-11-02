#로고 페이지이며 로딩 페이지

from pico2d import *
from GFW import gameframework
import titlepage


class LogoPage:
    def __init__(self, game):
        self.mGame = game
        self.mChangeTime = 0.0

    def __del__(self):
        del self.image

    def initialize(self):
        self.image = self.mGame.imageLoader.load(self.mGame.imageDir + 'loading.png')

    def update(self):
        self.mChangeTime += self.mGame.deltaTime
        if self.mChangeTime > 1.0:
            self.mGame.changePage(titlepage.TitlePage(self.mGame))

    def draw(self):
        self.image.draw(gameframework.canvasWidth / 2, gameframework.canvasHeight / 2)

    def processInput(self, key):
        if key.type == SDL_QUIT:
            self.mGame.quit()
        elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            self.mGame.quit()

def create(game):
    page = LogoPage(game)
    return page

if __name__ == '__main__':
    gameframework.run_main()