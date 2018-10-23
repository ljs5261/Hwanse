from pico2d import *


class JangPung:
    def __init__(self,x, dir):
        self.x, self.y =x , 70
        if(dir==0):
            self.dir = 1
        else:
            self.dir = -1
        self.frame = 0
        self.image = load_image('./Resource/JangPung.png')

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.x += self.dir * 15

    def draw(self):
        self.image.clip_draw(self.frame*35, 0, 35, 42, self.x, self.y)