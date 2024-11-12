import random

from pico2d import *
import game_framework

import game_world
from game_world import add_collision_pair
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy


    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    # fill here
    #Ball for _in range(30)
    balls = [Ball(random.randint(100, 1600 - 100), 60, 0) for _ in range(30)]
    game_world.add_objects(balls, 1)        #게임 월드에 추가.

    #충돌 대상들을 등록해주기
    #계속해서 소년을 추가해주지 않기 위해 이렇게 함.
    add_collision_pair('boy:ball', boy, None)
    for ball in balls:
        add_collision_pair('boy:ball', None, ball)
    #이 코드가 끝나면 dictionary가 이런 식으로 구성됨.
    #{'boy:ball':[ [boy], [ball1, ball2, ball3 .... ball30]  ] }

    #zombie 생성
    zombies = [Zombie() for _ in range(5)]
    game_world.add_objects(zombies, 1)

def finish():
    game_world.clear()
    pass

def update():
    game_world.update() #객체들의 위치가 다 결정 됐다. 따라서 이어서 충돌검사

    # fill here
    game_world.handle_collisions()      #게임월드에게 넘김

    # for ball in balls.copy():
    #     if game_world.collide(boy, ball):
    #         print('boy:ball  COLLIDE')
    #         boy.ball_count += 1
    #         game_world.remove_object(ball)
    #         balls.remove(ball)
    #         #게임 월드에서 제거했지만 루프는 balls에서 ball을 가져옴
    #         #완전히 없애주어야 함.
    #         #balls에서 제거하자

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

