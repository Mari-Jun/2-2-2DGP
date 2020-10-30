from pico2d import *
from Actor import actorhelper
import physics
from behaviortree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

class Bubble:
    page = None
    actions = ['Attack', 'Move', 'Die']
    imageIndexs = {'Attack': 7, 'Move': 1, 'Die': 1}
    images = { }

    def __init__(self, page):
        Bubble.page = page
        self.load()
        self.mImages = actorhelper.load_image(self, 'bubble')
        self.mBB = self.mImages['Move'].w // Bubble.imageIndexs['Move'] / 2 - 14, self.mImages['Move'].h / 2 - 13
        player = page.mActors['player'][0]
        self.mXDelta = -1 if player.mFlip == 'h' else 1
        self.mYDelta = 1 if player.mYPos < 430 else -1
        self.mXPos = player.mXPos + self.mXDelta * (player.mBB[0] + self.mBB[0])
        self.mYPos = player.mYPos
        self.mSpeed = 350
        self.mLength = 300
        self.mAttack = True
        self.mTime = 0
        self.mImageIndex = 0
        self.mAction = 'Attack'
        self.mEnemy = None

        #생성 위치가 충돌 위치라면
        for block in Bubble.page.map.datas['block']:
            if physics.collides(self, block):
                self.unLoad()

    def load(self):
        if len(Bubble.images) == 0:
            actorhelper.load_image(self, 'bubble')
        self.build_behavior_tree()

    def unLoad(self):
        Bubble.page.removeActor(self)

    def update(self):
        self.bt.run()

    def draw(self):
        # 이미지 변환
        self.mTime += self.page.mGame.deltaTime
        if self.mAction == 'Die':
            self.mImageIndex = int(self.mTime * 2)
        else:
            self.mImageIndex = int(self.mTime * 10)
            self.mImageIndex %= self.imageIndexs[self.mAction]

        image = self.mImages[self.mAction]
        startX = image.w // self.imageIndexs[self.mAction] * self.mImageIndex
        image.clip_draw(startX, 0, image.w // self.imageIndexs[self.mAction], image.h,
                        self.mXPos, self.mYPos, image.w // self.imageIndexs[self.mAction], image.h)

    def processInput(self, key):
        pass

    def getBB(self):
        return self.mXPos - self.mBB[0], self.mYPos - self.mBB[1], self.mXPos + self.mBB[0], self.mYPos + self.mBB[1]

    def collidePlayer(self):
        for player in Bubble.page.mActors['player']:
            if physics.collides(self, player.getBB()):
                if abs(player.mXDelta) < abs(player.mYDelta):
                    if self.mEnemy is not None:
                        self.mEnemy.mAction = 'Die'
                        actorhelper.resetImageIndex(self.mEnemy)
                    self.mAction = 'Die'
                    actorhelper.resetImageIndex(self)
                else:
                    self.mLength = 50
                    self.mSpeed = 300
                    self.mXDelta = player.mXDelta
                    self.mYDelta = 1

    def collideBubble(self):
        pass

    def collideEnemy(self):
        for enemy in Bubble.page.mActors['enemy']:
            if physics.collides(self, enemy.getBB()) and self.mEnemy is None and enemy.mBubble is None:
                enemy.mAction = 'Inb'
                enemy.mBubble = self
                self.mEnemy = enemy
                self.mAction = 'Move'
                self.mSpeed = 100
                actorhelper.resetImageIndex(enemy)

    def collideBlock(self, xMove):
        if self.mYDelta != 0:
            for block in Bubble.page.map.datas['block']:
                if physics.collides(self, block):
                    self.mXPos -= xMove
                    break

    def doAttack(self):
        if self.mAction != 'Attack':
            return BehaviorTree.FAIL

        # 이동
        xMove = self.mXDelta * self.mSpeed * Bubble.page.mGame.deltaTime

        self.mXPos += xMove
        if self.mImageIndex + 1 == Bubble.imageIndexs['Attack']:
            self.mAction = 'Move'
            self.mSpeed = 100
            return BehaviorTree.FAIL

        # 충돌 검사
        self.collideBlock(xMove)
        self.collideEnemy()

        return BehaviorTree.SUCCESS

    def doMove(self):
        if self.mAction != 'Move':
            return BehaviorTree.FAIL

        xMove = self.mXDelta * self.mSpeed * Bubble.page.mGame.deltaTime
        yMove = self.mYDelta * self.mSpeed * Bubble.page.mGame.deltaTime

        self.mXPos += xMove
        self.mYPos += yMove
        self.mXDelta = 0
        # 임시로 뭉쳐놓기
        if 430 < self.mYPos < 450:
            if self.mXPos >= get_canvas_width() / 2 + 10:
                self.mXDelta = -1
            elif self.mXPos <= get_canvas_width() / 2 - 10:
                self.mXDelta = 1
        elif self.mYPos <= 430:
            self.mYDelta = 1
        else:
            self.mYDelta = -1

        # 충돌 검사
        self.collidePlayer()
        self.collideBlock(xMove)

        return BehaviorTree.SUCCESS

    def doDie(self):
        if self.mAction != 'Die':
            return BehaviorTree.FAIL

        if self.mImageIndex >= Bubble.imageIndexs['Die']:
            self.unLoad()

        return BehaviorTree.SUCCESS

    def build_behavior_tree(self):
        self.bt = BehaviorTree.build({
            "name": "Bubble",
            "class": SelectorNode,
            "children": [
                {
                    "class": LeafNode,
                    "name": "Attack",
                    "function": self.doAttack,
                },
                {
                    "class": LeafNode,
                    "name": "Move",
                    "function": self.doMove,
                },
                {
                    "class": LeafNode,
                    "name": "Die",
                    "function": self.doDie,
                }
            ],
        })