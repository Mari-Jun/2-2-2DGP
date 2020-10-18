from pico2d import *
import actorhelper

class Chan:
    page = None
    actions = ['Move', 'Jump', 'Die']
    imageIndexs = {'Move': 4, 'Jump': 8, 'Die': 4}
    images = { }

    def __init__(self, page, xPos, yPos):
        Chan.page = page
        self.load()
        self.mImages = actorhelper.load_image(self, 'chan')
        self.mXPos = xPos
        self.mXDelta = 0
        self.mYPos = yPos
        self.mYDelta = -5
        self.mFlip = ''
        self.mSpeed = 200
        self.mTime = 0
        self.mImageIndex = 0
        self.mAction = 'Move'

    def __del__(self):
        pass

    def initialize(self):
        pass

    def load(self):
        if len(Chan.images) == 0:
            actorhelper.load_image(self, 'chan')

    def unLoad(self):
        self.removeActor(self)

    def update(self):
        actorhelper.commomUpdate(self)

    def draw(self):
        actorhelper.commomDraw(self)

    def processInput(self, key):
        pass

    def getBB(self):
        hw = self.mImages['Move'].w // Chan.imageIndexs['Move'] / 2 - 15
        hh = self.mImages['Move'].h / 2 - 10
        return self.mXPos - hw, self.mYPos - hh, self.mXPos + hw, self.mYPos + hh