from pico2d import *

class ImageLoader:
    def __init__(self):
        self.images = {}

    def load(self, fileName):
        if fileName in self.images:
            return self.images[fileName]

        image = load_image(fileName)
        self.images[fileName] = image
        return image

    def unload(self, fileName):
        if fileName in self.images:
            del self.images[fileName]

