from pico2d import *
import game_framework

PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 3                # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second, 75


class Bamboo:
    def __init__(self, x):
        self.x, self.y = x, 30
        self.image = load_image('./Resource/bamboo.png')
        self.scroll_toggle = None

    def update(self):
        self.x -= (RUN_SPEED_PPS * game_framework.frame_time)

    def draw(self):
        self.image.draw(self.x, self.y)

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                self.scroll_toggle = True

