from pico2d import *
from Ataho import ScrollState
import Stage1_state_new

PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 1.5                 # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second, 75


class Grass:
    def __init__(self, x):
        self.x, self.y = x, 30
        self.image = load_image('./Resource/grass.png')

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        # if ScrollState.do(Stage1_state_new.ataho):
            self.x -= RUN_SPEED_PPS / 3
        #else:
        #    pass

    def draw(self):
        self.image.draw(self.x, self.y)


