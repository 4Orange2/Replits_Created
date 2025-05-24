from tkinter import *
from random import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=600, background="skyblue")
screen.pack()

#CAN YOU MAKE IT LOOK LIKE IT'S SNOWING OUTSIDE?
wall = screen.create_rectangle(0, 0, 800, 600, fill="blanched almond")
floor = screen.create_rectangle(0, 500, 800, 600, fill="chocolate4")
window = screen.create_rectangle(400, 150, 650, 300, fill="skyblue", outline="sienna2", width=9)

for snowflake in range(10):
  x = randint(406, 644) 
  y = randint(156, 294) # 300 - 4 - 2, # 150 + 4 + 2, because we want the snowball to be two pixels away
  screen.create_oval(x, y, x+4, y+4, fill="white")


input()