from pico2d import *
import game_world
import game_framework

from Ataho import Ataho
from grass import Grass
from BackGround_One import BackGround
from tree import Tree
from wolf import Wolf
from thorn import Thorn
from slime import Slime
from pig import Pig
from dumpling import Dumpling
from Hellgate import Hellgate
from snake import Snake

ataho = None
team_grass = []
team_bg = []
team_tree = []
wolf = []
team_wolf = []
team_thorn_one = []
team_thorn_two = []
team_slime = []
pig = None
dumpling = None
hell_gate = None
snake = None


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
    global ataho, team_grass, team_bg, team_tree, team_wolf, team_thorn_one, team_thorn_two, team_slime, pig, dumpling
    global hell_gate, snake, wolf
    ataho = Ataho()
    team_grass = [Grass(i) for i in range(400, 6800, 800)]
    team_bg = [BackGround(i) for i in range(400, 3400, 800)]
    team_tree = [Tree(i) for i in range(800, 1400, 300)]
    wolf = Wolf(1200)
    team_wolf = [Wolf(i) for i in range(3250, 3450, 50)]
    team_wolf.append(wolf)
    team_thorn_one = [Thorn(i) for i in range(1600, 1720, 60)]
    team_thorn_two = [Thorn(i) for i in range(2000, 2120, 60)]
    team_slime = [Slime(i) for i in range(2200, 2600, 100)]
    pig = Pig()
    dumpling = Dumpling()
    hell_gate = Hellgate()
    snake = Snake()

    game_world.add_objects(team_grass, 1)
    game_world.add_object(ataho, 1)
    game_world.add_objects(team_bg, 0)
    game_world.add_objects(team_tree, 1)
    game_world.add_objects(team_wolf, 1)
    game_world.add_objects(team_thorn_one, 1)
    game_world.add_objects(team_thorn_two, 1)
    game_world.add_objects(team_slime, 1)
    game_world.add_object(pig, 1)
    game_world.add_object(dumpling, 1)
    game_world.add_object(hell_gate, 0)
    game_world.add_object(snake, 1)


def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    global ataho, pig, team_grass, team_bg, team_tree, team_wolf, team_thorn_one, team_thorn_two, team_slime, dumpling
    global hell_gate, snake
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            ataho.handle_event(event)
            pig.handle_event(event)
            dumpling.handle_event(event)
            hell_gate.handle_event(event)
            snake.handle_event(event)
            for grass in team_grass:
                grass.handle_event(event)
            for bg in team_bg:
                bg.handle_event(event)
            for tree in team_tree:
                tree.handle_event(event)
            for wolf in team_wolf:
                wolf.handle_event(event)
            for thorn in team_thorn_one:
                thorn.handle_event(event)
            for thorn in team_thorn_two:
                thorn.handle_event(event)
            for slime in team_slime:
                slime.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






