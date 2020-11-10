class UI:
    page = None
    player = None
    def __init__(self, page, player, right, y):
        UI.page = page
        UI.player = player
        self.right, self.y = right, y
        self.scoreNameImage = UI.page.mGame.imageLoader.load(UI.page.mGame.imageDir + 'scoreName.png')
        self.lifeNameImage =  UI.page.mGame.imageLoader.load(UI.page.mGame.imageDir + 'lifeName.png')
        self.stageNameImage =  UI.page.mGame.imageLoader.load(UI.page.mGame.imageDir + 'stageName.png')
        self.scoreimage = UI.page.mGame.imageLoader.load(UI.page.mGame.imageDir + 'score.png')
        self.itemimage = UI.page.mGame.imageLoader.load(UI.page.mGame.imageDir + 'Item/reinforce.png')
        self.digit_width = self.scoreimage.w // 10
        self.reset()

    def reset(self):
        self.score = 0
        self.display = 0

    def update(self):
        if self.display < self.score:
            dt = self.score - self.display
            if 10000 <= dt:
                self.display += 1000
            elif 1000 <= dt < 10000:
                self.display += 100
            elif 100 <= dt < 1000:
                self.display += 10
            else:
                self.display += 1

    def draw(self):
        self.drawScore()
        self.drawLife()
        self.drawStage()
        self.drawItem()

    def drawScore(self):
        x = self.right
        score = self.display

        text = repr(score)
        while len(text) < 8:
            text = '0' + text

        for n in text[::-1]:
            sx = int(n) * self.digit_width
            x -= self.digit_width
            self.scoreimage.clip_draw(sx, 0, self.digit_width, self.scoreimage.h, x, self.y)

        self.scoreNameImage.draw(x + 95, self.y + 35)

    def drawLife(self):
        x = self.right - 490
        self.lifeNameImage.draw(x + 40, self.y + 35)

        life = repr(UI.player.mLife)
        while len(life) < 2:
            life = '0' + life

        for n in life:
            sx = int(n) * self.digit_width
            x += self.digit_width
            self.scoreimage.clip_draw(sx, 0, self.digit_width, self.scoreimage.h, x, self.y)

    def drawStage(self):
        x = self.right + 130
        self.stageNameImage.draw(x + 50, self.y + 35)

        stage = repr(UI.page.map.mStage)
        while len(stage) < 3:
            stage = '0' + stage

        for n in stage:
            sx = int(n) * self.digit_width
            x += self.digit_width
            self.scoreimage.clip_draw(sx, 0, self.digit_width, self.scoreimage.h, x, self.y)

    def drawItem(self):
        x = 30
        y = 25
        sx = 0
        for item in UI.player.mHasItem:
            if item:
                self.itemimage.clip_draw(sx, 0, self.itemimage.w // 4, self.itemimage.h, x+sx, y)
            sx += self.itemimage.w // 4
