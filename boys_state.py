import game_framework
from pico2d import *

from Project import title_state
import random
import math


boy = None
grass = None
backGround = None

totalTime = 0
prevTime =0


def enter():
    global boy, grass, background

    boy=Boy()
    grass=Grass()
    background=BackGround()


def exit():
    global boy, grass, background
    del(boy)
    del(grass)
    del(background)


def Collision(param1, param2):
    dist = math.sqrt(pow(param1[0]-param2[0],2)+pow(param1[1]-param2[1],2))
    if(dist<10):
        return True
    return False


def handle_events():
    global prevTime, totalTime
    totalTime +=(get_time() - prevTime)
    prevTime = get_time()
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:   # esc키가 눌리면
            game_framework.change_state(title_state)        # 타이틀화면으로 전환

        boy.handle_event(event)


def update():
    global boy
    boy.update()


def draw():
    global boy, grass, background
    clear_canvas()
    background.draw()
    grass.draw()
    boy.draw()

    update_canvas()
    delay(0.04)
