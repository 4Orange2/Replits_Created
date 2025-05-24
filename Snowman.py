from tkinter import *
from time import *
myInterface = Tk()
screen = Canvas(myInterface, width=500, height=500, background="black")
screen.pack()


'''99% OF THE TIME WHEN I USE create_oval(), I JUST WANT A  CIRCLE.
BUT create_oval() IS ANNOYING BECAUSE IT HAS TO BE TOLD THE UPPER-LEFT
AND LOWER-RIGHT CORNERS, AND I DON'T LIKE HAVING TO WORK OUT WHERE THOSE ARE.
I WISH I COULD JUST TELL PYTHON THE CENTRE & RADIUS OF THE CIRCLE I WANT.
SO...LET'S MAKE A NEW COMMAND THAT LETS US DO PRECISELY THAT!'''


#USING THE EXISTING create_oval PROCEDURE TO MAKE A NEW PROCEDURE CALLED drawCircle()
def drawCircle( xCentre, yCentre, rad, col ):   
    screen.create_oval( xCentre-rad, yCentre-rad, xCentre+rad, yCentre+rad, fill= col, outline=col )

#TESTING OUR NEW PROCEDURE
drawCircle( 250, 250, 75, "white" )                   #circle with centre (0, 0), radius 100 and colour green
drawCircle( 250, 150, 60, "white" )      #circle with centre (500, 500), radius 50 and colour green
drawCircle(250, 80, 40, "white")


'''
#A COOL APPLICATION OF CIRCLES AND COLOURING
radius = 200
for i in range(100):  #100 circles of ever-shrinking size and ever-brightening grey scale.  Cool effect, eh?
    greyness = "grey"+str(i)  #will take on the Python colours grey1, grey2, grey3, ..., grey98, grey99
    drawCircle( 250, 250, radius, greyness ) 
    screen.update()
    sleep(0.1)
    radius = radius - 2  #make the circle slightly smaller 
'''

input()