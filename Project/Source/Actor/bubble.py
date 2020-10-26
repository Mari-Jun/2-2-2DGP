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
        self.mBB = self.mImages['Move'].w // Bubble.imageIndexs['Move'] / 2 - 13, self.mImages['Move'].h / 2 - 13
        player = page.mActors['player'][0]
        self.mXDelta = -1 if player.mFlip == 'h' else 1
        self.mYDelta = 0
        self.mXPos = player.mXPos + self.mXDelta * (player.mBB[0] + self.mBB[0])
        self.mYPos = player.mYPos
        self.mSpeed = 350
        self.mLength = 300
        self.mTime = 0
        self.mImageIndex = 0

        #생성 위치가 충돌 위치라면
        for block in Bubble.page.map.datas['block']:
            if physics.collides(self, block):
                self.unLoad()

    def initialize(self):
        pass

    def load(self):
        if len(Bubble.images) == 0:
            actorhelper.load_image(self, 'bubble')

    def unLoad(self):
        Bubble.page.removeActor(self)

    def update(self):
        # 이동
        xMove = self.mXDelta * self.mSpeed * Bubble.page.mGame.deltaTime
        if self.mYDelta == -5:
            xMove /= 5
        yMove = self.mYDelta * self.mSpeed / 2 * Bubble.page.mGame.deltaTime

        self.mLength -= abs(xMove)
        if self.mLength > 0:
            self.mXPos += xMove

        # 충돌 검사
        for block in Bubble.page.map.datas['block']:
            if physics.collides(self, block):
                self.mXPos -= xMove
                break

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
        image = self.mImages['Move']
        startX = image.w // self.imageIndexs['Move'] * self.mImageIndex
        image.clip_draw(startX, 0, image.w // self.imageIndexs['Move'], image.h,
                                  self.mXPos, self.mYPos, image.w //self.imageIndexs['Move'], image.h)

        # 이미지 변환
        if self.mImageIndex < Bubble.imageIndexs['Move'] - 1:
            self.mTime += self.page.mGame.deltaTime
            self.mImageIndex = int(self.mTime * 10)

    def processInput(self, key):
        pass

    def getBB(self):
        return self.mXPos - self.mBB[0], self.mYPos - self.mBB[1], self.mXPos + self.mBB[0], self.mYPos + self.mBB[1]