#
# Python Ver: 3.9.5
#
# Author:       Andrew Lorenz
#
# Purpose:      Simple Student Tracking App. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:    This code was written and tested to work with Windows 10.

# Using the wildcoard is bad practice  W/O it, you have to explicitly state which tool kit you are using
# which makes for easier reading.  W/O it, you have to prefix widgets with the toolkit like so:  tk.Frame vs Frame
#from tkinter import *  

import tkinter as tk
#from tkinter import ttk # treeview widget comes from ttk

# Import our other modules
import file_xfer_gui
import file_xfer_func

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(tk.Frame):
    """
    Class to create a parent window of the application
  
    Extended description of function.
  
    Parameters:
    arg1 (int): Description of arg1
  
    Returns:
    int: Description of return value
  
    """
    
    def __init__(self, master, *args, **kwargs):
        '''Class initialization to define the window and load gui widgets for the app'''

        tk.Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        print(type(master))
        self.master.geometry('480x170')  # Initial Height and Width

        # This CenterWindow method will center our app on the user's screen
        file_xfer_func.center_window(self,480,170)
        self.master.title('File Transfer')
        self.master.configure(bg="#F0F0F0")

        ##self.master.columnconfigure(0,weight=1) # if I uncomment this, then column 0 stretches with the size of the frame.
        self.master.columnconfigure(1,weight=2)

        # load in the GUI widgets from a separate module
        # keeping code comparmentalized and clutter free
        file_xfer_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
