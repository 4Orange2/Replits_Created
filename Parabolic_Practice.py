import math
'''
Write a Python program that animates a ball flying right to left across the screen in a parabolic arc. 

It should have:
a starting position of (700, 350)
a starting upward speed of -16 pixels per frame
a horizontal speed of -9 pixels per frame
gravity strength of 0.5 pixels per frame squared (it's accerlerating by 0.5 pixels every frame)
a diameter of 50 pixels


s(t) = −½ gx2 + v0x + h0


# gravity equation is in form of quadratic

change_in_x = -9
change_in_y = -16

for i in range(6):
  screen

# for determining the bounce, I read this link on the bounce of a ball:
https://scienceonline.tki.org.nz/Nature-of-science/Nature-of-science-teaching-activities/Predicting-the-behaviour-of-a-bouncing-ball

# the bouncing of balls has very interesting physics behind it: I used the following link from MIT Open Courseware to figure out the math that I need to use:

# I ended up with the equation: m(sqrt(2*g*h))
'''

from tkinter import *
from time import *

myInterface = Tk()
screen = Canvas(myInterface, width=800, height=550, background="sky blue")
screen.pack()

r = 25

initial_y = 300

initial_x = 700

height_after_bounce = 150

ball_mass = int(
    input(
        "what is the mass of the ball (the mass cannot be zero because that doesn't correlate with the laws of physics) I don't really need this to make the ball bounce, I only need this so that the normal force calculation can be done: "
    ))

bounciness = int(input("What is the bounciness of the ball on a scale of 0 to 10?"))

y_coordinate_to_bounce_up_from = 480
# you can change this value; depending on the screen that the utput is displayed on, the frame could be too small or too big for the screen and so the ball will bounce earlier or later than expected (respectively)


limit_for_frame = 100

for f in range(0, 200):
  #Linear motion to the right with constant speed
  # f stands for frame
  if f > 42 and f < limit_for_frame:
    x = -9 * f + 700
    y = -16*(bounciness/20 + 1) *(f-43) + 0.5 * (f-43)**2 + y_coordinate_to_bounce_up_from # I just kind of eyeballed
    print(f"y after bounce: {-20*(f-43) + 0.5 * (f-43)**2 + y_coordinate_to_bounce_up_from}, frame {f}")
    if f == 44:
      force_exerted = (ball_mass * ((math.sqrt(2 * ((.5) *
+(f)**2) * y)) + math.sqrt(2 * .5 *(f)**2 * 300))) / 1 + ball_mass * 0.5**2
      print("\n")
      print(f"I learned by doing this project, that when a ball bounces off the ground, the ground exerts a force (called normal force) on the object that is opposite to and greater than the force of gravity, and the velocity of the ball upon impact.")
      print("\n")
      print(f"Normal force = m(velocity_after + velocity_before) + mg")
      print("\n")
      print("i.e. in order for the change in direction that has happened to occur, the normal force has to provide an acceleration that can overcome the force of gravity in addition to the acceleration that can allow for that change in velocity.")
      print(f"This occurs over an instantaneous amount of time. I'm not really familiar with the concept of derivatives yet. ")
      print("\n")
      print(f"normal force {force_exerted}")
    yellowBall = screen.create_oval(x - r, y - r, x +r, y + r, fill="yellow")
  #elif f > 44:
  #  x = -9 * f + 700
  #  y = 35 * f - (0.5 * (f+2)**2)
  else:
    if f == 19:  # because we don't want the ball to overshoot
      f = 19.28
    x = -9 * f + initial_x  #Linear equation for X values
    y = .5 * f**2 - 16 * f + initial_y  #Parabolic equation for Y value
    # what is the downward velocity of the ball?
    # .5*f**2 - 16*f + 300
    # new equation for y: .5*f**2 -
    yellowBall = screen.create_oval(x - r, y - r, x + r, y + r, fill="yellow")
  screen.update()
  sleep(.03)
  screen.delete(yellowBall)
  #if (y+25) <= 600:

  #no delete so we can see the trail of the balls' movement

input()
