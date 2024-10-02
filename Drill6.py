from pico2d import *
import random

open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running,act
    global dirx, diry

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False


running = True
act = 1
x = 800 // 2
y = 600 // 2
frame = 0
dirx = 0
diry = 0

hand_x = 800 // 2
hand_y = 600 // 2
def set_hand_pos():
    global hand_x, hand_y
    hand_x = random.randrange(0,800)
    hand_y = random.randrange(0,600)

while running:
    clear_canvas()
    grass.draw(400, 300)

    if dirx < 0:
        act = 0
    elif dirx > 0:
        act = 1

    character.clip_draw(frame * 100, act*100, 100, 100, x, y)
    hand.draw(hand_x,hand_y)
    frame = (frame + 1) % 8

    update_canvas()
    handle_events()

    if (x == hand_x) & (y == hand_y):
        set_hand_pos()

    delay(0.03)


close_canvas()