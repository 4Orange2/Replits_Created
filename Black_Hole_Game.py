# This program will illustrate a mini, one-minute soccer game

from tkinter import *
from time import *
from random import *

# first step: get the collissions of the character with the maze to work.

canvas_width = 800
canvas_height = 600

myInterface = Tk()
screen = Canvas(myInterface,
                width=canvas_width,
                height=canvas_height,
                background="sky blue")
screen.pack()




def animation(starting_coord_array, end_coord_array, fill_shape, x_change, shape, vertical_direction="down", horizontal_direction="left"):
  if_horizontal = 1
  if (starting_coord_array[0] - (end_coord_array[0])) == 0:
    if vertical_direction == "down":
      slope = 1
    else:
      slope = -1
    if_horizontal = 0
  elif (end_coord_array[1] - starting_coord_array[1]) == 0:
    slope = 0
  else:
    slope = abs(end_coord_array[1] - starting_coord_array[1])/abs(end_coord_array[0] - starting_coord_array[0])
    slope = -slope
    if vertical_direction == "down":
      slope = abs(slope)
    if horizontal_direction == "left":
      if_horizontal = -1
  if shape == "oval":
    object = screen.create_oval(starting_coord_array[0] + x_change*if_horizontal, starting_coord_array[1] + x_change*slope, starting_coord_array[2] + x_change*if_horizontal, starting_coord_array[3] + x_change*slope, fill=fill_shape)
  elif shape == "rectangle":
    object = screen.create_rectangle(starting_coord_array[0] + x_change*if_horizontal, starting_coord_array[1] + x_change*slope, starting_coord_array[2] + x_change*if_horizontal, starting_coord_array[3] + x_change*slope, fill=fill_shape)
  return object


wall = screen.create_rectangle(100, 100, 200, 200, fill="red")

character_start = [230, 230, 280, 280]

character_end = [180,180,230,230]

change = 0

for f in range(60):
  fox = animation(character_start, character_end, "yellow", change, shape="oval", vertical_direction="up", horizontal_direction="left")
  screen.update()
  sleep(0.02)
  change += 1
  if f == 0:
    sleep(1)
    screen.delete(fox)
  elif f == 59:
    pass
  else:
    screen.delete(fox)


'''
Previous code for the black hole game:

start_increment = 20
diameter = 55

for row in range(1,7):
  if row == 0:
    screen.create_oval(canvas_width/2 - 30 - diameter/2, start_increment, canvas_width/2 + diameter/2 - 30, start_increment + diameter, width=2, outline="red")
  else:
    step = 2
    for circle in range(-row, row, step):
      screen.create_oval(canvas_width/2 - 30 - (diameter/2) - diameter*(circle) -10*(circle), start_increment + diameter*(row) + 10* (row), canvas_width/2 - 30 + diameter/2 - diameter*(circle) - 10*(circle), start_increment + diameter*(row+1) + 10*(row), width=2, outline="red")

global xe
xe = 20
global ye
ye = 20

def getextentx(eventextentx):
  global xe
  xe =  eventextentx.x

def getextenty(eventextenty):
  global ye
  ye = eventextenty.y


while True:
  if xnew != xe:
    print(f"{xe}, {ye}")
    xe=xnew
  screen.bind("<Button 1>", getextentx)
  screen.bind("<Button 1>", getextenty)
'''
input()
  