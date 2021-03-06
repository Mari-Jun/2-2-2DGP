from Actor import actorhelper
import physics
from behaviortree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

class Banebou:
    page = None
    actions = ['Move', 'Inb', 'Die']
    imageIndexs = {'Move': 6, 'Inb': 3, 'Die': 4}
    images = { }

    def __init__(self, page, xPos, yPos, left):
        Banebou.page = page
        self.load()
        self.mImages = actorhelper.load_image(self, 'banebou')
        self.mXPos = xPos
        self.mXDelta = -1 if left else 1
        self.mYPos = yPos
        self.mYDelta = -1
        self.mFlip = ''
        self.mXSpeed = 180
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
        if len(Banebou.images) == 0:
            actorhelper.load_image(self, 'banebou')
        self.build_behavior_tree()

    def unLoad(self):
        Banebou.page.removeActor(self)

    def update(self):
        # 중력 설정
        if self.mYDelta > -3:
            self.mYDelta -= 10 * Banebou.page.mGame.deltaTime

        # 공통 부분 업데이트
        if self.mAction != 'Die':
            actorhelper.commonUpdate(self)

        if not Banebou.page.map.mStageChange:
            self.bt.run()

    def draw(self):
        actorhelper.commonDraw(self)

    def getBB(self):
        hw = self.mImages['Move'].w // Banebou.imageIndexs['Move'] / 2 - 15
        hh = self.mImages['Move'].h / 2 - 10
        return self.mXPos - hw, self.mYPos - hh, self.mXPos + hw, self.mYPos + hh

    def doMove(self):
        if self.mAction != 'Move':
            return BehaviorTree.FAIL

        # 이동
        xMove = self.mXDelta * self.mXSpeed * self.page.mGame.deltaTime
        yMove = self.mYDelta * self.mYSpeed * self.page.mGame.deltaTime

        # 충돌 검사
        self.mXPos += xMove
        for block in self.page.map.getBlockData():
            if physics.collides(self, block):
                self.mXPos -= xMove
                self.mXDelta *= -1
                break

        self.mYPos += yMove
        for block in self.page.map.getBlockData():
            if physics.collides(self, block):
                self.mYPos -= yMove
                if self.mYDelta > 0:
                    self.mYDelta = 0
                else:
                    self.mYDelta = 3
                    self.mTime = 0
                    self.mImageIndex = 0
                break

        return BehaviorTree.SUCCESS

    def doInBubble(self):
        return actorhelper.commonInBubble(self)

    def doDie(self):
        return actorhelper.commonDoDie(self)

    def build_behavior_tree(self):
        self.bt = BehaviorTree.build({
            "name": "Banebou",
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