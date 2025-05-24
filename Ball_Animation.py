from tkinter import *
from time import *
tk = Tk()
screen = Canvas(tk, width=800, height=600, background="yellow")
screen.pack()

#INITIAL VALUES
diameter = 100

#Ball anchor points
x1 = 100
y1 = 400

xSpeed = 11
ySpeed = -2

#ANIMATION LOOP
for f in range(800): 
  ball = screen.create_oval(  x1,  y1,  x1 + diameter,  y1 + diameter,  fill="red") 

  #Update, sleep, delete
  screen.update()
  sleep(0.03)
  screen.delete( ball )

  #Update positions before the next frame
  x1 = x1 + xSpeed
  y1 = y1 + ySpeed

  if x1+diameter > 800: # This is where you change speed
    xSpeed = -1 * xSpeed

  #Add more if-statements that make the ball bounce off all 4 walls

input()