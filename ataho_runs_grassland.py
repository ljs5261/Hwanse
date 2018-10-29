from pico2d import *


class Ground1:
    def __init__(self):
        self.image = load_image('./Resource/grass.png')
        self.x, self.y = 400, 30

    def draw_grass(self):
        self.image.draw(self.x, self.y)

    def move_grass(self):
        self.x -= 5


class Ground2:
    def __init__(self):
        self.image = load_image('./Resource/grass.png')
        self.x, self.y = 1200, 30

    def draw_grass(self):
        self.image.draw(self.x, self.y)

    def move_grass(self):
        self.x -= 5


class BackGround1:
    def __init__(self):
        self.image = load_image('./Resource/grassland.png')
        self.x, self.y = 400, 300

    def draw_bg(self):
        self.image.draw(self.x, self.y)

    def move_bg(self):
        self.x -= 2


class Background2:
    def __init__(self):
        self.image = load_image('./Resource/grassland.png')
        self.x, self.y = 1200, 300

    def draw_bg(self):
        self.image.draw(self.x, self.y)

    def move_bg(self):
        self.x -= 2


class Tree:
    def __init__(self):
        self.image = load_image('./Resource/tree.png')
        self.x, self.y = 1200, 150

    def draw_tree(self):
        self.image.draw(self.x, self.y)

    def move_tree(self):
        self.x -= 5


class ataho:
    def __init__(self):
        self.image = load_image('./Resource/ataho.png')
        self.x, self.y = 200, 90
        self.frame = 0

    def draw_ataho(self):

        self.image.clip_draw(self.frame * 60, 0, 60, 100, 200, 90)
        self.frame = (self.frame + 1) % 5

    def move_ataho(self):
        pass


class Pig:
    def __init__(self):
        self.image = load_image('./Resource/pig_rush_ready.png')
        self.x, self.y = 600, 90
        self.frame = 0

    def draw_pig(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, 90)
        self.frame = (self.frame + 1) % 3

    def move_pig(self):
        self.x -= 13


class Dumpling:
    def __init__(self):
        self.image = load_image('./Resource/dumpling.png')
        self.x, self.y = 400, 90

    def draw_dumpling(self):
        self.image.draw(400, 90)


class Alcohol:
    def __init__(self):
        self.image = load_image('./Resource/alcohol.png')
        self.x, self.y = 400, 90

    def draw_alcohol(self):
        self.image.draw(400, 90)

'''
bg1 = BackGround1()
bg2 = Background2()
g1 = Ground1()
g2 = Ground2()
pig = Pig()
at = ataho()
dumpling = Dumpling()
tree = Tree()
alcohol = Alcohol()

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
    tree.move_tree()
    # pig.move_pig()

    bg1.draw_bg()
    bg2.draw_bg()
    g1.draw_grass()
    g2.draw_grass()
    at.draw_ataho()
    pig.draw_pig()
    tree.draw_tree()
    alcohol.draw_alcohol()
    # dumpling.draw_dumpling()
    update_canvas()

    delay(0.1)
'''


