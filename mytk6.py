from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("MessageBox BY DEVANSH SRIVASTAVA")

#show(info,warning,error) ,ask(question,yes/no,okcancel)

def popup():
    r = messagebox.askokcancel("This is my popup","This is Devansh")
    Label(root , text = r).pack()


Button(root ,  text = "Popup" , command = popup).pack()




root.mainloop()
