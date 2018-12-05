from pico2d import *
import Stage2_state
import game_framework
import random

PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 3                 # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second, 75

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
ATTACK_FRAMES_PER_ACTION = 5
Walk_FRAMES_PER_ACTION = 8


class WalkState:
    @staticmethod
    def do(gargoyle):
        gargoyle.frame = (gargoyle.frame + Walk_FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        gargoyle.x -= (gargoyle.velocity * game_framework.frame_time)

    @staticmethod
    def draw(gargoyle):
        gargoyle.image.clip_draw(int(gargoyle.frame) * 100, 0, 100, 100, gargoyle.x, gargoyle.y)
        draw_rectangle(*gargoyle.get_bb())


class AttackState:
    @staticmethod
    def do(gargoyle):
        gargoyle.frame = (gargoyle.frame + ATTACK_FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

    @staticmethod
    def draw(gargoyle):
        gargoyle.image.clip_draw(int(gargoyle.frame) * 100, 100, 100, 100, gargoyle.x, gargoyle.y)


class Gargoyle:
    image = None

    def __init__(self):
        self.x = random.randint(5000, 5500)
        self.y = 85
        if Gargoyle.image == None:
            Gargoyle.image = load_image('./Resource/gargoyle_full.png')
        self.frame = 0
        self.velocity = RUN_SPEED_PPS
        self.life = 200
        self.cur_state = WalkState

    def draw(self):
        self.cur_state.draw(self)

    def update(self):
        ataho = Stage2_state.get_ataho()
        if self.cur_state == WalkState:
            self.cur_state.do(self)
            if self.x - ataho.x < 60:
                self.cur_state = AttackState
        else:
            self.cur_state.do(self)

        ataho = Stage2_state.get_ataho()
        if Stage2_state.collide(self, ataho):
            ataho.life -= 50
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
        return self.x - 45, self.y - 45, self.x + 45, self.y + 45
