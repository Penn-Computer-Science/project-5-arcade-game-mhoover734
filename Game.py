#Imports
import tkinter as tk
import random

#Dimensions
WIDTH = 600
HEIGHT = 400

#Sprites created

# - Player 
'''WIP'''
def make_player_sprite():
    h = 150
    w = 75
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
    w = 13*scale
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

player_img=make_long_projectile_head_sprite()
player_img1=make_long_projectile_body_sprite()
player_img2=make_long_projectile_tail_sprite()
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

player = canvas.create_image(228,73, image=player_img)
player1 = canvas.create_image(280,73, image=player_img1)
player2 = canvas.create_image(333,73, image=player_img2)
root.mainloop()