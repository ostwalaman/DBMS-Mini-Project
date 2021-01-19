# Importing Files
from re import error
from tkinter import *
import tkinter
from tkinter import Label, mainloop, messagebox
import pymysql

window = tkinter.Tk()
window.title("Student Information Management System (SIMS)")
window.geometry("1000x500")

L0 = Label(window, text = "Enter Student ID: ", font = ('arial', 30), fg = 'blue')
L0.grid(row = 0, column = 0)
E0 = Entry(window, bd = 5, width = 50)
E0.grid(row = 0, column = 1)

L1 = Label(window, text = "Enter Student Name: ", font = ('arial', 30), fg = 'blue')
L1.grid(row = 2, column = 0)
E1 = Entry(window, bd = 5, width = 50)
E1.grid(row = 2, column = 1)

L2 = Label(window, text = "Enter Student Branch: ", font = ('arial', 30), fg = 'blue')
L2.grid(row = 4, column = 0)
E2 = Entry(window, bd = 5, width = 50)
E2.grid(row = 4, column = 1)

L3 = Label(window, text = "Enter Student Roll No.: ", font = ('arial', 30), fg = 'blue')
L3.grid(row = 6, column = 0)
E3 = Entry(window, bd = 5, width = 50)
E3.grid(row = 6, column = 1)

G1 = Label(window, text = "(M - Male / F - Female)", font = ('arial', 30), fg = "blue")
G1.grid(row = 8, column = 0)
G1 = Entry(window, bd = 5, width = 50)
G1.grid(row = 8, column = 1)

def myButtonEvent(selection):
    print("Student ID is: ", E0.get())
    print("Student Name is: ", E1.get())
    print("Student Branch is: ", E2.get())
    print("Student Roll No. is: ", E3.get())
    print("Gender of Student is: ", G1.get())

    ID = E0.get()
    NAME = E1.get()
    BRANCH = E2.get()
    ROLL_NO = E3.get()
    GENDER = G1.get()

    if selection in ('Insert'):
        con = pymysql.connect(host = "localhost", user = "root", password = "password", db = "project") #Connect to MySQL - In password type your MySQL Passowrd
        cur = con.cursor() #Get the Cursor Object

        query = "create table if not exists student(ID char(5) primary key not null, NAME char(20), BRANCH char(20), ROLL_NO char(5), GENDER char(1))"
        try:
            cur.execute(query)
            con.commit()
            # print("Table Student Created Successfully!")
        except error as e:
            print("Error occured at Database Table Creation ", e)
            con.rollback()
            con.close()

        insQuery = "insert into student (ID, NAME, BRANCH, ROLL_NO, GENDER) values ('%s','%s','%s','%s','%s')" % (ID, NAME, BRANCH, ROLL_NO, GENDER)
        
        try:
            cur.execute(insQuery)
            con.commit()
            print("Query Inserted!\n")
            con.close()
        except error as e:
            print("Error occured at Database Insertion ", e)
            con.rollback()
            con.close()
    
    elif selection in ('Update'):
        try:
            updQuery = "update student set NAME = '%s'"%(NAME) + ", BRANCH = '%s'"%(BRANCH) + ", ROLL_NO = '%s'"%(ROLL_NO) + ", GENDER = '%s'"%(GENDER) + " where ID = '%s'"%(ID)
            
            con = pymysql.connect(host = "localhost", user = "root", password = "Jio@1234", db = "project") #Connect to MySQL
            cur = con.cursor() #Get the Cursor Object
            cur.execute(updQuery)
            con.commit()
            con.close()
            print("Update Success!\n",)
        except error as e:
            print("Error occured at Database Updation ", e)
            con.rollback()
            con.close()
    
    elif selection in ('Delete'):
        try:
            delQuery = "delete from student where ID = '%s'"%(ID)
            
            con = pymysql.connect(host = "localhost", user = "root", password = "Jio@1234", db = "project") #Connect to MySQL
            cur = con.cursor() #Get the Cursor Object
            cur.execute(delQuery)
            con.commit()
            con.close()
            print("Delete Success!\n",)
        except error as e:
            print("Error occured at Database Deletion ", e)
            con.rollback()
            con.close()

    elif selection in ('Select'):
        try:
            selQuery = "select * from student where ID = '%s'"%(ID)
            
            con = pymysql.connect(host = "localhost", user = "root", password = "Jio@1234", db = "project") #Connect to MySQL
            cur = con.cursor() #Get the Cursor Object
            cur.execute(selQuery)
            rows = cur.fetchall()
            ID1 = ''
            NAME1 = ''
            BRANCH1 = ''
            ROLL_NO1 = ''
            GENDER1 = ''
            
            for row in rows:
                ID1 = row[0]
                NAME1 = row[1]
                BRANCH1 = row[2]
                ROLL_NO1 = row[3]
                GENDER1 = row[4]

            E0.delete(0, END)
            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)
            G1.delete(0, END)

            E0.insert(0, ID1)
            E1.insert(0, NAME1)
            E2.insert(0, BRANCH1)
            E3.insert(0, ROLL_NO1)
            G1.insert(0, GENDER1)

            con.close()
            print("Select Success!\n",)
        except error as e:
            print("Error occured at Database Selection ", e)
            con.rollback()
            con.close()

BInsert = tkinter.Button(text = 'Insert', fg = 'Green', font = ('arial', 30, 'bold'), command = lambda:myButtonEvent('Insert'))
BInsert.grid(row = 12, column = 0)

BUpdate = tkinter.Button(text = 'Update', fg = 'Blue', font = ('arial', 30,  'bold'), command = lambda:myButtonEvent('Update'))
BUpdate.grid(row = 12, column = 1)

BDelete = tkinter.Button(text = 'Delete', fg = 'Red', font = ('arial', 30, 'bold'), command = lambda:myButtonEvent('Delete'))
BDelete.grid(row = 20, column = 0)

BSelect = tkinter.Button(text = 'Select', fg = 'Orange', font = ('arial', 30,  'bold'), command = lambda:myButtonEvent('Select'))
BSelect.grid(row = 20, column = 1)

mainloop()
