import tkinter as tk 

root = tk.Tk()
root.geometry('600x300')
root.title("Check Files")

def create():

    top = tk.Toplevel()

    top.title("Main Panel")
    top.geometry('300x100')
    msg = tk.Message(top, text="Show on Sub-panel",width=100)
    msg.pack()

    def exit_btn():

        top.destroy()
        top.update()

    btn = tk.Button(top,text='EXIT',command=exit_btn)
    btn.pack()


tk.Button(root, text="Click me,Create a sub-panel", command=create).pack()
root.mainloop()
