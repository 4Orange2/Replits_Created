# This program aims to create a reuleaux triangle
# The requirements of this project don't state that the width of the releaux triangle should be modifiable but I'm going to make the width modifiable by taking a simple input from the user

# the extent of the arcs should be 20, 21, 22


# I calculate the rotations based off of a formula written on paper; I've attached it to the assignment

from math import *

from tkinter import *

canvas_width = 780
canvas_height = 600

myInterface = Tk()
screen = Canvas(myInterface, width=canvas_width, height=canvas_height, background="sky blue")
screen.pack()

starting_x = 200
starting_y = 200


size = int(input("Enter the size that you would like to see for the reuleaux triangle? "))
#rotation = int(input("Enter the angle that you would like the tip of the reuleaux triangle to be at (by tip I mean the vertex of the triangle where the triangle and the two arcs converge)?"))

#rotation = int(input())

# Initial thought:
# for both of these arcs, we're going to rotate them around the center of the first arc
# and the center is ((starting_x + size)/2, (starting_y + size)/2)

# I need to learn how to rotate an arc in python
# I need to rotate this arc around the centroid of the equilateral triangle
# I searched up ways to rotate a triangle in python and I found this link: https://mail.python.org/pipermail/python-list/2000-December/022013.html
# It said that you must rotate the points first before calling create_polygon again
# you use the tkinter apply() function
'''
def rotate_points(x0, ):


# The blue arc will always be to the right of the top point in python

red_arc = screen.create_arc(starting_x, starting_y, starting_x, starting_y + size, extent = 60, fill="red", style="pieslice")

#blue_arc = screen.create_arc()

green_arc = screen.create_arc(starting_x + size, starting_y + size, starting_x, starting_y, extent=60, fill="green", style="pieslice")

#screen.create_arc(starting_x, starting_y, starting_x + size, starting_)

'''
'''
new_angle_x = (starting_x * (cos(120) - sin(120)))
new_angle_y = (starting_y * (sin(120) + cos(120)))
'''
# this shape needs to be rotated 120 degrees
#screen.create_arc(starting_x + size, starting_y + size, starting_x, #starting_y + size, fill="blue", style="c")



# this shape needs to be rotated 240 degrees from the original shape
# The green arc will always be to the left of the top point in python
'''
center = [(size/2), size/2]
print(f"this is the center {center}")

distance_maker_x = ((starting_x - (starting_x + size/2)))
print(f"this is x {distance_maker_x}")

distance_maker_y = ((starting_y - (starting_y + size/2)))
print(f"this is y {distance_maker_y}")

distance_maker_x = (distance_maker_x * (cos(180) - sin(180)))
print(f"this is {distance_maker_x}")

distance_maker_y = (distance_maker_y * (sin(180) + cos(180)))

print(f"this is {distance_maker_y}")


screen.create_arc(((starting_x + size)/2) + distance_maker_x, ((starting_y + size)/2) + distance_maker_y, ((starting_x + size)/2) - size - distance_maker_x, ((starting_x + size)/2) - size - distance_maker_y, fill="green", style="pieslice")

'''

#screen.create_arc(starting_x - size, starting_y - size, starting_x + size, starting_y + size, fill="red", style="pieslice")

input()