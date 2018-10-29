from pico2d import *


class BackGround:
    def __init__(self):
        self.image = load_image('./Resource/grassland.png')
        self.x, self.y = 400, 300

    def draw(self):
        self.image.draw(self.x, self.y)

    def move(self):
        self.x -= 2