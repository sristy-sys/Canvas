from tkinter import *
r = Tk()
c=Canvas(r, height=5000, bg="white")
c.pack()
x=50
y=50
l,m=40,40
oval=c.create_oval(0,0,0,0)
n="black"
count=0
size=15
def color(text):
	global n
	n=text
	
def siz(s):
	global size
	size=s
def twoD_paint(event):
	global size
	global oval
	global l
	global m
	global n
	global count
	global x
	global y
	if count==0:
		x,y=event.x, event.y
		count+=1
		
	oval=c.create_line(x,y, event.x, event.y, fill=n, smooth=1, width=size, capstyle=ROUND)
	x,y=event.x, event.y

def threeD_paint(event):
	global size
	global oval
	global l
	global m
	global n
	global count
	global x
	global y
	if count==0:
		x,y=event.x, event.y
		count+=1
		
	oval=c.create_line(x,y, event.x, event.y, fill=n, smooth=1, width=6)
	for i in range(size):
		oval=c.create_line(x-i, y-i, event.x-i, event.y-i, fill=n, smooth=1, width=6)
		oval=c.create_line(x+i, y+i, event.x+i, event.y+i, fill=n, smooth=1, width=6)
	x,y=event.x, event.y

def circle_paint(event):
	global size
	global oval
	global l
	global m
	global n
	global count
	global x
	global y
	if count==0:
		x,y=event.x, event.y
		count+=1
		
	oval=c.create_oval(x,y, event.x, event.y, fill=n, outline=n, width=size//3)
	
	x,y=event.x, event.y

def erase(event):
	global size
	global oval
	global l
	global m
	global n
	global count
	global x
	global y
	if count==0:
		x,y=event.x, event.y
		count+=1
		
	new_oval=c.create_line(x,y, event.x, event.y, fill="white",  width=size, capstyle=ROUND)
	x,y=event.x, event.y
	

def paint_off(event):
	global x
	global y
	global count
	x,y,count=0,0,0


def eraserbutton():
	
	r.bind('<B1-Motion>', erase)
	
def twodbutton():
	r.bind('<B1-Motion>', twoD_paint)

def threedbutton():
	
	r.bind('<B1-Motion>', threeD_paint)
	
	
def circlepaintbutton():
	
	r.bind('<B1-Motion>', circle_paint)


change= Menu(r)
red=Menu(change, tearoff=0)
red.add_command(label="red", command=lambda:color("red"))
red.add_command(label="green", command=lambda:color("green"))
red.add_command(label="blue", command=lambda:color("blue"))
red.add_command(label="yellow", command=lambda:color("yellow"))
red.add_command(label="black", command=lambda:color("black"))
red.add_command(label="white", command=lambda:color("white"))
red.add_command(label="aquamarine", command=lambda:color("aquamarine"))
red.add_command(label="magenta", command=lambda:color("magenta"))

change.add_cascade(label="change", menu=red)
change.add_separator()
pen=Menu(change)
pen.add_command(label="2D pen", command=twodbutton)
pen.add_command(label="3d pen",  command=threedbutton)
pen.add_command(label="circle design", command=circlepaintbutton)
change.add_cascade(label="pen", menu=pen)


change.add_command(label="eraser", command=eraserbutton)
pensize= Menu(change)
pensize.add_command(label="1", command=lambda:siz(1))
pensize.add_command(label="2", command=lambda:siz(2))
pensize.add_command(label="3", command=lambda:siz(3))
pensize.add_command(label="4", command=lambda:siz(4))
pensize.add_command(label="5", command=lambda:siz(5))
pensize.add_command(label="6", command=lambda:siz(6))
pensize.add_command(label="7", command=lambda:siz(7))
pensize.add_command(label="8", command=lambda:siz(8))
pensize.add_command(label="9", command=lambda:siz(9))

pensize.add_command(label="10", command=lambda:siz(10))
pensize.add_command(label="11", command=lambda:siz(11))
pensize.add_command(label="12", command=lambda:siz(12))
pensize.add_command(label="13", command=lambda:siz(13))
pensize.add_command(label="14", command=lambda:siz(14))
pensize.add_command(label="15", command=lambda:siz(15))
pensize.add_command(label="16", command=lambda:siz(16))
pensize.add_command(label="17", command=lambda:siz(17))

pensize.add_command(label="18", command=lambda:siz(18))
pensize.add_command(label="19", command=lambda:siz(19))

pensize.add_command(label="20", command=lambda:siz(20))
pensize.add_command(label="21", command=lambda:siz(21))
pensize.add_command(label="22", command=lambda:siz(22))
pensize.add_command(label="23", command=lambda:siz(23))

change.add_cascade(label="size", menu=pensize)





r.config(menu=change)

r.bind('<ButtonRelease>', paint_off)
mainloop()
