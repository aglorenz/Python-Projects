#
# Python Ver:   3.9.5
#
# Author:       Andrew Lorenz
#
# Purpose:      Exercise to create a simple GUI with 2 buttons and an input text field.
#               Button 1: Display the default web page of, "Stay tuned for our amazing summer sale!"
#               Button 2: Display text entered in the input text field in the web page
#
# Tested OS:  This code was written and tested to work with Windows 10.
#

import tkinter as tk
from tkinter import Frame
import webbrowser

class ParentWindow(Frame):  # Frame is a class, not a parameter passed in from 

    def __init__(self,master):  # master = root = tk.Tk
        """
            Define the default tkinter widgets and their initial
            configuration and place them using the grid geometry.
        """
        Frame.__init__(self, master)
        self.master = master

        self.master.title("Web Page Generator")

        # Labels
        label_text = "Enter text to customize the text for your webpage."
        self.lbl_entry = tk.Label(text = label_text, font=("Verdana", 12))
        self.lbl_entry.grid(row=0, column=0, padx=(27,20), pady=(30,3))

        # Text Boxes
        self.txt_custom = tk.Entry(self.master, font=("Verdana", 12))
        self.txt_custom.grid(row=1, column=0, columnspan=3, ipady=3, padx=(30,20), sticky=('we'))

        # Buttons
        self.btn_default = tk.Button(self.master, text="Show Default Page", font=("Verdana", 12),
                                     command=self.default_page)
        self.btn_default.grid(row=2, column=1, pady=(20,20))

        self.btn_custom = tk.Button(self.master, text="Submit Custom Text", font=("Verdana", 12),
                                    command=self.custom_page)
        self.btn_custom.grid(row=2, column=2, padx=(20,20), pady=(20,20))

    def default_page(self):
        #Text of the webpage
        html_text='''<html>
    <body>
        <h1>
            Stay tuned for our amazing summer sale!
        </h1>
    </body>
</html>'''

        # open the web page file and save the text in it
        hf = open("web_page.html", "w") # create file if it doesn't exist and write to it
        hf.write(html_text)
        hf.close()

        # display the web page
        webbrowser.open_new_tab("web_page.html")

    def custom_page(self):
        html_text1='''<html>
    <body>
        <h1>
            '''
        html_text2='''
        </h1>
    </body>
</html>'''
        custom_text = self.txt_custom.get()       

        # open the web page file and save the text in it
        hf = open("web_page.html", "w") # create file if it doesn't exist and write to it
        hf.write(html_text1 + custom_text + html_text2)
        hf.close()

        # display the web page
        webbrowser.open_new_tab("web_page.html")


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
