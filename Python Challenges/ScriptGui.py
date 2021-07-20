#
# Python Ver:   3.9.5
#
# Author:       Andrew Lorenz
#
# Purpose:      Exercise to create a simple GUI with a button to open a dialog to capture a folder name and
#               paste it in a text field
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10.
#

# Using the wildcoard is bad practice  W/O it, you have to explicitly state which tool kit you are using
# which makes for easier reading.  W/O it, you have to prefix widgets with the toolkit like so:  tk.Frame vs Frame
#from tkinter import *  
import tkinter as tk
from tkinter import Frame
from tkinter import filedialog as fd
##from tkinter import ttk # Treeview widget comes from ttk

class ParentWindow(Frame):  # Frame is a class, not a parameter passed in from 

    def __init__(self,master):  # master = root = tk.Tk
        """
            Define the default tkinter widgets and their initial
            configuration and place them using the grid geometry.
        """
        Frame.__init__(self, master)
        self.master = master

        self.master.title('Check Files')
        #root.title('Check Files')
        self.master.geometry('480x170')
        #root.geometry('480x170')

        ##root.columnconfigure(0,weight=1) # if I uncomment this, then column 0 stretches with the size of the frame.
        self.master.columnconfigure(1,weight=2)
        
        # Labels

        # Text boxes
        self.txt_source = tk.Entry(self.master, font="Verdana 12")
        self.txt_source.grid(row=0,column=1,rowspan=1,padx=(30,27),pady=(40,0),sticky='nwwe')
        self.txt_dest = tk.Entry(self.master,text='')
        self.txt_dest.grid(row=1,column=1,rowspan=1,padx=(30,27),pady=(10,0),sticky='nswe')


        # Buttons
        self.btn_brws_src = tk.Button(self.master,width=12,height=1,text='Browse...', command=self.get_src_folder)
        self.btn_brws_src.grid(row=0,column=0,padx=(15,0),pady=(40,0),sticky='we')
        self.btn_brws_dest = tk.Button(self.master,width=12,height=1,text='Browse...')
        self.btn_brws_dest.grid(row=1,column=0,padx=(15,0),pady=(10,0),sticky='we')
        self.btn_check = tk.Button(self.master,width=12,height=2,text='Check for files...')
        self.btn_check.grid(row=2,column=0, padx=(15,0),pady=(10,0),sticky='we')
        self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program',command=self.master.destroy)
        self.btn_close.grid(row=2,column=1, padx=(0,27),pady=(10,0),sticky='e')

    def get_src_folder(self):
        self.txt_source.delete(0,'end')
        src_folder = fd.askdirectory()
        self.txt_source.insert(0,src_folder)

    ##    self.btn_check = tk.Button(self.master,width=12,height=2,text='Check',command=lambda: student_func.ask_quit(self))
    ##    self.btn_close.grid(row=2,column=0,columnspan=1,padx=(15,0),pady=(45,10),sticky='we')
    ##    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda: student_func.ask_quit(self))
    ##    self.btn_close.grid(row=2,column=1,columnspan=1,padx=(15,0),pady=(45,10),sticky='w')

    ##    student_func.create_db(self)  # create the db if it doesn't exist
    ##    student_func.onRefresh(self)  # display any data found in the db on the Treeview

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

    

    
    
