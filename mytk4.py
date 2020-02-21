from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("FRAME BY DEVANSH SRIVASTAVA")

frame = LabelFrame(root , text = "This is my Frame.....", padx = 50 , pady = 50  )
frame.pack(padx=10,pady = 10)
b = Button(frame,text = "Don't Click Here!")
b2 = Button(frame,text = "Don't Click Here!")
b.grid(row = 0,column = 2)
b2.grid(row=1,column = 1)

root.mainloop()
