from pico2d import *


class Ground1:
    def __init__(self):
        self.image = load_image('./Resource/bamboo.png')
        self.x, self.y = 400, 30

    def draw_grass(self):
        self.image.draw(self.x, self.y)

    def move_grass(self):
        self.x -= 5


class Ground2:
    def __init__(self):
        self.image = load_image('./Resource/bamboo.png')
        self.x, self.y = 1200, 30

    def draw_grass(self):
        self.image.draw(self.x, self.y)

    def move_grass(self):
        self.x -= 5


class BackGround1:
    def __init__(self):
        self.image = load_image('./Resource/ForestHouse.png')
        self.x, self.y = 400, 350

    def draw_bg(self):
        self.image.draw(self.x, self.y)

    def move_bg(self):
        self.x -= 2


class Background2:
    def __init__(self):
        self.image = load_image('./Resource/ForestHouse.png')
        self.x, self.y = 1200, 350

    def draw_bg(self):
        self.image.draw(self.x, self.y)

    def move_bg(self):
        self.x -= 2


class ataho:
    def __init__(self):
        self.image = load_image('./Resource/ataho.png')
        self.x, self.y = 300, 120
        self.frame = 0

    def draw_ataho(self):
        self.image.clip_draw(self.frame * 60, 0, 60, 100, 300, 120)
        self.frame = (self.frame + 1) % 5

    def move_ataho(self):
        pass


class Bisangak:
    def __init__(self):
        self.image = load_image('./Resource/맹호비상각완성.png')
        self.x, self.y = 100, 200

    def draw_bisangak(self):
        self.image.draw(self.x, 200)

    def move_bisangak(self):
        self.x += 5


class Dragon:
    def __init__(self):
        self.image = load_image('./Resource/dragon.png')
        self.x, self.y = 600, 200
        self.frame = 0

    def draw_dragon(self):
        self.image.clip_draw(self.frame * 350, 0, 350, 350, 600, 200)

    def dragon_frame(self):
        self.frame = (self.frame + 1) % 2

    def move_dragon(self):
        pass


class Rinshang:
    def __init__(self):
        self.image = load_image('./Resource/rinshang_skill.png')
        self.x, self.y = 600, 120
        self.frame = 0

    def draw_rinshang(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, 600, 120)

    def rinshang_frame(self):
        self.frame = (self.frame + 1) % 3


class Lightning:
    def __init__(self):
        self.image = load_image('./Resource/lightning.png')
        self.x, self.y = 600, 350
        self.frame = 0

    def draw_lightning(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 600, 600, 350)
        self.frame = (self.frame + 1) % 4


bg1 = BackGround1()
bg2 = Background2()
g1 = Ground1()
g2 = Ground2()
at = ataho()
dr = Dragon()
rin = Rinshang()
lightning = Lightning()
bisangak = Bisangak()

dr_frame_count = 0
rin_frame_count = 0

while True:
    clear_canvas()
    if g1.x <= -400:
        del g1
        g1 = Ground2()
    if g2.x <= -400:
        del g2
        g2 = Ground2()
    if bg1.x <= -400:
        del bg1
        bg1 = Background2()
    if bg2.x <= -400:
        del bg2
        bg2 = Background2()

    bg1.move_bg()
    bg2.move_bg()
    g1.move_grass()
    g2.move_grass()
    bisangak.move_bisangak()

    bg1.draw_bg()
    bg2.draw_bg()
    g1.draw_grass()
    g2.draw_grass()
    bisangak.draw_bisangak()
    # at.draw_ataho()
    # lightning.draw_lightning()
    rin.draw_rinshang()
    # dr.draw_dragon()
    if dr_frame_count % 4 == 0:
        dr.dragon_frame()
    if rin_frame_count % 2 == 0:
        rin.rinshang_frame()

    update_canvas()

    delay(0.1)
    dr_frame_count += 1
    rin_frame_count += 1



