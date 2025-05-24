from tkinter import *
from random import *
tk = Tk()
screen = Canvas(tk, width=800, height=600, background="black")
screen.pack()

def drawSandBox(fill_col, grain_col, border_col, top_left_x, top_left_y, bottom_right_x, bottom_right_y, grain_amount):
  screen.create_rectangle(top_left_x, top_left_y, bottom_right_x, bottom_right_y, fill=fill_col, outline=border_col)
  for i in range(grain_amount):
    grain_x = randint(top_left_x, bottom_right_x)
    grain_y = randint(top_left_y, bottom_right_y)
    screen.create_oval(grain_x, grain_y, grain_x + 2, grain_y + 2, fill=grain_col)

drawSandBox( "orange", "grey", "red", 200, 100, 530, 430, 2000)
drawSandBox( "yellow", "black", "green", 225, 500, 700, 700, 50)
input()