#Imports
import tkinter as tk
import random

#Dimensions
WIDTH = 600
HEIGHT = 400

#Sprites created

#Spacer lines
def make_spacer_lines():
    h = HEIGHT
    img = tk.PhotoImage(width=1, height=h)
    for y in range(h):
        img.put('Black', (0,y))
    return img
# - Player 
'''WIP'''
def make_player_sprite():
    h = 150
    w = 50
    img = tk.PhotoImage(width=w, height=h)
    color1 = "gray"
    for y in range(h):
        for x in range(w):
            img.put(color1, (x,y))
    return img
# - top spike
def make_top_spike_sprite():
    pattern = [
        "1111111",
        "1111111",
        "0111110",
        "0111110",
        "0111110",
        "0111110",
        "0011100",
        "0011100",
        "0011100",
        "0001000",
        "0001000"]
    scale = 5
    h = len(pattern)*scale
    w = len(pattern[0])*scale
    img = tk.PhotoImage(width=w, height=h)
    color1 = "red"
    for y in range(h):
        for x in range(w):
            if pattern[y//scale][x//scale] == "1":
                img.put(color1, (x,y))
    return img
# - top long spike
def make_top_long_spike_sprite():
    pattern = [
        "111111",
        "111111",
        "011111",
        "011111",
        "011111",
        "011111",
        "001110",
        "001110",
        "001110",
        "000100",
        "000100"]
    scale = 5
    h = len(pattern)*scale
    w = (len(pattern[0])*3+1)*scale
    img = tk.PhotoImage(width=w, height=h)
    color1 = "red"
    for y in range(h):
        for x in range(w):
            if pattern[y//scale][(x//scale)%6] == "1":
                img.put(color1, (x,y))
    return img
# - bottom spike
def make_bottom_spike_sprite():
    pattern = [
        "0001000",
        "0001000",
        "0011100",
        "0011100",
        "0011100",
        "0111110",
        "0111110",
        "0111110",
        "0111110",
        "1111111",
        "1111111"]
    scale = 5
    h = len(pattern)*scale
    w = len(pattern[0])*scale
    img = tk.PhotoImage(width=w, height=h)
    color1 = "red"
    for y in range(h):
        for x in range(w):
            if pattern[y//scale][x//scale] == "1":
                img.put(color1, (x,y))
    return img
# - bottom long spike
def make_bottom_long_spike_sprite():
    pattern = [
        "0001000",
        "0001000",
        "0011100",
        "0011100",
        "0011100",
        "0111110",
        "0111110",
        "0111110",
        "0111110",
        "1111111",
        "1111111"]
    scale = 5
    h = len(pattern)*scale
    w = 19*scale
    img = tk.PhotoImage(width=w, height=h)
    color1 = "red"
    for y in range(h):
        for x in range(w):
            if pattern[y//scale][(x//scale)%6] == "1":
                img.put(color1, (x,y))
    return img
# - short projectile
def make_projectile_sprite():
    pattern = [
        "00001110000",
        "00111111100",
        "01111111110",
        "01111111110",
        "11111011111",
        "11110201111",
        "11111011111",
        "01111111110",
        "01111111110",
        "00111111100",
        "00001110000"]
    scale = 5
    h = len(pattern)*scale
    w = len(pattern[0])*scale
    img = tk.PhotoImage(width=w, height=h)
    color1 = "gray"
    color2 = "red"
    for y in range(h):
        for x in range(w):
            if pattern[y//scale][x//scale] == "1":
                img.put(color1, (x,y))
            elif pattern[y//scale][x//scale] == "2":
                img.put(color2, (x,y))
    return img
# - long projectile (group)
def make_long_projectile_head_sprite():
    pattern = [
        "00001111",
        "00111111",
        "01111111",
        "01111111",
        "11111110",
        "11111000",
        "11111110",
        "01111111",
        "01111111",
        "00111111",
        "00001111"]
    scale = 5
    h = len(pattern)*scale
    w = len(pattern[0])*scale
    img = tk.PhotoImage(width=w, height=h)
    color1 = "gray"
    for y in range(h):
        for x in range(w):
            if pattern[y//scale][x//scale] == "1":
                img.put(color1, (x,y))
    return img
def make_long_projectile_body_sprite():
    pattern = "11110201111"
    scale = 5
    h = len(pattern)*scale
    w = 10*scale
    img = tk.PhotoImage(width=w, height=h)
    color1 = "gray"
    color2 = "red"
    for y in range(h):
        for x in range(w):
            if pattern[y//scale] == "1":
                img.put(color1, (x,y))
            elif pattern[y//scale] == "2":
                img.put(color2, (x,y))
    return img
def make_long_projectile_tail_sprite():
    pattern = [
        "11110000",
        "11111100",
        "11111110",
        "11111110",
        "01111111",
        "00011111",
        "01111111",
        "11111110",
        "11111110",
        "11111100",
        "11110000"]
    scale = 5
    h = len(pattern)*scale
    w = len(pattern[0])*scale
    img = tk.PhotoImage(width=w, height=h)
    color1 = "gray"
    for y in range(h):
        for x in range(w):
            if pattern[y//scale][x//scale] == "1":
                img.put(color1, (x,y))
    return img
# - extruded + extruded-long projectile (same sprite as short + long)




#initialize stuff
root = tk.Tk()
root.title("COSMOS INFILTRATORS")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

player_img=make_player_sprite()


spikes = []

small_top_spike_img = make_top_spike_sprite()
def make_small_top_spike():
    small_top_spike = canvas.create_image(670-225, 0, image=small_top_spike_img, anchor = 'nw')
    spikes.append(small_top_spike)
make_small_top_spike()

large_top_spike_img = make_top_long_spike_sprite()
def make_large_top_spike():
    large_top_spike = canvas.create_image(670-225, 0, image=large_top_spike_img, anchor = 'nw')
    spikes.append(large_top_spike)
make_large_top_spike()

small_bottom_spike_img = make_bottom_spike_sprite()
def make_small_bottom_spike():
    small_bottom_spike = canvas.create_image(670-225, HEIGHT, image=small_bottom_spike_img, anchor = 'sw')
    spikes.append(small_bottom_spike)
make_small_bottom_spike()

large_bottom_spike_img = make_bottom_long_spike_sprite()
def make_large_bottom_spike():
    large_bottom_spike = canvas.create_image(670-225, HEIGHT, image=large_bottom_spike_img, anchor = 'sw')
    spikes.append(large_bottom_spike)
make_large_bottom_spike()


projectiles = []

projectile_img = make_projectile_sprite()
def make_projectile(side):
    y_position = 73
    if side == "bottom":
        y_position+= 200
    projectile = canvas.create_image(648-225, y_position, image=projectile_img, anchor = 'nw')
    projectiles.append(projectile)
make_projectile("top")
make_projectile("bottom")

long_head_img=make_long_projectile_head_sprite()
long_body_img=make_long_projectile_body_sprite()
long_tail_img=make_long_projectile_tail_sprite()
def make_large_projectile(side):
    y_position = 73
    if side == "bottom":
        y_position+= 200
    long_projectile_head = canvas.create_image(648-225,y_position, image=long_head_img, anchor = 'nw')
    long_projectile_body = canvas.create_image(648-225+40,y_position, image=long_body_img, anchor = 'nw')
    long_projectile_tail = canvas.create_image(648-225+90,y_position, image=long_tail_img, anchor = 'nw')
    projectiles.append(long_projectile_head)
    projectiles.append(long_projectile_body)
    projectiles.append(long_projectile_tail)
make_large_projectile("top")
make_large_projectile("bottom")

print(projectiles)

spacer_line_img = make_spacer_lines()
def draw_spacers():
    for x in range(1,8):
        canvas.create_image(x*WIDTH/8, 0, image=spacer_line_img, anchor = 'n')




#jump function
def move_up(event):
    canvas.moveto(player, 0, 25)
def move_down(event):
    canvas.moveto(player, 0,225)
root.bind("<space>", move_up)
root.bind("<KeyRelease-space>", move_down)

#collisions
def collision(a, b):
    ax1, ay1, ax2, ay2 = canvas.bbox(a)
    bx1, by1, bx2, by2 = canvas.bbox(b)
    return ax1<bx2 and ax2>bx1 and ay1<by2 and ay2>by1

#score here??? could move

#projectile movement
def move_obstacles():
    for projectile in projectiles:
        canvas.move(projectile, -6, 0)
    for spike in spikes:
        canvas.move(spike, -6, 0)



previous_obstacle_num = -1
def make_obstacle():
    global previous_obstacle_num
    obstacle_list = [lambda:make_projectile("top"),
                     lambda:make_projectile("bottom"),
                     lambda:[make_projectile("top"), make_small_bottom_spike()],
                     lambda:[make_projectile("bottom"), make_small_top_spike()],
                     lambda:make_small_bottom_spike(),
                     lambda:make_small_top_spike(),
                     lambda:[make_projectile("top"), make_projectile("bottom")],
                     lambda:make_large_projectile("top"), #this and below are extruded
                     lambda:make_large_projectile("bottom"),
                     lambda:make_large_bottom_spike(),
                     lambda:make_large_top_spike(),
                     lambda:[make_large_projectile("top"), make_large_bottom_spike()],
                     lambda:[make_large_projectile("bottom"), make_large_top_spike()],
                     lambda:[make_projectile("bottom"), make_large_projectile("top")],
                     lambda:[make_projectile("top"), make_large_projectile("bottom")]
                     ]
    print(previous_obstacle_num)
    if previous_obstacle_num >= 7:
        previous_obstacle_num = -1
        return
    obstacle_num = random.randint(0, 14)
    while previous_obstacle_num == obstacle_num:
        obstacle_num = random.randint(0, 14)
    obstacle = obstacle_list[obstacle_num]()
    previous_obstacle_num = obstacle_num

    

#game loop
alive = True
timer = 0
def game_loop():
    global timer, alive
    timer += 40
    if timer > 500:
        timer -= 500
        make_obstacle()
    move_obstacles()
    if not alive:
        canvas.delete(all)
        reset()
        return
    for projectile in projectiles[:]:
        if collision(projectile,player):
            canvas.delete(projectile)
            if projectile in projectiles:
                projectiles.remove(projectile)
            break
    for projectile in projectiles:
        ex1, ey1, ex2, ey2 = canvas.bbox(projectile)
        px1, py1, px2, py2 = canvas.bbox(player)
        if ex1 <= px1:
            alive = False
    root.after(40, game_loop) #move 6 (150 = 100y/x) (150 = 100y/4) (y=6)

#start & reset game
def start():
    global player
    player = canvas.create_image(0,225, image=player_img, anchor = 'nw')
    draw_spacers()
    game_loop()

def reset(event=None):
    global alive
    canvas.delete("all")
    projectiles.clear()
    spikes.clear()
    alive = True
    start()
root.bind("r", reset)
reset()
root.mainloop()