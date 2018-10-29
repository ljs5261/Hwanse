# 아직 고치기 전, 1탄 보스 돼지는 마지막(지금은 세번째) grass의 x위치가 400이 되면 등장

from pico2d import *

RIGHT_DOWN, RIGHT_UP = range(2)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
}


class IdleState:
    @staticmethod
    def enter(grass1, event):
        if event == RIGHT_UP:
            grass1.velocity = 0

    @staticmethod
    def exit(grass1, event):
        pass

    @staticmethod
    def do(grass1):
        pass

    @staticmethod
    def draw(grass1):
        grass1.image.draw(grass1.x, grass1.y)


class RunState:
    @staticmethod
    def enter(grass1, event):
        if event == RIGHT_DOWN:
            grass1.velocity = -5

    @staticmethod
    def exit(grass1, event):
        pass

    @staticmethod
    def do(grass1):
        grass1.x += grass1.velocity

    @staticmethod
    def draw(grass1):
        grass1.image.draw(grass1.x, grass1.y)


next_state_table = {
    IdleState: {RIGHT_DOWN: RunState},
    RunState: {RIGHT_UP: IdleState}
}


class Grass:

    def __init__(self, xpos):
        self.x, self.y = xpos, 30
        self.image = load_image('./Resource/grass.png')
        self.velocity = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self, at):
        if at.x == 400:
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

