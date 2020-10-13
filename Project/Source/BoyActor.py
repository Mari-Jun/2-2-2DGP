#임시 실험용 파일

from pico2d import *
from actor import Actor

class BoyActor(Actor):

    def __init__(self, game):
        self.mGame = game;
        self.mImage = game.imageLoader.load(game.imageDir + 'character.png')

    def __del__(self):
        print("안녕2")
        super(BoyActor, self).__del__()

    def initialize(self):
        pass

    def unLoad(self):
        self.mGame.removeActor(self)

    def update(self):
        pass

    def draw(self):
        self.mImage.draw(400, 100)

    def processInput(self, key):
        pass