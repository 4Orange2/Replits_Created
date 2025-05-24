# Draw several concentric squares, spaced with gaps of 25 pixels
# First square should be 50 pixes x 50 pixels in size

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

spacer = 0

for i in range(5):
  screen.create_rectangle(375 - spacer, 375 - spacer, 425 + spacer, 425 + spacer, outline="red", width = 5)
  spacer += 25
  

screen.update()
input()