
import tkinter
from tkinter import *  # * means use all of the widgets

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title('Learning Tkinter')
        self.master.config(bg='lightgrey')
#        self.master.config(bg='#000')

        # Creating a Tkinter variable
        self.varFName = StringVar()
        self.varLName = StringVar()
        self.varFName.set('Bob')
        self.varLName.set('Smith')

        # debug print to console
        print(self.varFName.get())
        print(self.varLName.get())

        self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtFName.pack()

        self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtLName.pack()


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
