from pico2d import *
import Stage2_state
import game_framework
import random

PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 3                 # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second, 75

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

point_list = [(20, 300), (400, 580), (780, 300), (400, 90)]


class FlyState:
    @staticmethod
    def do(smashu, p1, p2):
        smashu.frame = (smashu.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        smashu.t += 1 / 100
        smashu.x = (1 - smashu.t) * p1[0] + smashu.t * p2[0]
        smashu.y = (1 - smashu.t) * p1[1] + smashu.t * p2[1]

    @staticmethod
    def draw(smashu):
        smashu.image.clip_draw(int(smashu.frame) * 100, 0, 100, 100, smashu.x, smashu.y)
        draw_rectangle(*smashu.get_bb())


class Smashu:

    def __init__(self):
        self.x = 400
        self.y = 90
        self.image = load_image('./Resource/smashu.png')
        self.frame = 0
        self.velocity = RUN_SPEED_PPS
        self.life = 500
        self.t = 0
        self.cur_state = FlyState
        self.i = -1

    def draw(self):
        self.cur_state.draw(self)

    def update(self):
        self.cur_state.do(self, point_list[self.i], point_list[self.i+1])
        if self.t >= 1:
            self.t = 0
            self.i += 1
            if self.i == 3:
                self.i = -1

        ataho = Stage2_state.get_ataho()
        if Stage2_state.collide(self, ataho):
            ataho.life -= 50
            print(ataho.life)
            at_x1, at_y1, at_x2, at_y2 = ataho.get_bb()
            x1, y1, x2, y2 = self.get_bb()
            if x1 < at_x2 < x1 + 20:
                ataho.x -= 60
            elif x2 - 20 < at_x1 < x2:
                ataho.x += 60
            elif at_y1 < y2:
                ataho.y = 270
                ataho.velocity = 0

    def get_bb(self):
        return self.x - 45, self.y - 45, self.x + 45, self.y + 45
