from math import *
# functions are really useful because they allow for your program to be much more comprehensible
def coneVolume(radius, height):
  '''returns the output of the volume of a cone'''
  volume = pi * radius**2 * 1/3 * height
  return volume

def getSlope(x1, y1, x2, y2):
  if (x1 - x2) == 0:
    return "Undefined"
  else:
    slope = (y1 - y2)/(x1 - x2)
    return slope 
  

def getEOL(m, b):
  '''returns a nicely formatted eq'n of a line (i.e.) y = mx + b or y = mx'''
  if m == "undefined":
    EOL = f"x = {b}"
  else:
    if b > 0:
      EOL = f"y = {m}x+{b}"
    elif b < 0:
      EOL = f"y = {m}x-{b}"
    else:
      EOL = f"y = {m}x"
  return EOL


print(f"the volume of the cone is: {coneVolume(5, 10)}")

print(f"the slope is: {getSlope(1,5,1,6)}")
print(f"the slope is: {getSlope(1,5,2,6)}")
print(f"the slope is: {getSlope(1,5,2,5)}")

print(f"the eq'n of the line is: {getEOL(5,5)}")
print(f"the eq'n of the line is: {getEOL(2,4)}")
print(f"the eq'n of the line is: {getEOL('undefined',3)}")
print(f"the eq'n of the line is: {getEOL(10,1)}")

