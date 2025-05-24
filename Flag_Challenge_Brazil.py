'''
Rectangles
Ovals
Lines
Polygons
Arcs

Text on canvas to label flag

The two flags that I chose were: 
Brazil - in a rectangular outline
South Africa - in a circular outline (and a rectangular outline)
-- maybe you could even convert circular to rectangular with the change of a simple constant
'''

#Initialize Tkinter with these
from tkinter import *

myInterface = Tk()
screen = Canvas(myInterface, width=800, height=600, background="black")
screen.pack()

# Ratio of the Brazil flag found with the following Wikipedia link: https://en.wikipedia.org/wiki/Flag_of_Brazil#/media/File:Flag_of_Brazil_(dimensions).svg

#
#Your code goes here
#
'''
# Constants so that it's easier to tweak my flag:

- y_stretch
- x_stretch

left of rhombus
right of rhombus
top of rhombus
bottom of rhombus
'''
# all of the rest of the shapes will then be relative to x_stretch
# I made the variable y_stretch such that my code is more readable and that not every number is written relative to the x_stretch

x_stretch = 600
y_stretch = (
    x_stretch * 7
) / 10  # using the cross-multiplication technique; 10;7 is the ratio of the x:y for brazil's flag
multiplier = x_stretch / 10  # this is the number that we use to keep the ratio but change the size

screen.create_rectangle(0,
                        0,
                        x_stretch,
                        y_stretch,
                        fill="forestgreen",
                        outline="white")
screen.create_polygon(0 + 0.85 * multiplier,
                      y_stretch / 2,
                      x_stretch - 0.85 * multiplier,
                      y_stretch / 2,
                      x_stretch / 2,
                      y_stretch - 0.85 * multiplier,
                      x_stretch / 2,
                      0 + 0.85 * multiplier,
                      fill="yellow")
screen.create_polygon(0 + 0.85 * multiplier,
                      y_stretch / 2,
                      x_stretch - 0.85 * multiplier,
                      y_stretch / 2,
                      x_stretch / 2,
                      0 + 0.85 * multiplier,
                      x_stretch / 2,
                      y_stretch - 0.85 * multiplier,
                      fill="yellow")
# Something that I learned from this exercise: the order in which you write the coordinates for the create_polygon function matter; the function will literally connect one point to the next with a line; fill that space with a fill if it's a triangle and then start filling triangle-by-triangle without even caring to go back to fill the dots

# Circle has a radius of 3.5 modules
# The centre of the Canvas is at (x_stretch/2, y_stretch/2)

screen.create_oval(x_stretch / 2 - 3.5 / 2 * multiplier,
                   y_stretch / 2 - 3.5 / 2 * multiplier,
                   x_stretch / 2 + 3.5 / 2 * multiplier,
                   y_stretch / 2 + 3.5 / 2 * multiplier,
                   fill="blue")

# White stars

# A list of a bunch of x and y coordinates all written in terms of x_stretch/2, y_stretch/2,  and the multiplier
# these coordinates are going to be for the top-left point of the star

module_multiplier = multiplier / 2 # half of initial multiplier
print(module_multiplier)

list_of_coordinates_for_stars = [
    [x_stretch / 2 - 3 * module_multiplier, y_stretch / 2 - 0.7 * module_multiplier],
    [x_stretch / 2 - 3 * module_multiplier, y_stretch / 2 + 0.8 * module_multiplier],
    [x_stretch / 2 - 2.4 * module_multiplier, y_stretch / 2 + 0.5 * module_multiplier],
    [x_stretch / 2 - 2.6 * module_multiplier, y_stretch / 2 + 1.8 * module_multiplier],
    [x_stretch / 2 - 1.3 * module_multiplier, y_stretch/2 - 0.1 * module_multiplier],
    [x_stretch / 2 - 1.45 * module_multiplier, y_stretch / 2 + 1 * module_multiplier],
    [x_stretch / 2 - 0.2 * module_multiplier, y_stretch / 2 + 1 * module_multiplier],
    [x_stretch / 2 - 0.15 * module_multiplier, y_stretch / 2 + 1.6 * module_multiplier],
    [x_stretch / 2 + 0.5 * module_multiplier, y_stretch / 2 + 0.2 * module_multiplier],
    [x_stretch / 2 + 0.3 * module_multiplier, y_stretch / 2 + 1 * module_multiplier],
    [x_stretch / 2, y_stretch / 2 + 2.6 * module_multiplier],
    [x_stretch / 2 + 0.6 * module_multiplier, y_stretch / 2 - 1.7 * module_multiplier],
    [x_stretch / 2 + 1 * module_multiplier, y_stretch / 2 + 2 * module_multiplier],
    [x_stretch / 2 + 1.2 * module_multiplier, y_stretch / 2 + 1.65 * module_multiplier],
    [x_stretch / 2 + 1.4 * module_multiplier, y_stretch / 2 + 1.6 * module_multiplier],
    [x_stretch / 2 + 1.6 * module_multiplier, y_stretch / 2 + 1.55 * module_multiplier],
    [x_stretch / 2 + 1.6 * module_multiplier, y_stretch / 2 + 2 * module_multiplier],
    [x_stretch / 2 + 1.9 * module_multiplier, y_stretch / 2 + 2.05 * module_multiplier],
    [x_stretch / 2 + 2.1 * module_multiplier, y_stretch / 2 + 0.6 * module_multiplier],
    [x_stretch / 2 + 2.2 * module_multiplier, y_stretch / 2 + 1 * module_multiplier]]

# (20,156) is the top-left coordinate of the star
y_loc = 20
x_loc = 156

#points=[200,20,80,396,380,156,20,156,320,396] # for the outside of the star
# copied a sample set of points that worked from stack overflow
# all of those numbers are going to be written in relation to the top_left star_coordinate

# figure out the the distance ratio for the star:


# Then calculated the coordinates of the inner pentagon using my knowledge of the equations of a line and points of intersection

#reen.create_polygon(points, outline='white', fill='white')

points2 = [
    200, 20, 80, 396
]  # for the pentagon inside of the star; the numbers were calculated using

divider = 25

#for loop for the stars of Brazil
for coordinate in list_of_coordinates_for_stars:
  print(coordinate)
  points = [
      coordinate[0] + 200 / divider, coordinate[1] - 20 / divider, coordinate[0] + 80 / divider, coordinate[1] + 396 / divider, coordinate[0] + 380 / divider, coordinate[1] + 156 / divider, coordinate[0], coordinate[1] + 156/divider, coordinate[0] + 320 / divider, coordinate[1] + 396 / divider]
  #points_pentagons = []
  screen.create_polygon(points, outline='white', fill='white')

screen.create_line(200,175, 300, 170,410,220,fill="white", width = 20, smooth="true") 

x_for_text = 210
y_for_text = 175
iteration = 0

for letter in "Ordem E Progresso":
  screen.create_text(x_for_text, y_for_text, text=letter, fill="green",
                     font=("Helvetica 15 bold"), anchor="center")
  x_for_text += 12
  if iteration < 7:
    y_for_text += 1
  elif iteration >=7 and iteration < 10:
    y_for_text += 2
  elif iteration >= 10:
    y_for_text += 4
  iteration += 1


# you need to list the points in the way that they appear around the star, from one point to the next around the star

#Grid lines
#REMOVE THESE BEFORE SUBMITTING ANY ASSIGNMENTS
spacing = 50

for x in range(0, 800, spacing):
  screen.create_line(x, 25, x, 600, fill="white")
  screen.create_text(x, 5, text=str(x), font="Times 9", anchor=N, fill="white")

for y in range(0, 600, spacing):
  screen.create_line(25, y, 800, y, fill="white")
  screen.create_text(5, y, text=str(y), font="Times 9", anchor=W, fill="white")

screen.update()
input()
