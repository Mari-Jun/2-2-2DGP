from pico2d import *

class Player:

    keyMap = {
        (SDL_KEYDOWN, SDLK_LEFT): (-1, 0),
        (SDL_KEYDOWN, SDLK_RIGHT): (1, 0),
        (SDL_KEYDOWN, SDLK_UP): (0, 1),
        (SDL_KEYUP, SDLK_LEFT): (1, 0),
        (SDL_KEYUP, SDLK_RIGHT): (-1, 0),
        (SDL_KEYUP, SDLK_UP): (0, -1),
    }

    game = None
    actions = ['Stop', 'Move', 'Jump', 'Attack', 'Die']
    imageIndex = {'Stop': 3, 'Move': 5, 'Jump': 8, 'Attack': 8, 'Die': 2}
    images = { }

    def __init__(self, game):
        Player.game = game
        self.load()

        self.images = Player.load_image('green')
        self.xPos = 100
        self.xDelta = 0
        self.yPos = 100
        self.yDelta = 0
        self.flip = ''
        self.speed = 200
        self.time = 0
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
        # 이동
        self.xPos += self.xDelta * self.speed * Player.game.deltaTime
        self.yPos += self.yDelta * self.speed * Player.game.deltaTime

        print('%d, %d' % (self.xPos, self.yPos))

        #이미지 변환
        self.time += Player.game.deltaTime
        frame = self.time * 5
        self.imageIndex = int(frame) % 5
        self.imageIndex %= Player.imageIndex[self.action]

    def draw(self):
        image = self.images[self.action]
        startX = image.w // Player.imageIndex[self.action] * self.imageIndex
        image.clip_composite_draw(startX, 0, image.w // Player.imageIndex[self.action], image.h, 0, self.flip,
                                  self.xPos, self.yPos, image.w // Player.imageIndex[self.action], image.h)
        pass

    def processInput(self, key):
        pair = (key.type, key.key)
        if pair in Player.keyMap:
            self.xDelta += Player.keyMap[pair][0]
            self.yDelta += Player.keyMap[pair][1]
            if self.xDelta < 0:
                self.flip = 'h'
            elif self.xDelta > 0:
                self.flip = ''

