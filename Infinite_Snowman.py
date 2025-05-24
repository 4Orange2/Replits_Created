# Draw infinite snowmen, with each snowball decreasing in size by 25%

from tkinter import*
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=600, background="sky blue" )
screen.pack()

spacing = 50

for x in range(0, 1000, spacing): 
    screen.create_line(x, 25, x, 1000, fill="blue")
    screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N)

for y in range(0, 1000, spacing):
    screen.create_line(25, y, 1000, y, fill="blue")
    screen.create_text(5, y, text=str(y), font="Times 9", anchor = W)

SHRINK = 0.75
distance_to_bring_in = 0
diameter_of_ball = 100
larger_coordinate_x = 400
smaller_coordinate_x = 300
y_coordinate1 = 350
y_coordinate2 = 450
''''''
while True:
  larger_coordinate_x -= distance_to_bring_in
  print(f"this is larger_coordinate {larger_coordinate_x}")
  smaller_coordinate_x += distance_to_bring_in
  print(f"this is smaller_coordinate {smaller_coordinate_x}")
  screen.create_oval(smaller_coordinate_x, y_coordinate1, larger_coordinate_x, y_coordinate2, fill="white", outline="black", width = 1)
  distance_to_bring_in = (diameter_of_ball - (diameter_of_ball * SHRINK))/2
  print(f"this is distance_to_bring_in {distance_to_bring_in}")
  y_coordinate1 -= diameter_of_ball * SHRINK
  y_coordinate2 -= diameter_of_ball
  diameter_of_ball *= SHRINK
  print(f"this is diameter_of_ball {diameter_of_ball}")
  screen.update()
input()