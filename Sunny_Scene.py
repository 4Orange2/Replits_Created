from tkinter import*
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=600, background="sky blue" )
screen.pack()

#Grass
screen.create_rectangle(0, 460, 800, 600, fill = "green4")

#Sun
screen.create_oval(500, 128, 693, 228, fill = "yellow")

#Octogon
screen.create_polygon(200, 210, 300, 210, 400, 310, 400, 410,
                      300, 510, 200, 510, 100, 410, 100, 310, fill = "red")

#Post
screen.create_line(250, 510, 250, 600, fill = "gray20", width = 25)

#Text
screen.create_text(250, 365, text = "STOP!", font = "Arial 72", fill = "white")

#Grid lines
spacing = 50

for x in range(0, 1000, spacing): 
    screen.create_line(x, 25, x, 1000, fill="blue")
    screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N)

for y in range(0, 1000, spacing):
    screen.create_line(25, y, 1000, y, fill="blue")
    screen.create_text(5, y, text=str(y), font="Times 9", anchor = W)

screen.update()
input() # basically just stalls the program forever