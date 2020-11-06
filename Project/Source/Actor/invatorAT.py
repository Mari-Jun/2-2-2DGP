from pico2d import *
import physics
from Actor import actorhelper

class InvatorAT:
    page = None
    actions = ['Fire']
    imageIndexs = {'Fire': 4 }
    images = { }

    def __init__(self, page, xPos, yPos):
        InvatorAT.page = page
        self.load()
        self.mImages = actorhelper.load_image(self, 'invator')
        self.mBB = self.mImages['Fire'].w // InvatorAT.imageIndexs['Fire'] / 2 - 14, self.mImages['Fire'].h / 2 - 13
        self.mYDelta = -5
        self.mXPos = xPos
        self.mYPos = yPos
        self.mFlip = ''
        self.mSpeed = 100
        self.mTime = 0
        self.mImageIndex = 0
        self.mAction = 'Fire'

    def load(self):
        if len(InvatorAT.images) == 0:
            actorhelper.load_image(self, 'invator')

    def unLoad(self):
        InvatorAT.page.removeActor(self)

    def update(self):
        yMove = self.mYDelta * self.mSpeed * InvatorAT.page.mGame.deltaTime
        self.mYPos += yMove

        if self.mImageIndex == 0:
            for block in InvatorAT.page.map.getBlockData():
                if physics.collidesBlock(self.getBB(), block):
                    self.mImageIndex = 1

    def draw(self):
        if self.mImageIndex > 1:
            self.mTime += self.page.mGame.deltaTime
            self.mImageIndex = int(self.mTime * 10)
            if self.mImageIndex >= InvatorAT.imageIndexs['Fire']:
                self.unLoad()

        image = self.mImages[self.mAction]
        startX = image.w // self.imageIndexs[self.mAction] * self.mImageIndex
        image.clip_draw(startX, 0, image.w // self.imageIndexs[self.mAction], image.h,
                        self.mXPos, self.mYPos, image.w // self.imageIndexs[self.mAction], image.h)

    def getBB(self):
        return self.mXPos - self.mBB[0], self.mYPos - self.mBB[1], self.mXPos + self.mBB[0], self.mYPos + self.mBB[1]