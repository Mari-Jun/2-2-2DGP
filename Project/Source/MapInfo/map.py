from pico2d import *
from MapInfo import mapdata
import Actor

class Map:

    page = None
    maxStage = 3
    imageName = ['front']
    images = {}
    datas = {}
    ldPos = (0, 50)
    sideBlocks = [(0, 0, 40, 700), (760, 0, 800, 700)]

    def __init__(self, page):
        self.mTime = 0.0
        self.mStage = 1
        Map.page = page
        self.loadImage('front')
        self.loadMapData('block')
        self.loadMapData('enemy')
        self.loadStage()

    def loadStage(self):
        # blocks는 벽돌들로 스테이지 넘어갈때 로딩하게 구현원함
        for enemy in Map.datas['enemy'][self.mStage - 1]:
            self.loadEnemy(enemy)

    def loadImage(self, char):
        fileName = '%s/map/stage%s%s.png'

        images = []

        for stage in range(0, Map.maxStage):
            fn = fileName % (Map.page.mGame.imageDir, stage + 1, char)
            if os.path.isfile(fn):
                images.append(Map.page.mGame.imageLoader.load(fn))
                print('Map %s load complete' % stage)
            else:
                break

        Map.images[char] = images

    def loadMapData(self, data):
        fileName = '%s/map/stage%s%s.json'

        mapData = []

        for stage in range(0, Map.maxStage):
            fn = fileName % (Map.page.mGame.imageDir, stage + 1, data)
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

    def update(self):
        if len(Map.page.mActors['enemy']) == 0:
            self.mTime += Map.page.mGame.deltaTime
            if self.mTime > 5.0:
                self.mStage += 1
                self.loadStage()
        else:
            self.mTime = 0.0

    def draw(self):
        image = Map.images['front'][self.mStage - 1]
        image.draw(image.w / 2 + Map.ldPos[0], image.h / 2 + Map.ldPos[1])

        #충돌 박스 그리기
        for block in self.getBlockData():
            draw_rectangle(*block)

    def getBlockData(self):
        return Map.datas['block'][self.mStage - 1]

