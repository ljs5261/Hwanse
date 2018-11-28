from pico2d import *
import game_world
import game_framework

from Ataho import Ataho
from BackGround_Two import BackGround
from bamboo import Bamboo

ataho = None
team_bg = []
team_bamboo = []


def get_ataho():
    return ataho


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def enter():
    global ataho, team_bg, team_bamboo
    ataho = Ataho()
    game_world.objects = [[],[]]
    team_bg = [BackGround(i) for i in range(400, 2800, 800)]
    team_bamboo = [Bamboo(i) for i in range(400, 4400, 800)]

    game_world.add_objects(team_bg, 0)
    game_world.add_objects(team_bamboo, 1)
    game_world.add_object(ataho, 1)

def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    global ataho, team_bg, team_bamboo
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            ataho.handle_event(event)
            for bg in team_bg:
                bg.handle_event(event)
            for bamboo in team_bamboo:
                bamboo.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    print(ataho.scroll_toggle)

    delay(0.02)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






