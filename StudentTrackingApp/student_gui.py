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

from tkinter import *
from tkinter import ttk # Treeview widget comes from ttk
import tkinter as tk

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
##    self.btn_column = tk.Button(self.master,text="I'm in column 3")
##    self.btn_column.grid(column=3, row=0, rowspan=2, sticky=N+S)
##
##    self.btn_columnspan = tk.Button(self.master, text="I am in column 2", width='10')
##    self.btn_columnspan.grid(column=2,row=1)
##
##    self.btn_columnspan1 = tk.Button(self.master, text="I am in column 2", width='10')
##    self.btn_columnspan1.grid(column=2,row=0)
##
##    self.btn_column0 = tk.Button(self.master, text="I am in column 0", width='20')
##    self.btn_column0.grid(column=0, row=0, columnspan=2, rowspan=3, sticky=N+S)
##
##    self.btn_column2 = tk.Button(self.master, text="I am in column 2", width='20')
##    self.btn_column2.grid(column=2, row=2, columnspan=2, sticky=E+W)
##
##    self.btn_column2 = tk.Button(self.master, text="I am in column 1", width='10')
##    self.btn_column2.grid(column=0, row=3, sticky=W)
    
##    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: student_func.ask_quit(self))
##    self.btn_close.grid(row=10,column=4,columnspan=1,padx=(15,0),pady=(45,10),sticky=E)

#---------------------------------------------------------------

#    self.l1 = tk.Label(self.master, text = "First:")
#    self.l1.grid(row = 0, column = 0, sticky = E, pady = 2)
#    self.l2 = tk.Label(self.master, text = "Second:")
#    self.l2.grid(row = 1, column = 0, sticky = E, pady = 2)

#    self.e1 = tk.Entry(self.master)
#    self.e1.grid(row=0,column=0,columnspan=4,sticky=N+S+W+E)
#    self.e2 = tk.Entry(self.master)
#    self.e2.grid(row=1,column=1,pady=3,columnspan=3,sticky=W+E)

#--------------------------------------------------------------------

    # Labels
    self.lbl_fname = tk.Label(self.master,text='First Name:')
    self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
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

    # Define the listbox with a scrollbar and grid them
##    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
##    self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
##    self.lstList1.bind('<<ListboxSelect>>',lambda event: student_func.onSelect(self,event))
##    self.scrollbar1.config(command=self.lstList1.yview)
##    self.scrollbar1.grid(row=1,column=5,rowspan=9,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
##    self.lstList1.grid(row=1,column=2,rowspan=9,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

    # Define the Treeview with 2 scrollbars and grid them
    self.treeList = ttk.Treeview(self.master)
    # Define columns for Treeview
    self.treeList['columns'] = ("fname","lname","phone","email","course")
    self.treeList.column("#0", width=0, stretch=NO) # not displayed, but will hold primary key from db
    self.treeList.column("fname", anchor=W, width=120)
    self.treeList.column("lname", anchor=W, width=120)
    self.treeList.column("phone", anchor=W, width=120)
    self.treeList.column("email", anchor=W, width=120)
    self.treeList.column("course", anchor=W, width=120)
    # Define display column headings
    self.treeList.heading("#0", text = "", anchor=W)
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
                         
    # Buttons
    self.btn_add = tk.Button(self.master,width=12,height=2,text='Add',command=lambda: student_func.onAdd(self))
    self.btn_add.grid(row=10,column=0,padx=(27,0),pady=(45,10),sticky=W+E)
    self.btn_delete = tk.Button(self.master,width=12,height=2,text='Delete',command=lambda: student_func.onDelete(self))
    self.btn_delete.grid(row=10,column=1,padx=(15,0),pady=(45,10),sticky=W+E)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: student_func.ask_quit(self))
    self.btn_close.grid(row=10,column=2,columnspan=1,padx=(15,0),pady=(45,10),sticky=W+E)

    student_func.create_db(self)
    student_func.onRefresh(self)


if __name__ == "__main__":
    pass


    
    
