from pico2d import *
import Stage1_state
import game_framework
import random

PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 3                 # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second, 75

TIME_PER_ACTION = 0.9
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class IdleState:
    @staticmethod
    def do(pig):
        if pig.move_count < 40:
            pig.frame = (pig.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            pig.dir = 0
            pig.x -= (pig.velocity * game_framework.frame_time)
            pig.move_count += 1
        if pig.move_count >= 40:
            pig.frame = (pig.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            pig.dir = 1
            pig.x += (pig.velocity * game_framework.frame_time)
            pig.move_count += 1
        if pig.move_count == 80:
            pig.move_count = 0

    @staticmethod
    def draw(pig):
        if pig.dir == 0:
            pig.image.clip_draw(int(pig.frame) * 120, 90, 120, 90, pig.x, pig.y)
        else:
            pig.image.clip_draw(int(pig.frame) * 120, 0, 120, 90, pig.x, pig.y)


class PigScrollState:
    @staticmethod
    def do(pig):
        if pig.move_count < 40:
            pig.frame = (pig.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
            pig.dir = 0
            pig.x -= 2 * (pig.velocity * game_framework.frame_time)
            pig.move_count += 1
        if pig.move_count >= 40:
            pig.frame = (pig.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
            pig.dir = 1
            pig.x += 0
            pig.move_count += 1
        if pig.move_count == 80:
            pig.move_count = 0

    @staticmethod
    def draw(pig):
        if pig.dir == 0:
            pig.image.clip_draw(int(pig.frame) * 120, 90, 120, 90, pig.x, pig.y)
        else:
            pig.image.clip_draw(int(pig.frame) * 120, 0, 120, 90, pig.x, pig.y)


class Pig:

    def __init__(self):
        self.x, self.y = 600, 80
        self.image = load_image('./Resource/Pig.png')
        self.frame = 0
        self.velocity = RUN_SPEED_PPS
        self.move_count = 0
        self.cur_state = IdleState
        self.dir = 0
        self.scroll_toggle = None
        self.life = 140
        self.collision_count = 0

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.cur_state.do(self)
        if Stage1_state.ataho.scroll_toggle:
            if self.scroll_toggle:
                self.cur_state = PigScrollState
            else:
                self.cur_state = IdleState
        else:
            self.cur_state = IdleState

        ataho = Stage1_state.get_ataho()
        if Stage1_state.collide(self, ataho):
            print(ataho.life)
            if self.collision_count == 0:
                ataho.flicker_toggle = True
                ataho.life -= 10
                self.collision_count += 1

        if ataho.flicker_toggle:
            ataho.flicker()
        else:
            pass

        if ataho.flicker_count >= 100:
            ataho.flicker_toggle = False
            self.collision_count = 0
            ataho.flicker_count = 0

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                self.scroll_toggle = True

    def get_bb(self):
        return self.x - 50, self.y - 40, self.x + 50, self.y + 40
