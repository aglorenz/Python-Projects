try:
    import tkinter as tk #python3
except ImportError:
    import Tkinter as tk #python2

def say_hi(self):
    print('hi')
    self.destroy()
    self.update()

def generate_new_window():
    window = tk.Toplevel()
    label = tk.Label(window, text="a generic Toplevel window")
    label.pack()

##def say_hi():
##    print('hi')
##    window.destroy()
##    window.update()

    button = tk.Button(window, text = "PRESS TO CLOSE", width = 25,
                                 command = lambda: say_hi(window))
##    lambda: student_func.ask_quit(self)
    button.pack()


root = tk.Tk()

spawn_window_button = tk.Button(root,
                                text="make a new window!",
                                command=generate_new_window)
spawn_window_button.pack()

root.mainloop()
