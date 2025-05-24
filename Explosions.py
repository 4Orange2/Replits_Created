from tkinter import *
from random import *
from time import *
from math import *
screen = Canvas(Tk(), height = 600, width = 800, background = "skyblue")
screen.pack()


def drawSquare( xC, yC, width, col ):
  # this is a procedure
  screen.create_rectangle(xC + width, yC + width, xC - width, yC - width, fill=col)


def makeExplosion( xC, yC, col ):
  numPieces = 150

  #SET UP THE EMPTY ARRAYS
  r = []
  angles = []

  speeds = []
  sizes = []
  debrisDrawings = []

  #FILL THE ARRAYS WITH RANDOM VALUES
  for i in range( numPieces ):    
    r.append( randint(0, 50) )
    angles.append( uniform( 0, 2*pi) )

    sizes.append( randint(2, 5) )
    speeds.append( uniform(3, 10) )
    debrisDrawings.append(0)

  #MAKE A SHORT FLASH
  flash = screen.create_polygon(xC-30,yC-35, xC-10, yC-35, xC+20,yC-45, xC+30,yC-40, xC+35,yC-15, xC+25,yC, xC+20,yC+40, xC,yC+20, xC-35,yC+35, xC-35,yC+8, xC-55,yC+10, xC-40,yC-15, fill="white")
  screen.update()
  sleep(0.06)
  screen.delete(flash)

  #ANIMATE THE EXPLOSION
  for f in range( 40 ): #f = 0 , 1, 2, 3, ...   37, 38, 39 
    for i in range( numPieces ):        
      x = xC + r[i]*cos( angles[i] )
      y = yC  - r[i]*sin( angles[i] )
      
      debrisDrawings[i] = drawSquare( x, y, sizes[i], col )
      r[i] = r[i] + speeds[i]
    screen.update()
  #sleep(0.001)

'''
Write a for-loop that uses the makeExplosion() procedure to create 10 explosions.
 The first explosion should be centered at (400, 100), and each new one centered 50 pixels below the previous.
Create an array of colours and randomly select from it to colour each new explosion.
There should be no trail from the explosion particles i.e. you need to make sure the squares are getting properly deleted.
'''

colList = ["green", "yellow", "purple", "black", "skyblue", "blue", "pink", "orange", "yellow", "brown"]

for i in range(0,9):
  makeExplosion(400, 100 + i*50, colList[i])
  screen.create_rectangle(0,0,800,600, fill="skyblue")
#Write a for-loop that makes 10 explosions in a row, starting at the top and moving
#gradually down the screen.  Make it choose a random colour each time, using an array of
#colours that you specify at the top of the program.
