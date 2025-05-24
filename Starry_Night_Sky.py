from tkinter import *
from random import *    #to use randint() we need to import the random package
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=600, background="black")
screen.pack()

random_list = []
'''
Proof that randint() generates random numbers all the way from 0 to 255 (inclusive)
while random_list.count(255) == 0:
  random_list.append(randint(0,255))
  print(random_list)
print("done")

while random_list.count(0) == 0:
  random_list.append(randint(0,255))
  print(random_list)
print("done")
'''

def rgb_to_hex(r, g, b):
  # ":02x" is a special command that formats three digit rgb numbers into hexadecimal numbers
  return '#{:02x}{:02x}{:02x}'.format(r, g, b)

'''
#1 DRAWING 1 RANDOM STAR
x = randint(0,800)   #randint chooses a random integer in the given range (0 to 800)
y = randint(0,600)
screen.create_oval(x, y, x+4, y+4, fill="white", outline="white")
'''

screen.create_rectangle(0,500, 800, 600, fill="green")

#2 DRAWING 200 RANDOM STARS

for star in range(800):
  x = randint(0,800)
  y = randint(0,400)
  size_factor = randint(0,50)
  red = randint(0,255)
  green = randint(0,255)
  blue = randint(0,255)
  hex_color = rgb_to_hex(red, green, blue)
  screen.create_oval(x, y, x+size_factor, y+size_factor, fill=hex_color, outline="white")

input()