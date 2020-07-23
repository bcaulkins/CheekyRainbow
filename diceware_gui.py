from tkinter import *
import random
import re

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

root = Tk()
app = Window(root)



# set window title
root.wm_title("Tkinter window")

# show window
root.mainloop()
