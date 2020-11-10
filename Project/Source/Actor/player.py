from pico2d import *
from Actor import actorhelper, bubble
from Item import item
import random
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
        self.mXPos = get_canvas_width() / 2
        self.mXDelta = 0
        self.mYPos = get_canvas_height() / 2
        self.mYDelta = -5
        self.mFlip = ''
        self.mXSpeed = 200
        self.mYSpeed = 200
        self.mAttackMaxDelay = 0.5
        self.mAttackDelay = 0
        self.mAttackInput = False
        self.mTime = 0
        self.mImageIndex = 0
        self.mAction = 'Stop'
        self.mLife = 2
        self.mNoHitTime = 0
        self.mHasItem = [False, False, False, False]

    def __del__(self):
        pass

    def load(self):
        if len(Player.images) == 0:
            actorhelper.load_image(self, 'green')

        self.mJumpSound = load_wav(Player.page.mGame.soundDir + 'Pjump.wav')
        self.mJumpSound.set_volume(80)
        self.mAttackSound = load_wav(Player.page.mGame.soundDir + 'Pattack.wav')
        self.mAttackSound.set_volume(35)
        self.mDieSound = load_wav(Player.page.mGame.soundDir + 'PDie.wav')
        self.mDieSound.set_volume(85)

    def unLoad(self):
        self.removeActor(self)

    def update(self):
        # 중력 설정
        if self.mYDelta > -5:
            self.mYDelta -= 10 * Player.page.mGame.deltaTime

        if not self.mAction == 'Die':
            # 공통 부분 업데이트
            actorhelper.commonUpdate(self)

            # 공격 딜레이 감소
            if self.mAttackDelay > 0:
                self.mAttackDelay = max(0, self.mAttackDelay - Player.page.mGame.deltaTime)

            # 공격 발사
            if self.mAttackInput and self.mImageIndex == 1:
                bubbleSpeed = 350 + self.mHasItem[2] * 50
                b = bubble.Bubble(Player.page, bubbleSpeed)
                Player.page.addActor('bubble', b)
                self.mAttackInput = False

            # 이동
            xMove = self.mXDelta * (self.mXSpeed + 100 * self.mHasItem[0]) * Player.page.mGame.deltaTime
            yMove = self.mYDelta * self.mYSpeed / 2 * Player.page.mGame.deltaTime

            # 로딩중일 경우
            if Player.page.map.mStageChange:
                xMove = 0
                yMove = 0
                self.mAction = 'Move'
            else:
                self.mNoHitTime = max(0.0, self.mNoHitTime - Player.page.mGame.deltaTime)
                self.collideBlock(xMove, yMove)
                self.collideItem()
                if self.mNoHitTime == 0.0:
                    self.collideEnemy()
        else:
            if self.mImageIndex >= Player.imageIndexs[self.mAction]:
                if self.mLife == 0:
                    Player.page.mEndGame = True
                else:
                    self.mAction = 'Stop'
                    actorhelper.resetImageIndex(self)
                    self.mXPos = 100
                    self.mYPos = 100
                    self.mNoHitTime = 3.0

    def collideBlock(self, xMove, yMove):
        self.mXPos += xMove
        for block in Player.page.map.sideBlocks:
            if physics.collides(self, block):
                self.mXPos -= xMove
                break

        jumpCol = False
        for block in Player.page.map.getBlockData():
            if physics.collidesBlock(self.getBB(), block):
                jumpCol = True
                break

        if self.mYDelta <= 0 and not jumpCol:
            for block in Player.page.map.getBlockData():
                if physics.collidesBlock(self.getBB(), block):
                    self.mXPos -= xMove
                    break

        self.mYPos += yMove
        for block in Player.page.map.getBlockData():
            if physics.collidesBlock(self.getBB(), block) and self.mYDelta < 0 and not jumpCol:
                self.mYPos -= yMove
                self.mYDelta = 0
                if physics.collidesBlock(self.getBB(), block):
                    self.mXPos -= xMove
                if self.mAction != 'Attack':
                    self.mAction = 'Stop' if self.mXDelta == 0 and 'Stop' in Player.actions else 'Move'
                break

    def collideEnemy(self):
        for enemy in Player.page.mActors['enemy']:
            if enemy.mAction != 'Die' and enemy.mAction != 'Inb' and physics.collidesBox(self, enemy):
                self.mAction = 'Die'
                self.mLife -= 1
                actorhelper.resetImageIndex(self)
                self.mDieSound.play()
                break

    def collideItem(self):
        for item in Player.page.mActors['item']:
            if physics.collidesBox(self, item):
                if item.mReinForce:
                    self.mHasItem[item.mItem] = True
                item.unload()

    def draw(self):
        actorhelper.commonDraw(self)

    def processInput(self, key):
        pair = (key.type, key.key)
        if pair in Player.keyMap:
            self.mXDelta += Player.keyMap[pair][0]
        elif pair == Player.KEYDOWN_ATTACK and not Player.page.map.mStageChange:
            self.attack()
        elif pair == Player.KEYDOWN_JUMP and not Player.page.map.mStageChange:
            self.jump()

    def attack(self):
        if self.mAttackDelay == 0:
            self.mAttackDelay = 0.5 - self.mHasItem[1] * 0.2
            self.mTime = 0
            self.mImageIndex = 0
            self.mAction = 'Attack'
            self.mAttackInput = True
            self.mAttackSound.play()

    def jump(self):
        if self.mAction != 'Jump' and self.mYDelta == 0:
            self.mTime = 0
            self.mImageIndex = 0
            if self.mAction != 'Attack':
                self.mAction = 'Jump'
            self.mYDelta = 5
            self.mJumpSound.play()

    def getBB(self):
        b = self.mHasItem[3] * 5
        return self.mXPos - self.mBB[0] + b, self.mYPos - self.mBB[1],\
               self.mXPos + self.mBB[0] - b, self.mYPos + self.mBB[1] - b