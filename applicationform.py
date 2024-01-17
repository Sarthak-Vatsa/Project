from tkinter import *
from tkinter import messagebox

master=Tk()
master.title("Student details")

Label(master,text="Enter Name").grid(row=0)
name=Entry(master).grid(row=0,column=1)

tkvar=StringVar()

class_=["I",'II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']
tkvar.set("Choose class")

OptionMenu(master,tkvar,*class_).grid(row=1)

Label(master,text="Enter marks").grid(row=2,column=0)
marks=Entry(master).grid(row=2,column=1)#grid(row=2,column=1)

Radiobutton(master,text='Male',value=1).grid(row=3,column=1)
Radiobutton(master,text='Female',value=2).grid(row=3,column=2)
Radiobutton(master,text='Other',value=3).grid(row=3,column=3)

Checkbutton(master,text='A').grid(row=4,column=0)
Label(master,text='Age').grid(row=4,column=1)
Spinbox(master,from_=15,to=22).grid(row=4,column=2)
#Scale(master,from_=10,to=25,orient=HORIZONTAL).grid(row=4,column=0) #text does not work with scale

Button(master,text='Submit',command=master.destroy).grid(row=5)
master.mainloop()