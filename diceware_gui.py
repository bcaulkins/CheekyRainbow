from tkinter import *
import random
import re

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.pack(fill=BOTH, expand=1)

        text = Label(self, text="Just do it", font=("Helvetica", 18))
        text.place(x=70,y=90)
        # create button, link it to clickExitButton()
        exitButton = Button(self, text="Exit", command=self.clickExitButton)

        # place button at (0,0)
        exitButton.place(x=0, y=0)

    def clickExitButton(self):
        exit()



root = Tk()
app = Window(root)



# set window title
root.wm_title("Tkinter window")

# show window
root.wm_title("DiceWare Generator")
root.geometry("800x600")
root.mainloop()
