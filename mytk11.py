from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Devansh")

#using databases
#create a database
conn = sqlite3.connect('address_book.db')
c = conn.cursor()


def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("INSERT INTO Devansh VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)",
        {
            'f_name' : f_name.get(),
            'l_name' : l_name.get(),
            'address' : address.get(),
            'city' : city.get(),
            'state' : state.get(),
            'zipcode' : zipcode.get()
        })
    conn.commit()
    conn.close()

    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("Select *,oid from Devansh")
    records = c.fetchall()
    print_records =  ''
    #print(records)
    for record in records :
        print_records += str(record[0])+" " + str(record[6]) + "\n"

    query_label = Label(root,text = print_records)
    query_label.grid(row=7,column = 0 , columnspan = 2)
    conn.commit()
    conn.close()

def update():
    editor = Tk()
    editor.title("Update Window")
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    rec = 1
    c.execute("Select *,oid from Devansh where oid = "+rec)
    records = c.fetchall()



    f_name_editor = Entry(editor, width = 30)
    f_name.grid(row=0,column = 1)
    l_name = Entry(editor, width = 30)
    l_name.grid(row=1,column = 1)
    address = Entry(editor, width = 30)
    address.grid(row=2,column = 1)
    city = Entry(editor, width = 30)
    city.grid(row=3,column = 1)
    state = Entry(editor, width = 30)
    state.grid(row=4,column = 1)
    zipcode = Entry(editor, width = 30)
    zipcode.grid(row=5,column = 1)

    f_name_label = Label(editor,text = "First Name")
    f_name_label.grid(row=0,column=0)
    l_name_label = Label(editor,text = "Last Name")
    l_name_label.grid(row=1,column=0)
    address_label = Label(editor,text = "Address")
    address_label.grid(row=2,column=0)
    city_label = Label(editor,text = "City")
    city_label.grid(row=3,column=0)
    state_label = Label(editor,text = "State")
    state_label.grid(row=4,column=0)
    zipcode_label = Label(editor,text = "Zipcode")
    zipcode_label.grid(row=5,column=0)


    for record in records:
        f_name_editor.insert(0,record[0])


    save = Button(editor,text = " Save Changes")
    save.grid(row = 6,column = 0,columnspan=2)







f_name = Entry(root, width = 30)
f_name.grid(row=0,column = 1)
l_name = Entry(root, width = 30)
l_name.grid(row=1,column = 1)
address = Entry(root, width = 30)
address.grid(row=2,column = 1)
city = Entry(root, width = 30)
city.grid(row=3,column = 1)
state = Entry(root, width = 30)
state.grid(row=4,column = 1)
zipcode = Entry(root, width = 30)
zipcode.grid(row=5,column = 1)

f_name_label = Label(root,text = "First Name")
f_name_label.grid(row=0,column=0)
l_name_label = Label(root,text = "Last Name")
l_name_label.grid(row=1,column=0)
address_label = Label(root,text = "Address")
address_label.grid(row=2,column=0)
city_label = Label(root,text = "City")
city_label.grid(row=3,column=0)
state_label = Label(root,text = "State")
state_label.grid(row=4,column=0)
zipcode_label = Label(root,text = "Zipcode")
zipcode_label.grid(row=5,column=0)

mybutton = Button(root,text = "Add Record to Database",command = submit)
mybutton.grid(row = 6,column = 0,columnspan =2,pady =10,ipadx = 100)
q = Button(root,text = "Query" , command = query)
q.grid(row = 7 , column = 0 , columnspan = 2 , pady = 10,padx = 10 ,ipadx = 137)
update_btn = Button(root,text = "Update" , command = update)
update_btn.grid(row = 12 , column = 0 , columnspan = 2 , pady = 10,padx = 10 ,ipadx = 137)

conn.commit()

conn.close()







root.mainloop()
