'''

    Written by Gregory Mejia
    Date: 1/25/2025

    Purpose: Main project file.

'''

##  Dependancies Importing  ##

from classes import DNA
from classes import RNA

from tkinter import Tk

##  Classes  ##

class WindowObject:
    def __init__(self):
        # Create our new window instance
        self.root = Tk()

        # Modify the properties of it
        self.root.title("Genetic Coder")
        self.root.minsize(500, 300)

        # Fire the mainloop so the window opens
        self.root.mainloop()

##  Start  ##

if (__name__ == "__main__"):
    WindowObject()
