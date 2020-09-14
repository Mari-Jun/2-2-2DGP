from pico2d import *

open_canvas()

grass = load_image('Image/grass.png')
character = load_image('Image/character.png')

x = 0
while x < 800:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, 85)
    x = x + 2
    update_canvas()
    delay(0.01)
    get_events()

close_canvas()