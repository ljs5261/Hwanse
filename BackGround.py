from pico2d import *
import Stage1_state
from Ataho import ScrollState
import game_framework

PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 1.5                 # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second, 75


class BackGround:
    def __init__(self, x):
        self.x, self.y = x, 300
        self.image = load_image('./Resource/grassland.png')

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        if Stage1_state.ataho.cur_state == ScrollState:
            if Stage1_state.ataho.frame_count:
                self.x -= (RUN_SPEED_PPS * game_framework.frame_time) / 2
            else:
                pass
        else:
            pass

    def draw(self):
        self.image.draw(self.x, self.y)


