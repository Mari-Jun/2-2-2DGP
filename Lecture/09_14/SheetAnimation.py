from pico2d import *

open_canvas()

grass = load_image('Image/grass.png')
character = load_image('Image/run_animation.png')

x = 0
frame_index = 0
while x < 800:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame_index * 100, 0, 100, 100, x, 85)
    update_canvas()
    frame_index = (frame_index + 1) % 8
    x = x + 4
    delay(0.01)
    get_events()

close_canvas()