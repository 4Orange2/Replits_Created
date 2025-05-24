from tkinter import *
from random import *
from time import *

root = Tk()
screen = Canvas( root, width=800, height=600, background = "black" )
screen.pack()

colors = [ "green", "yellow", "red" ]
lightHeights = [ 400, 275, 150 ]

diameter = 100
xLights1 = 450
xLights2 = xLights1 + diameter

xPlane = 100

#TRAFFIC LIGHT BOX
lamp = screen.create_rectangle(400, 100, 600, 550, fill = "orange")

#BLACK DISKS
for diskNum in range(0,3):

    yLights1 = lightHeights[ diskNum ]
    yLights2 = yLights1 + diameter

    screen.create_oval( xLights1, yLights1, xLights2, yLights2, fill ="black")
    screen.update()

#ANIMATION. WHY IS THE AIRPLANE NOT SMOOTH?
lightIndex = 0
for i in range(200):
  if lightIndex % 3 == 1:
    xPlane = xPlane + 10
  elif lightIndex % 3 == 2:
    xPlane += 5
  elif lightIndex % 3 == 0:
    pass
  airplane = screen.create_rectangle( xPlane, 100, xPlane + 30, 115, fill = "white")
  if i % 20 == 0:
    col = colors[lightIndex % 3]
    yPos = lightHeights[lightIndex % 3]
    lightIndex += 1

  light = screen.create_oval(xLights1, yPos, xLights2, yPos+diameter, fill = col)

  screen.update()
  sleep(0.1)
  screen.delete(airplane, light)