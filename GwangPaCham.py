from pico2d import *
import game_world


class GwangPaCham:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('./Resource/GwangPaCham.png')
        self.frame = 0
        self.count = 0

    def draw(self):
        self.image.clip_draw(0, 500 - self.frame * 100, 800, 100, self.x, self.y)
        delay(0.05)

    def update(self):
        if self.count % 2 == 0:
            self.frame = (self.frame + 1)% 6
        self.count += 1
        if self.count == 10:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 380, self.y - 50, self.x + 400, self.y + 45
