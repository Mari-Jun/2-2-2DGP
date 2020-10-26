from pico2d import *
from Actor import actorhelper
import physics

class Bubble:
    page = None
    actions = ['Move']
    imageIndexs = {'Move': 7}
    images = { }

    def __init__(self, page):
        Bubble.page = page
        self.load()
        self.mImages = actorhelper.load_image(self, 'bubble')
        self.mXPos = page.mActors['player'][0].mXPos
        self.mXDelta = -1 if page.mActors['player'][0].mFlip == 'h' else 1
        self.mYPos = page.mActors['player'][0].mYPos
        self.mYDelta = 0
        self.mSpeed = 350
        self.mTime = 0
        self.mImageIndex = 0
        self.mAction = 'Move'

    def __del__(self):
        pass

    def initialize(self):
        pass

    def load(self):
        if len(Bubble.images) == 0:
            actorhelper.load_image(self, 'bubble')

    def unLoad(self):
        self.removeActor(self)

    def update(self):
        # 이동
        xMove = self.mXDelta * self.mSpeed * Bubble.page.mGame.deltaTime
        if self.mYDelta == -5:
            xMove /= 5
        yMove = self.mYDelta * self.mSpeed / 2 * Bubble.page.mGame.deltaTime

        # # 충돌 검사
        self.mXPos += xMove
        # for block in Player.page.map.sideBlocks:
        #     if physics.collides(self, block):
        #         self.mXPos -= xMove
        #         break
        #
        # if self.mAction != 'Jump':
        #     for block in Player.page.map.datas['block']:
        #         if physics.collidesBlock(self.getBB(), block):
        #             self.mXPos -= xMove
        #             break
        #
        # self.mYPos += yMove
        # for block in Player.page.map.datas['block']:
        #     if physics.collidesBlock(self.getBB(), block) and self.mYDelta < 0:
        #         self.mYPos -= yMove
        #         self.mYDelta = 0
        #         if physics.collidesBlock(self.getBB(), block):
        #             self.mXPos -= xMove
        #         if self.mAction != 'Attack':
        #             self.mAction = 'Stop' if self.mXDelta == 0 and 'Stop' in Player.actions else 'Move'
        #         break

    def draw(self):
        image = self.mImages[self.mAction]
        startX = image.w // self.imageIndexs[self.mAction] * self.mImageIndex
        image.clip_draw(startX, 0, image.w // self.imageIndexs[self.mAction], image.h,
                                  self.mXPos, self.mYPos, image.w //self.imageIndexs[self.mAction], image.h)

        # 이미지 변환
        if self.mImageIndex < Bubble.imageIndexs['Move'] - 1:
            self.mTime += self.page.mGame.deltaTime
            self.mImageIndex = int(self.mTime * 10)

    def processInput(self, key):
        pass

    def getBB(self):
        hw = self.mImages['Move'].w // Bubble.imageIndexs['Move'] / 2 - 13
        hh = self.mImages['Move'].h / 2 - 13
        return self.mXPos - hw, self.mYPos - hh, self.mXPos + hw, self.mYPos + hh