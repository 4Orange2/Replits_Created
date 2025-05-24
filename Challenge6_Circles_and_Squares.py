#Initialize Tkinter with these
from tkinter import*
from math import*
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=600, background="black")
screen.pack()

starting_point = 200

square_length = int(input("Input the length of square (in pixels): "))

screen.create_rectangle(200, 200, 200+square_length, 200+square_length, fill="red")
screen.create_oval(200, 200, 200+square_length, 200+square_length, fill="blue")

# using the pythagorean theorem to calculate the length of the line
# then you would shrink the size of the original square such that the diagonals that attach to the centre of the square are equal to the radius of the circle
# the way we would shrink the size: 
# subtracting the length of the radius() from the length of the original diagonal of the bigger square that attaches to the middle

# Original diagonal calculated: square_length/2**2 + square_length/2**2
# Original diagonal - square_length/2 = the diagonal length that we need to remove
# Then we solve for the new coordiante using the pythagorean theorem; remove_diagonal**2 = x^2 + y^2 (x and y are equal because this is a square)
# Now we can just rearrange to solve for x



# Additional challenge for mysekf: I made it go on so that it makes squares infinitely

while True:
  big_diagonal = sqrt((square_length/2)**2 + (square_length/2)**2)
  print(f"big_diagonal {big_diagonal}")
  
  remove_diagonal = big_diagonal - square_length/2
  print(f"remove_diagonal {remove_diagonal}")
  
  distance_maker = sqrt(remove_diagonal**2/2)
  print(f"distance_maker {distance_maker}")
  
  screen.create_rectangle(starting_point + distance_maker, starting_point + distance_maker, starting_point + square_length - distance_maker, starting_point + square_length - distance_maker, fill = "red")
  screen.create_oval(starting_point + distance_maker, starting_point + distance_maker, starting_point + square_length - distance_maker, starting_point + square_length - distance_maker, fill = "blue")

  square_length = starting_point + square_length - distance_maker - (starting_point + distance_maker)
  starting_point += distance_maker
  
  screen.update()
  

spacing = 50
for x in range(0, 800, spacing): 
    screen.create_line(x, 25, x, 600, fill="white")
    screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N, fill = "white")

for y in range(0, 600, spacing):
    screen.create_line(25, y, 800, y, fill="white")
    screen.create_text(5, y, text=str(y), font="Times 9", anchor = W, fill = "white")

screen.update()
input()