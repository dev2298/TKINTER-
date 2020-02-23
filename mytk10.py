from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Devansh")
def click():
    mylabel = Label(root,text = clicked.get()).pack()


clicked = StringVar()
clicked.set("Monday")
drop = OptionMenu(root,clicked,"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
drop.pack()

mybutton = Button(root,text = "Selected dAY",command = click).pack()






root.mainloop()
