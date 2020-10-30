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
    pass

def commomDraw(actor):
    # 이미지 변환
    actor.mTime += actor.page.mGame.deltaTime
    actor.mImageIndex = int(actor.mTime * 10)

    # 액션 설정
    if actor.mAction == 'Attack' and actor.mImageIndex > actor.imageIndexs['Attack'] or \
        actor.mAction == 'Stop' or actor.mAction == 'Move':
        if 'Stop' in actor.imageIndexs and actor.mXDelta == 0:
            actor.mAction = 'Stop'
        elif 'Move' in actor.imageIndexs:
            actor.mAction = 'Move'

    actor.mImageIndex %= actor.imageIndexs[actor.mAction]

    if actor.mXDelta < 0:
        actor.mFlip = 'h'
    elif actor.mXDelta > 0:
        actor.mFlip = ''
    image = actor.mImages[actor.mAction]
    startX = image.w // actor.imageIndexs[actor.mAction] * actor.mImageIndex
    image.clip_composite_draw(startX, 0, image.w // actor.imageIndexs[actor.mAction], image.h, 0, actor.mFlip,
                              actor.mXPos, actor.mYPos, image.w // actor.imageIndexs[actor.mAction], image.h)

def resetImageIndex(actor):
    actor.mTime = 0
    actor.mImageIndex = 0