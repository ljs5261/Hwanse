from pico2d import *
import game_framework
from energy_pa import EnergyPa
import game_world
# import Stage1_state

# ataho run speed
# 100pixel = 2m
PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 3              # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second, 75
JUMP_YSPEED_PPS = 7.5 * RUN_SPEED_PPS  # pixel / second
JUMP_XSPEED_PPS = RUN_SPEED_PPS  # pixel / second
ACCELERATION_OF_GRAVITY = 7.0     # meter / second * second
FRAME_TIME = 0.16
VARIATION_OF_VELOCITY_MPS = (ACCELERATION_OF_GRAVITY * FRAME_TIME)  # meter / second, 1.6
VARIATION_OF_VELOCITY_PPS = (VARIATION_OF_VELOCITY_MPS * PIXEL_PER_METER)  # pixel / second, 80

# ataho Action Speed
TIME_PER_ACTION = 0.4
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


# ataho Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE_DOWN, A, S_DOWN, LANDING, gwangpacham_end = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYDOWN, SDLK_a): A,
    (SDL_KEYDOWN, SDLK_s): S_DOWN
}


class GwangpachamState:
    @staticmethod
    def enter(ataho, event):
        ataho.x_move = 0
        ataho.scroll_toggle = False
        if event == S_DOWN:
            ataho.frame = 0

    @staticmethod
    def exit(ataho, event):
        pass

    @staticmethod
    def do(ataho):
        ataho.y = 90
        if ataho.gwangpacham_count % 12 == 0:
            ataho.frame = (ataho.frame + 1) % 4
        ataho.gwangpacham_count += 1
        if ataho.gwangpacham_count == 36:
            ataho.add_event(gwangpacham_end)
            ataho.gwangpacham_count = 0

    @staticmethod
    def draw(ataho):
        ataho.image.clip_draw(ataho.frame * 180, 0, 180, 200, ataho.x, ataho.y)
        if ataho.frame == 3:
            delay(0.3)


class JumpState:
    @staticmethod
    def enter(ataho, event):
        if event == RIGHT_DOWN:
            if ataho.x == 400:
                ataho.velocity = ataho.velocity
                ataho.x_move = 0
                ataho.scroll_toggle = True
            else:
                ataho.velocity = ataho.velocity
                ataho.x_move = JUMP_XSPEED_PPS
                ataho.scroll_toggle = False
        elif event == LEFT_DOWN:
            ataho.velocity = ataho.velocity
            ataho.x_move = -JUMP_XSPEED_PPS
        elif event == RIGHT_UP:
            ataho.velocity = ataho.velocity
            ataho.scroll_toggle = False
        elif event == LEFT_UP:
            ataho.velocity = ataho.velocity
        elif event == SPACE_DOWN:
            if ataho.y == 90:
                ataho.velocity = JUMP_YSPEED_PPS

            else:
                ataho.velocity = ataho.velocity

    @staticmethod
    def exit(ataho, event):
        if event == A:
            ataho.shoot_energy_pa()

    @staticmethod
    def do(ataho):
        ataho.x += (ataho.x_move * game_framework.frame_time)
        ataho.y += (ataho.velocity * game_framework.frame_time)
        ataho.velocity -= VARIATION_OF_VELOCITY_PPS
        if ataho.y <= 90:
            ataho.y = 90
            ataho.add_event(LANDING)
        ataho.x = clamp(25, ataho.x, 400)
        if ataho.x == 400:
            ataho.scroll_toggle = True
        else:
            ataho.scroll_toggle = False

    @staticmethod
    def draw(ataho):
        if ataho.dir == 1:
            ataho.image.clip_draw(0, 200, 80, 100, ataho.x, ataho.y)
        else:
            ataho.image.clip_draw(80, 200, 80, 100, ataho.x, ataho.y)


class IdleState:
    @staticmethod
    def enter(ataho, event):
        ataho.x_move = 0
        ataho.scroll_toggle = False
        if event == RIGHT_DOWN:
            ataho.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            ataho.velocity -= RUN_SPEED_PPS

    @staticmethod
    def exit(ataho, event):
        if event == A:
            ataho.shoot_energy_pa()

    @staticmethod
    def do(ataho):
        ataho.y = 90
        if ataho.stage == 2:
            ataho.frame = (ataho.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        else:
            pass

    @staticmethod
    def draw(ataho):
        if ataho.stage == 1:
            if ataho.dir == 1:
                ataho.image.clip_draw(0, 300, 80, 100, ataho.x, ataho.y)
            else:
                ataho.image.clip_draw(0, 400, 80, 100, ataho.x, ataho.y)
        else:
            if ataho.dir == 1:
                ataho.image.clip_draw(int(ataho.frame) * 80, 300, 80, 100, ataho.x, ataho.y)
            else:
                ataho.image.clip_draw(int(ataho.frame) * 80, 400, 80, 100, ataho.x, ataho.y)


class RunState:
    @staticmethod
    def enter(ataho, event):
        if event == RIGHT_DOWN:
            ataho.dir = 1
            if ataho.x == 400:
                ataho.velocity = 0
                ataho.scroll_toggle = True
            else:
                ataho.velocity = RUN_SPEED_PPS
                ataho.scroll_toggle = False
        elif event == LEFT_DOWN:
            ataho.velocity = -RUN_SPEED_PPS
            ataho.dir = -1
        elif event == RIGHT_UP:
            pass
        elif event == LEFT_UP:
            pass

    @staticmethod
    def exit(ataho, event):
        if event == A:
            ataho.shoot_energy_pa()

    @staticmethod
    def do(ataho):
        ataho.frame = (ataho.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        ataho.x += ataho.velocity * game_framework.frame_time
        ataho.x = clamp(25, ataho.x, 400)
        ataho.y = 90
        if ataho.x == 400:
            ataho.scroll_toggle = True
        else:
            ataho.scroll_toggle = False

    @staticmethod
    def draw(ataho):
        if ataho.dir == 1:
            ataho.image.clip_draw(int(ataho.frame) * 80, 300, 80, 100, ataho.x, ataho.y)
        else:
            ataho.image.clip_draw(int(ataho.frame) * 80, 400, 80, 100, ataho.x, ataho.y)


next_state_table = {
    IdleState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
               RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
               SPACE_DOWN: JumpState, A: IdleState, LANDING: IdleState,
               S_DOWN: GwangpachamState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
               RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState,
                SPACE_DOWN: JumpState, LANDING: RunState, A: RunState, S_DOWN: RunState},
    JumpState: {RIGHT_UP: JumpState, LEFT_UP: JumpState,
               RIGHT_DOWN: JumpState, LEFT_DOWN: JumpState,
                SPACE_DOWN: JumpState, LANDING: IdleState, A: JumpState, S_DOWN: JumpState},
    GwangpachamState: {gwangpacham_end : IdleState, RIGHT_UP: GwangpachamState, LEFT_UP: GwangpachamState,
               RIGHT_DOWN: GwangpachamState, LEFT_DOWN: GwangpachamState, S_DOWN: GwangpachamState,
                SPACE_DOWN: GwangpachamState, LANDING: GwangpachamState, A: GwangpachamState}
}


class Ataho:

    def __init__(self):
        self.x, self.y = 200, 90
        self.image = load_image('./Resource/ataho_full.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.timer = 0
        self.x_move = 0
        self.scroll_toggle = None
        self.life = 800
        self.stage = 1
        self.gwangpacham_count = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)         # 가장 오래된 이벤트에 의해 현재 상태를 나가고
            self.cur_state = next_state_table[self.cur_state][event]  # 그 이벤트에 의해 다음 상태로 변화
            self.cur_state.enter(self, event)       # 다음 상태로 들어간다

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def shoot_energy_pa(self):
        energy_pa = EnergyPa(self.x, self.y, self.dir)
        game_world.add_object(energy_pa, 1)

    def get_bb(self):
        return self.x - 40, self.y - 50, self.x + 20, self.y + 50
