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
from idlelib.tooltip import Hovertip # Tooltips!

import file_xfer_main
import file_xfer_func


def load_gui(self):
    """
        Define the default tkinter widgets and their initial
        configuration and place them using the grid geometry.
    """

    # Labels

    # Text boxes
    self.txt_source = tk.Entry(self.master, font="Verdana 12")
    self.txt_source.grid(row=0,column=1,rowspan=1,padx=(30,27),pady=(40,0),sticky='nwwe')
    self.txt_dest = tk.Entry(self.master, font="Verdana 12")
    self.txt_dest.grid(row=1,column=1,rowspan=1,padx=(30,27),pady=(10,0),sticky='nswe')

    # Buttons
    # Source folder 
    self.btn_brws_src = tk.Button(self.master,width=12,height=1,text='Browse Src...',
                                  command=lambda: file_xfer_func.get_folder(self,self.txt_source))
    btn_src_tip = Hovertip(self.btn_brws_src,'Click to select source folder', hover_delay=600) # Tooltip
    self.btn_brws_src.grid(row=0,column=0,padx=(15,0),pady=(40,0),sticky='we')

    # Destination folder 
    self.btn_brws_dest = tk.Button(self.master,width=12,height=1,text='Browse Dest...',
                                   command=lambda: file_xfer_func.get_folder(self,self.txt_dest))
    btn_dest_tip = Hovertip(self.btn_brws_dest,'Click to select destination folder', hover_delay=600) # Tooltip
    self.btn_brws_dest.grid(row=1,column=0,padx=(15,0),pady=(10,0),sticky='we')

    # Transfer file(s) 
    self.btn_check = tk.Button(self.master,width=12,height=2,text='Check for files...',
                               command=lambda: file_xfer_func.xfer_files(self))
    btn_check_tip = Hovertip(self.btn_check,'Click to move files < 24 hours\n'
                             'old from Source to Destination', hover_delay=600) # Tooltip
    self.btn_check.grid(row=2,column=0, padx=(15,0),pady=(10,0),sticky='we')
    
    # Close application 
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program',command=self.master.destroy)
    self.btn_close.grid(row=2,column=1, padx=(0,27),pady=(10,0),sticky='e')

if __name__ == "__main__":
    pass
    

    
    
