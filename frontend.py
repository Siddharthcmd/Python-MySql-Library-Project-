from backend import viewData
import backend
from tkinter import ttk
from tkinter import *


def selectRow(Event):
    global sid
    index = list1.curselection()
    sid = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, sid[0])
    e2.delete(0, END)
    e2.insert(END, sid[1])
    e3.delete(0, END)
    e3.insert(END, sid[2])
    e4.delete(0, END)
    e4.insert(END, sid[3])
    e5.delete(0, END)
    e5.insert(END, sid[4])
    e6.delete(0, END)
    e6.insert(END, sid[5])


def viewBook():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def searchBook():
    list1.delete(0, END)
    for row in backend.search(bookId_txt.get(), title_txt.get(), author_txt.get(), year_txt.get(), publisher_txt.get()):
        list1.insert(END, row)


def addBook():
    backend.insert(bookId_txt.get(), title_txt.get(), author_txt.get(),
                   year_txt.get(), publisher_txt.get(), quantity_txt.get())
    list1.delete(0, END)
    list1.insert(END, (bookId_txt.get(), title_txt.get(), author_txt.get(),
                       year_txt.get(), publisher_txt.get(), quantity_txt.get()))


def deleteBook():
    backend.delete(sid[0])
    viewBook()


def updateBook():
    backend.update(bookId_txt.get(), title_txt.get(), author_txt.get(),
                   year_txt.get(), publisher_txt.get(), quantity_txt.get())
    viewBook()


window = Tk()


l1 = Label(window, text="bookId")
l1.grid(row=0, column=0)
l2 = Label(window, text="Title")
l2.grid(row=0, column=2)
l3 = Label(window, text="Author")
l3.grid(row=0, column=4)
l4 = Label(window, text="Year")
l4.grid(row=1, column=0)
l5 = Label(window, text="Publisher")
l5.grid(row=1, column=2)
l6 = Label(window, text="Quantity")
l6.grid(row=1, column=4)


bookId_txt = StringVar()
e1 = Entry(window, textvariable=bookId_txt)
e1.grid(row=0, column=1)
title_txt = StringVar()
e2 = Entry(window, textvariable=title_txt)
e2.grid(row=0, column=3)
author_txt = StringVar()
e3 = Entry(window, textvariable=author_txt)
e3.grid(row=0, column=5)
year_txt = StringVar()
e4 = Entry(window, textvariable=year_txt)
e4.grid(row=1, column=1)
publisher_txt = StringVar()
e5 = Entry(window, textvariable=publisher_txt)
e5.grid(row=1, column=3)
quantity_txt = StringVar()
e6 = Entry(window, textvariable=quantity_txt)
e6.grid(row=1, column=5)

list1 = Listbox(window, height=10, width=45)
list1.grid(row=5, column=0, rowspan=6, columnspan=2)

list1.bind('<<ListboxSelect>>', selectRow)

sb1 = Scrollbar(window)
sb1.grid(row=4, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = ttk.Button(window, text="View All Books",
                width=12, command=viewBook)
b1.grid(row=3, column=0)
b2 = ttk.Button(window, text="Search Entry", width=12, command=searchBook)
b2.grid(row=3, column=1)
b3 = ttk.Button(window, text="Add Entry", width=12, command=addBook)
b3.grid(row=3, column=2)
b4 = ttk.Button(window, text="Update Selected", width=12, command=updateBook)
b4.grid(row=3, column=3)
b5 = ttk.Button(window, text="Delete Selected", width=12, command=deleteBook)
b5.grid(row=3, column=4)
b6 = ttk.Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=3, column=5)


"---------------------------------BOOK issue----------------------------------"


def selectRow1(Event):
    global sidd
    index1 = list2.curselection()
    sidd = list2.get(index1)
    e7.delete(0, END)
    e7.insert(END, sidd[0])
    e8.delete(0, END)
    e8.insert(END, sidd[1])


def viewData():
    list2.delete(0, END)
    for row in backend.viewData():
        list2.insert(END, row)


def issueBook():
    backend.insertIssue(card_number.get(),
                        borrower_name.get(), bookId_txt.get())
    list2.delete(0, END)
    list2.insert(
        END, (card_number.get(), borrower_name.get(), bookId_txt.get()))
    updateIsBook()


def returnBook():
    backend.deleteIssueBook(sidd[0], sidd[2])
    viewData()
    viewBook()


def updateIsBook():
    backend.updateIssueBook(bookId_txt.get(), quantity_txt.get())
    viewBook()


l7 = Label(window, text="Card Number")
l7.grid(row=6, column=3)
l8 = Label(window, text="Borrower Name")
l8.grid(row=7, column=3)


card_number = StringVar()
e7 = Entry(window, textvariable=card_number)
e7.grid(row=6, column=4)
borrower_name = StringVar()
e8 = Entry(window, textvariable=borrower_name)
e8.grid(row=7, column=4)

list2 = Listbox(window, height=10, width=55)
list2.grid(row=9, column=3, rowspan=6, columnspan=2)

list2.bind('<<ListboxSelect>>', selectRow1)

sb2 = Scrollbar(window)
sb2.grid(row=9, column=5, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b7 = ttk.Button(window, text="View Data", width=12, command=viewData)
b7.grid(row=8, column=3)
b8 = ttk.Button(window, text="Issue Book", width=12, command=issueBook)
b8.grid(row=8, column=4)
b9 = ttk.Button(window, text="Return Book", width=12, command=returnBook)
b9.grid(row=8, column=5)

window.mainloop()
