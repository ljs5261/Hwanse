from pico2d import *
import Stage1_state
import game_framework

PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 2.5                # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second, 75

TIME_PER_ACTION = 0.8
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Slime:
    def __init__(self, x):
        self.x, self.y = x, 60
        self.image = load_image('./Resource/slime.png')
        self.scroll_toggle = None
        self.frame = 0
        self.life = 60

    def draw(self):
        self.image.clip_draw(int(self.frame) * 50, 0, 50, 50, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        if Stage1_state.ataho.scroll_toggle:
            if self.scroll_toggle:
                self.x -= (RUN_SPEED_PPS * game_framework.frame_time)
        else:
            pass

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                self.scroll_toggle = True

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20