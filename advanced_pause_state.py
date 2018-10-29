import game_framework
from pico2d import *
import Stage1_state

image = None


def enter():
    global image
    image = load_image('./Resource/pause.png')
    Stage1_state.pause()


def exit():
    global image
    del image


def update():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:         # p키가 눌리면
            game_framework.change_state(Stage1_state)                 # 타이틀화면으로 전환


def draw():
    global image
    clear_canvas()
    Stage1_state.draw_ataho_no_frame()
    image.draw(400, 300)
    update_canvas()
    delay(0.05)


def pause():
    pass
