# .5 * f**2 - 16 * f + initial_y

# I'm going to write all of my numbers in relation to canvas_width and canvas_height

from tkinter import *
from time import *
from random import *


canvas_width = 780
canvas_height = 600

myInterface = Tk()
screen = Canvas(myInterface, width=canvas_width, height=canvas_height, background="sky blue")
screen.pack()


# basketball net

b_const_x = 12
b_const_y = 2

stick_const_x = 2
stick_const_y = 3


body = screen.create_line(canvas_width*((stick_const_x + 0.5)/16), canvas_height*((stick_const_y*8 + 1)/32), canvas_width*((stick_const_x + 0.5)/16), canvas_height*((stick_const_y*8 + 6)/32), width = 20, fill="red")

face = screen.create_oval(canvas_width*(stick_const_x/16), canvas_height*((stick_const_y*8)/32), canvas_width*((stick_const_x + 1)/16), canvas_height*((stick_const_y*8 + 2.5)/32), fill="yellow")

print(body)
print(face)
input()
