from math import *

x1 = int(input("Enter x1:"))
y1 = int(input("Enter y1:"))
x2 = int(input("Enter x2:"))
y2 = int(input("Enter y2:"))
x3 = int(input("Enter x3:"))
y3 = int(input("Enter y3:"))
x4 = int(input("Enter x4:"))
y4 = int(input("Enter y4:"))

#Checks to see if any two of the points are the same,
#to test if the inputted co-ordinates will form a quadritaleral.
if x1 == x2:
  if y1 == y2:
    print("The shape you have entered is not a quadrilateral.")
    validinput = False
  else:
    validinput = True
elif x2 == x3:
  if y2 == y3:
    print("The shape you have entered is not a quadrilateral.")
    validinput = False
  else:
    validinput = True
elif x1 == x3:
  if y1 == y3:
    print("The shape you have entered is not a quadrilateral.")
    validinput = False
  else:
    validinput = True
elif x1 == x4:
  if y1 == y4:
    print("The shape you have entered is not a quadrilateral.")
    validinput = False
  else:
    validinput = True
elif x2 == x4:
  if y2 == y4:
    print("The shape you have entered is not a quadrilateral.")
    validinput = False
  else:
    validinput = True 
elif x3 == x4:
  if y3 == y4:
    print("The shape you have entered is not a quadrilateral.")
    validinput = False
  else:
    validinput = True
else:
  validinput = True

if validinput == True:
  #Calculates Lengths and Diagonals of points
  Lab = sqrt((x2-x1)**2+(y2-y1)**2)
  Lad = sqrt((x1-x4)**2+(y1-y4)**2)
  Lcb = sqrt((x2-x3)**2+(y2-y3)**2)
  Lcd = sqrt((x4-x3)**2+(y4-y3)**2)
  Dac = sqrt((x3-x1)**2+(y3-y1)**2)
  Dbd = sqrt((x4-x2)**2+(y4-y2)**2)

  #Calculates Slopes
  if x2 == x1:
    Sab = "undefined"
  else:
    Sab = (y2-y1)/(x2-x1)

  if x1 == x4:
    Sad = "undefined"
  else:
    Sad = (y4-y1)/(x4-x1)

  if x3 == x2:
    Scb = "undefined"
  else:
    Scb = (y2-y3)/(x2-x3)

  if x3 == x4:
    Scd = "undefined"
  else:
    Scd = (y4-y3)/(x4-x3)

  #Calculations for which shape the points form
  #If adjacent sides are equal and:
  #    - diagonals are equal then it is a square
  #    - opposite slopes are equal then is is a rhombus
  #    - else it is a kite
  if Lab == Lad and Lcd == Lcb:
    if Dac == Dbd:
      qud = "Square"
    else:
      if Sad == Scb:
        qud = "Rhombus"
      else:
        qud = "kite"

  #If two sets of slopes are equal and:
  #   - If other set of slopes are equal
  #       -If they have equal diagonals, it is a Rectangle
  #       -else it is a parallelogram
  #   - Else its a trapezoid
  elif Sab == Scd:
    if Scb == Sad:
      if Dac == Dbd:
        qud = "Rectangle"
      else:
        qud = "Parallelogram"
    else:
      qud = "Trapezoid"

  #If two sets of slopes are equal and:
  #   - If other set of slopes are equal
  #       -If they have equal diagonals, it is a Rectangle
  #       -else it is a parallelogram
  #   - Else its a trapezoid
  elif Scb == Sad:
    if Sab == Scd:
      if Dac == Dbd:
        qud = "Rectangle"
      else:
        qud = "Parallelogram"
    else:
      qud = "Trapezoid"
  #If no other conditions are met, its just a boring old quadrilateral.
  else:
    qud = "Boring Quadrilateral"

  #Prints conclusion
  print("The co-ordinates you have entered will make a", str(qud)+".")
  print()

else:
  print()

  #END OF PROGRAM
