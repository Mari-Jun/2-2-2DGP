#로고 페이지이며 로딩 페이지
from pico2d import *
from GFW import gameframework
import titlepage

class LogoPage:
    def __init__(self, game):
        self.mGame = game
        self.mChangeTime = 0.0
        self.index = 0

    def __del__(self):
        del self.image

    def initialize(self):
        self.image = self.mGame.imageLoader.load(self.mGame.imageDir + 'loading.png')

    def update(self):
        image_count = len(IMAGE_FILES)
        if self.index < image_count:
            self.mGame.imageLoader.load(self.mGame.imageDir + IMAGE_FILES[self.index])
        else:
            self.mGame.changePage(titlepage.TitlePage(self.mGame))
        self.index += 1

    def draw(self):
        self.image.draw(gameframework.canvasWidth / 2, gameframework.canvasHeight / 2)

    def processInput(self, key):
        if key.type == SDL_QUIT:
            self.mGame.quit()
        elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            self.mGame.quit()


IMAGE_FILES = [
    'game.png',
    'help.png',
    'lifeName.png',
    'loading.png',
    'pause.png',
    'score.png',
    'scoreName.png',
    'stageName.png',
    'Title.png',
    'titleselecter.png',
    'item/reinforce.png',
    'map/stage1front.png', 'map/stage2front.png', 'map/stage3front.png', 'map/stage4front.png',
    'map/stage5front.png', 'map/stage6front.png', 'map/stage7front.png', 'map/stage8front.png',
    'map/stage9front.png', 'map/stage10front.png',
    'actor/banebou/die.png', 'actor/banebou/inb.png', 'actor/banebou/move.png',
    'actor/chan/die.png', 'actor/chan/inb.png', 'actor/chan/move.png', 'actor/chan/jump.png',
    'actor/hidegons/die.png', 'actor/hidegons/inb.png', 'actor/hidegons/move.png', 'actor/hidegons/jump.png',
    'actor/hidegons/fire.png', 'actor/hidegons/attack.png',
    'actor/invator/die.png', 'actor/invator/inb.png', 'actor/invator/move.png',
    'actor/invator/fire.png', 'actor/invator/attack.png',
    'actor/monsta/die.png', 'actor/monsta/inb.png', 'actor/monsta/move.png',
    'actor/green/die.png', 'actor/green/jump.png', 'actor/green/move.png',
    'actor/green/stop.png', 'actor/green/attack.png',
    'actor/bubble/Attack.png', 'actor/bubble/die.png', 'actor/bubble/move.png', 'actor/bubble/Warning.png'
]

def create(game):
    page = LogoPage(game)
    return page

if __name__ == '__main__':
    gameframework.run_main()