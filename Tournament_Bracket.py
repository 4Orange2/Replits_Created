# Takes elimination round numbers from 1 to 6

# a bracket graphic will be produced the covers the whole canvas

from tkinter import *
from time import *
from random import *


canvas_width = 780
canvas_height = 600

myInterface = Tk()
screen = Canvas(myInterface, width=canvas_width, height=canvas_height, background="sky blue")
screen.pack()

elimination_rounds = int(input("How many elimination rounds are there? "))


box_thickness = (canvas_height - 10)/(2**elimination_rounds * 2) # because we need 2^that round to fit and we need the spaces in between
box_length = 90
box_x_position = 0
box_y_position = box_thickness

box_x_pos_increment = ((canvas_width) - box_length)/elimination_rounds

print(box_thickness)

for bracket_level in reversed(range(elimination_rounds + 1)):
  print(f"bracket level: {bracket_level}")
  for i in range(2**bracket_level):
    # where is bracket_level
    # creates a list that contains the largest number out of the range(elimination_rounds) and slowly decreases
    screen.create_rectangle(box_x_position, box_y_position, box_x_position + box_length, box_y_position + box_thickness, fill="yellow")
    mpgbxb = (box_x_position + box_x_pos_increment - (box_x_position + box_length)) # stands for middle_point_gap_between_x_brackets
    screen.create_line(box_x_position + box_length, box_y_position + box_thickness/2, box_x_position + box_length + mpgbxb/2, box_y_position + box_thickness/2, fill="red") # horizontal line that comes out of each of the brackets
    # vertical lines:
    # goes to meet the other line downward
    if i != (2**bracket_level - 1) and i % 2 == 0:
      screen.create_line(box_x_position + box_length + mpgbxb/2, box_y_position + box_thickness/2, box_x_position + box_length + mpgbxb/2, box_y_position + box_thickness * 2**((elimination_rounds+1) - (bracket_level)), fill="red") 
    else:
      pass
    # goes to meet the other line upward
    if i != 0 and i % 2 == 1:
      screen.create_line(box_x_position + box_length + mpgbxb/2, box_y_position + box_thickness/2, box_x_position + box_length + mpgbxb/2, box_y_position + box_thickness/2 - box_thickness * 2**((elimination_rounds + 1) - (bracket_level)), fill="red")
    else: 
      pass
    # for the final horizontal line
    if i % (2) == 0:
      screen.create_line((box_x_position + box_length + mpgbxb/2), box_y_position + (box_thickness/2 + (box_thickness * 2**((elimination_rounds + 1) - (bracket_level)) /2)), (box_x_position + box_length + mpgbxb), box_y_position + (box_thickness/2 + (box_thickness * 2**((elimination_rounds + 1) - (bracket_level)) /2)), fill="red")
    box_y_position += box_thickness * 2**((elimination_rounds+1)-bracket_level)
  box_y_position = 0 + box_thickness* (2**((elimination_rounds+1)-bracket_level))
  box_x_position += box_x_pos_increment
input()