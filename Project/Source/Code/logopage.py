from pico2d import *
from Code import gameframework, titlepage


class LogoPage:
    def __init__(self, game):
        self.mGame = game
        self.mChangeTime = 0.0

    def __del__(self):
        del self.image

    def initialize(self):
        print(os.getcwd())
        print(os.path.abspath(__file__))
        self.image = self.mGame.imageLoader.load(self.mGame.imageDir + 'kpu_credit.png')

    def update(self):
        self.mChangeTime += self.mGame.deltaTime
        if self.mChangeTime > 1.0:
            self.mGame.changePage(titlepage.TitlePage(self.mGame))

    def draw(self):
        self.image.draw(400, 300)

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