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
player = canvas.create_image(0,225, image=player_img, anchor = 'nw')


def make_small_top_spike():
    small_top_spike_img = make_top_spike_sprite()
    small_top_spike = canvas.create_image(670, 0, image=small_top_spike_img, anchor = 'nw')
make_small_top_spike()

def make_large_top_spike():
    large_top_spike_img = make_top_long_spike_sprite()
    large_top_spike = canvas.create_image(670, 0, image=large_top_spike_img, anchor = 'nw')
make_large_top_spike()

def make_small_bottom_spike():
    small_bottom_spike_img = make_bottom_spike_sprite()
    small_bottom_spike = canvas.create_image(670, HEIGHT, image=small_bottom_spike_img, anchor = 'sw')
make_small_bottom_spike()

def make_large_bottom_spike():
    large_bottom_spike_img = make_bottom_long_spike_sprite()
    large_bottom_spike = canvas.create_image(670, HEIGHT, image=large_bottom_spike_img, anchor = 'sw')
make_large_bottom_spike()

projectiles = []

def make_projectile(side):
    projectile_img = make_projectile_sprite()
    y_position = 73
    if side == "bottom":
        y_position+= 200
    projectile = canvas.create_image(648, y_position, image=projectile_img, anchor = 'nw')
    projectiles.append(projectile)
make_projectile("top")
make_projectile("bottom")

def make_large_projectile(side):
    long_head_img=make_long_projectile_head_sprite()
    long_body_img=make_long_projectile_body_sprite()
    long_tail_img=make_long_projectile_tail_sprite()
    y_position = 73
    if side == "bottom":
        y_position+= 200
    long_projectile_head = canvas.create_image(648,y_position, image=long_head_img, anchor = 'nw')
    long_projectile_body = canvas.create_image(648+40,y_position, image=long_body_img, anchor = 'nw')
    long_projectile_tail = canvas.create_image(648+90,y_position, image=long_tail_img, anchor = 'nw')
    projectiles.append(long_projectile_head)
    projectiles.append(long_projectile_body)
    projectiles.append(long_projectile_tail)
make_large_projectile("top")
make_large_projectile("bottom")

print(projectiles)

spacer_line_img = make_spacer_lines()
for x in range(1,8):
    spacer_line = canvas.create_image(x*WIDTH/8, 0, image=spacer_line_img, anchor = 'n')

#function to make small spike - with input of top/bottom
#function to make long spike - with input of top/bottom
#function to make small proj -  with input of top/bottom
#function to make long proj - with input of top/bottom
#funtion to make extruded projs
#function to make extruded + extruded-long proj -  with input of top/bottom (input is long)

#jump function
#bind ts - might have to do it differently than usual

#collisions

#score here??? could move

#projectile movement

#game loop

#start & reset game

root.mainloop()