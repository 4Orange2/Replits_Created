# This program will illustrate a mini, one-minute soccer game

from tkinter import *
from time import *
from random import *

canvas_width = 800
canvas_height = 600

myInterface = Tk()
screen = Canvas(myInterface,
                width=canvas_width,
                height=canvas_height,
                background="sky blue")
screen.pack()

start_increment = 20
diameter = 55

for row in range(1,7):
  if row == 0:
    screen.create_oval(canvas_width/2 - 30 - diameter/2, start_increment, canvas_width/2 + diameter/2 - 30, start_increment + diameter, width=2, outline="red")
  else:
    step = 2
    for circle in range(-row, row, step):
      screen.create_oval(canvas_width/2 - 30 - (diameter/2) - diameter*(circle) -10*(circle), start_increment + diameter*(row) + 10* (row), canvas_width/2 - 30 + diameter/2 - diameter*(circle) - 10*(circle), start_increment + diameter*(row+1) + 10*(row), width=2, outline="red")

input()