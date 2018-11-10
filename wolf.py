from pico2d import *
import Stage1_state
from Ataho import ScrollState
import game_framework

PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 1.5                 # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second, 75


class IdleState:
    @staticmethod
    def do(wolf):
        if wolf.move_count < 30:
            wolf.frame = (wolf.frame + 1) % 5
            wolf.x -= (wolf.velocity * game_framework.frame_time)
            wolf.move_count += 1
        if wolf.move_count >= 30:
            wolf.frame = (wolf.frame + 1) % 5
            wolf.x += (wolf.velocity * game_framework.frame_time)
            wolf.move_count += 1
        if wolf.move_count == 60:
            wolf.move_count = 0

    @staticmethod
    def draw(wolf):
        wolf.image.clip_draw(wolf.frame * 64, 0, 64, 40, wolf.x, wolf.y)


class WolfScrollState:
    @staticmethod
    def do(wolf):
        if wolf.move_count < 30:
            wolf.frame = (wolf.frame + 1) % 5
            wolf.x -= 2 * (wolf.velocity * game_framework.frame_time)
            wolf.move_count += 1
        if wolf.move_count >= 30:
            wolf.frame = (wolf.frame + 1) % 5
            wolf.x += 0
            wolf.move_count += 1
        if wolf.move_count == 60:
            wolf.move_count = 0

    @staticmethod
    def draw(wolf):
        wolf.image.clip_draw(wolf.frame * 64, 0, 64, 40, wolf.x, wolf.y)


class Wolf:

    def __init__(self):
        self.x, self.y = 1400, 66
        self.image = load_image('./Resource/wolf1.png')
        self.frame = 0
        self.velocity = RUN_SPEED_PPS
        self.move_count = 0
        self.cur_state = IdleState

    def update(self):
        self.cur_state.do(self)
        if Stage1_state.ataho.cur_state == ScrollState:
            if Stage1_state.ataho.frame_count:
                self.cur_state = WolfScrollState
            else:
                self.cur_state = IdleState
        else:
            self.cur_state = IdleState

    def draw(self):
        self.cur_state.draw(self)
