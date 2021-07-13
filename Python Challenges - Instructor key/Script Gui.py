from tkinter import *
import tkinter as tk

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.minsize(500,170)
        self.master.maxsize(500,170)

        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")

        self.Browse = StringVar()

        self.btnBrowse = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse.grid(row='0', column='0', padx=(15,0) , pady=(30,0))

        self.btnBrowse = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse.grid(row='1', column='0', padx=(15,0) , pady=(10,0))

        self.btnCheck = Button(self.master, text="Check for files...", width=12, height=2)
        self.btnCheck.grid(row='2', column='0', padx=(15,0) , pady=(10,0))

        self.txtBrowse = Entry(self.master,text=self.Browse, font=("Helvetica", 12), fg='black', bg='white')
        self.txtBrowse.grid(row='0', column='1', padx=(30,15), pady=(40,10), columnspan=2, sticky=W+E)

        self.txtBrowse = Entry(self.master,text=self.Browse, font=("Helvetica", 12), fg='black', bg='white')
        self.txtBrowse.grid(row='1', column='1', padx=(30,15), pady=(10,0), columnspan=2, sticky=W+E)

        self.btnClose = Button(self.master, text="Close Program", width=12, height=2, command=self.close)
        self.btnClose.grid(row='2', column='2', padx=(0,15) , pady=(10,0))

        self.master.columnconfigure(1,weight=1)

    def close(self):
        self.master.destroy()
        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
