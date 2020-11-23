from pico2d import *
from GFW import gameframework
import selecter
from ext_pico2d import *

from Project.Source.ext_pico2d import draw_centered_text


class HelpPage:
    def __init__(self, game):
        self.mGame = game

    def __del__(self):
        del self.mBKImage
        del self.mSelecter

    def initialize(self):
        self.load()

    def load(self):
        self.mBKImage = self.mGame.imageLoader.load(self.mGame.imageDir + 'help.png')
        self.mSelecter = selecter.Selecter(self.mGame, 0, 570, 40)
        self.font = self.mGame.fontLoader.load(self.mGame.fontDir + "ConsolaMalgun.ttf", 40)
        self.itemImage = self.mGame.imageLoader.load(self.mGame.imageDir + 'item/reinforce.png')

    def update(self):
        pass

    def draw(self):
        self.mBKImage.draw(gameframework.canvasWidth / 2, gameframework.canvasHeight / 2)
        self.mSelecter.draw()
        x, y, color = get_canvas_width() // 2, get_canvas_height() // 2 + 40, (255, 255, 255)
        self.font.draw(x - 200, y + 180, "이동 : 방향키 좌,우", color)
        self.font.draw(x - 200, y + 120, "공격 : SpaceBar", color)
        self.font.draw(x - 200, y + 60, "점프 : 방향키 위", color)
        self.font.draw(x - 200, y, "정지 : ESC", color)

        sx = 0
        for i in range(4):
            self.itemImage.clip_draw(sx, 0, self.itemImage.w // 4, self.itemImage.h, x - 240, y - (i + 1) * 60)
            sx += self.itemImage.w // 4

        self.font.draw(x - 200, y - 60, "이동 속도 증가", color)
        self.font.draw(x - 200, y - 120, "공격 속도 증가", color)
        self.font.draw(x - 200, y - 180, "버블 공격 사정거리 증가", color)
        self.font.draw(x - 200, y - 240, "플레이어 충돌 범위 감소", color)



    def processInput(self, key):
        if key.type == SDL_QUIT:
            self.mGame.quit()
        elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_SPACE):
            self.mGame.isPause = False
            if self.mSelecter.mSelect == 0:
                self.mGame.popPage()
            elif self.mSelecter.mSelect == 1:
                self.mGame.popPage()

        self.mSelecter.processInput(key)

def create(game):
    page = HelpPage(game)
    return page

if __name__ == '__main__':
    gameframework.run_main()