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
from tkinter import Button

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

        # Create the central input widget thing
        self.middle_frame = LabelFrame(self.root)
        self.middle_title = Label(self.middle_frame, text="Controls", font=("Helvetica", 15))

        # Now we have the mode switcher
        self.mode_frame = LabelFrame(self.middle_frame, padx=10, pady=10)
        self.dna_button = Button(self.mode_frame, text="DNA", padx=20)
        self.rna_button= Button(self.mode_frame, text="RNA", padx=20)

        # Modify their properties
        self.root.title("Genetic Coder")
        self.root.resizable(False, False)
        self.credit.config(font=("Helvetica", 7))
        self.credit.place(x=5, y=1)

        # Title Frame
        self.title_frame.pack(padx=5, pady=5)
        self.title_label.pack()

        # Input Frame
        self.input_frame.pack(padx=5, pady=5, side="left", anchor="nw")
        self.input_title.grid(row=0, column=0)
        self.box.grid(row=1, column=0)
        self.box.config(width=35, height=15)

        # Manage the middle stuff
        self.middle_frame.pack(padx=3, pady=5, anchor="center", side="top")
        self.middle_title.pack(anchor="center", side="top")

        # Middle stuff - mode switcher
        self.mode_frame.pack(padx=5, pady=5)
        # I don't know if this is overly redudant but just in case formatting is wrong
        self.mode_frame.columnconfigure(0, pad=5)
        self.mode_frame.columnconfigure(1, pad=5)

        self.dna_button.grid(row=0, column=0)
        self.rna_button.grid(row=0, column=1)

        # Output Frame
        self.output_frame.pack(padx=5, pady=5, side="right", anchor="ne")
        self.output_title.grid(row=0, column=0)
        self.output.grid(row=1, column=0)

        self.output.insert(END, "lorem ipsum dolor set")
        self.output.config(state=DISABLED, width=35, height=15)

        # Fire the mainloop so the window opens
        self.root.mainloop()

##  Start  ##

if (__name__ == "__main__"):
    WindowObject()
