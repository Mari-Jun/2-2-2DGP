from pico2d import *

def handle_events():
    global running, dx
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_RIGHT:
                dx = 1
            elif e.key == SDLK_LEFT:
                dx = -1
            elif e.key == SDLK_ESCAPE:
                running = False
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_RIGHT:
                dx = -1
            elif e.key == SDLK_LEFT:
                dx = +1



open_canvas()

grass = load_image('Image/grass.png')
character = load_image('Image/run_animation.png')

running = True
x = 400
dx = 0
fidx = 0

frame_index = 0
while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame_index*100, 0, 100, 100, x, 85)
    update_canvas()

    handle_events()

    x += dx

    frame_index = (frame_index + 1) % 8
    delay(0.01)

close_canvas()