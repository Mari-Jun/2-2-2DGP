from pico2d import *
from GFW import gameframework
import gamepage
import helppage
import rankpage
import selecter


class TitlePage:
    def __init__(self, game):
        self.mGame = game

    def __del__(self):
        del self.mBKImage
        del self.mSelecter

    def initialize(self):
        self.load()

    def load(self):
        self.mBKImage = self.mGame.imageLoader.load(self.mGame.imageDir + 'title.png')
        self.mSelecter = selecter.Selecter(self.mGame, 3, 210, 335)
        self.mBgm = load_music(self.mGame.soundDir +'titlePage.mp3')
        self.mBgm.set_volume(64)
        self.mBgm.repeat_play()

    def update(self):
        pass

    def draw(self):
        self.mBKImage.draw(gameframework.canvasWidth / 2, gameframework.canvasHeight / 2)
        self.mSelecter.draw()

    def processInput(self, key):
        if key.type == SDL_QUIT:
            self.mBgm.stop()
            self.mGame.quit()
        elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.mSelecter.mSelect == 0:
                self.mGame.pushPage(gamepage.GamePage(self.mGame))
            elif self.mSelecter.mSelect == 1:
                self.mGame.pushPage(helppage.HelpPage(self.mGame))
            elif self.mSelecter.mSelect == 2:
                self.mGame.pushPage(rankpage.RankPage(self.mGame))
            elif self.mSelecter.mSelect == 3:
                self.mBgm.stop()
                self.mGame.quit()


        self.mSelecter.processInput(key)

def create(game):
    page = TitlePage(game)
    return page

if __name__ == '__main__':
    gameframework.run_main()