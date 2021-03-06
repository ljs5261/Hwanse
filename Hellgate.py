from pico2d import *
import Stage1_state
import Stage2_state
import game_framework

PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 3                  # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second, 75


class Hellgate:
    def __init__(self):
        self.x, self.y = 5000, 150
        self.image = load_image('./Resource/Hellgate.png')
        self.scroll_toggle = None

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if Stage1_state.ataho.scroll_toggle:
            if self.scroll_toggle:
                self.x -= (RUN_SPEED_PPS * game_framework.frame_time)
        else:
            pass

        ataho = Stage1_state.get_ataho()
        if Stage1_state.collide(self, ataho):
            print("COLLISION")
            game_framework.change_state(Stage2_state)

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                self.scroll_toggle = True

    def get_bb(self):
        return self.x - 10, self.y - 60, self.x + 10, self.y + 200
