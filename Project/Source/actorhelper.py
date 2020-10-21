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