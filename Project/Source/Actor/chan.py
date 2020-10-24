from pico2d import *
import actorhelper
import physics
from behaviortree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

class Chan:
    page = None
    actions = ['Move', 'Jump', 'Die']
    imageIndexs = {'Move': 4, 'Jump': 8, 'Die': 4}
    images = { }

    def __init__(self, page, xPos, yPos):
        Chan.page = page
        self.load()
        self.mImages = actorhelper.load_image(self, 'chan')
        self.mXPos = xPos
        self.mOXDelta = 1
        self.mXDelta = 1
        self.mYPos = yPos
        self.mYDelta = -5
        self.mFlip = ''
        self.mSpeed = 200
        self.mTime = 0
        self.mImageIndex = 0
        self.mAction = 'Move'
        self.mJumpDelay = 0

    def __del__(self):
        pass

    def initialize(self):
        pass

    def load(self):
        if len(Chan.images) == 0:
            actorhelper.load_image(self, 'chan')
        self.build_behavior_tree()

    def unLoad(self):
        self.removeActor(self)

    def update(self):
        # 중력 설정
        if self.mYDelta > -5:
            self.mYDelta -= 0.125

        # 점프 딜레이 설정
        self.mJumpDelay = max(0, self.mJumpDelay - Chan.page.mGame.deltaTime)

        #AI 설정
        player = Chan.page.mActors['player'][0]
        if self.mYPos < player.mYPos - 80 and self.mAction != 'Jump' \
                and self.mJumpDelay == 0 and self.mXDelta * (player.mXPos - self.mXPos) > 0:
            self.mAction = "Jump"
            self.mYDelta = 5

        # 이동
        xMove = self.mXDelta * self.mSpeed * Chan.page.mGame.deltaTime
        if self.mAction == 'Jump':
            xMove = 0.0
        yMove = self.mYDelta * self.mSpeed / 2 * Chan.page.mGame.deltaTime

        self.collideBlock(player, xMove, yMove)

        # 액션 설정
        if self.mAction != 'Jump':
            self.mAction = 'Move'

    def draw(self):
        actorhelper.commomDraw(self)

    def processInput(self, key):
        pass

    def getBB(self):
        hw = self.mImages['Move'].w // Chan.imageIndexs['Move'] / 2 - 15
        hh = self.mImages['Move'].h / 2 - 10
        return self.mXPos - hw, self.mYPos - hh, self.mXPos + hw, self.mYPos + hh

    def collideBlock(self, player, xMove, yMove):
        # 충돌 검사

        self.mXPos += xMove
        for block in Chan.page.map.sideBlocks:
            if physics.collidesBlock(self, block):
                self.mXPos -= xMove
                self.mXDelta *= -1
                break

        if self.mAction != 'Jump':
            for block in Chan.page.map.datas['block']:
                if physics.collidesBlock(self, block):
                    self.mXPos -= xMove
                    break

        collide = False
        self.mYPos += yMove
        for block in Chan.page.map.datas['block']:
            if physics.collidesBlockJump(self, block) and self.mYDelta < 0:
                self.mYPos -= yMove
                self.mYDelta = 0
                if self.mXDelta == 0:
                    self.mXDelta = self.mOXDelta
                if physics.collidesBlock(self, block):
                    self.mXPos -= xMove

                # 점프 후 땅에 충돌할 때 AI 재정의
                if self.mAction == 'Jump':
                    if self.mXPos < player.mXPos:
                        self.mXDelta = 1
                    else:
                        self.mXDelta = -1
                    self.mJumpDelay = 0.5

                self.mAction = 'Move'
                collide = True
                break

        if not collide:
            if self.mXDelta != 0:
                self.mOXDelta = self.mXDelta
            self.mXDelta = 0
            self.mJumpDelay = 0.5

    def doMove(self):
        pass

    def doJump(self):
        pass

    def doDead(self):
        pass

    def build_behavior_tree(self):
        # node_gnp = LeafNode("Get Next Position", self.set_patrol_target)
        # node_mtt = LeafNode("Move to Target", self.update_position)
        # patrol_node = SequenceNode("Patrol")
        # patrol_node.add_children(node_gnp, node_mtt)
        # self.bt = BehaviorTree(patrol_node)

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
                    "name": "Dead",
                    "function": self.doDead,
                }
                # {
                #     "name": "Chase",
                #     "class": SequenceNode,
                #     "children": [
                #         {
                #             "class": LeafNode,
                #             "name": "Find Player",
                #             "function": self.find_player,
                #         },
                #         {
                #             "class": LeafNode,
                #             "name": "Move to Player",
                #             "function": self.move_to_player,
                #         },
                #     ],
                # },
                # {
                #     "class": LeafNode,
                #     "name": "Follow Patrol positions",
                #     "function": self.follow_patrol_positions,
                # },
            ],
        })