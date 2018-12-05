from pico2d import *
import Stage2_state
import game_framework
import game_world

PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 3                 # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second, 75

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


class Lightning:

    def __init__(self):
        self.x = Stage2_state.rinshang.x - 100
        self.y = 300
        self.image = load_image('./Resource/lightning.png')
        self.frame = 0
        self.velocity = RUN_SPEED_PPS
        self.timer = 0

    def draw(self):
        if self.timer <= 3:
            self.image.clip_draw(int(self.frame) * 100, 0, 100, 600, self.x, self.y)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        self.x = Stage2_state.rinshang.x - 100
        self.timer += 1
        if self.timer == 36:
            self.timer = 0

        if self.timer <= 3 and Stage2_state.collide(self, Stage2_state.ataho):
            Stage2_state.ataho.life -= 50
            print(Stage2_state.ataho.life)

        if Stage2_state.rinshang.life < 0:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 20, self.y - 280, self.x + 20, self.y + 280
