from pico2d import *
from gobj import *

def handle_events():
    global running
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False

open_canvas()

grass = Grass()
team = [ Boy() for i in range(11 )]

running = True

while running:
    clear_canvas()

    grass.draw()
    for boy in team:
        boy.draw()

    update_canvas()
    handle_events()

    for boy in team:
        boy.update()

    delay(0.01)
    get_events()

close_canvas()