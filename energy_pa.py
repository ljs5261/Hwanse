from pico2d import *
import game_framework
import game_world

PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 1.5                 # meter / second
RUN_SPEED_PPS = 2.5 * (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second, 75

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class EnergyPa:
    def __init__(self, x, y, dir):
        self.x, self.y = x, y
        self.image = load_image('./Resource/energy_pa.png')
        self.frame = 0
        self.dir = dir

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        if self.dir == 1:
            self.x += (RUN_SPEED_PPS * game_framework.frame_time)
        else:
            self.x -= (RUN_SPEED_PPS * game_framework.frame_time)

        if self.x < 0 or self.x > 800:
            game_world.remove_object(self)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 34, 0, 34, 42, self.x, self.y)


