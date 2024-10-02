from pico2d import *

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

while running:
    clear_canvas()
    grass.draw(400, 300)

    if dirx < 0:
        act = 0
    elif dirx > 0:
        act = 1

    character.clip_draw(frame * 100, act*100, 100, 100, x, y)

    frame = (frame + 1) % 8
    update_canvas()
    handle_events()
    delay(0.03)


close_canvas()