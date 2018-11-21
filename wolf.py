from pico2d import *
import Stage1_state
import game_framework

PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 3                 # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second, 75

TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class IdleState:
    @staticmethod
    def do(wolf):
        if wolf.move_count < 30:
            wolf.frame = (wolf.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
            wolf.dir = 0
            wolf.x -= (wolf.velocity * game_framework.frame_time)
            wolf.move_count += 1
        if wolf.move_count >= 30:
            wolf.frame = (wolf.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
            wolf.dir = 1
            wolf.x += (wolf.velocity * game_framework.frame_time)
            wolf.move_count += 1
        if wolf.move_count == 60:
            wolf.move_count = 0

    @staticmethod
    def draw(wolf):
        if wolf.dir == 0:
            wolf.image.clip_draw(int(wolf.frame) * 64, 0, 64, 40, wolf.x, wolf.y)
        else:
            wolf.image.clip_draw(int(wolf.frame) * 64, 40, 64, 40, wolf.x, wolf.y)


class WolfScrollState:
    @staticmethod
    def do(wolf):
        if wolf.move_count < 30:
            wolf.frame = (wolf.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
            wolf.dir = 0
            wolf.x -= 2 * (wolf.velocity * game_framework.frame_time)
            wolf.move_count += 1
        if wolf.move_count >= 30:
            wolf.frame = (wolf.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
            wolf.dir = 1
            wolf.x += 0
            wolf.move_count += 1
        if wolf.move_count == 60:
            wolf.move_count = 0

    @staticmethod
    def draw(wolf):
        if wolf.dir == 0:
            wolf.image.clip_draw(int(wolf.frame) * 64, 0, 64, 40, wolf.x, wolf.y)
        else:
            wolf.image.clip_draw(int(wolf.frame) * 64, 40, 64, 40, wolf.x, wolf.y)


class Wolf:

    def __init__(self):
        self.x, self.y = 1400, 66
        self.image = load_image('./Resource/wolf.png')
        self.frame = 0
        self.velocity = RUN_SPEED_PPS
        self.move_count = 0
        self.cur_state = IdleState
        self.dir = 0
        self.scroll_toggle = None
        self.life = 140
        self.collision_count = 0

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.cur_state.do(self)
        if Stage1_state.ataho.scroll_toggle:
            if self.scroll_toggle:
                self.cur_state = WolfScrollState
            else:
                self.cur_state = IdleState
        else:
            self.cur_state = IdleState

        ataho = Stage1_state.get_ataho()
        if Stage1_state.collide(self, ataho):
            print("COLLISION")
            ataho.life -= 10
            print(ataho.life)
            at_x1, at_y1, at_x2, at_y2 = ataho.get_bb()
            x1, y1, x2, y2 = self.get_bb()
            if x1 < at_x2 < x1 + 20:
                ataho.x -= 10
            elif x2 - 20 < at_x1 < x2:
                ataho.x += 10
            elif at_y1 < y2:
                ataho.y = 200
                ataho.velocity = 0

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                self.scroll_toggle = True

    def get_bb(self):
        return self.x - 35, self.y - 25, self.x + 30, self.y + 20
