from pico2d import *
import physics

def load_image(actor, char):
    if char in actor.images:
        return actor.images[char]

    images = {}

    fileName = '%s/actor/%s/%s.png'

    for action in actor.actions:
        fn = fileName % (actor.page.mGame.imageDir, char, action)
        if os.path.isfile(fn):
            action_image = actor.page.mGame.imageLoader.load(fn)
        else:
            break
        images[action] = action_image

    actor.images[char] = images

    print('actor %s load complete' % char)
    return images

def commomUpdate(actor):
    # 중력 설정
    if actor.mYDelta > -5:
        actor.mYDelta -= 0.125

    # 이동
    xMove = actor.mXDelta * actor.mSpeed * actor.page.mGame.deltaTime
    yMove = actor.mYDelta * actor.mSpeed / 2 * actor.page.mGame.deltaTime

    # 충돌 검사
    actor.mXPos += xMove
    for block in actor.page.map.sideBlocks:
        if physics.collidesBlock(actor, block):
            actor.mXPos -= xMove
            break

    if actor.mAction != 'Jump':
        for block in actor.page.map.datas['block']:
            if physics.collidesBlock(actor, block):
                actor.mXPos -= xMove
                break

    actor.mYPos += yMove
    for block in actor.page.map.datas['block']:
        if physics.collidesBlock(actor, block) and actor.mYDelta < 0:
            actor.mYPos -= yMove
            actor.mYDelta = 0
            if physics.collidesBlock(actor, block):
                actor.mXPos -= xMove
            if actor.mAction != 'Attack':
                actor.mAction = 'Stop' if actor.mXDelta == 0 and 'Stop' in actor.actions else 'Move'
            break

    # 액션 설정
    if actor.mAction != 'Attack' and actor.mAction != 'Jump':
        actor.mAction = 'Stop' if actor.mXDelta == 0 and 'Stop' in actor.actions else 'Move'

    # 이미지 변환
    actor.mTime += actor.page.mGame.deltaTime
    actor.mImageIndex = int(actor.mTime * 10)

    # 액션 재설정
    if actor.mAction == 'Attack' and actor.mImageIndex > actor.imageIndexs['Attack']:
        actor.mAction = 'Stop' if actor.mXDelta == 0 else 'Move'

    actor.mImageIndex %= actor.imageIndexs[actor.mAction]

def commomDraw(actor):
    if actor.mXDelta < 0:
        actor.mFlip = 'h'
    elif actor.mXDelta > 0:
        actor.mFlip = ''
    image = actor.mImages[actor.mAction]
    startX = image.w // actor.imageIndexs[actor.mAction] * actor.mImageIndex
    image.clip_composite_draw(startX, 0, image.w // actor.imageIndexs[actor.mAction], image.h, 0, actor.mFlip,
                              actor.mXPos, actor.mYPos, image.w // actor.imageIndexs[actor.mAction], image.h)

def attack(actor):
    if not actor.mAction == 'Attack':
        actor.mTime = 0
        actor.mImageIndex = 0
        actor.mAction = 'Attack'

def jump(actor):
    if actor.mAction != 'Jump' and actor.mYDelta == 0:
        actor.mTime = 0
        actor.mImageIndex = 0
        actor.mAction = 'Jump'
        actor.mYDelta = 5