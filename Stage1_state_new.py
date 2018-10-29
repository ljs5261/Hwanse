from pico2d import *

import game_framework

from Ataho import Ataho
from grass import Grass
from BackGround1 import BackGround

name = "MainState"

ataho = None
bg = None
team =[]
xpos_plus = 400


def enter():
    global ataho, bg, xpos_plus, team
    ataho = Ataho()
    for i in range(0, 1):
        team += [Grass(xpos_plus)]
        xpos_plus += 800
    bg = BackGround()


def exit():
    global ataho, team, bg
    del ataho
    for grass in team:
        del grass
    del bg


def pause():
    pass


def resume():
    pass


def handle_events():
    global ataho, team
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            ataho.handle_event(event)
            for grass in team:
                grass.handle_event(event)


def update():
    global ataho, team
    ataho.update()
    for grass in team:
        grass.update(ataho)
    delay(0.08)


def draw():
    global ataho, team, bg
    clear_canvas()
    for grass in team:
        grass.draw()
    ataho.draw()
    update_canvas()






