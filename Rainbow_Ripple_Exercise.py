from tkinter import *
from time import *
tk = Tk()
screen = Canvas(tk, width=800, height=600, background="grey10")
screen.pack()

ringColours = ["red", "yellow", "dark orange", "green", "blue", "purple"]

#How far to the right a ring is allowed to expand before it stops and the next ring begins
xRightWall = 600      


#Repeats the animation 20 times, once for each of the 20 rings
for i in range(20):

  #Resets the starting position of the next ring to the centre of the screen
  x1 = 400  #upper left corner of the ring
  y1 = 300

  x2 = 400  #lower right corner of the ring
  y2 = 300
    

  #Animates the next ring until its right edge (x2) reaches the current limit (xRightWall)
  while x2 < xRightWall:
  
    ring = screen.create_rectangle(x1, y1, x2, y2, outline = ringColours[i % 6], width=3 )

    #Makes the upper-left and lower-right corners of the ring expand outwards by a small amount before the next frame
    x1 = x1 - 5
    y1 = y1 - 5

    x2 = x2 + 5
    y2 = y2 + 5

    screen.update()
    sleep(0.03)

    #Avoid deleting the ring on the final frame of animation.
    if x2 < xRightWall:  
      screen.delete(ring)

  #Reduces xRightWall so that the next ring will stop sooner than the current one
  xRightWall = x2 - 10
