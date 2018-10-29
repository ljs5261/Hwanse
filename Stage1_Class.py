from pico2d import *
from Stage1_state import *
pause_x = 0

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP = range(4)  # 키입력을 숫자로 정의

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP
}


class IdleState:

    def enter(at, event):
        if event == RIGHT_DOWN:
            at.dir += 1
        elif event == LEFT_DOWN:
            at.dir -= 1
        elif event == RIGHT_UP:
            at.dir -= 1
        elif event == LEFT_UP:
            at.dir += 1
        at.timer = 300

    def exit(at, event):
        if event == RIGHT_DOWN:
            at.dir = 0
        elif event == LEFT_DOWN:
            at.dir = 0
        elif event == RIGHT_UP:
            at.dir = 0
        elif event == LEFT_UP:
            at.dir = 0

    def do(at):
        pass

    def draw(at):
        if at.dir == 1:
            at.image.clip_draw(0, 0, 80, 100, at.x, at.y)
        else:
            at.image.clip_draw(0, 100, 80, 100, at.x, at.y)


class RunState:

    def enter(at, event):
        if event == RIGHT_DOWN:
            at.dir += 1
            at.velocity += 5
        elif event == LEFT_DOWN:
            at.dir -= 1
            at.velocity -= 5
        elif event == RIGHT_UP:         # 오른쪽, 왼쪽 둘 다 눌리고 잇다가 오른쪽이 떼어지는 경우
            at.dir -= 1
            at.velocity -= 5
        elif event == LEFT_UP:
            at.dir += 1
            at.velocity += 5

    def exit(at, event):
        if event == RIGHT_DOWN:
            at.dir = 0
            at.velocity = 0
        elif event == LEFT_DOWN:
            at.dir = 0
            at.velocity = 0
        elif event == RIGHT_UP:         # 오른쪽, 왼쪽 둘 다 눌리고 잇다가 오른쪽이 떼어지는 경우
            at.dir = 0
            at.velocity = 0
        elif event == LEFT_UP:
            at.dir = 0
            at.velocity = 0

    def do(at):
        at.frame = (at.frame + 1) % 5
        at.x += at.velocity
        at.x = clamp(25, at.x, 800 - 25)

    def draw(at):
        if at.dir == 1:
            at.image.clip_draw(at.frame * 100, 0, 80, 100, at.x, at.y)
        else:
            at.image.clip_draw(at.frame * 100, 100, 80, 100, at.x, at.y)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState}
}


class ataho:

    def __init__(self):
        self.image = load_image('./Resource/ataho.png')
        self.x, self.y = 200, 90
        self.frame = 0
        self.dir = 1
        self.velocity = 0
        self.timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def fire_ball(self):
            # fill here
            pass

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def start_pause_next(self):     # 정지 순간의 x값이 담긴 pause_x로 아타호의 x값 초기화
        self.x = pause_x

    def draw(self):
        self.cur_state.draw(self)

    def draw_no_frame(self):
        self.image.clip_draw(self.frame * 80, 0, 80, 100, self.x, self.y)

    def pause(self):            # 정지 순간의 x값을 pause_x에 대입
        global pause_x
        pause_x = self.x

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


class Grass:

    def __init__(self):
        self.image = load_image('./Resource/grass.png')

    def draw_grass(self):
        self.image.draw(400, 30)


class BackGround:
    def __init__(self):
        self.image = load_image('./Resource/grassland.png')
        self.x, self.y = 400, 300

    def draw_bg(self):
        self.image.draw(self.x, self.y)

    def move_bg(self):
        self.x -= 2