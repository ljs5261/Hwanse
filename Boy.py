from pico2d import *


class Boy:
    RIGHT_RUN, LEFT_RUN, RIGHT_STAND, LEFT_STAND = 0, 1, 2, 3
    def __init__(self):
        self.x, self.y = 0, 75
        self.frame = 0
        self.image = load_image('./Resource/ataho1.png')
        self.state = 2
        self.hp = 100

    def update(self):
        self.frame = (self.frame + 1) % 5+5
        if self.state in (self.RIGHT_RUN,):
            self.x = min(764, self.x + 6)
        elif self.state in (self.LEFT_RUN,):
            self.x = max(32, self.x - 6)

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                if self.state in (self.LEFT_RUN,  self.RIGHT_STAND,self.LEFT_STAND):
                    self.state = self.RIGHT_RUN
            elif event.key == SDLK_LEFT:
                if self.state in (self.RIGHT_RUN,  self.RIGHT_STAND,self.LEFT_STAND):
                    self.state = self.LEFT_RUN
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                if self.state in (self.RIGHT_RUN,):
                    self.state = self.RIGHT_STAND
            elif event.key == SDLK_LEFT:
                if self.state in (self.LEFT_RUN,):
                    self.state = self.LEFT_STAND
    def draw(self):
        if self.state  == self.RIGHT_RUN:
            self.image.clip_draw(self.frame * 48, (self.state), 50, 64, self.x, self.y)
        elif self.state  == self.RIGHT_STAND:
            self.image.clip_draw(self.frame * 0, ((self.state - 1) * 64), 50, 64, self.x, self.y)
        elif self.state  == self.LEFT_RUN:
            self.image.clip_draw(self.frame * 48, 64, 50, 64, self.x, self.y)
        elif self.state  == self.LEFT_STAND:
            self.image.clip_draw(self.frame * 0, ((self.state - 2) * 64), 50, 64, self.x, self.y)

