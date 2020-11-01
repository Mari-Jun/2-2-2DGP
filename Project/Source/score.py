class Score:
    page = None
    def __init__(self, page, right, y):
        Score.page = page
        self.right, self.y = right, y
        self.nameImage = Score.page.mGame.imageLoader.load(Score.page.mGame.imageDir + 'scoreName.png')
        self.image = Score.page.mGame.imageLoader.load(Score.page.mGame.imageDir + 'score.png')
        self.digit_width = self.image.w // 10
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
        x = self.right
        score = self.display

        text = repr(score)
        while len(text) < 8:
            text = '0' + text

        for n in text[::-1]:
            sx = int(n) * self.digit_width
            x -= self.digit_width
            self.image.clip_draw(sx, 0, self.digit_width, self.image.h, x, self.y)

        self.nameImage.draw(x + 95, self.y + 35)

