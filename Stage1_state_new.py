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
team_grass =[]
team_bg = []
grass_xpos_plus = 400
bg_xpos_plus = 400
tree1 = None
wolf = None
pig = None


def enter():
    global ataho, grass_xpos_plus, bg_xpos_plus, team_grass, team_bg, tree1, wolf, pig
    ataho = Ataho()
    for i in range(0, 3):
        team_grass += [Grass(grass_xpos_plus)]
        grass_xpos_plus += 800
    for i in range(0, 3):
        team_bg += [BackGround(bg_xpos_plus)]
        bg_xpos_plus += 800
    tree1 = Tree(1100)
    wolf = Wolf(1000)
    pig = Pig()

    game_world.add_object(ataho, 1)
    game_world.add_object(tree1, 1)
    game_world.add_object(wolf, 1)
    game_world.add_object(pig, 1)

    for grass in team_grass:
        game_world.add_object(grass, 0)
    for bg in team_bg:
        game_world.add_object(bg, 0)


def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    global ataho, team_grass, team_bg, tree1, wolf, pig
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            ataho.handle_event(event)
            for grass in team_grass:
                grass.handle_event(event)
            for bg in team_bg:
                bg.handle_event(event)
            tree1.handle_event(event)
            wolf.handle_event(event)
            pig.handle_event(event)


def update():
    global ataho, team_grass, team_bg, tree1, wolf, pig
    if team_grass[2].x >= 410:
        for bg in team_bg:
            bg.update(ataho)
        for grass in team_grass:
            grass.update(ataho)

    ataho.update()
    tree1.update(ataho)
    wolf.update(ataho)
    pig.update(ataho)
    delay(0.08)


def draw():
    global ataho, team_grass, team_bg, tree1, wolf, pig
    clear_canvas()
    for bg in team_bg:
        bg.draw()
    for grass in team_grass:
        grass.draw()
    ataho.draw()
    tree1.draw()
    wolf.draw()
    pig.draw()

    update_canvas()






