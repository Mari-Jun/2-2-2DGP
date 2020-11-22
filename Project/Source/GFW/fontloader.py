from pico2d import *

class FontLoader:
    def __init__(self):
        self.fonts = {}

    def load(self, file, size):
        key = file + '_' + str(size)
        if key in self.fonts:
            return self.fonts[key]

        font = load_font(file, size)
        self.fonts[key] = font
        return font

    def unload(self, file, size):
        key = file + '_' + str(size)
        if key in self.fonts:
            del self.fonts[key]





