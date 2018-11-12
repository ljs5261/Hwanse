from pico2d import *
import game_framework
import game_world

PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 1.5                 # meter / second
RUN_SPEED_PPS = 2.5 * (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second, 75


class EnergyPa:
    def __init__(self, x, y, dir):
        self.x, self.y = x, y
        self.image = load_image('./Resource/energy_pa.png')
        self.frame = 0
        self.dir = dir

    def update(self):
        self.frame = (self.frame + 1) % 3
        if self.dir == 1:
            self.x += (RUN_SPEED_PPS * game_framework.frame_time)
        else:
            self.x -= (RUN_SPEED_PPS * game_framework.frame_time)

        if self.x < 0 or self.x > 800:
            game_world.remove_object(self)

    def draw(self):
        self.image.clip_draw(self.frame * 34, 0, 34, 42, self.x, self.y)


