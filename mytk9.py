from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
var = StringVar()

c = Checkbutton(root,text ="Devansh",variable = var, onvalue = "On",offvalue = "Off")
c.deselect()
c.pack()
def clicked():

    mylabel = Label(root,text =  var.get()).pack()

mybutton = Button(root,text = "click",command = clicked).pack()

root.mainloop()
