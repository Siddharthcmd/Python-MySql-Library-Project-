import pymysql

def connect():
    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="sidd")
    mydb.close()


def insert(id, title, author, year, publisher, quantity):

    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="sidd")
    cur = mydb.cursor()
    insertBooks = "insert into books values('"+id + "','"+title+"','" + \
        author+"','" + year+"','"+publisher+"', '"+quantity+"')"
    cur.execute(insertBooks)
    mydb.commit()
    mydb.close()


def view():
    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="sidd")
    cur = mydb.cursor()
    cur.execute("select * from books")
    rows = cur.fetchall()
    mydb.close()
    return rows


def search(id="", title="", author="", year="", publisher=""):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="sidd")
    cur = mydb.cursor()
    searchBook = ("select * from books where id = '"+id+"' or title = '"+title +
                  "' or author = '"+author+"' or year = '"+year+
                  "' or publiser = '"+publisher+"'")
    cur.execute(searchBook)
    row = cur.fetchall()
    mydb.close()
    return row


def delete(id):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="sidd")
    cur = mydb.cursor()
    deleteBook = ("delete from books where id = '"+str(id)+"'")
    cur.execute(deleteBook)
    mydb.commit()
    mydb.close()


def update(id, title, author, year, publisher, quantity):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="sidd")
    cur = mydb.cursor()
    updateBook = ("update books set title = '"+title+"', author = '" +
                  author+"' , year = '"+year+"' , publiser = '"+
                  publisher+"' , quantity = '"+quantity+"' where id='"+id+"'")
    cur.execute(updateBook)
    mydb.commit()
    mydb.close()


"--------------------------------------BOOK ISSUE---------------------------------------"


def viewData():
    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="sidd")
    cur = mydb.cursor()
    cur.execute("select * from issueBooks")
    rows = cur.fetchall()
    mydb.close()
    return rows


def insertIssue(cardNumber, borrowerName, id):

    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="sidd")
    cur = mydb.cursor()
    insertdata = "insert into issueBooks values('" + \
        cardNumber + "','"+borrowerName+"','"+id+"')"
    cur.execute(insertdata)
    mydb.commit()
    mydb.close()


def updateIssueBook(id, quantity):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="sidd")
    cur = mydb.cursor()
    updateBook = ("update books set quantity = '" +
                  str(int(quantity)-1)+"' where id='"+str(id)+"'")
    cur.execute(updateBook)
    mydb.commit()
    mydb.close()


def deleteIssueBook(cardNumber, id):
    mydb = pymysql.connect(host="localhost",
                           user="root", password="misraa123", database="sidd")
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
