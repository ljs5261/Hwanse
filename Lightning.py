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


class Lightning:

    def __init__(self):
        rinshang = Stage2_state.get_rinshang()
        self.x = rinshang.x - 100
        self.y = 300
        self.image = load_image('./Resource/lightning.png')
        self.frame = 0
        self.velocity = RUN_SPEED_PPS
        self.timer = 0

    def draw(self):
        if self.timer <= 3:
            self.image.clip_draw(int(self.frame) * 100, 0, 100, 600, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        self.x -= (self.velocity * game_framework.frame_time)
        self.timer += 1
        if self.timer == 36:
            self.timer = 0
        ataho = Stage2_state.get_ataho()
        if self.timer <= 3 and Stage2_state.collide(self, ataho):
            ataho.life -= 50
            print(ataho.life)

    def get_bb(self):
        return self.x - 20, self.y - 280, self.x + 20, self.y + 280
