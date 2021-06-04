#
# Python Ver:   3.9.5
#
# Author:       Typed in by Andrew Lorenz from code by Daniel Christie
#
# Purpose:      Simple Student Tracking App. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10.
#

import tkinter as tk
from tkinter import ttk # Treeview widget comes from ttk

# Import our other modules
# so we can access them
import student_main
import student_func


def load_gui(self):
    """
        Define the default tkinter widgets and their initial
        configuration and place them using the grid geometry.
        I prefer to use grid as it offers the best control
        for pacing the widgets, but is a little confusing at
        first, but that is what this demo is here for...
    """

    # Labels
    self.lbl_fname = tk.Label(self.master,text='First Name:')
    self.lbl_fname.tk.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_lname = tk.Label(self.master,text='Last Name:')
    self.lbl_lname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_phone = tk.Label(self.master,text='Phone Number:')
    self.lbl_phone.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_email = tk.Label(self.master,text='Email Address:')
    self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_course = tk.Label(self.master,text='Current Course:')
    self.lbl_course.grid(row=8,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

    # Text boxes
    self.txt_fname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=1,column=0,rowspan=1,padx=(30,0),pady=(0,0),sticky=N+E+W)
    self.txt_lname = tk.Entry(self.master,text='')
    self.txt_lname.grid(row=3,column=0,rowspan=1,padx=(30,0),pady=(0,0),sticky=N+E+W)
    self.txt_phone = tk.Entry(self.master,text='')
    self.txt_phone.grid(row=5,column=0,rowspan=1,padx=(30,0),pady=(0,0),sticky=N+E+W)
    self.txt_email = tk.Entry(self.master,text='')
    self.txt_email.grid(row=7,column=0,rowspan=1,padx=(30,0),pady=(0,0),sticky=N+E+W)
    self.txt_course = tk.Entry(self.master,text='')
    self.txt_course.grid(row=9,column=0,rowspan=1,padx=(30,0),pady=(0,0),sticky=N+E+W)

    ######################################################
    # Define the Treeview with 2 scrollbars and grid them
    ######################################################

##    self.treeList = ttk.Treeview(self.master)
##    self.treeList['columns'] = columns
##    self.treeList['show'] = 'headings'  

    # These are the columns we want to display. Column #0, the primary key, "ID" will be hidden 
    # Define identifiers for columns in Treeview widget
    columns = ("ID","fname","lname","phone","email","course") # All columns
    displayColumns = ("fname","lname","phone","email","course") # columns that will be displayed
    
    # here's a way to combine the above three commented out statements into one
    self.treeList = ttk.Treeview(self.master,columns=columns,displaycolumns=displayColumns,show='headings')

##    self.treeList.column("#0", anchor=W, width=40) 
##    self.treeList.column("#0", width=0, stretch=NO) # not displayed, but will hold primary key (first column) from db
    self.treeList.column("ID", anchor=W, width=120)
    self.treeList.column("fname", anchor=W, width=120)
    self.treeList.column("lname", anchor=W, width=120)
    self.treeList.column("phone", anchor=W, width=120)
    self.treeList.column("email", anchor=W, width=120)
    self.treeList.column("course", anchor=W, width=120)

    # Define display column headings
##    self.treeList.heading("#0", text = "ID", anchor=W)
    self.treeList.heading("ID", text = "Student ID", anchor=W) # will be hidden and hold primary key
    self.treeList.heading("fname", text = "First Name", anchor=W)
    self.treeList.heading("lname", text = "Last Name", anchor=W)
    self.treeList.heading("phone", text = "Phone", anchor=W)
    self.treeList.heading("email", text = "Email", anchor=W)
    self.treeList.heading("course", text = "Course", anchor=W)

    # Manual test of Adding Data
    #self.treeList.insert(parent='', index='end', iid=0, text="", values=("Andy", "Lorenz","555-555-5555","andy@gmail.com","Python"))

    # Label for the Treeview
    self.lbl_info = tk.Label(self.master,text='Students:')
    self.lbl_info.grid(row=0,column=1,padx=(12,0),pady=(10,0),sticky=N+W)

    # Grid the Treeview widget
    self.treeList.grid(row=1, column=1, padx=(15,0), rowspan=9, columnspan=2, sticky=N+S+E+W)

    # Add a vertical scrollbar widget
    self.scrollbar = Scrollbar(self.master, orient=VERTICAL, command=self.treeList.yview)
    self.treeList.configure(yscroll=self.scrollbar.set)

    # Grid the Scrollbar widget
    self.scrollbar.grid(row=1, column=3, rowspan=9, sticky=N+S)
    
    # Buttons
    self.btn_add = tk.Button(self.master,width=12,height=2,text='Add',command=lambda: student_func.onAdd(self))
    self.btn_add.grid(row=10,column=0,padx=(27,0),pady=(45,10),sticky=W+E)
    self.btn_delete = tk.Button(self.master,width=12,height=2,text='Delete',command=lambda: student_func.onDelete(self))
    self.btn_delete.grid(row=10,column=1,padx=(15,0),pady=(45,10),sticky=W+E)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: student_func.ask_quit(self))
    self.btn_close.grid(row=10,column=2,columnspan=1,padx=(15,0),pady=(45,10),sticky=W+E)

    # onSelect is only a stub now; saving for future
    # bind the select event
    self.treeList.bind('<<TreeviewSelect>>',lambda event: student_func.onSelect(self,event))

    student_func.create_db(self)  # create the db if it doesn't exist
    student_func.onRefresh(self)  # display any data found in the db on the Treeview

if __name__ == "__main__":
    pass


    
    
