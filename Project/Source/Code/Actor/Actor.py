from pico2d import *

class Actor:
    mGame = None

    def __init__(self, game):
        Actor.mGame = game
        game.mActors.apeends(self)

    def __del__(self):
        pass

    def initialize(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def processInput(self, key):
        pass