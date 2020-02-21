from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("DEVANSH SRIVASTAVA")

my_img1 = ImageTk.PhotoImage(Image.open("dev1.png"))

my_img2 = ImageTk.PhotoImage(Image.open("dev2.png"))

my_img3 = ImageTk.PhotoImage(Image.open("dev3.png"))

image_list = [my_img1, my_img2, my_img3]
status = Label(root,text = "Image 1 of " + str(len(image_list)),anchor = E)
my_label = Label(image = my_img1)
my_label.grid(row = 0,column = 0 , columnspan = 3)

def forward(img) :
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[img-1])
    button_back = Button(root,text = "<<",command =  lambda : back(img-1))
    button_forward = Button(root,text = ">>",command = lambda : forward(img+1) )
    my_label.grid(row = 0,column = 0 , columnspan = 3)
    status = Label(root,text = "Image"+str(img)+"of " + str(len(image_list)),anchor = E)
    status.grid(row = 2 , column = 1,columnspan=3,sticky = W+E)
    button_back.grid(row = 1,column = 0)
    button_forward.grid(row = 1,column = 2)


def back(img) :
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[img-1])
    button_back = Button(root,text = "<<",command =  lambda : back(img-1))
    button_forward = Button(root,text = ">>",command = lambda : forward(img+1) )
    my_label.grid(row = 0,column = 0 , columnspan = 3)
    status = Label(root,text = "Image"+str(img)+"of " + str(len(image_list)),anchor = E)
    status.grid(row = 2 , column = 1,columnspan=3,sticky = W+E)
    button_back.grid(row = 1,column = 0)
    button_forward.grid(row = 1,column = 2)


button_back = Button(root,text = "<<",command =  back,state = DISABLED)
button_forward = Button(root,text = ">>",command = lambda : forward(2) )
button_exit = Button(root,command = root.quit , text = "EXIT")

button_back.grid(row = 1,column = 0)
button_forward.grid(row = 1,column = 2)
button_exit.grid(row = 1,column = 1)
status.grid(row = 2 , column = 1,columnspan=3,sticky = W+E)
root.mainloop()
