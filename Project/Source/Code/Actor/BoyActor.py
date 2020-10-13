#임시 실험용 파일

from pico2d import *
from Code.Actor import Actor

class BoyActor(Actor):

    def __init__(self, game):
        super(BoyActor, self).__init__(game)
        self.mImage = game.imageLoader.load(game.imageDir + 'character.png')

    def __del__(self):
        pass

    def initialize(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.mImage.draw(400, 100)

    def processInput(self, key):
        pass