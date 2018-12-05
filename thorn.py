from pico2d import *
import Stage1_state
import game_framework

PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 3                # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second, 75


class Thorn:
    def __init__(self, x):
        self.x, self.y = x, 100
        self.image = load_image('./Resource/thorn.png')
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
        if Stage1_state.collide(ataho, self):
            print("COLLISION")
            ataho.life -= 5
            print(ataho.life)
            at_x1, at_y1, at_x2, at_y2 = ataho.get_bb()
            x1, y1, x2, y2 = self.get_bb()
            if x1 < at_x2 < x1 + 5:
                ataho.x -= 10
            elif x2 - 5 < at_x1 < x2:
                ataho.x += 10
            elif at_y1 < y2 :
                ataho.y = 270
                ataho.velocity = 0

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                self.scroll_toggle = True

    def get_bb(self):
        return self.x - 15, self.y - 30, self.x + 15, self.y + 40
