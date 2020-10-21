from pico2d import *
import mapdata
import Actor

class Map:

    page = None
    stage = 1
    maxStage = 1
    imageName = ['front', 'back']
    images = {}
    datas = {}
    ldPos = (0, 50)
    sideBlocks = [(0, 0, 40, 700), (760, 0, 800, 700)]

    def __init__(self, page):
        Map.page = page
        self.load()

    def load(self):
        Map.loadImage('front')
        Map.loadImage('back')

        #blocks는 벽돌들로 스테이지 넘어갈때 로딩하게 구현원함
        Map.datas.clear()
        Map.datas['block'] = Map.loadMapData(Map.stage, 'block')
        Map.datas['enemy'] = Map.loadMapData(Map.stage, 'enemy')
        for enemy in Map.datas['enemy']:
            self.loadEnemy(enemy)

    @staticmethod
    def loadImage(char):
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

    @staticmethod
    def loadMapData(stage, data):
        fileName = '%s/map/stage%s%s.json'
        fn = fileName % (Map.page.mGame.imageDir, stage, data)
        return mapdata.load(fn, data, Map.ldPos)

    def loadEnemy(self, enemy):
        if enemy[0] == 'chan':
            chan = Actor.chan.Chan(Map.page, enemy[1], enemy[2])
            Map.page.addActor('enemy', chan)
        elif enemy[0] == 'monsta':
            monsta = Actor.monsta.Monsta(Map.page, enemy[1], enemy[2])
            Map.page.addActor('enemy', monsta)
        elif enemy[0] == 'banebou':
            banebou = Actor.banebou.Banebou(Map.page, enemy[1], enemy[2])
            Map.page.addActor('enemy', banebou)

    def update(self):
        pass

    def draw(self):
        image = Map.images['back'][Map.stage - 1]
        image.draw(image.w / 2 + Map.ldPos[0], image.h / 2 + Map.ldPos[1])
        image = Map.images['front'][Map.stage - 1]
        image.draw(image.w / 2 + Map.ldPos[0], image.h / 2 + Map.ldPos[1])

        #충돌 박스 그리기
        for block in Map.datas['block']:
            draw_rectangle(*block)


