from pico2d import *

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

grass = load_image('Image/grass.png')
character = load_image('Image/run_animation.png')

running = True
x = 0
frame_index = 0
while running and x < 800:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame_index*100, 0, 100, 100, x, 85)
    update_canvas()

    handle_events()

    x += 2
    frame_index = (frame_index + 1) % 8
    delay(0.01)

close_canvas()