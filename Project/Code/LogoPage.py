from pico2d import *
import titlepage

class LogoPage:
    def __init__(self, game):
        self.mGame = game
        self.mChangeTime = 0.0

    def __del__(self):
        del self.image

    def initialize(self):
        print(self.mGame)
        self.image = self.mGame.imageLoader.load('res/kpu_credit.png')

    def update(self):
        self.mChangeTime += self.mGame.deltaTime
        print(self.mChangeTime)
        if self.mChangeTime > 1.0:
            exit()

    def draw(self):
        self.image.draw(400, 300)

    def processInput(self, key):
        if key.type == SDL_QUIT:
            self.mGame.quit()
        elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            self.mGame.quit()

