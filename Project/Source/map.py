from pico2d import *
import mapdata

class Map:

    game = None
    stage = 1
    maxStage = 1
    imageName = ['front', 'back']
    images = {}
    blocks = []
    ldPos = (0, 50)

    def __init__(self, game):
        Map.game = game
        self.load()

    def load(self):
        Map.loadImage('front')
        Map.loadImage('back')

        #blocks는 벽돌들로 스테이지 넘어갈때 로딩하게 구현원함
        Map.loadMapData(Map.stage)

    @staticmethod
    def loadImage(char):
        fileName = '%s/map/stage%s%s.png'

        images = []

        for stage in range(0, Map.maxStage):
            fn = fileName % (Map.game.imageDir, stage + 1, char)
            if os.path.isfile(fn):
                images.append(Map.game.imageLoader.load(fn))
                print('Map %s load complete' % stage)
            else:
                break

        Map.images[char] = images

    @staticmethod
    def loadMapData(stage):
        fileName = '%s/map/stagedata%s.json'
        fn = fileName % (Map.game.imageDir, stage)
        Map.blocks = mapdata.load(fn)

    def update(self):
        pass

    def draw(self):
        image = Map.images['back'][Map.stage - 1]
        image.draw(image.w / 2 + Map.ldPos[0], image.h / 2 + Map.ldPos[1])
        image = Map.images['front'][Map.stage - 1]
        image.draw(image.w / 2 + Map.ldPos[0], image.h / 2 + Map.ldPos[1])
