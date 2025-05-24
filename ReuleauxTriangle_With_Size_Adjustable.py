# this program aims to create a reuleaux triangle with a variable size set by the user

# idea: set the coordinates as x and y and then rotate the x and y coordinates

# this program is based off of the following diagram

from math import *

from tkinter import *

canvas_width = 780
canvas_height = 600

myInterface = Tk()
screen = Canvas(myInterface, width=canvas_width, height=canvas_height, background="sky blue")
screen.pack()

hypotenuse_length_square = int(input("Enter your size (scale of 100 to 500): "))

#  converting degrees into radians because sin takes radians as its parameter

leg_length_square = sqrt((hypotenuse_length_square**2)/2)
print(f"this is {leg_length_square}")


starting_x = 200
starting_y = 200

end_point_x = (200 + leg_length_square)
end_point_y = (200 + leg_length_square)

screen.create_arc(
  starting_x, starting_y, end_point_x, end_point_y,
  fill="red", style="pieslice", start=90, extent=60,width=1,outline="red")

screen.create_arc(
starting_x, starting_y - leg_length_square/2, end_point_x, end_point_y - leg_length_square/2,
fill="red", style="pieslice", start=90+120, extent=60, width=1, outline="red")

screen.create_arc(
starting_x - (cos(radians(30)) * (leg_length_square/2)), starting_y - leg_length_square/4, end_point_x - (cos(radians(30)) * (leg_length_square/2)), end_point_y - leg_length_square/4, fill="red", style="pieslice", start=90+120+120, extent=60, width=1, outline="red")


#screen.create_arc(sin(radians(60)))

input()