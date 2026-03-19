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
#Player - WIP, never finished a sprite for player unfortunately
def make_player_sprite():
    h = 150
    w = 10
    img = tk.PhotoImage(width=w, height=h)
    color1 = "blue"
    for y in range(h):
        for x in range(w):
            img.put(color1, (x,y))
    return img
#Top spike
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
#Top long spike
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
#Bottom spike
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
#Bottom long spike
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
#Short projectile
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
#Long projectile (group)
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

#Initialize Stuff
root = tk.Tk()
root.title("Bad \"Rhythm\" Game")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

    #Initializing Sprites
#Player
player_img=make_player_sprite()
#Spikes
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
#Projectiles
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
#Spacer/Beat Lines
spacer_line_img = make_spacer_lines()
def draw_spacers():
    for x in range(1,8):
        canvas.create_image(x*WIDTH/8, 0, image=spacer_line_img, anchor = 'n')
#Scoreboard
scoreboard_img = make_scoreboard()
def draw_scoreboard():
    canvas.create_image(WIDTH/2, HEIGHT/2, image=scoreboard_img, anchor = 'center')

#Movement Binding
def move_up(event):
    canvas.moveto(player, 40, 25)
def move_down(event):
    canvas.moveto(player, 40,225)

''' Comment out unused controls - Given configurations: Space, E/F, J/N, J/F '''
root.bind("<space>", move_up)
root.bind("<KeyRelease-space>", move_down)
root.bind("e", move_up)
root.bind("j", move_up)
root.bind("f", move_down)
root.bind("n", move_down)

#Collisions
def update_score(score_change):
    global score #Updates score given input & updates scoreboard given strikes & score
    score += score_change
    colors = ['black', 'orange', 'red', 'black'] #index corresponds to # of strikes
    canvas.itemconfigure(score_count, text=f"Score: {score}", fill = colors[strikes])
def collision(a, b):
    ax1, ay1, ax2, ay2 = canvas.bbox(a) #Used for player collision only since
    bx1, by1, bx2, by2 = canvas.bbox(b) #missing checks for if it's offscreen
    return ax1<bx2 and ax2>bx1 and ay1<by2 and ay2>by1
def check_collisions():
    global strikes, projectiles, spikes
    for projectile in projectiles[:]:
        if collision(projectile,player):
            canvas.delete(projectile)
            update_score(1) #If a projectile is hit, +1 point
            if projectile in projectiles: #(Large gives 3)
                projectiles.remove(projectile)
    for projectile in projectiles:
        ex1, ey1, ex2, ey2 = canvas.bbox(projectile)
        if ex2 <= 0:
            canvas.delete(projectile)
            if ex2-ex1 >= 50:
                strikes += 1
            update_score(-4) #If a projectile is missed, -4 points
            if projectile in projectiles:
                projectiles.remove(projectile)
    for spike in spikes[:]:
        if collision(spike,player):
            strikes += 1
            update_score(-4) #If a spike is hit, -4 points
            canvas.delete(spike)
            if spike in spikes:
                spikes.remove(spike)
    for spike in spikes:
        sx1, sy1, sx2, sy2 = canvas.bbox(spike)
        if sx2 <= 0:
            update_score(1) #If a spike is dodged, +1 points
            canvas.delete(spike)
            if spike in spikes:
                spikes.remove(spike)

#Projectile Movement
def move_obstacles(): 
    for projectile in projectiles:
        canvas.move(projectile, displacement, 0)
    for spike in spikes: #Moves everything by [displacement] every [delay] ms
        canvas.move(spike, displacement, 0)

#Making Random Projectiles
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
    if previous_obstacle_num >= 7: #Makes the extruded wait a turn before spawning another
        previous_obstacle_num = -1 #Has the side effect of making them possible to repeat
        return
    obstacle_num = random.randint(0, 14)
    while previous_obstacle_num == obstacle_num: #Scrambles it until its not a repeat
        obstacle_num = random.randint(0, 14)
    obstacle = obstacle_list[obstacle_num]()
    previous_obstacle_num = obstacle_num
    #For testing bpm, comment out everything in function above and uncomment below
    #make_projectile("bottom")

#Variables
strikes = 0 #How many strikes (out of 3) you have
score = 0 #Game score (check collisions for values)
timer = 0 #Timer for spawning enemies every ___
heal_delay = 0 #Timer for delaying healing

''' BPM Input - Can be anything '''
bpm_input = 120 #I recommend 300 (:
#Unfortunately, due to lag, you can't put a song or metronome to this

#Calculations
#DO NOT CHANGE ANYTHING BELOW
bpm = bpm_input*1.28 #Adjusts for lag (usually ~78% slower)
delay = 24
bps = bpm/60 #Beats per second
ups = bps*75 #Units per second
tps = 1000/delay #Ticks per second (updates)
#Results of calculations
displacement = -ups/tps #Negative because everything moves left (= Units per tick)
spawn_delay = 60000/bpm

#Game Loop
def game_loop():
    global timer, heal_delay, strikes, score_count
    timer += delay
    if timer > spawn_delay: #spawn delay - every beat spawn enemy
        timer -= spawn_delay
        make_obstacle()
        if strikes > 0:
            heal_delay += 1 #every x beats heal 1 strike
            if heal_delay >= 30:
                heal_delay = 0 
                strikes -= 1
                update_score(0) #update the scoreboard to display heal
    move_obstacles() #move all obstacles
    check_collisions() #check out new collisions
    if strikes >= 3: #check for game over (3 strikes)
        reset()
        return
    root.after(delay, game_loop) #every [delay], run game_loop (24ms default)

#Start & reset game
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
    if score > 1: #If you have a score when game ends, put the score in terminal
        print(f"\nYour score was: {score}\n")
    score = 0
    start()
def kill(event):
    global strikes
    strikes = 4
root.bind("`", kill) #Bind key to resetting the game (just gives u 4 strikes)
reset()
root.mainloop()