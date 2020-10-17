from pico2d import *
import physics

class Player:

    keyMap = {
        (SDL_KEYDOWN, SDLK_LEFT):  (-1,  0),
        (SDL_KEYDOWN, SDLK_RIGHT): ( 1,  0),
        (SDL_KEYDOWN, SDLK_DOWN):  ( 0, -1),
        (SDL_KEYDOWN, SDLK_UP):    ( 0,  1),
        (SDL_KEYUP, SDLK_LEFT):    ( 1,  0),
        (SDL_KEYUP, SDLK_RIGHT):   (-1,  0),
        (SDL_KEYUP, SDLK_DOWN):    ( 0,  1),
        (SDL_KEYUP, SDLK_UP):      ( 0, -1),
    }
    KEYDOWN_JUMP = (SDL_KEYDOWN, SDLK_UP)
    KEYDOWN_ATTACK = (SDL_KEYDOWN, SDLK_SPACE)

    page = None
    actions = ['Stop', 'Move', 'Jump', 'Attack', 'Die']
    imageIndex = {'Stop': 3, 'Move': 5, 'Jump': 8, 'Attack': 4, 'Die': 2}
    images = { }

    def __init__(self, page):
        Player.page = page
        self.load()

        self.images = Player.load_image('green')
        self.xPos = 100
        self.xDelta = 0
        self.yPos = 100
        self.yDelta = 0
        self.flip = ''
        self.speed = 200
        self.time = 0
        self.imageIndex = 0
        self.action = 'Stop'

    def __del__(self):
        pass

    def initialize(self):
        pass

    def load(self):
        if len(Player.images) == 0:
            Player.load_all_images()

    @staticmethod
    def load_all_images():
        Player.load_image('green')

    @staticmethod
    def load_image(char):
        if char in Player.images:
            return Player.images[char]

        images = {}

        fileName = '%s/dragon/%s/player_%s.png'

        for action in Player.actions:
            fn = fileName % (Player.page.mGame.imageDir, char, action)
            if os.path.isfile(fn):
                action_image = Player.page.mGame.imageLoader.load(fn)
            else:
                break
            images[action] = action_image

        Player.images[char] = images

        print('player %s load complete' % char)
        return images

    def unLoad(self):
        self.removeActor(self)

    def update(self):
        # 이동
        xMove = self.xDelta * self.speed * Player.page.mGame.deltaTime
        yMove = self.yDelta * self.speed * Player.page.mGame.deltaTime

        #충돌 검사
        self.xPos += xMove
        self.yPos += yMove
        for block in Player.page.map.blocks:
            if physics.collidesBlock(self, block):
                self.xPos -= xMove
                self.yPos -= yMove
                break;


        # 액션 설정
        if not self.action == 'Attack':
            self.action = 'Stop' if self.xDelta == 0 else 'Move'

        #이미지 변환
        self.time += Player.page.mGame.deltaTime
        self.imageIndex = int(self.time * 10)

        #액션 재설정
        if self.action == 'Attack' and self.imageIndex > Player.imageIndex['Attack']:
            self.action = 'Stop' if self.xDelta == 0 else 'Move'

        self.imageIndex %= Player.imageIndex[self.action]

    def draw(self):
        image = self.images[self.action]
        startX = image.w // Player.imageIndex[self.action] * self.imageIndex
        image.clip_composite_draw(startX, 0, image.w // Player.imageIndex[self.action], image.h, 0, self.flip,
                                  self.xPos, self.yPos, image.w // Player.imageIndex[self.action], image.h)
        #print('%d %d, %d' % (startX, image.w // Player.imageIndex[self.action], image.h))

    def processInput(self, key):
        pair = (key.type, key.key)
        if pair in Player.keyMap:
            self.xDelta += Player.keyMap[pair][0]
            self.yDelta += Player.keyMap[pair][1]
            if self.xDelta < 0:
                self.flip = 'h'
            elif self.xDelta > 0:
                self.flip = ''
        elif pair == Player.KEYDOWN_ATTACK:
            self.attack()

    def attack(self):
        if not self.action == 'Attack':
            self.time = 0
            self.imageIndex = 0
            self.action = 'Attack'

    def getBB(self):
        hw = self.images[self.action].w // Player.imageIndex[self.action] / 2 - 10
        hh = self.images[self.action].h / 2 - 10
        return self.xPos - hw, self.yPos - hh, self.xPos + hw, self.yPos + hh

