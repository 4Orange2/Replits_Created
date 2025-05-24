# prograam testeed from stack overflow
# this program rotates a triangle around a center point that you can change within this program
# the variable that changes this center point is called: center


from tkinter import *

import cmath,math

root = Tk()

c = Canvas(root,width=200, height=200)
c.pack()

# keypress event
def key(event): # this module is able to rotate the triangle using degrees (e.g. 360 degrees roation is the same as 0 degrees rotation)
    text.focus_force()
    ch=event.char # this creates a list of all the numbers that were typed in

    # handle backspace
    if ch=='\x08': # This is the ASCII character for backspace
        if len(text.get())>1:
            entry_text=text.get()[:-1] # get nothing
            if entry_text=='-': entry_text='0'
        else:
            entry_text='0'
    else:
        entry_text=text.get()+ch 

    # we want an integer
    try:
        angle_degrees=int(entry_text)
        cangle = cmath.exp(angle_degrees*1j*math.pi/180) # putting "j" after a number in python makes it imaginary
      # cangle is the exponent of the arc length of the  python
        print(f"this is cangle {cangle}") # cangle is the extent to which we want to rotate the triangle
      # the exp() function returns a value that is equal to E^(the value that you give it)
      # where E is the mathematical constant ~2.178

        offset = complex(center[0], center[1]) # the first entry is the real number and the econd entry is the imaginary number
        print(f"This is the center: {offset}")
        # what is the point of the offset variable?
        # the offset variable 
        newxy = []
        for (x, y) in triangle:
            v = cangle * (complex(x, y) - offset) + offset 
          # you initially take away the center because you just want to worry about the points in relation to one another
          # you add offset again so that your number can rotate over the center point
            print(f"this is subtraction: {complex(x, y) - offset}")
            print(f"this is multiplication: {cangle * (complex(x, y) - offset)}")
            print(f"this is {v}")
            newxy.append(v.real) # the real part of the number, which becomes the x coordinate
            print(f"this is v.imag {v.imag}")
            newxy.append(v.imag) # the imaginary part of the number, which becomes the y coordinate
            print(f"this is the {newxy}")
        c.coords(polygon_item, *newxy)
    except ValueError: # if a value error occurs, we go into this block
        print("not integer")

text = Entry(root)
text.bind("<Key>", key) # binding the keyboard with the main window
# this is where the key() function is called


text.pack()
text.focus_force()

center = 75, 75

# a triangle
# goes from top left corner, down, and then right 
triangle = [(center[0]-50, center[1]-50), (center[0]-50, center[1]+50), (center[0]+50, center[1]+50)]

polygon_item = c.create_polygon(triangle)


mainloop()
