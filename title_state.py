import game_framework
from pico2d import *

from Project import main_state

name= "TitleState"
image=None
title_time = 0

def enter():
    global image
    image = load_image('hwanse.png')

def exit():
    global image
    del(image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key)==(SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)


def update():
    global title_time

    if (title_time > 1.0):
        title_time = 0
        # game_framework.quit()
        game_framework.change_state(main_state)
        delay(0.01)

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()