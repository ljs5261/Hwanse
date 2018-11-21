from pico2d import *
import Stage1_state
import game_framework
import game_world

PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 3                  # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second, 75


class Dumpling:
    def __init__(self):
        self.x, self.y = 2600, 70
        self.image = load_image('./Resource/dumpling.png')
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

        ataho = Stage1_state.get_ataho()
        if Stage1_state.collide(self, ataho):
            ataho.life += 300
            game_world.remove_object(self)
            print(ataho.life)

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                self.scroll_toggle = True

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50