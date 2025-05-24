from tkinter import *
from time import *
from random import *

myInterface = Tk()
screen = Canvas(myInterface, width=550, height=550, background="sky blue")
screen.pack()

width = 500
height = width
# because we want to create a square shape

# find the top-right coordinate of the given grid segment
circle_diameter = 2 
for row in range(0,8): 
  for column in range(0,8):
    for i in range(1,200):
      x = randint(int(width/8*(row)), int(width/8*(row+1)))
      y = randint(int(height/8*(column)), int(height/8*(column+1)))
      if row % 2 == 1:
        if column%2 == 1:
          color = "green"
        else:
          color = "red"
      if row%2 == 0:
        if column%2 == 0:
            color = "green"
        else:
          color = "red"
      screen.create_oval(x-circle_diameter +25,y -circle_diameter + 25,x+circle_diameter + 25, y+circle_diameter + 25,fill=color)
      screen.update()

input()