#
# Python Ver: 3.9.5
#
# Author:       Andrew Lorenz
#
# Purpose:      Simple Student Tracking App. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:    This code was written and tested wo work with Windows 10.

from tkinter import *
from tkinter import ttk # treeview widget comes from ttk
import tkinter as tk


# Import our other modules
import student_gui
import student_func


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(800,350)  # Height and Width
        self.master.maxsize(800,350)
        # This CenterWindow method will center our app on the user's screen
        student_func.center_window(self,800,350)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module
        # keeping code comparmentalized and clutter free
        student_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
##    root.grid_columnconfigure(0,weight=1)
##    root.grid_rowconfigure(0,weight=1)
    root.mainloop()
    
