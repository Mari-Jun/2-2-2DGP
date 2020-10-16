from pico2d import *

class Map:

    game = None
    stage = 1
    maxStage = 1
    imageName = ['front', 'back']
    images = {}

    def __init__(self, game):
        Map.game = game
        self.load()

    def load(self):
        Map.load_image('front')
        Map.load_image('back')

    @staticmethod
    def load_image(char):
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

    def update(self):
        pass

    def draw(self):
        image = Map.images['back'][Map.stage - 1]
        image.draw(image.w / 2, image.h / 2 + 50)
        image = Map.images['front'][Map.stage - 1]
        image.draw(image.w / 2, image.h / 2 + 50)
