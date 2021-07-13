#
# Python Ver: 3.9.5
#
# Author:       Andrew Lorenz
#
# Purpose:      Simple Student Tracking App. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:    This code was written and tested wo work with Windows 10.

import os
# use of wildcard imports discouraged unless you want to import everything
#from tkinter import *
from tkinter import messagebox

import tkinter as tk
import sqlite3

# import our other modules
# so we can have access to them
import student_main
import student_gui


def center_window(self, w, h): # pass in the tkinter frame (master) reference and the v and h
    '''Center the application window on the user's screen'''
    
    # get User's screen width and height
    screen_width = self.master.winfo_screenwidth() # get user's width and height
    screen_height = self.master.winfo_screenheight() # and height
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def ask_quit(self):
    '''Catch if the user clicks on the windows upper-right 'X' to ensure they want to close'''
    
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes the app
        self.master.destroy()
        os._exit(0)

def create_db(self):
    '''Create the school db and student table if they don't exist'''
    
    conn = sqlite3.connect('school.db')
    with conn:
        cur = conn.cursor()
        # SQLite3 handles autoincrement for us of the ID (see insert statement in onAdd func
        cur.execute("CREATE TABLE if not exists student( \
            ID INTEGER PRIMARY KEY, \
            fname TEXT, \
            lname TEXT, \
            phone TEXT, \
            email TEXT, \
            course TEXT \
            );")
        # You must commit() to save changes & close the database connection
        # conn.commit()  # This is not necessary if you are using the with statement

def onSelect(self,event):
    ''' This function is called when a item(s) selected in Treeview (This function is a stub right now)'''
    
    print("onSelect function called")
    return
##    # the rest of this code is from the listbox Phonebook app.  Keeping here as template in case it's needed.
##    # calling the event is the self.lstList1 widget
##    varList = event.widget
##    select = varList.curselection()[0]
##    value = varList.get(select)
##    conn = sqlite3.connect('school.db')
##    with conn:
##        cursor = conn.cursor()
##        cursor.execute("SELECT fname, lname, phone, email, course \
##                          FROM student \
##                          WHERE col_fullname = (?)", [value])
##        varBody = cursor.fetchall()
##        # This returns a tuple and we can slice it into 4 parts using data[] during the iteration
##        for data in varBody:
##            self.txt_fname.delete(0,END)  #change to 'end' or tk.END
##            self.txt_fname.insert(0,data[0])
##            self.txt_lname.delete(0,END)
##            self.txt_lname.insert(0,data[1])
##            self.txt_phone.delete(0,END)
##            self.txt_phone.insert(0,data[2])
##            self.txt_email.delete(0,END)
##            self.txt_email.insert(0,data[3])

##    # the rest of this code is from the listbox Phonebook app.  Keeping here as template in case it's needed.
##    # calling the event is the self.lstList1 widget

def onAdd(self):
    '''When Add button pressed, add the field entries to the Treelist and to the database'''
    
    # normalize the data to keep it consistent in the database
    fname = self.txt_fname.get().strip().title() # get text, stip of whitespace and capitalize it
    lname = self.txt_lname.get().strip().title()
    phone = self.txt_phone.get().strip()
    email = self.txt_email.get().strip()
    course = self.txt_course.get().strip().title()

    if not "@" or not "." in email: # will use this soon
        print("Incorrect email format!!!")
    # Make sure all fields have been entered
    if (len(fname) > 0) and (len(lname) > 0) and (len(phone) > 0) \
       and (len(email) > 0) and (len(course) > 0):
        conn = sqlite3.connect('school.db')
        with conn:
            cursor = conn.cursor()
            # This is an attempt to make sure that the INSERT and the return of lastrowid is one transaction.  Hoping to prevent
            # a second thread from inserting a row and lastrowid returning the rowid of the second INSERT.
            cursor.execute("BEGIN") 
            # Insert the new row and capture the last used rowid needed for the Treeview StudentID (a hidden column)
            studentID = cursor.execute("INSERT INTO student (fname, lname, phone, email, course)\
                            VALUES (?,?,?,?,?)",
                           (fname, lname, phone, email, course)).lastrowid
            self.treeList.insert(parent='', index='end', text="",
                                 values=(studentID,fname,lname,phone,email,course))
            onClear(self) # call the function to clear all of the textboxes
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all fields.")

def onDelete(self):
    '''When Delete button is pressed, delete all selected items from the Treeview and from the db'''
    
    currRows = self.treeList.selection()
    print("Number of rows selected = {}".format(len(currRows)))
    if len(currRows) == 0:
        messagebox.showinfo("Missing selection","No student was selected. \nCancelling Delete request.")
    else:
        confirm = messagebox.askokcancel("Delete Confirmation",
                                         "All selected information will be permanently"
                                         "\ndeleted from the database."
                                         "\n\nDo you wish to proceed?")
        if confirm:
            conn = sqlite3.connect('school.db')
            with conn:
                # delete all selected rows
                cursor = conn.cursor()
                # for each selected row, delete it from the database and the Treeview
                for index in currRows:  
                    print("\nIndex of selected Treeview row = {0}".format(index))
                    print("Treeview row contents = {}".format(self.treeList.item(index)))
                    rowValues = (self.treeList.item(index)["values"])
                    studentID = rowValues[0]
                    # index 0 is the studentID (hidden from display) we will use when deleting the row from the database
                    print("Student ID = {0}".format(studentID))
                    cursor.execute("DELETE FROM student WHERE ID = {}".format(studentID))
                    self.treeList.delete(index)
                return

def onClear(self):
    '''Clear the text in the input textboxes'''
    
    # self.txt_fname.delete(0,tk.END)
    self.txt_fname.delete(0,'end')
    self.txt_lname.delete(0,'end')
    self.txt_phone.delete(0,'end')
    self.txt_email.delete(0,'end')
    self.txt_course.delete(0,'end')

def onRefresh(self):
    '''Populate the Treeview with all data from the database.  Called on application startup'''

    #self.treeList.delete(0,END)
    conn = sqlite3.connect('school.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")   
        rows = cursor.fetchall()
        for row in rows:    # loop through the query results and insert each full name into the list box
            print(row)
            self.treeList.insert(parent='',index='end',values=(row))  # row[0] is the ID, primary key and is hidden


if __name__ == "__main__":
    pass
                
 
