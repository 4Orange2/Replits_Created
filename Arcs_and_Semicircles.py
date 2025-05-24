from tkinter import *
master = Tk()
screen = Canvas( master, width = 800, height = 600, background = "black")
screen.pack()


#White circle background
screen.create_oval( 50, 50, 250, 250, fill="white") 
#Red quarter circle drawn overtop
screen.create_arc( 50, 50, 250, 250, start=150, extent=90, fill="red")

#Semicircle (the "extent" is 180 degrees)
screen.create_arc( 50, 300, 250, 500, start=0, extent=180, fill="blue")
#Same semicircle flipped upside down
screen.create_arc( 50, 320, 250, 520, start=180, extent=180, fill="green")

#Pacman (arc starting at 60 degrees and extending for 300 degrees)
screen.create_arc( 260, 50, 460, 250, start=55, extent=270, fill="yellow")



#Racetrack
trackWidth = 200
xLeft = 500
xRight = xLeft + trackWidth
yTop = 150
yBottom = 450

screen.create_rectangle( xLeft, yTop, xRight, yBottom, fill="tan" ) #the middle of the track
screen.create_arc( xLeft, yTop-trackWidth/2, xRight, yTop+trackWidth/2, start=0, extent=180, fill="yellow") #rounded end 1
screen.create_arc( xLeft, yBottom-trackWidth/2, xRight, yBottom+trackWidth/2, start=180, extent=180, fill="yellow") #rounded end 2




#Fun stuff
numSlices = 20
anglePerSlice = (360/numSlices) / 2  #why do we divide by 2?

angleStart = 0

for n in range(1, numSlices+1 ):
   screen.create_arc( 260, 300, 460, 500, start = angleStart, extent = anglePerSlice, fill="white")
   angleStart = angleStart + anglePerSlice*2  #why is it times 2?

 

 
#Put it all on screen
screen.update()
input()