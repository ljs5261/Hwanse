from pico2d import *


class Enemy:
    RIGHT_RUN, LEFT_RUN, RIGHT_STAND, LEFT_STAND = 0, 1, 2, 3
    def __init__(self):
        self.x, self.y = 850, 70
        self.frame = 0
        self.image = load_image('./Resource/wolf3.png')
        self.state = 2
        self.dead = False

    def update(self):
        self.frame = (self.frame + 1) % 5
        self.x -= 10

    def draw(self):
        self.image.clip_draw(self.frame*64, 0, 64, 32, self.x, self.y)