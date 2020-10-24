from pico2d import *
import gameframework
import Actor
import map
import pausepage
import physics

class GamePage:
    def __init__(self, game):
        self.mGame = game
        self.mActorName = ['item', 'enemy', 'bubble', 'player', 'ui']
        self.mActors = {}
        self.mDeadActors = []
        self.map = None

    def __del__(self):
        self.clearActor()

    def initialize(self):
        for name in self.mActorName:
            self.mActors[name] = []
        self.load()

    def load(self):
        dragon = Actor.player.Player(self)
        self.addActor('player', dragon)
        self.map = map.Map(self)

    def update(self):
        self.map.update()
        for name in self.mActorName:
            for actor in self.mActors[name]:
                actor.update()

    def draw(self):
        self.map.draw()
        for name in self.mActorName:
            for actor in self.mActors[name]:
                physics.drawCollisionBox(actor)
                actor.draw()

    def processInput(self, key):
        if key.type == SDL_QUIT:
            self.mGame.quit()
        elif (key.type, key.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            self.mGame.pushPage(pausepage.PausePage(self.mGame))
            self.mGame.isPause = True

        for name in self.mActorName:
            for actor in self.mActors[name]:
                actor.processInput(key)

    def addActor(self, name, actor):
        self.mActors[name].append(actor)

    def removeActor(self, actor):
        self.mDeadActors.append(actor)

    def clearActor(self):
        for name in self.mActorName:
            for actor in self.mActors[name]:
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