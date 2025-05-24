from tkinter import *
from time import *
tk = Tk()
screen = Canvas(tk, width=800, height=600, background="yellow")
screen.pack()

#INITIAL VALUES
diameter = 100
eye_diameter = 20


#Ball anchor points
x1 = 100
y1 = 400

xSpeed = 11
ySpeed = -2

#ANIMATION LOOP
while True: 
  face = screen.create_oval(x1,  y1,  x1 + diameter,  y1 + diameter,  fill="green") 
  eye1 = screen.create_oval(x1 + 10,  y1 + 30, x1 + 30,  y1 + 50,  fill="red")
  eye2 = screen.create_oval(x1 + diameter - 10,  y1 + 30,  x1 + diameter - 30,  y1 + + 50,  fill="red")
  mouth = screen.create_oval(x1 + 20, y1 + diameter - 25, x1 + diameter - 20, y1 + diameter - 35, fill = "red")     
  

  #Update, sleep, delete
  screen.update()
  sleep(0.03)
  screen.delete(face, eye1, eye2, mouth)

  #Update positions before the next frame
  x1 = x1 + xSpeed
  y1 = y1 + ySpeed

  if x1+diameter > 800:
    xSpeed = -1 * xSpeed

  elif x1 + diameter < 0:
    xSpeed = -1 * xSpeed

  if y1 + diameter > 800:
    ySpeed = -1 * ySpeed
  
  elif y1 + diameter < 0:
    ySpeed = -1 * ySpeed
    