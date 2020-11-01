from pico2d import *
from Actor import actorhelper
import physics
from behaviortree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

class Monsta:
    page = None
    actions = ['Move', 'Inb', 'Die']
    imageIndexs = {'Move': 2, 'Inb': 3, 'Die': 4}
    images = { }

    def __init__(self, page, xPos, yPos):
        Monsta.page = page
        self.load()
        self.mImages = actorhelper.load_image(self, 'monsta')
        self.mXPos = xPos
        self.mXDelta = -1
        self.mYPos = yPos
        self.mYDelta = -1
        self.mFlip = ''
        self.mSpeed = 200
        self.mTime = 0
        self.mImageIndex = 0
        self.mAction = 'Move'
        self.mBubble = None

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
        self.bt.run()

    def draw(self):
        actorhelper.commomDraw(self)

    def getBB(self):
        hw = self.mImages['Move'].w // Monsta.imageIndexs['Move'] / 2 - 15
        hh = self.mImages['Move'].h / 2 - 10
        return self.mXPos - hw, self.mYPos - hh, self.mXPos + hw, self.mYPos + hh

    def doMove(self):
        if self.mAction != 'Move':
            return BehaviorTree.FAIL

        # 이동
        xMove = self.mXDelta * self.mSpeed * self.page.mGame.deltaTime
        yMove = self.mYDelta * self.mSpeed * self.page.mGame.deltaTime

        # 충돌 검사
        self.mXPos += xMove
        for block in self.page.map.datas['block']:
            if physics.collides(self, block):
                self.mXPos -= xMove
                self.mXDelta *= -1
                break

        self.mYPos += yMove
        for block in self.page.map.datas['block']:
            if physics.collides(self, block):
                self.mYPos -= yMove
                self.mYDelta *= -1
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