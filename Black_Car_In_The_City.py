#Graphics Assignment
#By: Alex Vucicevich
#Title: Random City Shenanigans

from tkinter import *
from random import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background="dodger blue")
screen.pack()

##Clouds
for cloudCount in range(1, 35):
    x = randint(450,600)
    y = randint(25,100)
    size = randint(30, 50)
    screen.create_oval( x, y, x + size, y + size, fill="WhiteSmoke", outline = "WhiteSmoke")
    
for cloudCount in range(1, 40):
    x = randint(250,375)
    y = randint(25,100)
    size = randint(30, 55)
    screen.create_oval( x, y, x + size, y + size, fill="WhiteSmoke",outline = "whitesmoke")
    
for cloudCount in range(1, 20):
    x = randint(-50,50)
    y = randint(0,75)
    size = randint(30, 50)
    screen.create_oval( x, y, x + size, y + size, fill="WhiteSmoke",outline = "whitesmoke")
    
#Fifth Building
screen.create_rectangle(75,50,125,200,fill = "lightsteelblue",outline = "black")
screen.create_polygon(125,50,135,60,135,200,125,200,125,50,fill = "steelblue")
numFloor = 30
y = 50

for stones in range (1, numFloor):
    y = y + 5
    screen.create_line(75, y, 125, y, fill = "black")
    
screen.create_text(100, 62.5, text = "TSM", font = "Helvetica 15 bold")

#Fourth Building
screen.create_rectangle(200,100,150,200,fill = "lightsteelblue",outline = "black")
screen.create_polygon(200,100,210,110,210,200,200,200,200,100,fill = "steelblue")
screen.create_polygon(175,100,185,100,185,65,175,65,fill = "dodgerblue",outline = "red",width = 2)
screen.create_line(180,100,180,35,fill = "red")
numBeams = 7
y = 65

for beams in range(1,numBeams):
    y = y + 5
    screen.create_line(175,y,185,y,fill = "white")
    
numFloor = 20
gap = 5
y = 100

for stones in range (1, numFloor):
    y = y + 5
    screen.create_line(150,y,200,y, fill = "black")
  
#Dome
screen.create_oval(75,150,525,325,fill = "white")
screen.create_line(300,150,300,200,fill = "black")
screen.create_line(125,200,175,175,300,150,fill = "black",smooth = "true")
screen.create_line(200,200,225,175,300,150,fill = "black",smooth = "true")
screen.create_line(262,200,275,175,300,150,fill = "black",smooth = "true")
screen.create_line(332,200,325,175,300,150,fill = "black",smooth = "true")
screen.create_line(400,200,375,175,300,150,fill = "black",smooth = "true")
screen.create_line(500,200,425,175,300,150,fill = "black",smooth = "true")

#Third Building
screen.create_rectangle(450,100,550,225,fill = "peru",outline = "black")
screen.create_polygon(450,100,440,105,440,200,450,200,450,50,fill = "saddlebrown")
numFloor = 6
y = 115

for floor in range (1, numFloor):
    y = y + 7
    screen.create_line(450,y,550,y, fill = "hot pink", width=3)
    
screen.create_line(475,100,475,200,fill = "black")
screen.create_line(500,100,500,200,fill = "black")
screen.create_line(525,100,525,200,fill = "black")
numFloor = 20
x = 450

for floor in range (1, numFloor):
    x = x + 5
    screen.create_line(x,100,x,125, fill = "dimgrey")
    
numFloor = 3
y = 105

for floor in range (1, numFloor):
    y = y + 5
    screen.create_line(450, y, 550, y, fill = "dimgrey")
    
screen.create_line(500, 100, 500, 200, fill = "black")

#Second Building
screen.create_rectangle(575,50,650,225,fill = "lightsteelblue",outline = "black")
screen.create_polygon(575,50,565,55,565,200,575,200,575,50,fill = "steelblue")
numFloor = 30
y = 50

for stones in range (1, numFloor):
    y = y + 5
    screen.create_line(575, y, 650, y, fill = "black")

#Sony Building
screen.create_rectangle(675,50,750,225,fill = "lightsteelblue",outline = "black")
screen.create_polygon(675,50,665,55,665,200,675,200,675,50,fill = "steelblue")
numFloor = 10
y = 50

for n in range (1, numFloor):
    y = y + 15
    screen.create_line(675, y, 750, y, fill = "green", width=3)

screen.create_line(700,50,700,200,fill = "black")
screen.create_line(725,50,725,200,fill = "black")
screen.create_rectangle(700,150,600,225, fill = "lightsteelblue",outline = "black")
screen.create_polygon(600,150,590,155,590,200,600,200,600,50,fill = "steelblue")
numFloor = 10
y = 150

for stones in range (1, numFloor):
    y = y + 15
    screen.create_line(600, y, 700, y, fill = "black")
    
screen.create_text(712.5,62.5,text = "Sony HQ", font = "Helvetica 14 bold")

##Wall
screen.create_rectangle(-50,200,800,800,fill = "darkgrey")
screen.create_rectangle(-50,200,800,225,fill = "gainsboro")
gap = 70
numStones = int(800/gap) + 1

x = 0

for stones in range (1, numStones):
    x = x + gap
    screen.create_line(x,200,x,225, fill = "slategrey", width = 3)

#Tunnel
screen.create_polygon(600,450,600,275,700,225,800,275,800,450,600,450,fill = "dimgrey",smooth = "true",outline = "black")
screen.create_rectangle(600,375,800,450,fill = "dimgrey",outline = "dimgrey")
screen.create_polygon(600,450,675,350,725,350,800,450,600,450,fill = "darkgrey",outline = "black")
screen.create_polygon(675,350,675,300,700,275,725,300,725,350,675,350,fill = "yellow",smooth = "true")
screen.create_rectangle(675,325,725,350,fill = "yellow",outline = "yellow")

#Writing
screen.create_polygon(175,250,150,275,150,350,175,375,200,350,200,275,175,250,fill = "red")
screen.create_line(200,300,175,300,175,275,175,300,200,325,fill = "yellow",width = 2)
screen.create_line(150,325,175,325,175,350,175,325,150,300,fill = "yellow",width = 2)
screen.create_polygon(150,300,175,325,150,325,150,300,fill = "darkgrey")
screen.create_polygon(175,300,200,325,200,300,175,300,fill = "darkgrey")
screen.create_line(150,325,175,325,fill = "yellow",width = 2)
screen.create_line(150,300,175,325,fill = "yellow",width = 2)
screen.create_line(150,300,150,275,175,250,200,275,200,300, fill = "yellow",width = 2)
screen.create_line(175,300,200,325,200,350,175,375,150,350,150,325,fill = "yellow",width = 2)

#Sign
screen.create_polygon(500,250,575,250,575,325,500,325,500,250,fill = "white",outline = "black",width = 2)
screen.create_oval(500,250,575,325,fill = "white",outline = "red",width = 3)
screen.create_text(537,287,text = "P",font = "Helvetica 30 bold",fill = "red")
screen.create_line(512,262,562,317,fill = "red",width = 3)
screen.create_oval(500,250,505,255,fill = "dimgrey")
screen.create_oval(575,325,570,320,fill = "dimgrey")

#Cracks
screen.create_line(320,275,300,285,285,275,fill = "dimgrey")
screen.create_polygon(325,250,333,255,328,275,300,315,325,250,fill = "dimgrey",outline = "black")
screen.create_line(325,275,330,280,350,275,385,281,fill = "dimgrey")
screen.create_line(350,275,357,296,fill = "dimgrey")
screen.create_line(350,275,367,265,375,235,fill = "dimgrey")
screen.create_line(370,250,385,260,425,275,fill = "dimgrey")

#Car
screen.create_oval(550,400,600,450,fill = "black", outline = "dimgrey", width = 3)
screen.create_oval(300,400,350,450,fill = "black", outline = "dimgrey", width = 3)
screen.create_oval(310,415,340,435,fill = "grey", outline = "yellow")
screen.create_oval(560,415,585,435,fill = "grey", outline = "yellow")
screen.create_polygon(400,300,450,300,575,425,250,425,250,350,325,350,400,300, fill = "black")
screen.create_polygon(525,350,600,350,625,375,625,412,600,425,475,425,500,350, fill = "black", smooth = "true")
screen.create_polygon(335,350,400,310,450,310,490,350,335,350, fill = "lightsteelblue")
screen.create_line(425,310,425,350, fill = "lightgrey")
screen.create_oval(525,400,575,450,fill = "black", outline = "dimgrey", width = 3)
screen.create_oval(275,400,325,450,fill = "black", outline = "dimgrey", width = 3)
screen.create_line(250,350,250,325,fill = "dimgrey", width = 3)
screen.create_line(250,325,275,350,fill = "dimgrey", width = 3)
screen.create_line(250,335,261,335,fill = "dimgrey")
screen.create_oval(285,415,315,435,fill = "grey", outline = "yellow")
screen.create_oval(535,415,560,435,fill = "grey", outline = "yellow")
screen.create_polygon(240,335,285,335,275,330,235,310,240,335, fill = "dimgrey",outline = "black")
screen.create_polygon(612,375,590,375,590,365,612,365,612,375, fill = "yellow", smooth = "true", outline = "dimgrey")
screen.create_rectangle(250,415,240,405, fill = "grey", outline = "black")

#Fence
numPosts = 18
gap = 50
x = -50

for posts in range (1, numPosts):
    x = x + gap
    screen.create_rectangle(x,450,x+12,375, fill = "chocolate")
    
screen.create_rectangle(-50,415,800,425,fill = "chocolate")
screen.create_rectangle(-50,390,800,400,fill = "chocolate")

#Grass
Grass = screen.create_rectangle(0,450,800,800, fill = "forest green")
grassColours = ["green","red","light green"]

for grassCount in range (1,30001):
    x = randint(0,800)
    y = randint (450,800)
    deltaX = randint (1,15)
    deltaY = randint(-15,-6)
    b = choice( grassColours )

    grassBlade = screen.create_line(x, y, x+deltaX, y+deltaY, fill = b)

#Baseball Field
Path = screen.create_oval(-1500,1600,1500,600, fill = "sienna")

#Baseball Plate
screen.create_polygon(175,650,174,655,275,680,400,655,300,625,175,650,fill = "whitesmoke")
Chairthing = screen.create_polygon(300,625,175,650,275,675,400,650,300,625,fill = "white",outline = "black")

#Baseball Shadow
screen.create_oval(468,675,500,700,fill = "brown",outline = "sienna")

#Baseball
screen.create_oval(475,650,510,685,fill = "blue",outline = "black")
screen.create_line(490,650,480,677,fill = "red")
screen.create_line(500,680,506,657,fill = "red")
screen.create_line(150,100,200,100,fill = "black")

screen.update()
input()
