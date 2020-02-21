from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root,width = 50 ,borderwidth = 5)
e.grid(row = 0 , column = 0 ,columnspan = 3)

def add1(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def clearr():
    e.delete(0,END)

def plusa() :
    n1 = e.get()
    global number1
    number1 = int(n1)
    e.delete(0,END)


def equal2() :
    number2 = e.get()
    e.delete(0,END)
    e.insert(0, number1 + int(number2  ))

button1 = Button(root,text = " 1",padx = 40,pady = 20, command = lambda : add1(1) )
button2 = Button(root,text = " 2",padx = 40,pady = 20, command = lambda : add1(2))
button3 = Button(root,text = " 3",padx = 40,pady = 20, command = lambda : add1(3))
button4 = Button(root,text = " 4",padx = 40,pady = 20, command = lambda : add1(4))
button5 = Button(root,text = " 5",padx = 40,pady = 20, command = lambda : add1(5))
button6 = Button(root,text = " 6",padx = 40,pady = 20,command = lambda : add1(6))
button7 = Button(root,text = " 7",padx = 40,pady = 20,command = lambda : add1(7))
button8 = Button(root,text = " 8",padx = 40,pady = 20,command = lambda : add1(8))
button9 = Button(root,text = " 9",padx = 40,pady = 20,command = lambda : add1(9))
button10 = Button(root,text = " 0",padx = 40,pady = 20,command = lambda : add1(10))
button11= Button(root,text = "+",padx = 40,pady = 20,command = plusa)
button12= Button(root,text = "clear",padx = 40,pady = 20,command = clearr)
button13 = Button(root,text = " = ",padx = 40,pady = 20,command = equal2)


button1.grid(row=1 ,column=0 )
button2.grid(row = 1 ,column = 1 )
button3.grid(row = 1 ,column = 2)

button4.grid(row =  2,column = 0)
button5.grid(row = 2 ,column = 1)
button6.grid(row = 2 ,column = 2)

button7.grid(row = 3 ,column = 0 )
button8.grid(row = 3 ,column = 1)
button9.grid(row = 3 ,column = 2)

button10.grid(row = 4 ,column = 1)
button11.grid(row = 4 , column = 0)
button13.grid(row = 4 , column = 2)
button12.grid(row = 5 , columnspan = 3 )

root.mainloop()
