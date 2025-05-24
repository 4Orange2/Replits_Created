from tkinter import *
from time import *
from math import *

tk = Tk()
screen = Canvas(tk, width=800, height=600,background="skyblue")
screen.pack()

redBall=0
greenBall=0
circleBall=0
line1=0
line2=0


for f in range(5000):
  #Red ball oscillates up and down via sin(f)   
  redx1 = 100
  redy1 = 100*sin( 0.05*f ) + 200
  redx2 = redx1 + 20
  redy2 = redy1 + 20
  redBall = screen.create_oval(redx1, redy1, redx2, redy2, fill="red")

  #Green ball oscillates left and right via cos(f)
  greenx1 = 100*cos( 0.05*f ) + 200
  greeny1 = 100
  greenx2 = greenx1 + 20    
  greeny2 = greeny1 + 20
  greenBall = screen.create_oval(greenx1, greeny1, greenx2, greeny2, fill="green")

  #Lines to help demonstrate white ball's position
  line1 = screen.create_line(redx1+10, redy1+10, greenx1+10, redy1+10, fill="yellow", width=4)
  line2 = screen.create_line(greenx1+10, greeny1+10, greenx1+10, redy1+10, fill="yellow", width=4)

  #White ball combines x movement of green ball and y movement of red ball
  if iteration %2 == 1:
    whiteBall = screen.create_oval(greenx1, redy1, greenx2, redy2, fill="white") # used a combination of sin() and cos()
  elif iteration %2 == 

  screen.update()
  sleep(0.03)
  screen.delete( greenBall, redBall, line1, line2)

#What happens if you change the frequency of one of the periodic functions?
#Try replacing the 0.05 in greenx1 to 0.025, or some other value!
