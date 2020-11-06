from pico2d import *
from GFW import gameframework
import Actor
import MapInfo
import score
import pausepage
import physics

class GamePage:
    def __init__(self, game):
        self.mGame = game
        self.mActorName = ['item', 'bubble', 'enemy', 'enemyAT', 'player', 'ui']
        self.mActors = {}
        self.mDeadActors = []
        self.map = None
        self.mEndGame = False

    def __del__(self):
        self.clearActor()

    def initialize(self):
        for name in self.mActorName:
            self.mActors[name] = []
        self.load()

    def load(self):
        self.mBKImage = self.mGame.imageLoader.load(self.mGame.imageDir + 'game.png')
        dragon = Actor.player.Player(self)
        self.addActor('player', dragon)
        self.map = MapInfo.map.Map(self)
        self.mScore = score.Score(self, gameframework.canvasWidth / 2 + 130, gameframework.canvasHeight - 60)
        self.addActor('ui', self.mScore)

    def update(self):
        self.map.update()
        for name in self.mActorName:
            for actor in self.mActors[name]:
                actor.update()

        if len(self.mDeadActors) > 0:
            self.clearDeadActor()

        if self.mEndGame:
            self.mGame.popPage()

    def draw(self):
        self.mBKImage.draw(gameframework.canvasWidth / 2, gameframework.canvasHeight / 2)
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

        for actor in self.mActors['player']:
            actor.processInput(key)

    def addActor(self, name, actor):
        self.mActors[name].append(actor)

    def removeActor  (self, actor):
        self.mDeadActors.append(actor)

    def clearActor(self):
        for name in self.mActorName:
            for actor in self.mActors[name]:
                del actor
        self.mActors.clear()

    def clearDeadActor(self):
        for dActor in self.mDeadActors:
            for actor in self.mActors:
                try:
                    self.mActors[actor].remove(dActor)
                except ValueError:
                    pass
        self.mDeadActors.clear()

def create(game):
    page = GamePage(game)
    return page

if __name__ == '__main__':
    gameframework.run_main()