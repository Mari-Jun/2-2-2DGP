from pico2d import *
from Actor import actorhelper

class HidegonsAT:
    page = None
    actions = ['Fire']
    imageIndexs = {'Fire': 15}
    images = { }

    def __init__(self, page, xPos, yPos, xDelta):
        HidegonsAT.page = page
        self.load()
        self.mImages = actorhelper.load_image(self, 'hidegons')
        self.mBB = self.mImages['Fire'].w // HidegonsAT.imageIndexs['Fire'] / 2 - 14, self.mImages['Fire'].h / 2 - 13
        self.mXDelta = xDelta
        self.mXPos = xPos
        self.mYPos = yPos
        self.mFlip = ''
        self.mSpeed = 400
        self.mTime = 0
        self.mImageIndex = 0
        self.mAction = 'Fire'

    def load(self):
        if len(HidegonsAT.images) == 0:
            actorhelper.load_image(self, 'hidegons')

    def unLoad(self):
        HidegonsAT.page.removeActor(self)

    def update(self):
        xMove = self.mXDelta * self.mSpeed * HidegonsAT.page.mGame.deltaTime
        self.mXPos += xMove

    def draw(self):
        # 이미지 변환
        self.mTime += self.page.mGame.deltaTime
        self.mImageIndex = int(self.mTime * 10)
        if self.mImageIndex >= HidegonsAT.imageIndexs['Fire']:
            self.unLoad()

        actorhelper.commonDrawClipComposite(self)

    def getBB(self):
        return self.mXPos - self.mBB[0], self.mYPos - self.mBB[1], self.mXPos + self.mBB[0], self.mYPos + self.mBB[1]