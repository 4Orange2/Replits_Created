from math import pi
from math import sqrt

circle_area = float(input("What is the area of the circle? "))

units = input("What were the units used? ")

radius_squared = circle_area / pi

radius = sqrt(radius_squared)

print(f"The radius is: {radius} {units}")

circumference = radius * 2 * pi

print(f"The circumference is: {circumference} {units}")