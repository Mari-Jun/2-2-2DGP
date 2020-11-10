from pico2d import *
from Actor import actorhelper
import physics
from behaviortree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

class Monsta:
    page = None
    actions = ['Move', 'Inb', 'Die']
    imageIndexs = {'Move': 2, 'Inb': 3, 'Die': 4}
    images = { }

    def __init__(self, page, xPos, yPos, left):
        Monsta.page = page
        self.load()
        self.mImages = actorhelper.load_image(self, 'monsta')
        self.mXPos = xPos
        self.mXDelta = -1 if left else 1
        self.mYPos = yPos
        self.mYDelta = -1
        self.mFlip = ''
        self.mXSpeed = 200
        self.mYSpeed = 200
        self.mTime = 0
        self.mImageIndex = 0
        self.mAction = 'Move'
        self.mBubble = None
        self.mBubTime = 0

    def __del__(self):
        pass

    def initialize(self):
        pass

    def load(self):
        if len(Monsta.images) == 0:
            actorhelper.load_image(self, 'Monsta')
        self.build_behavior_tree()

    def unLoad(self):
        Monsta.page.removeActor(self)

    def update(self):
        # 공통 부분 업데이트
        if self.mAction != 'Die':
            actorhelper.commonUpdate(self)

        if not Monsta.page.map.mStageChange:
            self.bt.run()

    def draw(self):
        actorhelper.commonDraw(self)

    def getBB(self):
        hw = self.mImages['Move'].w // Monsta.imageIndexs['Move'] / 2 - 15
        hh = self.mImages['Move'].h / 2 - 10
        return self.mXPos - hw, self.mYPos - hh, self.mXPos + hw, self.mYPos + hh

    def doMove(self):
        if self.mAction != 'Move':
            return BehaviorTree.FAIL

        actorhelper.commonDiagonalMove(self)

        return BehaviorTree.SUCCESS

    def doInBubble(self):
        return actorhelper.commonInBubble(self)

    def doDie(self):
        return actorhelper.commonDoDie(self)

    def build_behavior_tree(self):
        self.bt = BehaviorTree.build({
            "name": "Monsta",
            "class": SelectorNode,
            "children": [
                {
                    "class": LeafNode,
                    "name": "Move",
                    "function": self.doMove,
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