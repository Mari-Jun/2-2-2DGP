from pico2d import *
import random
from Actor import actorhelper, invatorAT
from behaviortree import BehaviorTree, SelectorNode, SequenceNode, LeafNode


class Invator:
    page = None
    player = None
    actions = ['Move', 'Attack', 'Inb', 'Die']
    imageIndexs = {'Move': 2, 'Attack': 6, 'Inb': 3, 'Die': 4}
    images = {}

    def __init__(self, page, xPos, yPos, left):
        Invator.page = page
        Invator.player = page.mActors['player'][0]
        self.load()
        self.mImages = actorhelper.load_image(self, 'invator')
        self.mXPos = xPos
        self.mXDelta = -1 if left else 1
        self.mYPos = yPos
        self.mYDelta = -1
        self.mFlip = ''
        self.mXSpeed = 100
        self.mYSpeed = 100
        self.mTime = 0
        self.mImageIndex = 0
        self.mAction = 'Move'
        self.mAttackDelay = 2.0
        self.mBubble = None

    def __del__(self):
        pass

    def initialize(self):
        pass

    def load(self):
        if len(Invator.images) == 0:
            actorhelper.load_image(self, 'invator')
        self.build_behavior_tree()

    def unLoad(self):
        Invator.page.removeActor(self)

    def update(self):
        # 공통 부분 업데이트
        if self.mAction != 'Die':
            actorhelper.commonUpdate(self)

        if not Invator.page.map.mStageChange:
            self.bt.run()

    def draw(self):
        actorhelper.commonDraw(self)

    def getBB(self):
        hw = self.mImages['Move'].w // Invator.imageIndexs['Move'] / 2 - 15
        hh = self.mImages['Move'].h / 2 - 10
        return self.mXPos - hw, self.mYPos - hh, self.mXPos + hw, self.mYPos + hh

    def doMove(self):
        if self.mAction != 'Move':
            return BehaviorTree.FAIL

        actorhelper.commonSetAttackDelay(self)
        actorhelper.commonDiagonalMove(self)

        if self.mAttackDelay == 0.0:
            self.mAction = 'Attack'
            self.mAttackDelay = random.randint(5, 10) * 0.2
            fire = invatorAT.InvatorAT(Invator.page, self.mXPos, self.mYPos)
            Invator.page.addActor('enemy', fire)
            actorhelper.resetImageIndex(self)

        return BehaviorTree.SUCCESS

    def doAttack(self):
        if self.mAction != 'Attack':
            return BehaviorTree.FAIL

        actorhelper.commonDiagonalMove(self)

        return BehaviorTree.SUCCESS

    def doInBubble(self):
        return actorhelper.commonInBubble(self)

    def doDie(self):
        return actorhelper.commonDoDie(self)

    def build_behavior_tree(self):
        self.bt = BehaviorTree.build({
            "name": "Invator",
            "class": SelectorNode,
            "children": [
                {
                    "class": LeafNode,
                    "name": "Move",
                    "function": self.doMove,
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
