from pico2d import *
import actorhelper

class Player:
    keyMap = {
        (SDL_KEYDOWN, SDLK_LEFT):  (-1,  0),
        (SDL_KEYDOWN, SDLK_RIGHT): ( 1,  0),
        (SDL_KEYUP, SDLK_LEFT):    ( 1,  0),
        (SDL_KEYUP, SDLK_RIGHT):   (-1,  0),
    }
    KEYDOWN_JUMP = (SDL_KEYDOWN, SDLK_UP)
    KEYDOWN_ATTACK = (SDL_KEYDOWN, SDLK_SPACE)

    page = None
    actions = ['Stop', 'Move', 'Jump', 'Attack', 'Die']
    imageIndexs = {'Stop': 3, 'Move': 5, 'Jump': 8, 'Attack': 4, 'Die': 2}
    images = { }

    def __init__(self, page):
        Player.page = page
        self.load()
        self.mImages = actorhelper.load_image(self, 'green')
        self.mXPos = 100
        self.mXDelta = 0
        self.mYPos = 110
        self.mYDelta = -5
        self.mFlip = ''
        self.mSpeed = 200
        self.mTime = 0
        self.mImageIndex = 0
        self.mAction = 'Stop'

    def __del__(self):
        pass

    def initialize(self):
        pass

    def load(self):
        if len(Player.images) == 0:
            actorhelper.load_image(self, 'green')

    def unLoad(self):
        self.removeActor(self)

    def update(self):
        actorhelper.commomUpdate(self)

    def draw(self):
        actorhelper.commomDraw(self)

    def processInput(self, key):
        pair = (key.type, key.key)
        if pair in Player.keyMap:
            self.mXDelta += Player.keyMap[pair][0]
            if self.mXDelta < 0:
                self.mFlip = 'h'
            elif self.mXDelta > 0:
                self.mFlip = ''
        elif pair == Player.KEYDOWN_ATTACK:
            actorhelper.attack(self)
        elif pair == Player.KEYDOWN_JUMP:
            actorhelper.jump(self)

    def getBB(self):
        hw = self.mImages['Stop'].w // Player.imageIndexs['Stop'] / 2 - 10
        hh = self.mImages['Stop'].h / 2 - 10
        return self.mXPos - hw, self.mYPos - hh, self.mXPos + hw, self.mYPos + hh