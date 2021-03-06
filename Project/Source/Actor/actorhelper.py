from pico2d import *
import random
import math
import physics
from behaviortree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

def load_image(actor, char):
    if char in actor.images:
        return actor.images[char]

    images = {}

    fileName = 'actor/%s/%s.png'

    for action in actor.actions:
        fn = actor.page.mGame.imageDir + fileName % (char, action)
        if os.path.isfile(fn):
            action_image = actor.page.mGame.imageLoader.load(fn)
        else:
            break
        images[action] = action_image

    actor.images[char] = images
    
    return images

def commonUpdate(actor):
    if actor.mYPos < 50:
        actor.mYPos = 570
    if actor.mYPos > 570:
        col = False
        for block in actor.page.map.getBlockData():
            if physics.collides(actor, block):
                col = True
        if not col:
            actor.mYPos = 50

def commonDraw(actor):
    # 이미지 변환
    actor.mTime += actor.page.mGame.deltaTime
    if 'Inb' in actor.imageIndexs and actor.mAction == 'Inb' or\
            'Die' in actor.imageIndexs and actor.mAction == 'Die':
        actor.mImageIndex = math.floor(actor.mTime * 5)
    else:
        actor.mImageIndex = math.floor(actor.mTime * 10)

    # 액션 설정
    if actor.mAction == 'Attack' and actor.mImageIndex >= actor.imageIndexs['Attack'] or \
            actor.mAction == 'Stop' or actor.mAction == 'Move':
        if 'Stop' in actor.imageIndexs and actor.mXDelta == 0.0:
            actor.mAction = 'Stop'
        elif 'Move' in actor.imageIndexs:
            actor.mAction = 'Move'

    if actor.mAction != 'Die':
        actor.mImageIndex %= actor.imageIndexs[actor.mAction]

    commonDrawClipComposite(actor)

def commonDrawClipComposite(actor):
    if actor.mXDelta < 0.0:
        actor.mFlip = 'h'
    elif actor.mXDelta > 0.0:
        actor.mFlip = ''

    image = actor.mImages[actor.mAction]
    startX = image.w // actor.imageIndexs[actor.mAction] * actor.mImageIndex
    image.clip_composite_draw(startX, 0, image.w // actor.imageIndexs[actor.mAction], image.h, 0, actor.mFlip,
                              actor.mXPos, actor.mYPos, image.w // actor.imageIndexs[actor.mAction], image.h)

def commonSetJumpDelay(actor):
    # 점프 딜레이 설정
    actor.mJumpDelay = max(0, actor.mJumpDelay - actor.page.mGame.deltaTime)
    if abs(actor.mXPos - actor.player.mXPos) < 10:
        actor.mJumpDelay = min(0.1, actor.mJumpDelay - actor.page.mGame.deltaTime)

def commonSetAttackDelay(actor):
    #공격 딜레이 설정
    actor.mAttackDelay = max(0, actor.mAttackDelay - actor.page.mGame.deltaTime)

def commonMove(actor, x, y):
    # 이미 충돌중인지 검사
    inBlock = []
    for block in actor.page.map.getBlockData():
        if physics.collides(actor, block):
            inBlock.append(block)

    yMove = actor.mYDelta * actor.mYSpeed / 2 * actor.page.mGame.deltaTime

    if y:
        actor.mYPos += yMove
        collide = False
        for block in actor.page.map.getBlockData():
            if physics.collides(actor, block) and actor.mYDelta < 0 and \
                    (len(inBlock) == 0 or inBlock.count(block) == 0):
                actor.mYPos -= yMove
                actor.mYDelta = 0
                if actor.mXDelta == 0:
                    actor.mXDelta = actor.mOXDelta
                collide = True

                commonCheckJump(actor, block)
                commonCheckSemiJump(actor, block)
                break

        # 그냥 떨어지는 경우
        if not collide:
            if actor.mXDelta != 0:
                actor.mOXDelta = actor.mXDelta
            actor.mXDelta = 0
            actor.mJumpDelay = 0.5

    if x:
        xMove = actor.mXDelta * actor.mXSpeed * actor.page.mGame.deltaTime
        actor.mXPos += xMove
        for block in actor.page.map.getBlockData():
            if physics.collidesBlock(actor, block) and \
                    (len(inBlock) == 0 or inBlock.count(block) == 0):
                actor.mXPos -= xMove
                actor.mXDelta *= -1
                break

def commonDiagonalMove(actor):
    # 이동
    xMove = actor.mXDelta * actor.mXSpeed * actor.page.mGame.deltaTime
    yMove = actor.mYDelta * actor.mYSpeed * actor.page.mGame.deltaTime

    # 충돌 검사
    actor.mXPos += xMove
    for block in actor.page.map.getBlockData():
        if physics.collides(actor, block):
            actor.mXPos -= xMove
            actor.mXDelta *= -1
            break

    actor.mYPos += yMove
    for block in actor.page.map.getBlockData():
        if physics.collides(actor, block):
            actor.mYPos -= yMove
            actor.mYDelta *= -1
            break

def commonCheckJump(actor, block):
    if actor.mYPos < actor.player.mYPos - 60 and actor.mJumpDelay == 0:
        jumpSize = actor.getBB()
        upSize = jumpSize[-1] + 80
        jumpSize = jumpSize[0], jumpSize[1], jumpSize[2], upSize;
        for b in actor.page.map.getBlockData():
            if block != b and physics.collidesJumpCheck(jumpSize, b):
                actor.mAction = "Jump"
                actor.mYDelta = 5
                resetImageIndex(actor)

def commonCheckSemiJump(actor, block):
    # 세미 점프. 살짝 뛰는 방식이다.
    if actor.mYPos <= actor.player.mYPos + 10 and \
            ((actor.mXDelta > 0 and block[2] - 1 < actor.mXPos < block[2]) or \
            (actor.mXDelta < 0 and block[0] < actor.mXPos < block[0] + 1)):

        if actor.player.mXPos > actor.mXPos and actor.mXDelta > 0 or \
                actor.player.mXPos < actor.mXPos and actor.mXDelta < 0:
            if actor.mYPos < 60:
                r = 1
            else:
                r = 0
        else:
            r = random.randint(0, 4)

        if r == 0:
            actor.mAction = 'Jump'
            actor.mYDelta = 3
            resetImageIndex(actor)
            actor.mSemiJump = True

def commonJump(actor):
    if actor.mAction != 'Jump':
        return BehaviorTree.FAIL

    yMove = actor.mYDelta * actor.mYSpeed / 2 * actor.page.mGame.deltaTime

    #이미 충돌중인지 검사
    inBlock = []
    for block in actor.page.map.getBlockData():
        if physics.collides(actor, block):
            inBlock.append(block)

    # 충돌 검사
    actor.mYPos += yMove

    for block in actor.page.map.getBlockData():
        if physics.collides(actor, block) and actor.mYDelta < 0 and \
                (len(inBlock) == 0 or inBlock.count(block) == 0):
            actor.mYPos -= yMove
            actor.mYDelta = 0

            # 점프 후 땅에 충돌할 때 AI 재정의
            if actor.mYPos <= actor.player.mYPos + 10 and not actor.mSemiJump:
                if actor.mXPos < actor.player.mXPos:
                    actor.mXDelta = 1
                else:
                    actor.mXDelta = -1

            r = random.randint(5, 15)
            actor.mJumpDelay = r / 10
            actor.mSemiJump = False
            actor.mAction = 'Move'
            break

    if actor.mSemiJump:
        xMove = actor.mXDelta * actor.mXSpeed * actor.page.mGame.deltaTime
        actor.mXPos += xMove
        for block in actor.page.map.getBlockData():
            if physics.collidesBlock(actor, block) and \
                    (len(inBlock) == 0 or inBlock.count(block) == 0):
                actor.mXPos -= xMove
                break


    return BehaviorTree.SUCCESS

def commonInBubble(actor):
    if actor.mAction != 'Inb':
        return BehaviorTree.FAIL

    actor.mXPos = actor.mBubble.mXPos
    actor.mYPos = actor.mBubble.mYPos

    actor.mBubTime -= actor.page.mGame.deltaTime;
    if actor.mBubTime <= 0.0:
        actor.mAction = 'Move'
        actor.mBubble.mAction = 'Die'
        actor.mBubble.mEnemy = None
        resetImageIndex(actor.mBubble)
        actor.mBubble = None
        return BehaviorTree.FAIL

    return BehaviorTree.SUCCESS

def commonDoDie(actor):
    if actor.mAction != 'Die':
        return BehaviorTree.FAIL

    xMove = actor.mXDelta * actor.mXSpeed * actor.page.mGame.deltaTime
    yMove = actor.mYDelta * actor.mYSpeed / 2 * actor.page.mGame.deltaTime

    actor.mXPos += xMove
    actor.mYPos += yMove

    if actor.mImageIndex >= actor.imageIndexs['Die']:
        actor.page.mUI.score += 1000
        actor.unLoad()

    return BehaviorTree.SUCCESS

def resetImageIndex(actor):
    actor.mTime = 0.0
    actor.mImageIndex = 0