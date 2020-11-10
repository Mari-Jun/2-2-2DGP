import random

class Item:
    Page = None
    def __init__(self, page, force):
        Item.Page = page
        block = page.map.mItemBlock
        blockSelect = random.randint(0, len(block) - 1)
        self.mReinForce = force
        self.mItem = random.randint(0, 3)
        self.mImage = page.mGame.imageLoader.load(page.mGame.imageDir + 'Item/reinforce.png')
        self.mBB = self.mImage.w // 4, self.mImage.h
        self.mXPos = random.randint(block[blockSelect][0] + self.mBB[0] // 2, block[blockSelect][2] - self.mBB[0] // 2)
        self.mYPos = block[blockSelect][3] + self.mBB[1] // 2
        self.mTime = 10.0

    def unload(self):
        Item.Page.removeActor(self)

    def update(self):
        self.mTime -= Item.Page.mGame.deltaTime
        if self.mTime < 0.0:
            self.unload()

    def draw(self):
        startX = self.mBB[0] * self.mItem
        self.mImage.clip_draw(startX, 0, self.mBB[0],  self.mBB[1], self.mXPos, self.mYPos,  self.mBB[0], self.mBB[1])

    def getBB(self):
        return self.mXPos - self.mBB[0] // 2, self.mYPos - self.mBB[1] // 2,\
               self.mXPos + self.mBB[0] // 2, self.mYPos + self.mBB[1] // 2

