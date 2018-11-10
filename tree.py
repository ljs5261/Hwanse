from pico2d import *
from Ataho import Ataho
RIGHT_DOWN, RIGHT_UP = range(2)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,

}



class IdleState:
    @staticmethod
    def enter(tree, event):
        if event == RIGHT_UP:
            tree.velocity = 0

    @staticmethod
    def exit(tree, event):
        pass

    @staticmethod
    def do(tree):
        pass

    @staticmethod
    def draw(tree):
        tree.image.draw(tree.x, tree.y)


class RunState:
    @staticmethod
    def enter(tree, event):
        if event == RIGHT_DOWN:
            tree.velocity = -5

    @staticmethod
    def exit(tree, event):
        pass

    @staticmethod
    def do(tree):
        tree.x += tree.velocity

    @staticmethod
    def draw(tree):
        tree.image.draw(tree.x, tree.y)


next_state_table = {
    IdleState: {RIGHT_DOWN: RunState},
    RunState: {RIGHT_UP: IdleState}
}


class Tree:

    def __init__(self):
        self.x, self.y = 1200, 145
        self.image = load_image('./Resource/tree.png')
        self.velocity = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self, at):

        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)         # 가장 오래된 이벤트에 의해 현재 상태를 나가고
            self.cur_state = next_state_table[self.cur_state][event]  # 그 이벤트에 의해 다음 상태로 변화
            self.cur_state.enter(self, event)       # 다음 상태로 들어간다

    def draw(self):
        self.cur_state.draw(self)
