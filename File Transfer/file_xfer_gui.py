#
# Python Ver:   3.9.5
#
# Author:       Andrew Lorenz
#
# Tested OS:  This code was written and tested to work with Windows 10.

'''
Module to set up the GUI for the file transfer application.

More Detailed description goes here (if necessary)

Functions:

    load_gui(self)
    
'''

# Using the wildcard is bad practice  W/O it, you have to explicitly state which tool kit you are using
# which makes for easier reading.  W/O it, you have to prefix widgets with the toolkit like so:  tk.Frame vs Frame
# from tkinter import *
import tkinter as tk
from tkinter import Frame
from idlelib.tooltip import Hovertip # Tooltips!

# Import our other modules
import file_xfer_func

def load_gui(self):
    ''' Define the tkinter widgets and their initial
        configuration and place them using the grid geometry.

    Parameters
    ----------
    self : Frame
        The tkinter Frame in which this function will place widgets

    Returns
    -------
        None
        
    '''

    # Labels

    # Text boxes
    self.txt_source = tk.Entry(self.master, font="Verdana 12")
    self.txt_source.grid(row=0,column=1,rowspan=1,padx=(30,27),pady=(40,0),sticky='nwwe')
    self.txt_dest = tk.Entry(self.master, font="Verdana 12")
    self.txt_dest.grid(row=1,column=1,rowspan=1,padx=(30,27),pady=(10,0),sticky='nswe')

    # Buttons
    # Source folder 
    self.btn_brws_src = tk.Button(self.master,width=12,height=1,text='Browse Src...',
                                  command=lambda: file_xfer_func.get_folder(self.txt_source))
    btn_src_tip = Hovertip(self.btn_brws_src,'Click to select Source folder', hover_delay=600) # Tooltip
    self.btn_brws_src.grid(row=0,column=0,padx=(15,0),pady=(40,0),sticky='we')

    # Destination folder 
    self.btn_brws_dest = tk.Button(self.master,width=12,height=1,text='Browse Dest...',
                                   command=lambda: file_xfer_func.get_folder(self.txt_dest))
    btn_dest_tip = Hovertip(self.btn_brws_dest,'Click to select Destination folder', hover_delay=600) # Tooltip
    self.btn_brws_dest.grid(row=1,column=0,padx=(15,0),pady=(10,0),sticky='we')

    # Transfer file(s) 
    self.btn_check = tk.Button(self.master,width=12,height=2,text='Check for Files...',
                               command=lambda: file_xfer_func.xfer_files(self.txt_source.get(), self.txt_dest.get()))
    btn_check_tip = Hovertip(self.btn_check,'Click to copy files < 24 hours\n'
                             'old from Source to Destination', hover_delay=600) # Tooltip
    self.btn_check.grid(row=2,column=0, padx=(15,0),pady=(10,0),sticky='we')
    
    # Close application 
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program',command=self.master.destroy)
    self.btn_close.grid(row=2,column=1, padx=(0,27),pady=(10,0),sticky='e')

if __name__ == "__main__":
    pass
    

    
    
