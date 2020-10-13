from pico2d import *

class Actor:
    mGame = None

    def __init__(self, game):
        Actor.mGame = game

    def __del__(self):
        print("안녕3")
        self.mGame.removeActor(self)

    def initialize(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def processInput(self, key):
        pass