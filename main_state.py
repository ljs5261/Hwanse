import game_framework
from pico2d import *
from Boy import *
from World import *
from Enemy import *
from JangPung import *
from Project import title_state
import random
import math



boy = None
grass = None
backGround = None
jangPungList = []
enemyList = []
totalTime = 0
prevTime =0

def enter():
    global boy, grass, background, enemy

    boy=Boy()
    grass=Grass()
    background=BackGround()

def exit():
    global boy,grass,background, enemy
    del(boy)
    del(grass)
    del(background)
    del(enemy)

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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if (random.randint(0, 100) < 40):
                if(totalTime>0.1):
                    Jang = JangPung(boy.x, boy.state % 2)
                    jangPungList.append(Jang)
                    totalTime = 0
        boy.handle_event(event)
def update():
    global boy,  enemy, Jang
    boy.update()
    for jangPung in jangPungList:
        jangPung.update()
    for enemy in enemyList:
        enemy.update()
        if(enemy.dead):
            enemyList.remove(enemy)
            continue
        if(Collision((enemy.x,enemy.y),(boy.x,boy.y))):
            boy.hp -=1
        for jangPung in jangPungList:
            if(Collision((enemy.x,enemy.y),(jangPung.x,jangPung.y))):
                enemy.dead = True

    if(boy.hp<0):#죽을때
        pass

    if(random.randint(0,100)<3):
        newEnemy = Enemy()
        enemyList.append(newEnemy)
def draw():
    global boy, grass, background, enemy,jangPungList
    clear_canvas()
    background.draw()
    grass.draw()
    boy.draw()
    for jangPung in jangPungList:
        jangPung.draw()
    for enemy in enemyList:
        enemy.draw()
    update_canvas()
    delay(0.04)
