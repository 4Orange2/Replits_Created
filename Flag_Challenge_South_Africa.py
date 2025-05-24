'''
Rectangles
Ovals
Lines
Polygons
Arcs

Text on canvas to label flag

The two flags that I chose were: 
Brazil - in a rectangular outline
South Africa - in a circular outline (and a rectangular outline)
-- maybe you could even convert circular to rectangular with the change of a simple constant
'''

#Initialize Tkinter with these
from tkinter import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=600, background="black")
screen.pack()

#
#
#Your code goes here
#

screen.create_rectangle(0, 500, 550, 0, fill = "forestgreen")
screen.create_polygon(550, 0, -10, 0, 250, 200, 550, 200,  fill = "tomato1", width = 10)
screen.create_polygon(550, 300, 550, 500, -10, 500, 250, 300, fill = "blue4", width = 10)
screen.create_polygon(-10, 100, -10, 400, 200, 250, fill = "black", outline = "goldenrod1", width = 10)
screen.create_line(-10, 500, 250, 300, 550, 300, fill = "white", width = 10)
screen.create_line(-10, 0, 250, 200, 550, 200,  fill = "white", width = 10)

'''
#Grid lines
#REMOVE THESE BEFORE SUBMITTING ANY ASSIGNMENTS
spacing = 50

for x in range(0, 800, spacing): 
    screen.create_line(x, 25, x, 600, fill="white")
    screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N, fill = "white")

for y in range(0, 600, spacing):
    screen.create_line(25, y, 800, y, fill="white")
    screen.create_text(5, y, text=str(y), font="Times 9", anchor = W, fill = "white")

'''

screen.update()
input()