from pico2d import *
from Actor import actorhelper
import physics

class Monsta:
    page = None
    actions = ['Move', 'Die']
    imageIndexs = {'Move': 2, 'Die': 4}
    images = { }

    def __init__(self, page, xPos, yPos):
        Monsta.page = page
        self.load()
        self.mImages = actorhelper.load_image(self, 'monsta')
        self.mXPos = xPos
        self.mXDelta = -1
        self.mYPos = yPos
        self.mYDelta = -1
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
        if len(Monsta.images) == 0:
            actorhelper.load_image(self, 'monsta')

    def unLoad(self):
        self.removeActor(self)

    def update(self):
        # 이동
        xMove = self.mXDelta * self.mSpeed * self.page.mGame.deltaTime
        yMove = self.mYDelta * self.mSpeed * self.page.mGame.deltaTime

        # 충돌 검사
        self.mXPos += xMove
        for block in self.page.map.datas['block']:
            if physics.collides(self, block):
                self.mXPos -= xMove
                self.mXDelta *= -1
                break

        self.mYPos += yMove
        for block in self.page.map.datas['block']:
            if physics.collides(self, block):
                self.mYPos -= yMove
                self.mYDelta *= -1
                break

        # 이미지 변환
        self.mTime += self.page.mGame.deltaTime
        self.mImageIndex = int(self.mTime * 5)
        self.mImageIndex %= self.imageIndexs[self.mAction]

    def draw(self):
        actorhelper.commomDraw(self)

    def processInput(self, key):
        pass

    def getBB(self):
        hw = self.mImages['Move'].w // Monsta.imageIndexs['Move'] / 2 - 15
        hh = self.mImages['Move'].h / 2 - 10
        return self.mXPos - hw, self.mYPos - hh, self.mXPos + hw, self.mYPos + hh