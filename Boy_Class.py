from pico2d import *

# ataho Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER = range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,

}


class IdleState:
    @staticmethod
    def enter(ataho, event):
        if event == RIGHT_DOWN:
            ataho.velocity = 2
        elif event == LEFT_DOWN:
            ataho.velocity = -2
        elif event == RIGHT_UP:
            ataho.velocity = -2
        elif event == LEFT_UP:
            ataho.velocity = 2
        ataho.timer = 1000

    @staticmethod
    def exit(ataho, event):
        pass

    @staticmethod
    def do(ataho):
        ataho.frame = (ataho.frame + 1) % 8
        ataho.timer -= 1
        if ataho.timer == 0:
            ataho.add_event(SLEEP_TIMER)

    @staticmethod
    def draw(ataho):
        if ataho.dir == 2:
            ataho.image.clip_draw(ataho.frame * 100, 300, 100, 100, ataho.x, ataho.y)
        else:
            ataho.image.clip_draw(ataho.frame * 100, 200, 100, 100, ataho.x, ataho.y)


class RunState:
    @staticmethod
    def enter(ataho, event):
        if event == RIGHT_DOWN:
            ataho.velocity = 2
        elif event == LEFT_DOWN:
            ataho.velocity = -2
        elif event == RIGHT_UP:
            ataho.velocity = 2
        elif event == LEFT_UP:
            ataho.velocity = -2
        ataho.dir = ataho.velocity

    @staticmethod
    def exit(ataho, event):
        pass

    @staticmethod
    def do(ataho):
        ataho.frame = (ataho.frame + 1) % 8
        ataho.timer -= 1
        ataho.x += ataho.velocity
        ataho.x = clamp(25, ataho.x, 800 - 25)

    @staticmethod
    def draw(ataho):
        if ataho.velocity == 2:
            ataho.image.clip_draw(ataho.frame * 100, 100, 100, 100, ataho.x, ataho.y)
        else:
            ataho.image.clip_draw(ataho.frame * 100, 0, 100, 100, ataho.x, ataho.y)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
               LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState}

}


class ataho:

    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.image = load_image('./Resource/animation_sheet.png')
        self.dir = 2
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