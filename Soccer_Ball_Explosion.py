# This program will illustrate a mini, one-minute soccer game

from tkinter import *
from time import *
from random import *
from playsound import playsound

canvas_width = 591
canvas_height = 418

myInterface = Tk()
screen = Canvas(myInterface,
                width=canvas_width,
                height=canvas_height,
                background="sky blue")
screen.pack()

img= PhotoImage(file='Soccer-field-birds-eye-view-horizontal.png')
screen.create_image(0,0,anchor=NW,image=img) # image of the soccer field

# Players on the blue team in 433 formation

x_start = canvas_width/118.2
y_start = canvas_height/7.88679245283
y_dividend_const = canvas_height/1.38
x_increment = (canvas_width/1.182)/4
y_increment = y_dividend_const/5
size = 15
ball_diameter = 5

# when you put these two variables together in the form {x_start, y_start}, you get the coordinates for the top-left corner of the soccer pitch



# something to note: whenever you have a given amnt_of_players_in_row, you divide te canvas_width by (amnt_of_players_in_row + 1)

colList = ["blue", "red"]
goal_line = [x_start, canvas_width-x_start - canvas_width/49.25]
# the two x goalline coordinates

# we want the arrangement of players in the 433 

# blue team code:
'''
x_coord_back_line = x_start+x_increment
'''
# for the back line
'''
for y_coord in y_back_line:
  screen.create_oval(x_coord_back_line, y_coord, x_coord_back_line + size, y_coord + size, fill = "blue")
'''

# for the other two lines

for team in range(2):
  # 0 is blue
  # 1 is read

  y_increment = y_dividend_const/5
  for y_multiplier in range(1,5):
    if team == 0:
      screen.create_oval(goal_line[team]+x_increment, y_start+y_increment*y_multiplier, goal_line[team]+x_increment + size, y_start+y_increment*y_multiplier + size, fill = colList[team])
    elif team == 1:
      screen.create_oval(goal_line[team]-x_increment, y_start+y_increment*y_multiplier, goal_line[team]-x_increment + size, y_start+y_increment*y_multiplier + size, fill = colList[team])

  y_increment = y_dividend_const/10
  for x_multiplier in range(2,4):
    if team == 0:
      screen.create_oval(goal_line[team]+x_increment*x_multiplier, y_start+y_increment*3, x_start+x_increment*x_multiplier + size, y_start+y_increment*3 + size, fill = colList[team])
      screen.create_oval(x_start+x_increment*x_multiplier, y_start+y_increment*5, x_start+x_increment*x_multiplier + size, y_start+y_increment*5 + size, fill = colList[team])
      screen.create_oval(x_start+x_increment*x_multiplier, y_start+y_increment*7,x_start+x_increment*x_multiplier + size,y_start+y_increment*7 + size, fill = colList[team])
    elif team == 1:
      screen.create_oval(goal_line[team]-x_increment*x_multiplier, y_start+y_increment*3, goal_line[team]-x_increment*x_multiplier + size, y_start+y_increment*3 + size, fill = colList[team])
      screen.create_oval(goal_line[team]-x_increment*x_multiplier, y_start+y_increment*5, goal_line[team]-x_increment*x_multiplier + size, y_start+y_increment*5 + size, fill = colList[team])
      screen.create_oval(goal_line[team]-x_increment*x_multiplier, y_start+y_increment*7,goal_line[team]-x_increment*x_multiplier + size,y_start+y_increment*7 + size, fill = colList[team])

ball = screen.create_oval(canvas_width/7-ball_diameter,canvas_height/2-ball_diameter,canvas_width/7+ball_diameter,canvas_height/2+ball_diameter, fill="yellow")


#Animation loop

# plan: I'm going to create an animation list that contains instructions for how to modify each player on the field
# there's going to be multiple animation lists for each type of goal scored
# goal #1: the centre-back dribbles through the whole team in an organic emotion
# goal #2: the left-back dribbles thourgh all

left_back_opening = [goal_line[0]+x_increment*1, y_start+y_increment*0, goal_line[0]+x_increment*1 + size, y_start+y_increment*0 + size]

right_back_opening = [goal_line[0]+x_increment*1, y_start+y_increment*10, goal_line[0]+x_increment*1 + size, y_start+y_increment*10 + size]
'''
screen.create_oval(left_back_opening_up[0], left_back_opening_up[1], left_back_opening_up[2], left_back_opening_up[3], fill = colList[0])

screen.create_oval(right_back_opening_up[0], right_back_opening_up[1], right_back_opening_up[2], right_back_opening_up[3], fill = colList[0])
'''
left_centre_back_opening = [goal_line[0]+x_increment*0.7, y_start+y_increment*3, goal_line[0]+x_increment*0.7 + size, y_start+y_increment*3 + size]

right_centre_back_opening = [goal_line[0]+x_increment*0.7, y_start+y_increment*7, goal_line[0]+x_increment*0.7 + size, y_start+y_increment*7 + size]
'''
screen.create_oval(left_centre_back_opening[0], left_centre_back_opening[1], left_centre_back_opening[2], left_centre_back_opening[3], fill=colList[0])

screen.create_oval(right_centre_back_opening[0], right_centre_back_opening[1], right_centre_back_opening[2], right_centre_back_opening[3], fill=colList[0])
'''
horizontal = 1 
x_change_ball = 0
# a variable to enable us to have a vertical slope
for f in range(30):
  # calculating the slope between each of the player's start and end points
  # this statement is to prevent the 0 float division error for zero 
  if abs(left_back_opening[0] - (x_start+x_increment)) == 0:
    left_back_slope = 1
    horizontal = 0
  elif abs(left_back_opening[1]- (y_start+y_increment*1)):
    left_back_slope = 0
  else:
    print(abs(left_back_opening[1] - (y_start+y_increment*1)))
    print(abs(left_back_opening[0] - (x_start+x_increment)))
    left_back_slope = abs(left_back_opening[1]- (y_start+y_increment*1))/abs(left_back_opening[0] - (x_start+x_increment))
  #left_centre_back_slope = abs(left_back_opening)
  #right_centre_back_slope = abs()
  left_back = screen.create_oval((x_start+x_increment) - x_change_ball*horizontal, (y_start+y_increment*1) - x_change_ball*left_back_slope, (x_start+x_increment + size) - x_change_ball*horizontal, (y_start+y_increment*1+size) - x_change_ball*left_back_slope, fill=colList[0])
  x_change_ball += 1
  screen.update()
  sleep(0.05)
  if f == 29:
    pass
  else:
    screen.delete(left_back)

'''

# Players on the red team in 433 formation
'''
input()