from pico2d import *

RIGHT_DOWN, RIGHT_UP = range(2)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
}


class IdleState:
    @staticmethod
    def enter(pig, event):
        pass

    @staticmethod
    def exit(grass1, event):
        pass

    @staticmethod
    def do(pig):
        if pig.move_count < 30:
            pig.frame = (pig.frame + 1) % 4
            pig.x -= pig.idle_velocity
            pig.move_count += 1
        if pig.move_count >= 30:
            pig.frame = (pig.frame + 1) % 4
            pig.x += pig.idle_velocity
            pig.move_count += 1
        if pig.move_count == 60:
            pig.move_count = 0

    @staticmethod
    def draw(pig):
        pig.image.clip_draw(pig.frame * 110, 0, 110, 100, pig.x, pig.y)


class RunState:
    @staticmethod
    def enter(pig, event):
        if event == RIGHT_DOWN:
            pig.velocity = -5

    @staticmethod
    def exit(pig, event):
        pass

    @staticmethod
    def do(pig):
        if pig.move_count < 30:
            pig.frame = (pig.frame + 1) % 4
            pig.x -= pig.idle_velocity + 5
            pig.move_count += 1
        if pig.move_count >= 30:
            pig.frame = (pig.frame + 1) % 4
            pig.x += 0
            pig.move_count += 1
        if pig.move_count == 60:
            pig.move_count = 0

    @staticmethod
    def draw(pig):
        pig.image.clip_draw(pig.frame * 110, 0, 110, 100, pig.x, pig.y)


next_state_table = {
    IdleState: {RIGHT_DOWN: RunState},
    RunState: {RIGHT_UP: IdleState}
}


class Pig:

    def __init__(self):
        self.x, self.y = 2300, 80
        self.image = load_image('./Resource/pig_rush.png')
        self.frame = 0
        self.velocity = 0
        self.idle_velocity = 5
        self.move_count = 0
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
