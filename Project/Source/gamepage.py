from pico2d import *
import gameframework
import Actor
import map
import pausepage
import physics

class GamePage:
    def __init__(self, game):
        self.mGame = game
        self.mActors = []
        self.mDeadActors = []
        self.map = None

    def __del__(self):
        self.clearActor()

    def initialize(self):
        self.load()

    def load(self):
        self.map = map.Map(self.mGame)
        dragon = Actor.player.Player(self)
        self.addActor(dragon)
        chan = Actor.chan.Chan(self)
        self.addActor(chan)

    def update(self):
        self.map.update()
        for actor in self.mActors:
            actor.update()

    def draw(self):
        self.map.draw()
        for actor in self.mActors:
            physics.drawCollisionBox(actor)
            actor.draw()

    def processInput(self, key):
        if key.type == SDL_QUIT:
            self.mGame.quit()
        elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            self.mGame.pushPage(pausepage.PausePage(self.mGame))
            self.mGame.isPause = True

        for actor in self.mActors:
            actor.processInput(key)

    def addActor(self, actor):
        self.mActors.append(actor)

    def removeActor(self, actor):
        self.mDeadActors.append(actor)

    def clearActor(self):
        for actor in self.mActors:
            del actor
        self.mActors.clear()

    def clearDeadActor(self):
        for actor in self.mDeadActors:
            try:
                self.mActors.remove(actor)
            except ValueError:
                pass
        self.mDeadActors.clear()

def create(game):
    page = GamePage(game)
    return page

if __name__ == '__main__':
    gameframework.run_main()