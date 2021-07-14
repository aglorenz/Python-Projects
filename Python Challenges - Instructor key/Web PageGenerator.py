import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Webpage Generator")
        self.labelTxt = Label(text = "Would you like to create custom text for your webpage?", font=("Arial", 12))
        self.labelTxt.grid(row=0,column=0, padx=20, pady=(20,0))

        self.txtEntry = Entry(self.master, font=("Helvetica", 12))
        self.txtEntry.grid(row=1, column=0, padx=(30,15), pady=(10,10), columnspan=3, sticky=W+E)

        self.btnSubmit = Button(self.master, text="View Default", width=20, height=1, command=self.defaultEntry)
        self.btnSubmit.grid(row=2, column=1, padx=(0,10) , pady=(0,10))

        self.btnSubmit = Button(self.master, text="Submit Custom Text", width=20, height=1, command=self.customEntry)
        self.btnSubmit.grid(row=2, column=2, padx=(0,10) , pady=(0,10))
        
    def customEntry(self):
        self.labelTxt = Label(text = "Customize your webpage by entering text, then click to view!", font=("Arial", 12))
        customText = self.txtEntry.get()
        htmlFile = open("user_customized.html", "w")
        htmlFormat = "<html>\n<body>\n<p>" + customText + "</p>\n</body>\n</html>"
        htmlFile.write(htmlFormat)
        htmlFile.close()
        webbrowser.open_new_tab("user_customized.html")
        
    def defaultEntry(self):
        sameText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("user_customized.html", "w")
        htmlFormat = "<html>\n<body>\n<p>" + sameText + "</p>\n</body>\n</html>"
        htmlFile.write(htmlFormat)
        htmlFile.close()
        webbrowser.open_new_tab("user_customized.html")
        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
