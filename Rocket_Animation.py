from tkinter import *
from time import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=600, background="black")
screen.pack()

#SET INITIAL VARIABLES
xRocket = 50            #Rocket's x anchor point
yRocket = 50            #Rocket's y anchor point


xSpeed = 10


#RUNS THE ANIMATION FOR 800 FRAMES
for f in range(800):
  body = screen.create_rectangle( xRocket, yRocket, xRocket + 100, yRocket + 40, fill= "yellow")
  nose = screen.create_polygon( xRocket + 100, yRocket,  xRocket + 100, yRocket + 40, xRocket + 150, yRocket + 20,  fill="red")
  window = screen.create_oval(xRocket+10, yRocket + 10, xRocket + 90, yRocket + 35, fill= "blue")
  
  screen.update() # Python shows you what its made before it deletes it
  #We sleep for .03 seconds before the next frame.
  #How many frames per second will we have? 
  sleep(.03)
  screen.delete(body, nose, window)

  #Update the rocket's x anchor point to increase by 3 pixels for the next frame
  xRocket = xRocket + xSpeed
input()