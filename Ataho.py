from pico2d import *

# ataho Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SHIFT_DOWN, SLEEP_TIMER, DASH_TIMER = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_RSHIFT) : SHIFT_DOWN,
    (SDL_KEYDOWN, SDLK_LSHIFT) : SHIFT_DOWN

}

# ataho States


class DashState:
    def enter(ataho, event):
        if event == SHIFT_DOWN:
            if ataho.velocity == 1:
                ataho.dash_speed += 5
            elif ataho.velocity == -1:
                ataho.dash_speed -= 5

        ataho.timer = 10

    def exit(ataho, event):
        pass

    def do(ataho):
        ataho.frame = (ataho.frame + 1) % 8
        ataho.x += ataho.dash_speed
        ataho.x = clamp(25, ataho.x, 800 - 25)
        ataho.timer -= 1
        if ataho.timer == 0:
            ataho.add_event(DASH_TIMER)

    def draw(ataho):
        if ataho.velocity == 1:
            ataho.image.clip_draw(ataho.frame * 100, 100, 100, 100, ataho.x, ataho.y)
        else:
            ataho.image.clip_draw(ataho.frame * 100, 0, 100, 100, ataho.x, ataho.y)


class SleepState:
    def enter(ataho, event):
        ataho.frame = 0

    def exit(ataho, event):
        pass

    def do(ataho):
        ataho.frame = (ataho.frame + 1) % 8

    def draw(ataho):
        if ataho.dir == 1:
            ataho.image.clip_composite_draw(ataho.frame * 100, 300, 100, 100,
            3.141592 / 2, '', ataho.x - 25, ataho.y - 25, 100, 100)
        else:
            ataho.image.clip_composite_draw(ataho.frame * 100, 200, 100, 100,
            -3.141592 / 2, '', ataho.x + 25, ataho.y - 25, 100, 100)


class IdleState:
    @staticmethod
    def enter(ataho, event):
        if event == RIGHT_DOWN:
            ataho.velocity = 7
        elif event == LEFT_DOWN:
            ataho.velocity = -7
        elif event == RIGHT_UP:
            ataho.velocity = -7
        elif event == LEFT_UP:
            ataho.velocity = 7

    @staticmethod
    def exit(ataho, event):
        pass

    @staticmethod
    def do(ataho):
        pass

    @staticmethod
    def draw(ataho):
        if ataho.dir == 7:
            ataho.image.clip_draw(0, 0, 80, 100, ataho.x, ataho.y)
        else:
            ataho.image.clip_draw(0, 100, 80, 100, ataho.x, ataho.y)


class RunState:
    @staticmethod
    def enter(ataho, event):
        if event == RIGHT_DOWN:
            ataho.velocity = 7
        elif event == LEFT_DOWN:
            ataho.velocity = -7
        elif event == RIGHT_UP:
            ataho.velocity = -7
        elif event == LEFT_UP:
            ataho.velocity = 7
        ataho.dir = ataho.velocity

    @staticmethod
    def exit(ataho, event):
        pass

    @staticmethod
    def do(ataho):
        ataho.frame = (ataho.frame + 1) % 5
        ataho.timer -= 1
        ataho.x += ataho.velocity
        ataho.x = clamp(25, ataho.x, 400)

    @staticmethod
    def draw(ataho):
        if ataho.velocity == 7:
            ataho.image.clip_draw(ataho.frame * 80, 0, 80, 100, ataho.x, ataho.y)
        else:
            ataho.image.clip_draw(ataho.frame * 80, 100, 80, 100, ataho.x, ataho.y)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,
               RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
               SLEEP_TIMER: SleepState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
               LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
                SHIFT_DOWN: DashState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN:RunState,
                 LEFT_UP: RunState, RIGHT_UP: RunState},
    DashState: {DASH_TIMER: RunState, SHIFT_DOWN: DashState
                }
}


class Ataho:

    def __init__(self):
        self.x, self.y = 200, 90
        self.image = load_image('./Resource/ataho.png')
        self.dir = 7
        self.velocity = 0
        self.frame = 0
        self.timer = 0
        self.dash_speed = 0
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

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)



