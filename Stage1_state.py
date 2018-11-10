from pico2d import *
import game_world
import game_framework

from Ataho import Ataho
from grass import Grass
from BackGround import BackGround
from tree import Tree
from wolf import Wolf
from pig import Pig

ataho = None
team_grass = []
team_bg = []
team_tree = []
team_wolf = []
pig = None


def enter():
    global ataho, team_grass, team_bg, team_tree, team_wolf, pig, x_plus
    ataho = Ataho()
    team_grass = [Grass(i) for i in range(400, 2800, 800)]
    team_bg = [BackGround(i) for i in range(400, 2000, 800)]
    team_tree = [Tree() for i in range(1)]
    team_wolf = [Wolf() for i in range(1)]
    pig = Pig()

    game_world.add_objects(team_grass, 1)
    game_world.add_object(ataho, 1)
    game_world.add_objects(team_bg, 0)
    #game_world.add_objects(team_tree, 1)
    #game_world.add_objects(team_wolf, 1)
    #game_world.add_object(pig, 1)


def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    global ataho
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            ataho.handle_event(event)
            pig.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.08)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






