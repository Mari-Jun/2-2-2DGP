import random
from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('../Image/grass.png')
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self, y=85, dx=2):
        self.image = load_image('../Image/run_animation.png')
        self.x, self.y = random.randint(0, 300), y
        self.dx = dx
        self.frame_index = random.randint(0, 7)
        self.action = 0
    def draw(self):
        self.image.clip_draw(self.frame_index * 100, 0, 100, 100, self.x, self.y)
    def update(self):
        self.frame_index = (self.frame_index + 1) % 8
        self.x += self.dx