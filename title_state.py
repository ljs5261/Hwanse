import game_framework
from pico2d import *
import Stage2_state
name = "TitleState"
image = None


def enter():
    global image
    image = load_image('./Resource/hwanse.png')


def exit():
    global image
    del image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(Stage2_state)


def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()


def update():   # 그림만 보여주면 되므로 업데이트할 필요없다
    pass


def pause():
    pass


def resume():
    pass






