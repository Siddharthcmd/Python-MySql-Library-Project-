import tkinter
from tkinter import *
from tkinter import ttk

def branchWindow():

    window = Tk()

    l1 = Label(window, text="Branch Id").grid(row=0,column=0)
    l2 = Label(window, text="Name").grid(row=0,column=3)
    l3 = Label(window, text="Address").grid(row=0,column=5)

    e1 = Entry(window).grid(row=0,column=1)
    e2 = Entry(window).grid(row=0,column=4)
    e3 = Entry(window).grid(row=0,column=6)

    list1 = Listbox(window, height=10, width=45)
    list1.grid(row=1, column=2, rowspan=6, columnspan=2)
    
    window.mainloop()