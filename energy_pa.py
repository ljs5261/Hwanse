from pico2d import *
import game_framework
import game_world
# import Stage1_state
import Stage2_state

PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 4                 # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class EnergyPa:
    image = None

    def __init__(self, x, y, dir):
        if EnergyPa.image is None:
            EnergyPa.image = load_image('./Resource/energy_pa.png')
        self.x, self.y = x, y
        self.frame = 0
        self.dir = dir

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        if self.dir == 1:
            self.x += (RUN_SPEED_PPS * game_framework.frame_time)
        else:
            self.x -= (RUN_SPEED_PPS * game_framework.frame_time)

        if self.x < 0 or self.x > 800:
            game_world.remove_object(self)

        '''for wolf in Stage1_state.team_wolf:
            if Stage1_state.collide(self, wolf):
                wolf.life -= 20
                game_world.remove_object(self)
                print(wolf.life)
                if wolf.life < 0:
                    game_world.remove_object(wolf)
                    Stage1_state.team_wolf.remove(wolf)

        for slime in Stage1_state.team_slime:
            if Stage1_state.collide(self, slime):
                slime.life -= 20
                game_world.remove_object(self)
                print(slime.life)
                if slime.life < 0:
                    game_world.remove_object(slime)
                    Stage1_state.team_slime.remove(slime)

        if Stage1_state.collide(self, Stage1_state.pig):
            Stage1_state.pig.life -= 20
            game_world.remove_object(self)
            print(Stage1_state.pig.life)
            if Stage1_state.pig.life < 0:
                game_world.remove_object(Stage1_state.pig)
'''
        for mummy in Stage2_state.team_mummy:
            if Stage2_state.collide(self, mummy):
                mummy.life -= 20
                game_world.remove_object(self)
                print(mummy.life)
                if mummy.life < 0:
                    game_world.remove_object(mummy)
                    Stage2_state.team_mummy.remove(mummy)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 34, 0, 34, 42, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 15, self.y - 20, self.x + 20, self.y + 15

