from pico2d import *
import actorhelper
import physics

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
        # 중력 설정
        if self.mYDelta > -5:
            self.mYDelta -= 0.125

        # 이동
        xMove = self.mXDelta * self.mSpeed * Player.page.mGame.deltaTime
        if self.mYDelta == -5:
            xMove /= 5
        yMove = self.mYDelta * self.mSpeed / 2 * Player.page.mGame.deltaTime

        # 충돌 검사
        self.mXPos += xMove
        for block in Player.page.map.sideBlocks:
            if physics.collidesBlock(self, block):
                self.mXPos -= xMove
                break

        if self.mAction != 'Jump':
            for block in Player.page.map.datas['block']:
                if physics.collidesBlock(self, block):
                    self.mXPos -= xMove
                    break

        self.mYPos += yMove
        for block in Player.page.map.datas['block']:
            if physics.collidesBlockJump(self, block) and self.mYDelta < 0:
                self.mYPos -= yMove
                self.mYDelta = 0
                if physics.collidesBlock(self, block):
                    self.mXPos -= xMove
                if self.mAction != 'Attack':
                    self.mAction = 'Stop' if self.mXDelta == 0 and 'Stop' in Player.actions else 'Move'
                break

        # 액션 설정
        if self.mAction != 'Attack' and self.mAction != 'Jump':
            self.mAction = 'Stop' if self.mXDelta == 0 and 'Stop' in Player.actions else 'Move'

        # 이미지 변환
        self.mTime += self.page.mGame.deltaTime
        self.mImageIndex = int(self.mTime * 10)

        # 액션 재설정
        if self.mAction == 'Attack' and self.mImageIndex > Player.imageIndexs['Attack']:
            self.mAction = 'Stop' if self.mXDelta == 0 else 'Move'

        self.mImageIndex %= Player.imageIndexs[self.mAction]

    def draw(self):
        actorhelper.commomDraw(self)

    def processInput(self, key):
        pair = (key.type, key.key)
        if pair in Player.keyMap:
            self.mXDelta += Player.keyMap[pair][0]
        elif pair == Player.KEYDOWN_ATTACK:
            actorhelper.attack(self)
        elif pair == Player.KEYDOWN_JUMP:
            actorhelper.jump(self)

    def getBB(self):
        hw = self.mImages['Stop'].w // Player.imageIndexs['Stop'] / 2 - 10
        hh = self.mImages['Stop'].h / 2 - 10
        return self.mXPos - hw, self.mYPos - hh, self.mXPos + hw, self.mYPos + hh