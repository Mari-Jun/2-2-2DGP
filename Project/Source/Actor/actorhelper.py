from pico2d import *
from Actor import player
import physics
from behaviortree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

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
    if actor.mYPos < 50:
        actor.mYPos = 570
    if actor.mYPos > 570:
        col = False
        for block in actor.page.map.getBlockData():
            if physics.collides(actor, block):
                col = True
        if not col:
            actor.mYPos = 50

def commomDraw(actor):
    # 이미지 변환
    actor.mTime += actor.page.mGame.deltaTime
    if 'Inb' in actor.imageIndexs and actor.mAction == 'Inb' or\
            'Die' in actor.imageIndexs and actor.mAction == 'Die':
        actor.mImageIndex = int(actor.mTime * 5)
    else:
        actor.mImageIndex = int(actor.mTime * 10)


    # 액션 설정
    if actor.mAction == 'Attack' and actor.mImageIndex > actor.imageIndexs['Attack'] or \
        actor.mAction == 'Stop' or actor.mAction == 'Move':
        if 'Stop' in actor.imageIndexs and actor.mXDelta == 0.0:
            actor.mAction = 'Stop'
        elif 'Move' in actor.imageIndexs:
            actor.mAction = 'Move'

    if actor.mAction != 'Die':
        actor.mImageIndex %= actor.imageIndexs[actor.mAction]

    if actor.mXDelta < 0.0:
        actor.mFlip = 'h'
    elif actor.mXDelta > 0.0:
        actor.mFlip = ''
    image = actor.mImages[actor.mAction]
    startX = image.w // actor.imageIndexs[actor.mAction] * actor.mImageIndex
    image.clip_composite_draw(startX, 0, image.w // actor.imageIndexs[actor.mAction], image.h, 0, actor.mFlip,
                              actor.mXPos, actor.mYPos, image.w // actor.imageIndexs[actor.mAction], image.h)

def commonDoDie(actor):
    if actor.mAction != 'Die':
        return BehaviorTree.FAIL

    xMove = actor.mXDelta * actor.mSpeed * actor.page.mGame.deltaTime
    yMove = actor.mYDelta * actor.mSpeed / 2 * actor.page.mGame.deltaTime

    actor.mXPos += xMove
    actor.mYPos += yMove

    if actor.mImageIndex >= actor.imageIndexs['Die']:
        actor.page.mScore.score += 1000
        actor.unLoad()

    return BehaviorTree.SUCCESS

def resetImageIndex(actor):
    actor.mTime = 0.0
    actor.mImageIndex = 0