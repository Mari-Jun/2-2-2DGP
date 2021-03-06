from pico2d import *
from MapInfo import mapdata
import Actor

class Map:

    page = None
    maxStage = 20
    imageName = ['front']
    images = {}
    datas = {}
    dataPos = []
    ldPos = (0, 50)

    def __init__(self, page):
        self.mTime = 0.0
        self.mStage = 1
        self.mStageChange = True
        Map.page = page
        self.loadImage('front')
        self.loadPlayerPos()
        self.loadMapData('block')
        self.loadMapData('enemy')
        self.loadStage()

    def loadStage(self):
        for enemy in Map.page.mActors['enemy']:
            enemy.mAction = 'Die'
        for enemy in Map.datas['enemy'][self.mStage - 1]:
            self.loadEnemy(enemy)
        for bubble in Map.page.mActors['bubble']:
            bubble.mAction = 'Die'
        for item in Map.page.mActors['item']:
            item.mTime = 0
        self.moveX = Map.dataPos[self.mStage - 1][0] - Map.page.mActors['player'][0].mXPos
        self.moveY = Map.dataPos[self.mStage - 1][1] - Map.page.mActors['player'][0].mYPos
        self.mItemBlock = []
        for block in Map.datas['block'][self.mStage - 1]:
            if block[0] < 760 and block[1] < 500 and block[2] > 40 and block[2] - block[0] > 40:
                self.mItemBlock.append(block)

    def loadImage(self, char):
        fileName = 'map/stage%s%s.png'

        images = []

        for stage in range(0, Map.maxStage):
            fn = Map.page.mGame.imageDir + fileName % (stage + 1, char)
            if os.path.isfile(fn):
                images.append(Map.page.mGame.imageLoader.load(fn))
            else:
                break

        Map.images[char] = images

    def loadPlayerPos(self):
        fn = Map.page.mGame.mapDir + 'datapos.json'
        if os.path.isfile(fn):
            Map.dataPos = mapdata.loadDataPos(fn, Map.ldPos)

    def loadMapData(self, data):
        fileName = 'stage%s%s.json'

        mapData = []

        for stage in range(0, Map.maxStage):
            fn = Map.page.mGame.mapDir + fileName % (stage + 1, data)
            if os.path.isfile(fn):
                mapData.append(mapdata.load(fn, data, Map.ldPos))

        Map.datas[data] = mapData

    def loadEnemy(self, enemy):
        if enemy[0] == 'chan':
            chan = Actor.chan.Chan(Map.page, enemy[1], enemy[2], enemy[3])
            Map.page.addActor('enemy', chan)
        elif enemy[0] == 'monsta':
            monsta = Actor.monsta.Monsta(Map.page, enemy[1], enemy[2], enemy[3])
            Map.page.addActor('enemy', monsta)
        elif enemy[0] == 'banebou':
            banebou = Actor.banebou.Banebou(Map.page, enemy[1], enemy[2], enemy[3])
            Map.page.addActor('enemy', banebou)
        elif enemy[0] == 'hidegons':
            hidegons = Actor.hidegons.Hidegons(Map.page, enemy[1], enemy[2], enemy[3])
            Map.page.addActor('enemy', hidegons)
        elif enemy[0] == 'invator':
            invator = Actor.invator.Invator(Map.page, enemy[1], enemy[2], enemy[3])
            Map.page.addActor('enemy', invator)

    def update(self):
        if len(Map.page.mActors['enemy']) == 0:
            self.mTime += Map.page.mGame.deltaTime
            if self.mTime > 8.0:
                if self.mStage == Map.maxStage:
                    Map.page.mEndGame = True
                else:
                    self.mStage += 1
                    self.loadStage()
                    self.mStageChange = True
                    self.mTime = 0.0

        if self.mStageChange:
            self.mTime += Map.page.mGame.deltaTime
            Map.page.mActors['player'][0].mXPos += self.moveX * Map.page.mGame.deltaTime / 2
            Map.page.mActors['player'][0].mYPos += self.moveY * Map.page.mGame.deltaTime / 2


    def draw(self):
        if self.mStageChange:
            self.divideY = round(275 * self.mTime)

            if self.mStage > 1:
                bImage = Map.images['front'][self.mStage - 2]
                bImage.clip_draw_to_origin(0, 0, bImage.w, bImage.h - self.divideY, \
                                           0, 50 + self.divideY, bImage.w, bImage.h - self.divideY)

            nImage = Map.images['front'][self.mStage - 1]
            nImage.clip_draw_to_origin(0, nImage.h - self.divideY, nImage.w, self.divideY,\
                                       0, 50,  nImage.w, self.divideY)
            if self.divideY > nImage.h:
                self.mStageChange = False

        else:
            image = Map.images['front'][self.mStage - 1]
            image.draw_to_origin(0, 50)

        # #충돌 박스 그리기
        # for block in self.getBlockData():
        #     draw_rectangle(*block)

    def getBlockData(self):
        return Map.datas['block'][self.mStage - 1]

