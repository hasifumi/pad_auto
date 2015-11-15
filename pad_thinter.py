import sys
import Tkinter
import pad

circle_height = 50

root = Tkinter.Tk()
root.title(u'Software Title')
root.geometry(str(6*circle_height) + "x" + str(5*2*circle_height+50))

#Canvas1
c1 = Tkinter.Canvas(root, width=6*circle_height, height=5*2*circle_height+50)
c1.place(x=1, y=1)

c1_circles = []
c2_circles = []

def draw_circles(circles, x, y):
    for j in range(5):
        for i in range(6):
            #circles.append(c1.create_oval(1+j*circle_height, 1+i*circle_height, (j+1)*circle_height, (i+1)*circle_height))
            circles.append(c1.create_oval(x+i*circle_height, y+j*circle_height, x+(i+1)*circle_height, y+(j+1)*circle_height))

def fill_circles(circles, lst, cvs):
    for index, value in enumerate(circles):
        if lst[index] == 'r':
            cvs.itemconfig(circles[index], fill='red')
        elif lst[index] == 'b':
            cvs.itemconfig(circles[index], fill='blue')
        elif lst[index] == 'g':
            cvs.itemconfig(circles[index], fill='green')
        elif lst[index] == 'l':
            cvs.itemconfig(circles[index], fill='yellow')
        elif lst[index] == 'd':
            cvs.itemconfig(circles[index], fill='gray')
        elif lst[index] == 'c':
            cvs.itemconfig(circles[index], fill='pink')

lst1 = pad.create_drops_random()
dct = pad.pivot_drops(lst1)
max_cmb = pad.max_combo(dct)
lst2 = pad.sort_drops(dct)
lst = pad.create_goal_drops(lst2, max_cmb)

draw_circles(c1_circles, 1, 1)
draw_circles(c2_circles, 1, 5*circle_height+51)
fill_circles(c1_circles, lst1, c1)
fill_circles(c2_circles, lst, c1)

#c1.pack()

#label
Static1 = Tkinter.Label(text=str(max_cmb))
#Static1.place(x=270, y=50)
Static1.pack()

root.mainloop()
