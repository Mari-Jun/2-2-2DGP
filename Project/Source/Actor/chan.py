from pico2d import *
import actorhelper
import physics

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
        # 중력 설정
        if self.mYDelta > -5:
            self.mYDelta -= 0.125

        #AI 설정


        # 이동
        xMove = self.mXDelta * self.mSpeed * Chan.page.mGame.deltaTime
        if self.mAction == 'Jump':
            xMove = 0.0
        yMove = self.mYDelta * self.mSpeed / 2 * Chan.page.mGame.deltaTime

        # 충돌 검사
        self.mXPos += xMove
        for block in Chan.page.map.sideBlocks:
            if physics.collidesBlock(self, block):
                self.mXPos -= xMove
                break

        if self.mAction != 'Jump':
            for block in Chan.page.map.datas['block']:
                if physics.collidesBlock(self, block):
                    self.mXPos -= xMove
                    break

        self.mYPos += yMove
        for block in Chan.page.map.datas['block']:
            if physics.collidesBlockJump(self, block) and self.mYDelta < 0:
                self.mYPos -= yMove
                self.mYDelta = 0
                if physics.collidesBlock(self, block):
                    self.mXPos -= xMove
                self.mAction = 'Move'
                break

        # 액션 설정
        if self.mAction != 'Jump':
            self.mAction = 'Move'

        # 이미지 변환
        self.mTime += self.page.mGame.deltaTime
        self.mImageIndex = int(self.mTime * 10)

        self.mImageIndex %= Chan.imageIndexs[self.mAction]

    def draw(self):
        actorhelper.commomDraw(self)

    def processInput(self, key):
        pass

    def getBB(self):
        hw = self.mImages['Move'].w // Chan.imageIndexs['Move'] / 2 - 15
        hh = self.mImages['Move'].h / 2 - 10
        return self.mXPos - hw, self.mYPos - hh, self.mXPos + hw, self.mYPos + hh