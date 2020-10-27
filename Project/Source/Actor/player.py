from pico2d import *
from Actor import actorhelper, bubble
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
        self.mBB = self.mImages['Stop'].w // Player.imageIndexs['Stop'] / 2 - 10, self.mImages['Stop'].h / 2 - 10
        self.mXPos = 100
        self.mXDelta = 0
        self.mYPos = 110
        self.mYDelta = -5
        self.mFlip = ''
        self.mSpeed = 200
        self.mAttackDelay = 0
        self.mTime = 0
        self.mImageIndex = 0
        self.mAction = 'Stop'

    def __del__(self):
        pass

    def load(self):
        if len(Player.images) == 0:
            actorhelper.load_image(self, 'green')

    def unLoad(self):
        self.removeActor(self)

    def update(self):
        # 중력 설정
        if self.mYDelta > -5:
            self.mYDelta -= 10 * Player.page.mGame.deltaTime

        # 공격 딜레이 감소
        if self.mAttackDelay > 0:
            self.mAttackDelay = max(0, self.mAttackDelay - Player.page.mGame.deltaTime)

        # 이동
        xMove = self.mXDelta * self.mSpeed * Player.page.mGame.deltaTime
        if self.mYDelta <= -5:
            xMove /= 5
        yMove = self.mYDelta * self.mSpeed / 2 * Player.page.mGame.deltaTime

        # 충돌 검사
        self.collideBlock(xMove, yMove)

    def collideBlock(self, xMove, yMove):
        self.mXPos += xMove
        for block in Player.page.map.sideBlocks:
            if physics.collides(self, block):
                self.mXPos -= xMove
                break

        if self.mYDelta <= 0:
            for block in Player.page.map.datas['block']:
                if physics.collidesBlock(self.getBB(), block):
                    self.mXPos -= xMove
                    break

        self.mYPos += yMove
        for block in Player.page.map.datas['block']:
            if physics.collidesBlock(self.getBB(), block) and self.mYDelta < 0:
                self.mYPos -= yMove
                self.mYDelta = 0
                if physics.collidesBlock(self.getBB(), block):
                    self.mXPos -= xMove
                if self.mAction != 'Attack':
                    self.mAction = 'Stop' if self.mXDelta == 0 and 'Stop' in Player.actions else 'Move'
                break

    def draw(self):
        actorhelper.commomDraw(self)

    def processInput(self, key):
        pair = (key.type, key.key)
        if pair in Player.keyMap:
            self.mXDelta += Player.keyMap[pair][0]
        elif pair == Player.KEYDOWN_ATTACK:
            self.attack()
        elif pair == Player.KEYDOWN_JUMP:
            self.jump()

    def attack(self):
        if self.mAttackDelay == 0:
            self.mAttackDelay = 0.5
            self.mTime = 0
            self.mImageIndex = 0
            self.mAction = 'Attack'
            b = bubble.Bubble(Player.page)
            Player.page.addActor('bubble', b)

    def jump(self):
        if self.mAction != 'Jump' and self.mYDelta == 0:
            self.mTime = 0
            self.mImageIndex = 0
            if self.mAction != 'Attack':
                self.mAction = 'Jump'
            self.mYDelta = 5

    def getBB(self):
        return self.mXPos - self.mBB[0], self.mYPos - self.mBB[1], self.mXPos + self.mBB[0], self.mYPos + self.mBB[1]