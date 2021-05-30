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
from tkinter import *
from tkinter import messagebox

import tkinter as tk
import sqlite3

# import our other modules
# so we can have access to them
import student_main
import student_gui


def center_window(self, w, h): # pass in the tkinter frame (master) reference and the v and h
    # get User's screen width and height
    screen_width = self.master.winfo_screenwidth() # get user's width and height
    screen_height = self.master.winfo_screenheight() # and height
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# catch if the user clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes the app
        self.master.destroy()
        os._exit(0)

#=========================================
def create_db(self):
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
        conn.commit()

def count_records(cur):
    count = ""
    cur.execute("SELECT COUNT(*) FROM student")
    count = cur.fetchone()[0]
    return cur,count

# Select item in Treeview
def onSelect(self,event):
    print("hi onSelect called")
    return
    #calling the event is the self.lstList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('school.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT fname, lname, phone, email, course \
                          FROM student \
                          WHERE col_fullname = (?)", [value])
        varBody = cursor.fetchall()
        # This returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])

def onAdd(self):
    # Add the field entries to the Treelist and to the database
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
            # An attempt to make sure that the INSERT and the return of lastrowid is one transaction.  Hoping to prevent
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
    try:
        currRows = self.treeList.selection()
        print("Number of rows selected = {}".format(len(currRows)))
        if len(currRows) == 0:
            messagebox.showinfo("Missing selection","No student was selected for deletion. \nCancelling Delete request.")
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
    except:
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the Delete request.")
        return
    conn = sqlite3.connect('school.db')
    with conn:
        cur = conn.cursor()
        # check count to ensure that this is not the  last record in
        # the database.... cannot delete last record or we will get an error
        cur.execute("SELECT COUNT(*) FROM student")
        count = cur.fetchone()[0]
        if count > 0:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({})"
                                             "\n will be permanently deleted from the database."
                                             "\n\nProceed with the deletion request?".format(fullName))
            if confirm:
                conn = sqlite3.connect('school.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM student WHERE ID = '{}'".format(studentID))
                
                #onDeleted(self) # call the function to clear all of the textboxes and the selected index of listbox
                #### onRefresh(self) # update the listbox of the changes
                #conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the databsase and " 
                                            "cannot be deleted at this time. \n\nPlease add another record " 
                                            "first before deleting ({}).".format(var_select, fullName))
    conn.close()

def onDeleted(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
##  onRefresh(self) # update the listbox of the changes
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)

def onRefresh(self):
    # Populate the Treeview with data from the database
    #self.treeList.delete(0,END)
    conn = sqlite3.connect('school.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")   
        rows = cursor.fetchall()
###
###  put the id in column #1 or #0 (determine this first) instead of the text field and just hide  columns 0 and 1 - Find out how to hide specific columns
###        
        for row in rows:    # loop through the query results and insert each full name into the list box
            print(row)
##            self.treeList.insert(parent='', index='end', text=row[0],
##                                 values=(row[1],row[2],row[3],row[4],row[5]))  # row[0] is the ID, text=row[0] is primary key and is hidden
##            self.treeList.insert(parent='', index='end',
##                                 values=(row[0],row[1],row[2],row[3],row[4],row[5]))  # row[0] is the ID, text=row[0] is primary key and is hidden
            self.treeList.insert(parent='',index='end',values=(row))  # row[0] is the ID, primary key and is hidden

    
def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0] # index of the list selection
        var_fullName = self.lstList1.get(var_select) # list selection's text value
    except:
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the Update request.")
        return
    # The user will only abe allowed to update changes for phone and emails.
    # for name changes, the user iwll need to delete the entire record and start over.
    var_phone = self.txt_phone.get().strip() # normalize the data to maintain database ingegrity
    var_email = self.txt_email.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0): # ensure data is present
        conn = sqlite3.connect('school.db')
        with conn:
            cur = conn.cursor()
            # countrecords to see if the user's changes are already in
            # the database...meaning, there are no changes to update.
            # Updated the query to check if the ph/email values for the selected name have changed
            #  (rather than if they exist anywhere in the db.
            #  Assumption (biz rule) is that multiple people can share the same email and phone number 
            cur.execute("SELECT COUNT(*) FROM student WHERE phone = '{}' and col_fullname = '{}'".format(var_phone,var_fullName))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("SELECT COUNT(*) FROM student WHERE email = '{}' and col_fullname = '{}'".format(var_email,var_fullName))
            count2 = cur.fetchone()[0]
            print(count2)
            if count == 0 or count2 == 0: # if proposed changes are not already in the database, then proceed
                response = messagebox.askokcancel("Update Request","The following changes({}) and ({}) will be implemented for ({})."
                                                  "\n\nProceed with the update request?".format(var_phone,var_email,var_fullName))
                print(response)
                if response:
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("UPDATE student \
                                        SET phone = '{}', email = '{}' \
                                        WHERE col_fullname = '{}'".format(var_phone,var_email,var_fullName))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request","No changes have been made to ({}).".format(var_fullName))
            else:
                messagebox.showinfo("No changes detected","Values ({}) and ({}) \nalready exist for "
                                    "{}. \n\nYour update request has been cancelled.".format(var_phone,var_email,var_fullName))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing information","Please select a name from the list."
                             "\nThen edit the phone or email information.")
        onClear(self)

if __name__ == "__main__":
    pass
                
    


    




















    
    
