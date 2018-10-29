from pico2d import *
import game_framework

import advanced_pause_state
from ataho_Class import *

jump = 0        # 0:점프아닌 상태, 1:점프중인 상태
ataho = None
grass = None
bg = None
first_start = 1


def enter():
    global ataho, grass, bg, first_start
    if first_start == 1:    # stage1 최초 실행 시

        ataho = ataho()
        grass = Grass()
        bg = BackGround()
        first_start += 1
    else:                   # pause키 눌린 이후 실행

        ataho = ataho()
        grass = Grass()
        bg = BackGround()
        at.start_pause_next()


def exit():
    global ataho, grass, bg
    del ataho
    del grass
    del bg


def handle_events():
    global ataho
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_p:          # p키가 눌리면
                game_framework.push_state(advanced_pause_state)               # pause 화면으로 전환
            elif event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            ataho.handle_event(event)


def update():
    global ataho
    ataho.update()


def draw():
    global ataho, grass, bg
    clear_canvas()
    bg.draw_bg()
    grass.draw_grass()
    ataho.draw()
    update_canvas()
    delay(0.04)


def draw_ataho_no_frame():
    global at, grass, bg
    clear_canvas()
    bg.draw_bg()
    grass.draw_grass()
    at.draw_no_frame()
    update_canvas()
    delay(0.04)


def pause():
    global ataho
    ataho.pause()


def resume():
    pass