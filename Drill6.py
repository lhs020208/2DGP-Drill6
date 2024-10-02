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
def move():
    global x,y, hand_x, hand_y
    for i in range(0, 100 + 1, 1):
        t = i / 1500
    if t == 1:
        x = hand_x
        y = hand_y
    else:
        x = (1 - t) * x + t * hand_x
        y = (1 - t) * y + t * hand_y
def check_boy_hand_L():
    if (x >= hand_x and x - hand_x <= 20) or (x < hand_x and hand_x - x <= 20):
        if (y >= hand_y and y - hand_y <= 20) or (y < hand_y and hand_y - y <= 20):
            return 1
    return 0

while running:
    clear_canvas()
    grass.draw(400, 300)

    if dirx < 0:
        act = 0
    elif dirx > 0:
        act = 1

    move()
    character.clip_draw(frame * 100, act*100, 100, 100, x, y)
    hand.draw(hand_x,hand_y)
    frame = (frame + 1) % 8

    update_canvas()
    handle_events()

    if (check_boy_hand_L()):
        set_hand_pos()

    delay(0.03)


close_canvas()