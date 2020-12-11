import pymysql
from tkinter import *
from tkinter import messagebox 

def errorMessage():  
    root = Tk() 
    root.withdraw()
    messagebox.showwarning("Unknow Publisher",
    """Publisher name not yet added in\nthe publisher data.
    Go to: View->Publisher->Add Publisher""")
    root.destroy()
    root.mainloop()

def connect():
    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="MainLibraryDatabase")
    mydb.close()


#--------------------------------------Publilsher Details--------------------------------------

def insertPublisherData(name,number,address):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    insertPublisher = "insert into PUBLISHER values('"+name+"','"+number+"','" +address+"')"
    cur.execute(insertPublisher)
    mydb.commit()
    mydb.close()


def viewPublisherData():
    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    viewPublisher = "select * from PUBLISHER"
    cur.execute(viewPublisher)
    row = cur.fetchall()
    mydb.close()
    return row














"--------------------------------------add book details---------------------------------------"


def insert(id, title, author, year, publisher):

    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    insertBooks = "insert into Book values('"+id+"','"+title+"','" + \
        author+"','" + publisher+"','"+year+"')"
    
    try:
        cur.execute(insertBooks)
    except:
        errorMessage()
    
    mydb.commit()
    mydb.close()


def view():
    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    cur.execute("select * from books")
    rows = cur.fetchall()
    mydb.close()
    return rows


def search(id="", title="", author="", year="", publisher=""):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    searchBook = ("select * from books where id = '"+id+"' or title = '"+title +
                  "' or author = '"+author+"' or year = '"+year+
                  "' or publisher = '"+publisher+"'")
    cur.execute(searchBook)
    row = cur.fetchall()
    mydb.close()
    return row


def delete(id):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    deleteBook = ("delete from Book where id = '"+str(id)+"'")
    cur.execute(deleteBook)
    mydb.commit()
    mydb.close()


def update(id, title, author, year, publisher, quantity):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    updateBook = ("update books set title = '"+title+"', author = '" +
                  author+"' , year = '"+year+"' , publisher = '"+
                  publisher+"' , quantity = '"+quantity+"' where id='"+id+"'")
    cur.execute(updateBook)
    mydb.commit()
    mydb.close()


"--------------------------------------BOOK ISSUE---------------------------------------"


def viewData():
    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    cur.execute("select * from issueBooks")
    rows = cur.fetchall()
    mydb.close()
    return rows


def insertIssue(cardNumber, borrowerName, id):

    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    insertdata = "insert into issueBooks values('" + \
        cardNumber + "','"+borrowerName+"','"+id+"')"
    cur.execute(insertdata)
    mydb.commit()
    mydb.close()


def updateIssueBook(id, quantity):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    updateBook = ("update books set quantity = '" +
                  str(int(quantity)-1)+"' where id='"+str(id)+"'")
    cur.execute(updateBook)
    mydb.commit()
    mydb.close()


def deleteIssueBook(cardNumber, id):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="MainLibraryDatabase")
    cur = mydb.cursor()

    # to obtain book quantity from books table
    showData1 = ("select quantity from books where id = '" +
                 str(id)+"'")
    cur.execute(showData1)          # ((2),)
    row1 = cur.fetchall()
    bookQuantity = (row1[0][0])
    bookQuantity += 1

    deleteBook = ("delete from issuebooks where cardNumber = '" +
                  str(cardNumber)+"'")
    updateBook = ("update books set quantity = '" +
                  str(bookQuantity) + "' where id='"+str(id)+"'")
    cur.execute(updateBook)
    cur.execute(deleteBook)
    mydb.commit()
    mydb.close()


connect()
