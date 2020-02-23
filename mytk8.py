from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
root = Tk()
root.title("This is Devansh Gui")

var = IntVar()
c = Checkbutton(root,text = "Check this box",variable = var).pack()
 myLabel = Label(root,text = var.get()).pack()

root.mainloop()
