import sys
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename

path = None
root= Tk()

def savefileas():
	global text1
	global text2
	global path
	t = text2.get("1.0", "end-1c")
	savelocation = asksaveasfilename()
	file = open(savelocation, 'w+')
	path = file.name
	file.write(t)
	file.close()
	text1.delete(0.0, END)
	text1.insert(END, path.split('/')[-1])

def savefile():
    t = text2.get("1.0", "end-1c")
    t1 = text1.get("1.0", "end-1c")
    file1 = open(path, 'w+')
    file1.write(t)
    file1.close()

def openfile():
	global path
	global text1
	global text2
	openlocation = askopenfilename(initialdir= "/home/")
	file2 = open(openlocation, 'r+')
	t2 = file2.read()
	text2.delete(0.0, END)
	text2.insert(0.0, t2)
	path= file2.name
	text1.delete(0.0, END)
	text1.insert(END, path.split('/')[-1])
	file2.close()

def newfile():
	text1.delete(0.0, "end-1c")
	text1.insert(END, "Untitled")
	text2.delete(0.0, "end-1c")

def FontHelvertica():
	global text2
	text2.config(font= 'Helvertica')
def FontCourier():
	global text2
	text2.config(font= 'Courier')
def FontTimes():
	global text2
	text2.config(font= 'Times')
def FontArial():
	global text2
	text2.config(font= 'Arial')

root.title("DetOrk Text Editor")
root.minsize(width=400, height=400)

text1= Text(root, height=1, width=20)
text1.pack()
text1.insert(END, "Untitled")

text2 = Text(root)
text2.pack(side= LEFT, expand= True, fill= 'both')

b1= Button(root, text = "New", command= newfile)
b1.pack()
b2= Button(root, text = "Open", command= openfile)
b2.pack()
b3= Button(root, text = "Save", command= savefile)
b3.pack()
b4= Button(root, text = "SaveAs", command= savefileas)
b4.pack()

font = Menubutton(root, text= "Font", relief= RAISED)
font.pack()

font.menu  =  Menu ( font, tearoff = 0 )
font["menu"]  =  font.menu

Helvertica= IntVar()
Courier= IntVar()
Times= IntVar()
Arial= IntVar()

font.menu.add_checkbutton(label= "Helvertica", variable= Helvertica, command= FontHelvertica)
font.menu.add_checkbutton(label= "Courier", variable= Courier, command= FontCourier)
font.menu.add_checkbutton(label= "Times", variable= Times, command= FontTimes)
font.menu.add_checkbutton(label= "Arial", variable= Arial, command= FontArial)

b5= Button(root, text = "Exit", command= root.quit)
b5.pack()

root.mainloop()