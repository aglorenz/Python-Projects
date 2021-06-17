from tkinter import *
win = Tk()
print(win)
f = Frame(win)
b1 =  Button(f, text="One")
b2 =  Button(f, text="Two")
b3 =  Button(f, text="Three")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
l = Label(win, text = "This label  is over all buttons")
l.pack()
f.pack()

def but1():
   print(v.get())

def but2():
    v.set("This is set by the program when clicking button 2")

b1.configure(command=but1)
b2.configure(command=but2)
sb = Scrollbar(win, orient=VERTICAL)
sb.pack(side=LEFT, fill=Y)

v=StringVar()
e=Entry(win, textvariable = v)
e.pack()

lb=Listbox(win,height=3)
lb.pack()
lb.insert(END, "first entry")
lb.insert(END, "second entry")
lb.insert(END, "third entry")
lb.insert(END, "fourth entry")

# Tie the scroll bar to the listbox
sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)
lb.curselection() # will return a tuple of the items selected
