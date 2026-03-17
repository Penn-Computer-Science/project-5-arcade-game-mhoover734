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
#Scoreboard
def make_scoreboard():
    h = 30
    w = 150
    img = tk.PhotoImage(width=w, height=h)
    color1 = "gray"
    for y in range(h):
        for x in range(w):
            img.put(color1, (x,y))
    return img
# - Player 
'''WIP'''
def make_player_sprite():
    h = 150
    w = 10
    img = tk.PhotoImage(width=w, height=h)
    color1 = "blue"
    for y in range(h):
        for x in range(w):
            img.put(color1, (x,y))
    return img
# - top spike
def make_top_spike_sprite():
    pattern = [
        "11111",
        "11111",
        "11111",
        "11111",
        "01110",
        "01110",
        "01110",
        "01110",
        "00100",
        "00100",
        "00100",
        "00100"]
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
        "11111",
        "11111",
        "11111",
        "11111",
        "01110",
        "01110",
        "01110",
        "01110",
        "00100",
        "00100",
        "00100",
        "00100"]
    scale = 5
    h = len(pattern)*scale
    w = (len(pattern[0])*3-2)*scale
    img = tk.PhotoImage(width=w, height=h)
    color1 = "red"
    for y in range(h):
        for x in range(w):
            if pattern[y//scale][(x//scale)%(len(pattern[0])-1)] == "1":
                img.put(color1, (x,y))
    return img
# - bottom spike
def make_bottom_spike_sprite():
    pattern = [
        "00100",
        "00100",
        "00100",
        "00100",
        "01110",
        "01110",
        "01110",
        "01110",
        "11111",
        "11111",
        "11111",
        "11111"]
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
        "00100",
        "00100",
        "00100",
        "00100",
        "01110",
        "01110",
        "01110",
        "01110",
        "11111",
        "11111",
        "11111",
        "11111"]
    scale = 5
    h = len(pattern)*scale
    w = (len(pattern[0])*3-2)*scale
    img = tk.PhotoImage(width=w, height=h)
    color1 = "red"
    for y in range(h):
        for x in range(w):
            if pattern[y//scale][(x//scale)%(len(pattern[0])-1)] == "1":
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
root.title("Le Bad \"Rhythm\" Game")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

#Initializing Sprites - Player
player_img=make_player_sprite()

#Initializing Sprites - Spikes
spikes = []

small_top_spike_img = make_top_spike_sprite()
def make_small_top_spike():
    small_top_spike = canvas.create_image(670, 0, image=small_top_spike_img, anchor = 'nw')
    spikes.append(small_top_spike)

large_top_spike_img = make_top_long_spike_sprite()
def make_large_top_spike():
    large_top_spike = canvas.create_image(670, 0, image=large_top_spike_img, anchor = 'nw')
    spikes.append(large_top_spike)

small_bottom_spike_img = make_bottom_spike_sprite()
def make_small_bottom_spike():
    small_bottom_spike = canvas.create_image(670, HEIGHT, image=small_bottom_spike_img, anchor = 'sw')
    spikes.append(small_bottom_spike)

large_bottom_spike_img = make_bottom_long_spike_sprite()
def make_large_bottom_spike():
    large_bottom_spike = canvas.create_image(670, HEIGHT, image=large_bottom_spike_img, anchor = 'sw')
    spikes.append(large_bottom_spike)

#Initializing Sprites - Projectiles
projectiles = []

projectile_img = make_projectile_sprite()
def make_projectile(side):
    y_position = 73
    if side == "bottom":
        y_position+= 200
    projectile = canvas.create_image(648, y_position, image=projectile_img, anchor = 'nw')
    projectiles.append(projectile)

long_head_img=make_long_projectile_head_sprite()
long_body_img=make_long_projectile_body_sprite()
long_tail_img=make_long_projectile_tail_sprite()
def make_large_projectile(side):
    y_position = 73
    if side == "bottom":
        y_position+= 200
    long_projectile_head = canvas.create_image(648,y_position, image=long_head_img, anchor = 'nw')
    long_projectile_body = canvas.create_image(648+40,y_position, image=long_body_img, anchor = 'nw')
    long_projectile_tail = canvas.create_image(648+90,y_position, image=long_tail_img, anchor = 'nw')
    projectiles.append(long_projectile_head)
    projectiles.append(long_projectile_body)
    projectiles.append(long_projectile_tail)

#Initializing Sprites - Spacer/Beat Lines
spacer_line_img = make_spacer_lines()
def draw_spacers():
    for x in range(1,8):
        canvas.create_image(x*WIDTH/8, 0, image=spacer_line_img, anchor = 'n')

#Initializing Sprites - Scoreboard
scoreboard_img = make_scoreboard()
def draw_scoreboard():
    canvas.create_image(WIDTH/2, HEIGHT/2, image=scoreboard_img, anchor = 'center')


#Movement Binding
def move_up(event):
    canvas.moveto(player, 40, 25)
def move_down(event):
    canvas.moveto(player, 40,225)
root.bind("<space>", move_up)
root.bind("<KeyRelease-space>", move_down)

#collisions
def update_score(score_change):
    global score
    score += score_change
    colors = ['black', 'orange', 'red', 'black']
    canvas.itemconfigure(score_count, text=f"Score: {score}", fill = colors[strikes])

def collision(a, b):
    ax1, ay1, ax2, ay2 = canvas.bbox(a)
    bx1, by1, bx2, by2 = canvas.bbox(b)
    return ax1<bx2 and ax2>bx1 and ay1<by2 and ay2>by1

def check_collisions():
    global strikes, projectiles, spikes
    for projectile in projectiles[:]:
        if collision(projectile,player):
            canvas.delete(projectile)
            update_score(1)
            if projectile in projectiles:
                projectiles.remove(projectile)
    for projectile in projectiles:
        ex1, ey1, ex2, ey2 = canvas.bbox(projectile)
        if ex2 <= 0:
            canvas.delete(projectile)
            if ex2-ex1 >= 50:
                strikes += 1
            update_score(-4)
            if projectile in projectiles:
                projectiles.remove(projectile)
    for spike in spikes[:]:
        if collision(spike,player):
            strikes += 1
            update_score(-4)
            canvas.delete(spike)
            if spike in spikes:
                spikes.remove(spike)
    for spike in spikes:
        sx1, sy1, sx2, sy2 = canvas.bbox(spike)
        if sx2 <= 0:
            update_score(1)
            canvas.delete(spike)
            if spike in spikes:
                spikes.remove(spike)

#projectile movement
def move_obstacles():
    for projectile in projectiles:
        canvas.move(projectile, displacement, 0)
    for spike in spikes:
        canvas.move(spike, displacement, 0)



previous_obstacle_num = -1
def make_obstacle():
    global previous_obstacle_num #This is NOT chatgpt, I was trying to figure out a way to do this 
    obstacle_list = [lambda:make_projectile("top"), #efficiently and found this out through google.
                     lambda:make_projectile("bottom"),
                     lambda:[make_projectile("top"), make_small_bottom_spike()],
                     lambda:[make_projectile("bottom"), make_small_top_spike()],
                     lambda:make_small_bottom_spike(),
                     lambda:make_small_top_spike(),
                     lambda:[make_projectile("top"), make_projectile("bottom")],
                     lambda:make_large_projectile("top"), #this and below are extruded (2 long)
                     lambda:make_large_projectile("bottom"),
                     lambda:make_large_bottom_spike(),
                     lambda:make_large_top_spike(),
                     lambda:[make_large_projectile("top"), make_large_bottom_spike()],
                     lambda:[make_large_projectile("bottom"), make_large_top_spike()],
                     lambda:[make_projectile("bottom"), make_large_projectile("top")],
                     lambda:[make_projectile("top"), make_large_projectile("bottom")]
                     ]
    if previous_obstacle_num >= 7:
        previous_obstacle_num = -1
        return
    obstacle_num = random.randint(0, 14)
    while previous_obstacle_num == obstacle_num:
        obstacle_num = random.randint(0, 14)
    obstacle = obstacle_list[obstacle_num]()
    previous_obstacle_num = obstacle_num

    

#Variables
strikes = 0
score = 0
timer = 0
heal_delay = 0
'''
BPM - Only change BPM and adjust displacement using commented out print statement until delay is an integer
      If you can't find a displacement that yields an integer delay and displacement, try a different bpm
'''
bpm = 150
#displacement = -4.5
delay = 24
bps = bpm/60
dps = bps*75
tps = 1000/delay
units_per_beat = dps/tps


print(units_per_beat)
'''
units_per_second = bpm/60*75
movements_per_second = units_per_second/abs(displacement)
delay = int(1000/movements_per_second)
spawn_delay = 60000/bpm
print(f"Delay: {1000/movements_per_second}\nDisplacement: {displacement}")
'''


#Game Loop
def game_loop():
    global timer, heal_delay, strikes, score_count
    timer += delay
    if timer > spawn_delay:
        timer -= spawn_delay
        make_obstacle()
        if strikes > 0:
            heal_delay += 1
            if heal_delay >= 20:
                heal_delay = 0 
                strikes -= 1
    move_obstacles()
    check_collisions()
    if strikes >= 3:
        reset()
        return
    root.after(delay, game_loop) #move 6 (150 = 100y/x) (150 = 100y/4) (y=6)

#start & reset game
def start():
    global player, score_count
    player = canvas.create_image(40,225, image=player_img, anchor = 'nw')
    draw_spacers()
    draw_scoreboard()
    score_count = canvas.create_text(300,200,text=f"score: 0", font=('Arial', 20), anchor = "center")
    game_loop()

def reset():
    global strikes, score
    canvas.delete("all")
    projectiles.clear()
    spikes.clear()
    strikes = 0
    if score > 1:
        print(f"Your score was: {score}")
    score = 0
    start()
def kill(event):
    global strikes
    strikes = 4
root.bind("r", kill)
reset()
root.mainloop()