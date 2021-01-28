import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import datetime
from datetime import timedelta, date,datetime
def connect():
    mydb = pymysql.connect(
        host="localhost",   
        user="root", 
        password="test123", 
        database="MainLibraryDatabase")
    mydb.close()

#--------------------------------------Book copies--------------------------------------

def LiBBranch():    


    def addDetail():
        
        mydb = pymysql.connect(host="localhost",
                        user="root", password="test123", database="MainLibraryDatabase")
        cur = mydb.cursor()
        add = "insert into BOOK_COPIES values('"+e1.get()+"','"+e2.get()+"','"+e3.get()+"')"
        cur.execute(add)
        mydb.commit()
        mydb.close()
        list1.delete(0, END)
        list1.insert(END, (e1.get(),e2.get(),e3.get())) 
        
    def viewBook():
        mydb = pymysql.connect(host="localhost",
                        user="root", password="test123", database="MainLibraryDatabase")
        cur = mydb.cursor()
        view = "select * from BOOK_COPIES"
        cur.execute(view)
        rows=cur.fetchall()
        mydb.close()
        list1.delete(0,END)
        for row in rows:
            list1.insert(END, row)
    def quit_me():
        print('quit')
        window.quit()
        window.destroy()  
    window = Tk()
    window.protocol("WM_DELETE_WINDOW", quit_me)
    l1 = Label(window, text="Quantity")
    l1.grid(row=0, column=0)
    l2 = Label(window, text="Book ID")
    l2.grid(row=0, column=2)
    l3 = Label(window, text="Branch ID")
    l3.grid(row=0, column=4)
    
    qquantity_txt = StringVar()
    e1 = Entry(window, textvariable=qquantity_txt, fg='blue')
    e1.grid(row=0, column=1) 
    qbookId_txt = StringVar()
    e2 = Entry(window, textvariable=qbookId_txt, fg='blue')
    e2.grid(row=0, column=3)
    qbranchid_txt = StringVar()
    e3 = Entry(window, textvariable=qbranchid_txt, fg='blue')
    e3.grid(row=0, column=5)    
    
    list1 = Listbox(window, height=10, width=45)
    list1.grid(row=1, column=1, rowspan=6, columnspan=3)
    
    b1 = ttk.Button(window, text="View data",
                    width=12, command=viewBook)
    b1.grid(row=1, column=5)
    b2 = ttk.Button(window, text="Add Entry", width=12, command=addDetail)
    b2.grid(row=2,column=5)
    b3 = ttk.Button(window, text="Done", width=12, command=quit_me)
    b3.grid(row=3,column=5)   
    
    window.mainloop()   

#--------------------------------------error Block--------------------------------------

def errorMessage(error):
    if(error==1):
        messagebox.showerror("Depulicate entry",
        "this book is already been added")
        
        MsgBox = messagebox.askquestion ('Add Book Quantity',
        'Do you want to add book copies in another branch',icon = 'warning')
        if MsgBox == 'yes':
            LiBBranch()
        else:
            messagebox.showinfo('Return','You will now return to the application screen')
    elif(error==2):    
        messagebox.showwarning("Unknow Publisher",
        """Publisher name not yet added in\nthe publisher data.
        Go to: View->Publisher->Add Publisher""")
    elif(error==3):
        messagebox.showerror("Book not available","This book is not available")
    elif(error==4):
        messagebox.showerror("Already issued","This book from your branch id is already been issued to this card holder")

#--------------------------------------Publilsher Details--------------------------------------

def insertPublisherData(name,number,address):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="test123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    insertPublisher = "insert into PUBLISHER values('"+name+"','"+number+"','" +address+"')"
    cur.execute(insertPublisher)
    mydb.commit()
    mydb.close()


def viewPublisherData():
    mydb = pymysql.connect(host="localhost",
                           user="root", password="test123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    viewPublisher = "select * from PUBLISHER"
    cur.execute(viewPublisher)
    row = cur.fetchall()
    mydb.close()
    return row

def deletePublisherData(name):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="test123", database="MainLibraryDatabase")
    cur = mydb.cursor()    
    deletePublisher="delete from PUBLISHER where NAME ='"+name+"'"
    cur.execute(deletePublisher)
    mydb.commit()
    mydb.close()    

#--------------------------------------Branch Details--------------------------------------

def insertBranchData(id,name,address):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="test123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    insertBranch = "insert into LibraryBranch values('"+id+"','"+name+"','" +address+"')"
    cur.execute(insertBranch)
    mydb.commit()
    mydb.close()


def viewBranchData():
    mydb = pymysql.connect(host="localhost",
                           user="root", password="test123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    viewBranch = "select * from LibraryBranch"
    cur.execute(viewBranch)
    row = cur.fetchall()
    mydb.close()
    return row

def deleteBranchData(id):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="test123", database="MainLibraryDatabase")
    cur = mydb.cursor()    
    deletePublisher="delete from LibraryBranch where branchId ='"+str(id)+"'"
    cur.execute(deletePublisher)
    mydb.commit()
    mydb.close()    

"--------------------------------------add book details---------------------------------------"


def insert(Branch_id,id, title, author, year, publisher,quantity):

    mydb = pymysql.connect(host="localhost",
                           user="root", password="test123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    insertBooks = "insert into Book values('"+id+"','"+title+"','" + \
        author+"','" + publisher+"','"+year+"')"
    insertBookCopies= "insert into BOOK_COPIES values('"+str(quantity)+"','"+str(id)+"','"+ \
        str(Branch_id)+"')"    
    try:
        cur.execute(insertBooks)
        cur.execute(insertBookCopies)
        mydb.commit()
        mydb.close()
        return True
    except pymysql.err.IntegrityError as e:
        if(e.args[0]==1062): 
            mydb.commit()
            mydb.close()        
            errorMessage(1)
            return False
        elif(e.args[0]==1452):
            mydb.commit()
            mydb.close()  
            errorMessage(2)
            return False
    


def view(bID):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="test123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    if bID == "books":
        cur.execute("select * from Book")
        rows=cur.fetchall()
    elif bID == "all":
        cur.execute("select Book.*,branchID,NoOfCopies from BOOK,BOOK_COPIES where Book.book_id=BOOK_COPIES.bookId")
        rows = cur.fetchall()
    else:
        cur.execute("select Book.*,branchId,NoOfCopies from BOOK,BOOK_COPIES where branchID ='" +str(bID)+"'  and Book.book_id=BOOK_COPIES.bookId")
        rows = cur.fetchall()
    mydb.close()
    return rows


def search(id="", title="", author="", year="", publisher=""):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="test123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    searchBook = ("select * from Book where book_id = '"+id+"' or title = '"+title +
                  "' or author = '"+author+"' or publisher = '"+publisher+
                  "' or year_of_publish = '"+year+"'")
    cur.execute(searchBook)
    row = cur.fetchall()
    mydb.close()
    return row


def delete(id):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="test123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    deleteBook = ("delete from Book where book_id = '"+str(id)+"'")
    cur.execute(deleteBook)
    mydb.commit()
    mydb.close()


def update(branhid, id, title, author, year, publisher, quantity):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="test123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    updateBook = ("update Book set TITLE = '"+title+"', AUTHOR = '" +
                  author+"' , PUBLISHER = '"+publisher+"' , year_of_publish = '"+
                  year+"' where book_id = '"+str(id)+"'") 
    cur.execute(updateBook)
    mydb.commit()
    mydb.close()
 

"--------------------------------------BOOK ISSUE---------------------------------------"


def viewData():
    mydb = pymysql.connect(host="localhost",
                           user="root", password="test123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    cur.execute("select * from BOOK_LENDING")
    rows = cur.fetchall()
    mydb.close()
    return rows

def searchCards(cardNo):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="test123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    searchcard = ("select * from BOOK_LENDING where CARD_NO  = '"+cardNo+"'")
    cur.execute(searchcard)
    row = cur.fetchall()
    mydb.close()
    return row


def insertIssue(dateo,ddate,bookId,branchId,cardNumber):

    mydb = pymysql.connect(host="localhost",
                           user="root", password="test123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    try:
        insertdata = "insert into BOOK_LENDING values('" + \
            str(dateo) + "','"+str(ddate)+"','"+str(bookId)+"','"+str(branchId)+"','"+str(cardNumber)+"')"
        cur.execute(insertdata)
    except pymysql.err.IntegrityError as e:
        if(e.args[0]==1062):
            errorMessage(4)
    mydb.commit()
    mydb.close()


def deleteIssueBook(dateout,BId,BraId,cardNumber):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="test123", database="MainLibraryDatabase")
    cur = mydb.cursor()
    datein=date.today()
    calcFine = ("call fine('"+str(datein)+"','"+str(dateout)+"')")
    cur.execute(calcFine)
    fine=cur.fetchall()
    deleteBook = ("delete from BOOK_LENDING where CARD_NO = '" +
                  str(cardNumber)+"'and BOOK_ID = '" +
                  str(BId)+"' and BRANCH_ID = '" +
                  str(BraId)+"'")
    cur.execute(deleteBook)
    mydb.commit()
    mydb.close()
    #fine=((30,),) [1,2,3]
    #((30,),)
    return fine[0][0]


connect()
