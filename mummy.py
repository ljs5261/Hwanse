from pico2d import *
import Stage2_state
import game_framework
import random

PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 3                 # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second, 75

TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Mummy:

    def __init__(self):
        self.x = random.randint(600, 800)
        self.y = 90
        self.image = load_image('./Resource/Mummy.png')
        self.frame = random.randint(0, 5)
        self.velocity = random.uniform(RUN_SPEED_PPS, (2*RUN_SPEED_PPS))
        self.life = 180

    def draw(self):
        self.image.clip_draw(int(self.frame) * 80, 0, 80, 100, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        self.x -= 1

        ataho = Stage2_state.get_ataho()

    def get_bb(self):
        return self.x - 35, self.y - 40, self.x + 30, self.y + 40
