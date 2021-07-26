#
# Python Ver: 3.9.5
#
# Author:       Andrew Lorenz
#
# Purpose:      Simple file transfer application
#              
#
# Tested OS:    This code was written and tested to work with Windows 10.

'''
Main module for the file transfer app

Classes:
    ParentWindow(tk.Frame)    
'''


# Using the wildcard is bad practice  W/O it, you have to explicitly state which tool kit you are using
# which makes for easier reading.  W/O it, you have to prefix widgets with the toolkit like so:  tk.Frame vs Frame
#from tkinter import *  
import tkinter as tk

# Import our other modules
import file_xfer_gui
import file_xfer_func

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(tk.Frame):
    '''
    Class to represent the parent window of the file transfer application
  
    Applicaton will copy files in Source folder to Destination folder if they were modified < 24 hour ago
  
    Attributes:
    master : tkinter.Tk
        Toplevel widget of Tk which represents mostly the main window of the application
  
    Methods:
        None
  
    '''
    
    def __init__(self, master, *args, **kwargs):
        '''Class initialization to define the parent window and load gui widgets for the app

        Parameters
        ----------
            master : tkinter.Tk
                Toplevel widget of Tk which represents mostly the main window of the application

        '''
        
        tk.Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master

        # This CenterWindow method will center our app on the user's screen
        file_xfer_func.center_window(self,480,170) # initial width and height
        
        self.master.title('File Transfer')
        self.master.config(bg="#C0C0C0")

        ##self.master.columnconfigure(0,weight=1) # if I uncomment this, then column 0 stretches with the size of the frame.
        self.master.columnconfigure(1,weight=2)

        # load in the GUI widgets from a separate module
        # keeping code compartmentalized and clutter free
        file_xfer_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk() # root = main window of the application
    App = ParentWindow(root)
    root.mainloop()
    
