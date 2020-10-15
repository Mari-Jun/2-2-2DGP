from pico2d import *

class Player:

    game = None
    actions = ['Stop', 'Move', 'Jump', 'Attack', 'Die']
    imageSize = {'Stop': 30, 'Move': 27, 'Jump': 28, 'Attack': 29, 'Die': 29}
    imageIndex = {'Stop': 3, 'Move': 5, 'Jump': 8, 'Attack': 8, 'Die': 2}
    images = {}
    FPS = 12

    def __init__(self, game):
        Player.game = game
        self.load()

        self.images = Player.load_image('green')
        self.xPos = 100
        self.yPos = 100
        self.imageIndex = 0
        self.action = 'Stop'

    def __del__(self):
        pass

    def initialize(self):
        pass

    def load(self):
        if len(Player.images) == 0:
            Player.load_all_images()

    @staticmethod
    def load_all_images():
        Player.load_image('green')

    @staticmethod
    def load_image(char):
        if char in Player.images:
            return Player.images[char]

        images = {}

        fileName = '%s/dragon/%s/player_%s.png'

        for action in Player.actions:
            fn = fileName % (Player.game.imageDir, char, action)
            if os.path.isfile(fn):
                action_image = Player.game.imageLoader.load(fn)
            else:
                break

            images[action] = action_image
        Player.images[char] = images

        print('player %s load complete' % char)
        return images

    def unLoad(self):
        self.mGame.removeActor(self)

    def update(self):
        #이미지 변환
        self.imageIndex += 1
        self.imageIndex %= Player.imageIndex[self.action]


    def draw(self):
        image = self.images[self.action]
        startX = Player.imageSize[self.action] * self.imageIndex
        image.clip_draw(startX, 0, Player.imageSize[self.action], 30, self.xPos, self.yPos)
        pass

    def processInput(self, key):
        pass

