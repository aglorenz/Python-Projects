#
# Python Ver:   3.9.5
#
# Author:       Andrew 
#
# Purpose:      Simple Student Tracking App. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10.
#

# Using the wildcoard is bad practice  W/O it, you have to explicitly state which tool kit you are using
# which makes for easier reading.  W/O it, you have to prefix widgets with the toolkit like so:  tk.Frame vs Frame
#from tkinter import *  
import tkinter as tk
from tkinter import *
##from tkinter import ttk # Treeview widget comes from ttk


def load_gui():
    """
        Define the default tkinter widgets and their initial
        configuration and place them using the grid geometry.
    """

    # Labels

    # Text boxes
    txt_source = tk.Entry(root.master,text='')
    txt_source.grid(row=0, column=1, rowspan=1, padx=(30,27), pady=(40,0),sticky='nswe')
    txt_dest = tk.Entry(root.master,text='')
    txt_dest.grid(row=1, column=1, rowspan=1,padx=(30,27),pady=(10,0),sticky='nswe')


    # Buttons
    btn_brws_src = tk.Button(root.master,width=12,height=1,text='Browse...')
    btn_brws_src.grid(row=0,column=0,padx=(15,0),pady=(40,0),sticky='we')
    btn_brws_dest = tk.Button(root.master,width=12,height=1,text='Browse...')
    btn_brws_dest.grid(row=1,column=0,padx=(15,0),pady=(10,0),sticky='we')
    btn_check = tk.Button(root.master,width=12,height=2,text='Check for files...')
    btn_check.grid(row=2,column=0, padx=(15,0),pady=(10,0),sticky='we')
    btn_close = tk.Button(root.master,width=12,height=2,text='Close Program')
    btn_close.grid(row=2,column=1, padx=(0,15),pady=(10,0),sticky='e')

##    self.btn_check = tk.Button(self.master,width=12,height=2,text='Check',command=lambda: student_func.ask_quit(self))
##    self.btn_close.grid(row=2,column=0,columnspan=1,padx=(15,0),pady=(45,10),sticky='we')
##    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda: student_func.ask_quit(self))
##    self.btn_close.grid(row=2,column=1,columnspan=1,padx=(15,0),pady=(45,10),sticky='w')

##    student_func.create_db(self)  # create the db if it doesn't exist
##    student_func.onRefresh(self)  # display any data found in the db on the Treeview

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('480x170')
    root.title('Check Files')
    
    ##root.columnconfigure(0,weight=1) # if I uncomment this, then column 0 stretches with the size of the frame.
    root.columnconfigure(1,weight=2)
    load_gui()
    root.mainloop()


    
    
