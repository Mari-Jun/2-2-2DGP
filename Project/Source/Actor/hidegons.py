from pico2d import *
import random
from Actor import actorhelper, hidegonsAT
from behaviortree import BehaviorTree, SelectorNode, SequenceNode, LeafNode


class Hidegons:
    page = None
    player = None
    actions = ['Move', 'Jump', 'Attack', 'Inb', 'Die']
    imageIndexs = {'Move': 4, 'Jump': 4, 'Attack': 5, 'Inb': 3, 'Die': 4}
    images = {}

    def __init__(self, page, xPos, yPos, left):
        Hidegons.page = page
        Hidegons.player = page.mActors['player'][0]
        self.load()
        self.mImages = actorhelper.load_image(self, 'hidegons')
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
        self.mAttackDelay = 0
        self.mSemiJump = False
        self.mBubble = None

    def __del__(self):
        pass

    def initialize(self):
        pass

    def load(self):
        if len(Hidegons.images) == 0:
            actorhelper.load_image(self, 'hidegons')
        self.build_behavior_tree()

    def unLoad(self):
        Hidegons.page.removeActor(self)

    def update(self):
        # 중력 설정
        if self.mYDelta > -5:
            self.mYDelta -= 10 * Hidegons.page.mGame.deltaTime

        # 공통 부분 업데이트
        if self.mAction != 'Die':
            actorhelper.commonUpdate(self)

        if not Hidegons.page.map.mStageChange:
            self.bt.run()

    def draw(self):
        actorhelper.commonDraw(self)
        if self.mAction == 'Jump':
            self.mTime -= Hidegons.page.mGame.deltaTime / 2

    def getBB(self):
        hw = self.mImages['Move'].w // Hidegons.imageIndexs['Move'] / 2 - 15
        hh = self.mImages['Move'].h / 2 - 10
        return self.mXPos - hw, self.mYPos - hh, self.mXPos + hw, self.mYPos + hh

    def doMove(self):
        if self.mAction != 'Move':
            return BehaviorTree.FAIL

        actorhelper.commonSetJumpDelay(self)
        actorhelper.commonSetAttackDelay(self)
        actorhelper.commonXMove(self)
        actorhelper.commonYMove(self)

        if self.mYPos - 10 < Hidegons.player.mYPos < self.mYPos + 10 and \
                0 < self.mXDelta * (Hidegons.player.mXPos - self.mXPos) < 600 and \
                self.mAttackDelay == 0.0:
            self.mAction = 'Attack'
            self.mAttackDelay = 1.0
            fire = hidegonsAT.HidegonsAT(Hidegons.page, self.mXPos, self.mYPos, self.mXDelta)
            Hidegons.page.addActor('enemyAT', fire)
            actorhelper.resetImageIndex(self)

        return BehaviorTree.SUCCESS

    def doJump(self):
        return actorhelper.commonJump(self)

    def doAttack(self):
        if self.mAction != 'Attack':
            return BehaviorTree.FAIL

        return BehaviorTree.SUCCESS

    def doInBubble(self):
        return actorhelper.commonInBubble(self)

    def doDie(self):
        return actorhelper.commonDoDie(self)

    def build_behavior_tree(self):
        self.bt = BehaviorTree.build({
            "name": "Hidegons",
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
                    "name": "Attack",
                    "function": self.doAttack,
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
