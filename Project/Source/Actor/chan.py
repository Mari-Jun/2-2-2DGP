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

        # 공통 부분 업데이트
        if self.mAction != 'Die':
            actorhelper.commomUpdate(self)

        if not Chan.page.map.mStageChange:
            self.bt.run()

    def draw(self):
        actorhelper.commomDraw(self)

    def getBB(self):
        hw = self.mImages['Move'].w // Chan.imageIndexs['Move'] / 2 - 15
        hh = self.mImages['Move'].h / 2 - 10
        return self.mXPos - hw, self.mYPos - hh, self.mXPos + hw, self.mYPos + hh

    def doMove(self):
        return actorhelper.commomMove(self)

    def doJump(self):
        return actorhelper.commomJump(self)

    def doInBubble(self):
        return actorhelper.commomInBubble(self)

    def doDie(self):
        return actorhelper.commomDoDie(self)

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
