from pico2d import *
import Stage2_state
import game_framework
import random

PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 3                 # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second, 75

TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3


class Rinshang:

    def __init__(self):
        self.x = 2200
        self.y = 90
        self.image = load_image('./Resource/rinshang_skill.png')
        self.frame = 0
        self.velocity = RUN_SPEED_PPS
        self.life = 500

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        self.x -= (self.velocity * game_framework.frame_time)

        ataho = Stage2_state.get_ataho()
        if Stage2_state.collide(self, ataho):
            ataho.life -= 30
            print(ataho.life)
            at_x1, at_y1, at_x2, at_y2 = ataho.get_bb()
            x1, y1, x2, y2 = self.get_bb()
            if x1 < at_x2 < x1 + 20:
                ataho.x -= 10
            elif x2 - 20 < at_x1 < x2:
                ataho.x += 10
            elif at_y1 < y2:
                ataho.y = 200
                ataho.velocity = 0

    def get_bb(self):
        return self.x - 40, self.y - 40, self.x + 35, self.y + 40
