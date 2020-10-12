import GameFrameWork
from pico2d import *
import TitlePage

class LogoPage(object) :

    def __init__(self):
        self.game = GameFrameWork.Game()
        self.image =  load_image('../res/kpu_credit.png')
        self.changeTime = 0.0

    def __del__(self):
        del self.image;

    def update(self):
        self.changeTime += game.deltaTime

    def draw(self):
        self.image.draw(400,300)

    def processInput(self):



