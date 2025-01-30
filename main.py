'''

    Written by Gregory Mejia
    Date: 1/25/2025

    Purpose: Main project file.

'''

##  Dependancies Importing  ##

from classes import DNA
from classes import RNA

from tkinter import Tk
from tkinter import Label
from tkinter import LabelFrame
from tkinter import Text

from tkinter import DISABLED
from tkinter import NORMAL
from tkinter import END

##  Classes  ##

class WindowObject:
    def __init__(self):
        # Create our objects
        self.root: Tk = Tk()
        self.credit = Label(self.root, text="Created by Gregory Mejia")

        self.title_frame = LabelFrame(self.root, padx=5, pady=-5)
        self.title_label = Label(self.title_frame, text="Genetic Coder", font=("Helvetica", 14, "bold"), padx=15)

        # Create the input side
        self.input_frame = LabelFrame(self.root)
        self.input_title = Label(self.input_frame, text="Input", font=("Helvetica", 10))

        self.box = Text(self.input_frame)

        # Create the output side
        self.output_frame = LabelFrame(self.root)
        self.output_title = Label(self.output_frame, text="Output", font=("Helvetica", 10))

        self.output = Text(self.output_frame)

        # Modify their properties
        self.root.title("Genetic Coder")
        self.root.minsize(500, 300)
        self.credit.config(font=("Helvetica", 7))
        self.credit.place(x=5, y=1)

        # Title Frame
        self.title_frame.pack(padx=5, pady=5)
        self.title_label.pack()

        # Input Frame
        self.input_frame.pack(padx=5, pady=5, side="left", anchor="nw")
        self.input_title.grid(row=0, column=0)
        self.box.grid(row=1, column=0)

        # Output Frame
        self.output_frame.pack(padx=5, pady=5, side="right", anchor="ne")
        self.output_title.grid(row=0, column=0)
        self.output.grid(row=1, column=0)

        self.output.insert(END, "lorem ipsum dolor set")
        self.output.config(state=DISABLED)

        # Fire the mainloop so the window opens
        self.root.mainloop()

##  Start  ##

if (__name__ == "__main__"):
    WindowObject()
