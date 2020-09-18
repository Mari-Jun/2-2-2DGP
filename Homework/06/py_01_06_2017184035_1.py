from pico2d import *
import helper

def handle_events():
    global running, speed
    global move_list, move_count
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
        elif e.type == SDL_MOUSEBUTTONDOWN:
            move_list.append((e.x, get_canvas_height() - 1 - e.y, move_list[len(move_list) - 1][2] + 1))
            if move_count == 0:
                move_count += 1

def move_character():
    global x, y, speed
    global move_list, move_count

    if move_count < len(move_list):
        delta = helper.delta((x, y), move_list[move_count][0:2], move_list[move_count][2])
        (x, y), done = helper.move_toward((x, y), delta, move_list[move_count][0:2])

        if done:
            move_count += 1
    else:
        move_list.append((x, y, 0))
        move_count += 1

open_canvas()

grass = load_image('Image/grass.png')
character = load_image('Image/run_animation.png')

running = True
x, y = 400, 85
move_list = [(400, 85, 0)]
move_count = 0

frame_index = 0
while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame_index*100, 0, 100, 100, x, y)
    update_canvas()

    handle_events()
    move_character()

    frame_index = (frame_index + 1) % 8
    delay(0.01)

close_canvas()
