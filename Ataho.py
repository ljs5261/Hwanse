from pico2d import *
import game_framework

# ataho run speed
# 100pixel = 2m
PIXEL_PER_METER = (100.0 / 2.0)     # pixel / meter
RUN_SPEED_MPS = 1.5                 # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)       # pixel / second, 75
JUMP_YSPEED_PPS = 9 * (RUN_SPEED_MPS * PIXEL_PER_METER)  # pixel / second, 150
JUMP_XSPEED_PPS = 2 * (RUN_SPEED_MPS * PIXEL_PER_METER)  # pixel / second, 150
ACCELERATION_OF_GRAVITY = 10.0     # meter / second * second
FRAME_TIME = 0.16
VARIATION_OF_VELOCITY_MPS = (ACCELERATION_OF_GRAVITY * FRAME_TIME)  # meter / second, 0.16
VARIATION_OF_VELOCITY_PPS = (VARIATION_OF_VELOCITY_MPS * PIXEL_PER_METER)  # pixel / second, 8


# ataho Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE_DOWN, LANDING, ENTER_SCROLL_STATE = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,

}


class ScrollState:
    @staticmethod
    def enter(ataho, event):
        ataho.frame_count = True
        if event == RIGHT_DOWN:
            ataho.frame_count = True
        elif event == RIGHT_UP:
            ataho.frame_count = False

    @staticmethod
    def exit(ataho, event):
        pass

    @staticmethod
    def do(ataho):
        if ataho.frame_count:
            ataho.frame = (ataho.frame + 1) % 5
            return ataho.frame_count
        else:
            ataho.frame = 0
            return ataho.frame_count

    @staticmethod
    def draw(ataho):
        if ataho.dir == 1:
            ataho.image.clip_draw(ataho.frame * 80, 300, 80, 100, ataho.x, ataho.y)
        else:
            ataho.image.clip_draw(ataho.frame * 80, 400, 80, 100, ataho.x, ataho.y)


class JumpState:
    @staticmethod
    def enter(ataho, event):
        if event == RIGHT_DOWN:
            ataho.velocity = ataho.velocity
            ataho.x_move = JUMP_XSPEED_PPS
        elif event == LEFT_DOWN:
            ataho.velocity = ataho.velocity
            ataho.x_move = -JUMP_XSPEED_PPS
        elif event == RIGHT_UP:
            ataho.velocity = ataho.velocity
        elif event == LEFT_UP:
            ataho.velocity = ataho.velocity
        elif event == SPACE_DOWN:
            if ataho.y == 90:
                ataho.velocity = JUMP_YSPEED_PPS

            else:
                ataho.velocity = ataho.velocity

    @staticmethod
    def exit(ataho, event):
        pass

    @staticmethod
    def do(ataho):
        ataho.x += (ataho.x_move * game_framework.frame_time)
        ataho.y += (ataho.velocity * game_framework.frame_time)
        ataho.velocity -= VARIATION_OF_VELOCITY_PPS
        if ataho.y <= 90:
            ataho.y = 90
            ataho.add_event(LANDING)
        ataho.x = clamp(25, ataho.x, 399)

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
        if event == RIGHT_DOWN:
            ataho.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            ataho.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            pass
        elif event == LEFT_UP:
            pass

    @staticmethod
    def exit(ataho, event):
        pass

    @staticmethod
    def do(ataho):
        pass

    @staticmethod
    def draw(ataho):
        if ataho.dir == 1:
            ataho.image.clip_draw(0, 300, 80, 100, ataho.x, ataho.y)
        else:
            ataho.image.clip_draw(0, 400, 80, 100, ataho.x, ataho.y)


class RunState:
    @staticmethod
    def enter(ataho, event):
        if event == RIGHT_DOWN:
            ataho.velocity = RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            ataho.velocity = -RUN_SPEED_PPS
        elif event == RIGHT_UP:
            pass
        elif event == LEFT_UP:
            pass

        ataho.dir = clamp(-1, ataho.velocity, 1)

    @staticmethod
    def exit(ataho, event):
        pass

    @staticmethod
    def do(ataho):
        ataho.frame = (ataho.frame + 1) % 5
        ataho.x += ataho.velocity * game_framework.frame_time
        ataho.x = clamp(25, ataho.x, 400)
        if ataho.x == 400:
            ataho.add_event(ENTER_SCROLL_STATE)

    @staticmethod
    def draw(ataho):
        if ataho.dir == 1:
            ataho.image.clip_draw(ataho.frame * 80, 300, 80, 100, ataho.x, ataho.y)
        else:
            ataho.image.clip_draw(ataho.frame * 80, 400, 80, 100, ataho.x, ataho.y)


next_state_table = {
    IdleState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
               RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
               SPACE_DOWN: JumpState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
               RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState,
                SPACE_DOWN: JumpState, ENTER_SCROLL_STATE: ScrollState},
    JumpState: {RIGHT_UP: JumpState, LEFT_UP: JumpState,
               RIGHT_DOWN: JumpState, LEFT_DOWN: JumpState,
                SPACE_DOWN: JumpState, LANDING: IdleState},
    ScrollState: {RIGHT_UP: ScrollState, RIGHT_DOWN: ScrollState,
                  LEFT_DOWN: RunState, SPACE_DOWN: JumpState}

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
        self.former_state_jump = 0
        self.frame_count = None
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.frame_control = 0

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            print(self.cur_state)
            print(event)
            self.cur_state.exit(self, event)         # 가장 오래된 이벤트에 의해 현재 상태를 나가고
            self.cur_state = next_state_table[self.cur_state][event]  # 그 이벤트에 의해 다음 상태로 변화
            self.cur_state.enter(self, event)       # 다음 상태로 들어간다
            print(self.cur_state)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def determine_scroll(self, right_on_off):
        if right_on_off:
            return True
        else:
            return False
