from tkinter import *
from random import*
myInterface = Tk()
screen = Canvas(myInterface, width=975,height=900, background="white")
screen.pack()

#Sky
screen.create_rectangle(0,0,1000,700,fill="sky blue")


#Puck
screen.create_polygon(350,612,380,612,380,628,350,628,fill="grey26",smooth="true",outline="black")
screen.create_oval(350,600,380,625,fill="black")
screen.create_text(365,612,text="NHL",font="times 9 bold",fill="white")





#Grass
for x in range(20000):
    x1 = randint(0,1000)
    y1= randint(680,750)
    colour= choice(["blue","green3","green yellow","brown"])
    lengthX = randint(1,30) 
    lengthY = randint(1,20)
    screen.create_line(x1, y1, x1+lengthX, y1-lengthY, fill=colour, width=2)


#Dirt
screen.create_rectangle(0,750,1000,900,fill="sienna4")

for x in range(2000):
    x1 = randint(0,1000)
    y1= randint(755,900)
    colour2= choice(["brown4","sienna4","saddle brown","tan4","sienna3"])
    lengthX = randint(1,5) 
    lengthY = randint(1,5)
    screen.create_oval(x1, y1, x1+lengthX, y1+lengthY, fill=colour2, width=2,outline=colour2)

    
#Back Legs
screen.create_polygon(125,625,125,675,130,700,147,700,152,675,155,640, fill="palegoldenrod",outline="black", smooth="true")



#Tail
screen.create_polygon(75,600,75,575,68,563,50,537,40,512,50,500,62,488,75,500,88,550,88,595, fill="palegoldenrod", smooth="true",outline="black")
screen.create_line(48,525,75,510,fill="gold",width=7)
screen.create_line(60,550,85,540,fill="gold",width=7)


#front Legs1
screen.create_polygon(245,590,275,600,300,610,322,627,312,635,312,633,275,627,232,610, fill="palegoldenrod",smooth="true",outline="black")



#body
screen.create_oval(250,550,75,650,fill="palegoldenrod")


#front Legs2
screen.create_polygon(240,605,275,615,300,625,322,642,312,650,312,648,275,642,232,625, fill="palegoldenrod",smooth="true",outline="black")


# Back legs2
screen.create_polygon(100,625,100,675,100,700,120,700,130,675,130,640, fill="palegoldenrod",outline="black", smooth="true")


#Grass covering legs

for x in range(2000):
    x1 = randint(90,175)
    y1= randint(700,710)
    colour= choice(["green2","green3","green yellow","brown"])
    lengthX = randint(1,5) 
    lengthY = randint(1,5)
    screen.create_line(x1, y1, x1+lengthX, y1-lengthY, fill=colour, width=2)


#Cat Head 
screen.create_oval(150,450,325,600,fill="palegoldenrod",outline="black", width=1)

#Ears

screen.create_polygon(152,500,200,453,138,438,fill="yellow",outline="gold", width=2)
screen.create_polygon(162,490,190,463,148,448,fill="pink",outline="pink", width=2)


screen.create_polygon(325,500,275,457,338,438,fill="yellow",outline="gold", width=2)
screen.create_polygon(315,490,285,463,328,448,fill="pink",outline="pink", width=2)


#strips Top
screen.create_polygon(200,460,230,453,220,490,fill="gold",outline="gold", width=2)
screen.create_polygon(240,450,285,463,263,490,fill="gold",outline="gold", width=2)

#strips left side
screen.create_polygon(155,500,150,525,180,515,fill="gold",outline="gold", width=2)
screen.create_polygon(153,525,155,550,180,538,fill="gold",outline="gold", width=2)


#strips Right side
screen.create_polygon(320,500,325,525,300,512,fill="gold",outline="gold", width=2)
screen.create_polygon(325,525,320,550,297,538,fill="gold",outline="gold", width=2)

#eyes
screen.create_oval(200,490,225,540,fill="white",outline="black", width=1)
screen.create_oval(250,490,275,540,fill="white",outline="black", width=1)

screen.create_oval(210,515,225,535,fill="black")
screen.create_oval(260,515,275,535,fill="black")


#nose
screen.create_polygon(225,550,250,550,238,575,fill="pink",outline="pink", smooth="true")

#mouth
screen.create_line(238,570,213,585,195,563,fill="red",smooth="true",width=3)
screen.create_line(238,570,263,585,278,563,fill="red", smooth="true",width=3)
screen.create_polygon(225,585,250,585,238,565,fill="red", smooth="true",width=3)




#Table
screen.create_rectangle(500,475,900,550,fill="sienna",outline="black")
screen.create_polygon(500,550,518,675,533,675,550,550,fill="sienna",outline="black")
screen.create_polygon(850,550,865,675,880,675,900,550,fill="sienna",outline="black")


#Grass covering table legs

for x in range(2000):
    x1 = randint(475,878)
    y1= randint(670,680)
    colour= choice(["green2","green3","green yellow","brown"])
    lengthX = randint(1,5) 
    lengthY = randint(1,5)
    screen.create_line(x1, y1, x1+lengthX, y1-lengthY, fill=colour, width=2)
    
#Picture Frame
screen.create_polygon(575,400,575,500,650,525,650,400,fill="white",outline="black",width=3,)
screen.create_polygon(585,410,585,490,640,505,640,410,fill="grey")
screen.create_polygon(650,500,675,500,650,450,fill="black")
screen.create_line(599,455,628,455,fill="black",width=5)
screen.create_line(600,475,612,425,625,475,fill="black",width=5)



#Glass with BLUUUEEE WATER
screen.create_oval(700,475,750,500,fill="white smoke",outline="black")
screen.create_rectangle(720,480,730,425,fill="white smoke",outline="black")
screen.create_arc(695,385,750,425, start=180,extent=180,fill="white smoke")
screen.create_arc(697,400,749,425, start=180,extent=180,fill="dodger blue")



#The BLUUUEEE WATER bottle
screen.create_polygon(825,500,820,480,820,470,823,450,823,440,817,420,817,405,825,375,850,375,860,410,860,420,853,440,854,447,857,475,859,480,850,500,fill="dodger blue",smooth="true",outline="black")
screen.create_polygon(824,438,854,438,854,450,824,450,fill="white")
screen.create_text(838,443,text="stroff",font="times 9 bold")
screen.create_text(837,410, text="BLUUEE", font="Times 7 bold",fill="white")
screen.create_text(837,420, text="Water", font="Times 7 bold",fill="white")


#Cap of BLUUUEEE WATER bottle
screen.create_rectangle(826,365,850,379,fill="white")
        
x1=830
y1=365
y2=379

for x in range(4):
    screen.create_line(x1,y1,x1,y2,fill="black")
    x1=x1+5



screen.update()
input()