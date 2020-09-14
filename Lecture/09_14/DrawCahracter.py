from pico2d import *

open_canvas()

grass = load_image('Image/grass.png')
character = load_image('Image/character.png')

grass.draw_now(400, 30)
character.draw_now(400, 85)

delay(2)

close_canvas()