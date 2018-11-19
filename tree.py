from pico2d import *
import Stage1_state
import game_framework

PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 3                 # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second, 75


class Tree:
    def __init__(self, x):
        self.x, self.y = x, 110
        self.image = load_image('./Resource/tree.png')
        self.scroll_toggle = None

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        if Stage1_state.ataho.scroll_toggle:
            if self.scroll_toggle:
                self.x -= (RUN_SPEED_PPS * game_framework.frame_time)
        else:
            pass

        if Stage1_state.collide(self, Stage1_state.ataho):
            print("COLLISION")
            Stage1_state.ataho.life -= 10
            print(Stage1_state.ataho.life)
            at_x1, at_y1, at_x2, at_y2 = Stage1_state.ataho.get_bb()
            x1, y1, x2, y2 = self.get_bb()
            if x1 < at_x2 < x1 + 20:
                Stage1_state.ataho.x -= 10
            elif x2 - 20 < at_x1 < x2:
                Stage1_state.ataho.x += 10
            if at_y1 < y2 and x1 < at_x1 < x2:
                Stage1_state.ataho.y = 270
                Stage1_state.ataho.velocity = 0

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                self.scroll_toggle = True

    def get_bb(self):
        return self.x - 60, self.y - 70, self.x + 60, self.y + 55
