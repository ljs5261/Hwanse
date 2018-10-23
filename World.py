from pico2d import *

class BackGround:
    def __init__(self):
        self.image = load_image('./Resource/hell1-new.jpg')

    def draw(self):
        self.image.draw(400, 300)

class Grass:
    def __init__(self):
        self.image = load_image('./Resource/hellgrass.png')


    def draw(self):
        self.image.draw(400,30)