#Imports
import tkinter as tk
import random

#Dimensions
WIDTH = 600
HEIGHT = 400

#Sprites created - temporarily boxes. Change later

# - Player
def make_player_sprite():
    pattern = [
        "11111111111",
        "11111111111",
        "11111111111",
        "11111111111",
        "11111111111",
        "11111111111",
        "11111111111",
        "11111111111"]
    scale = 2
    h = len(pattern)*scale
    w = len(pattern[0])*scale
    img = tk.PhotoImage(width=w, height=h)
    color = "black"
    for y in range(h):
        for x in range(w):
            if pattern[y//scale][x//scale] == "1":
                img.put(color, (x,y))
    return img

# - top spike
def make_spike_sprite():
    pattern = [
        "11111111111",
        "01111111110",
        "00111111100",
        "00011111000",
        "00001110000",
        "00000100000",
        "00000000000",
        "00000000000",
        "00000000000",
        "00000000000"]
    scale = 5
    h = len(pattern)*scale
    w = len(pattern[0])*scale
    img = tk.PhotoImage(width=w, height=h)
    color = "black"
    for y in range(h):
        for x in range(w):
            if pattern[y//scale][x//scale] == "1":
                img.put(color, (x,y))
    return img
# - top long spike (merge top/bottom if able to flip)
# - bottom spike
# - bottom long spike
# - short projectile
# - long projectile (group)
# - extruded projectiles (same as short)
# - extruded + extruded-long projectile (same sprite as short + long)




#initialize stuff
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