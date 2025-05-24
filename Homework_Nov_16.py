# Triangle Drawer
from tkinter import *
tk = Tk()
screen = Canvas(tk, width=800, height=600, background="grey10")
screen.pack()

# This program currently takes user inputs to draw a triangle

# 1. Modify the program by replacing these inputs with a 

#"create_triangle" procedure that has triX, triY, and col as parameters

def create_triangle(triX, triY, col):
  screen.create_polygon(triX, triY - 34.6410161514/2, triX-20, triY+34.6410161514/2, triX+20, triY+34.6410161514/2, fill=col)


create_triangle(100,150,"green")
create_triangle(150,100,"yellow") 
create_triangle(200,150, "blue")



input()