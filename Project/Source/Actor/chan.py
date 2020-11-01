from pico2d import *
import random
from Actor import actorhelper
import physics
from behaviortree import BehaviorTree, SelectorNode, SequenceNode, LeafNode


class Chan:
    page = None
    player = None
    actions = ['Move', 'Jump', 'Inb', 'Die']
    imageIndexs = {'Move': 4, 'Jump': 8, 'Inb': 3, 'Die': 4}
    images = {}

    def __init__(self, page, xPos, yPos, left):
        Chan.page = page
        Chan.player = page.mActors['player'][0]
        self.load()
        self.mImages = actorhelper.load_image(self, 'chan')
        self.mXPos = xPos
        self.mOXDelta = 1
        self.mXDelta = -1 if left else 1
        self.mYPos = yPos
        self.mYDelta = -5
        self.mFlip = ''
        self.mSpeed = 200
        self.mTime = 0
        self.mImageIndex = 0
        self.mAction = 'Move'
        self.mJumpDelay = 0
        self.mSemiJump = False
        self.mBubble = None

    def __del__(self):
        pass

    def initialize(self):
        pass

    def load(self):
        if len(Chan.images) == 0:
            actorhelper.load_image(self, 'chan')
        self.build_behavior_tree()

    def unLoad(self):
        Chan.page.removeActor(self)

    def update(self):
        # 중력 설정
        if self.mYDelta > -5:
            self.mYDelta -= 10 * Chan.page.mGame.deltaTime
        self.bt.run()

    def draw(self):
        actorhelper.commomDraw(self)

    def getBB(self):
        hw = self.mImages['Move'].w // Chan.imageIndexs['Move'] / 2 - 15
        hh = self.mImages['Move'].h / 2 - 10
        return self.mXPos - hw, self.mYPos - hh, self.mXPos + hw, self.mYPos + hh

    def doMove(self):
        if self.mAction != 'Move':
            return BehaviorTree.FAIL

        # 점프 딜레이 설정
        self.mJumpDelay = max(0, self.mJumpDelay - Chan.page.mGame.deltaTime)
        if abs(self.mXPos - Chan.player.mXPos) < 10:
            self.mJumpDelay = min(0.1, self.mJumpDelay - Chan.page.mGame.deltaTime)

        xMove = self.mXDelta * self.mSpeed * Chan.page.mGame.deltaTime
        yMove = self.mYDelta * self.mSpeed / 2 * Chan.page.mGame.deltaTime

        self.mXPos += xMove
        for block in Chan.page.map.datas['block']:
            if physics.collides(self, block):
                self.mXPos -= xMove
                self.mXDelta *= -1
                break

        self.mYPos += yMove
        collide = False
        for block in Chan.page.map.datas['block']:
            if physics.collidesBlock(self.getBB(), block) and self.mYDelta < 0:
                self.mYPos -= yMove
                self.mYDelta = 0
                if self.mXDelta == 0:
                    self.mXDelta = self.mOXDelta
                collide = True

                self.checkJump(block)
                self.checkSemiJump(block)
                break

        # 그냥 떨어지는 경우
        if not collide:
            if self.mXDelta != 0:
                self.mOXDelta = self.mXDelta
            self.mXDelta = 0
            self.mJumpDelay = 0.5

        return BehaviorTree.SUCCESS

    def checkJump(self, block):
        if self.mYPos < Chan.player.mYPos - 80 and self.mJumpDelay == 0:
            jumpSize = self.getBB()
            upSize = jumpSize[-1] + 80
            jumpSize = jumpSize[0], jumpSize[1], jumpSize[2], upSize;
            for b in Chan.page.map.datas['block']:
                if block != b and physics.collidesJumpCheck(jumpSize, b):
                    self.mAction = "Jump"
                    self.mYDelta = 5
                    actorhelper.resetImageIndex(self)
                    return BehaviorTree.FAIL

    def checkSemiJump(self, block):
        # 세미 점프. 살짝 뛰는 방식이다.
        if ((self.mXDelta > 0 and block[2] - 20 < self.mXPos < block[2] - 10) or \
            (self.mXDelta < 0 and block[0] + 10 < self.mXPos < block[0] + 20)) and \
                self.mYPos <= Chan.player.mYPos + 10:
            # 바라보는 경우
            if (Chan.player.mXPos - self.mXPos) * self.mXDelta > 0:
                r = 0
            # 바라보지 않는 경우
            else:
                r = random.randint(0, 4)
            if r == 0:
                self.mAction = 'Jump'
                self.mYDelta = 3
                actorhelper.resetImageIndex(self)
                self.mSemiJump = True
                return BehaviorTree.FAIL

    def doJump(self):
        if self.mAction != 'Jump':
            return BehaviorTree.FAIL

        if self.mSemiJump:
            xMove = self.mXDelta * self.mSpeed * Chan.page.mGame.deltaTime
            self.mXPos += xMove

        yMove = self.mYDelta * self.mSpeed / 2 * Chan.page.mGame.deltaTime

        # 충돌 검사
        self.mYPos += yMove
        for block in Chan.page.map.datas['block']:
            if physics.collidesBlock(self.getBB(), block) and self.mYDelta < 0 or \
                    physics.collides(self, Chan.page.map.sideBlocks[0]) or \
                    physics.collides(self, Chan.page.map.sideBlocks[1]):
                self.mYPos -= yMove
                self.mYDelta = 0

                # 점프 후 땅에 충돌할 때 AI 재정의
                if self.mYPos <= Chan.player.mYPos + 10 and not self.mSemiJump:
                    if self.mXPos < Chan.player.mXPos:
                        self.mXDelta = 1
                    else:
                        self.mXDelta = -1

                r = random.randint(5, 15)
                self.mJumpDelay = r / 10
                self.mSemiJump = False
                self.mAction = 'Move'
                break

        return BehaviorTree.SUCCESS

    def doInBubble(self):
        if self.mAction != 'Inb':
            return BehaviorTree.FAIL

        self.mXPos = self.mBubble.mXPos
        self.mYPos = self.mBubble.mYPos

        return BehaviorTree.SUCCESS

    def doDie(self):
        return actorhelper.commonDoDie(self)

    def build_behavior_tree(self):
        self.bt = BehaviorTree.build({
            "name": "Chan",
            "class": SelectorNode,
            "children": [
                {
                    "class": LeafNode,
                    "name": "Move",
                    "function": self.doMove,
                },
                {
                    "class": LeafNode,
                    "name": "Jump",
                    "function": self.doJump,
                },
                {
                    "class": LeafNode,
                    "name": "Inb",
                    "function": self.doInBubble,
                },
                {
                    "class": LeafNode,
                    "name": "Die",
                    "function": self.doDie,
                }
            ],
        })
