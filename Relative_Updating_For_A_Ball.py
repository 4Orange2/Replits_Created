from tkinter import *
from time import *
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=600, background = "black" )
screen.pack()

for f in range(100):    #100 frames.  f = 0, 1, 2, …, 99

  x1 = 5*f + 70
  
  ball = screen.create_oval( x1, 400, x1 + 20, 420, fill="yellow" )   #Creates the object in its current position

  screen.update()	#Draws all objects on the screen
  sleep(.03)	            #Pauses for a short time
  screen.delete( ball )          #Erases the object before the next frame begins

  x1 = x1 + 5  	#Increment statement updates the object's position before the next frame
  
input()