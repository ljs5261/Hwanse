from pico2d import *
open_canvas()
import math
import time


class Ground1:
    def __init__(self):
        self.image = load_image('./Resource/hellgrass.png')
        self.x, self.y = 400, 30

    def draw_grass(self):
        self.image.draw(self.x, self.y)

    def move_grass(self):
        self.x -= 5


class Ground2:
    def __init__(self):
        self.image = load_image('./Resource/hellgrass.png')
        self.x, self.y = 1200, 30

    def draw_grass(self):
        self.image.draw(self.x, self.y)

    def move_grass(self):
        self.x -= 5


class BackGround1:
    def __init__(self):
        self.image = load_image('./Resource/hell.png')
        self.x, self.y = 400, 300

    def draw_bg(self):
        self.image.draw(self.x, self.y)

    def move_bg(self):
        self.x -= 2


class Background2:
    def __init__(self):
        self.image = load_image('./Resource/hell.png')
        self.x, self.y = 1200, 300

    def draw_bg(self):
        self.image.draw(self.x, self.y)

    def move_bg(self):
        self.x -= 2


class ataho:
    def __init__(self):
        self.image = load_image('./Resource/ataho.png')
        self.x, self.y = 200, 85
        self.frame = 0

    def draw_ataho(self):
        self.image.clip_draw(self.frame * 60, 0, 60, 100, 200, 85)
        self.frame = (self.frame + 1) % 5

    def move_ataho(self):
        pass


class Gargoyle:
    def __init__(self):
        self.image = load_image('./Resource/Gargoyle_attack.png')
        self.x, self.y = 600, 95
        self.frame = 0

    def draw_gargoyle(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, 95)

    def gargoyle_frame(self):
        self.frame = (self.frame + 1) % 5

    def move_gargoyle(self):
        self.x -= 5


class Devil:
    def __init__(self):
        self.image = load_image('./Resource/Devil.png')
        self.x, self.y = 600, 300

    def draw_devil(self):
        global T
        T = time.time()
        self.image.draw(self.x, 300 + (30 * math.sin(T)))


bg1 = BackGround1()
bg2 = Background2()
g1 = Ground1()
g2 = Ground2()
at = ataho()
gargoyle = Gargoyle()
gargoyle_frame_count = 0
devil = Devil()


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
    # gargoyle.move_gargoyle()

    bg1.draw_bg()
    bg2.draw_bg()
    g1.draw_grass()
    g2.draw_grass()
    at.draw_ataho()
    devil.draw_devil()
    # gargoyle.draw_gargoyle()
    # if gargoyle_frame_count % 2 == 0:
    #    gargoyle.gargoyle_frame()

    update_canvas()

    delay(0.1)
    gargoyle_frame_count += 1

close_canvas()

