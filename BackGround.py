from pico2d import *
import Stage1_state
import game_framework

PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 3               # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER) / 2         # pixel / second, 75


class BackGround:
    def __init__(self, x):
        self.x, self.y = x, 300
        self.image = load_image('./Resource/grassland.png')
        self.scroll_toggle = None

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if Stage1_state.ataho.scroll_toggle:
            if self.scroll_toggle:
                self.x -= (RUN_SPEED_PPS * game_framework.frame_time)
        else:
            pass

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                self.scroll_toggle = True






