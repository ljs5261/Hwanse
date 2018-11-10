from pico2d import *

RIGHT_DOWN, RIGHT_UP = range(2)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
}


class IdleState:
    @staticmethod
    def enter(bg, event):
        if event == RIGHT_UP:
            bg.velocity = 0

    @staticmethod
    def exit(bg, event):
        pass

    @staticmethod
    def do(bg):
        pass

    @staticmethod
    def draw(bg):
        bg.image.draw(bg.x, bg.y)


class RunState:
    @staticmethod
    def enter(bg, event):
        if event == RIGHT_DOWN:
            bg.velocity = -3

    @staticmethod
    def exit(bg, event):
        pass

    @staticmethod
    def do(bg):
        bg.x += bg.velocity

    @staticmethod
    def draw(bg):
        bg.image.draw(bg.x, bg.y)


next_state_table = {
    IdleState: {RIGHT_DOWN: RunState},
    RunState: {RIGHT_UP: IdleState}
}


class BackGround:

    def __init__(self, x):
        self.x, self.y = x, 300
        self.image = load_image('./Resource/grassland.png')
        self.velocity = 0
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


