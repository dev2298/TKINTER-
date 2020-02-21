from tkinter import *
root =Tk()
def myclick():
    label1 = Label(root,text = "This is Me Devansh")
    label1.pack()
button1 = Button(root,text = " Click Me",padx = 80,pady = 100,command = myclick)

button1.pack()

root.mainloop()
