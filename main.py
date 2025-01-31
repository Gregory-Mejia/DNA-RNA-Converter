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
from tkinter import Button
from tkinter import Checkbutton
from tkinter import Text
from tkinter import BooleanVar

from tkinter import DISABLED
from tkinter import NORMAL
from tkinter import END

##  Classes  ##

class WindowObject:
    def __init__(self):

        # Create our objects
        self.root: Tk = Tk()
        self.credit = Label(self.root, text="Created by Gregory Mejia")

        self.title_frame = LabelFrame(self.root, padx=100, pady=-15)
        self.title_label = Label(self.title_frame, text="Genetic Coder", font=("Helvetica", 20, "bold"), padx=15)

        # Here are our variables that we'll bind to later
        self.ontop = BooleanVar()
        self.mode = "DNA"

        # Create the input side
        self.input_frame = LabelFrame(self.root)
        self.input_title = Label(self.input_frame, text="Input", font=("Helvetica", 10))

        self.box = Text(self.input_frame)

        # Create the output side
        self.output_frame = LabelFrame(self.root)
        self.output_title = Label(self.output_frame, text="Output", font=("Helvetica", 10))

        self.output = Text(self.output_frame)

        # Create the central input widget thing
        self.middle_frame = LabelFrame(self.root, pady=4)
        self.middle_title = Label(self.middle_frame, text="Controls", font=("Helvetica", 25, "bold"))

        self.convert_outline = LabelFrame(self.middle_frame)
        self.convert = Button(self.convert_outline, text="Convert Strand")

        # Mode identifier
        self.identifier_font = ("Helvetica", 13)
        self.identifier_frame = LabelFrame(self.middle_frame, padx=45, pady=5)
        self.identifier_text = Label(self.identifier_frame, text="Current Mode: ", font=self.identifier_font)
        self.identifier_actual = Label(self.identifier_frame, text="DNA", font=self.identifier_font)

        # Now we have the mode switcher
        self.mode_font = ("Helvetica", 12)

        self.mode_frame = LabelFrame(self.middle_frame, padx=5, pady=5)
        self.dna_button = Button(
                self.mode_frame, text="DNA", padx=10, font=self.mode_font, command=lambda: self.mode_switcher("DNA")
            )
        self.mrna_button = Button(
                self.mode_frame, text="mRNA", padx=5, font=self.mode_font, command=lambda: self.mode_switcher("mRNA")
            )
        self.trna_button = Button(
                self.mode_frame, text="tRNA", padx=10, font=self.mode_font, command=lambda: self.mode_switcher("tRNA")
            )

        # Always on-top button
        self.ontop_frame = LabelFrame(self.middle_frame, padx=37, pady=3)
        self.ontop_button = Checkbutton(self.ontop_frame, command=self.always_on_top, variable=self.ontop)
        self.ontop_text = Label(self.ontop_frame, text="Always Ontop?", font=self.identifier_font)

        # Modify their properties
        self.root.title("Genetic Coder")
        self.root.resizable(False, False)
        self.credit.config(font=("Times", 7))
        self.credit.place(x=5, y=1)

        # Title Frame
        self.title_frame.pack(padx=5, pady=5, side="top", anchor="center")
        self.title_label.pack()

        # Input Frame
        self.input_frame.pack(padx=5, pady=5, side="left", anchor="nw")
        self.input_title.grid(row=0, column=0)
        self.box.grid(row=1, column=0)
        self.box.config(width=35, height=15)

        # Manage the middle stuff
        self.middle_frame.pack(padx=3, pady=5, anchor="center", side="left")
        self.middle_title.pack(anchor="center", side="top")

        # Mode Identifier
        self.identifier_frame.pack(padx=5, pady=3)
        self.identifier_text.grid(row=0, column=0)
        self.identifier_actual.grid(row=0, column=1)

        # Middle stuff - mode switcher
        self.mode_frame.pack(padx=5, pady=5)
        # I don't know if this is overly redudant but just in case formatting is wrong
        self.mode_frame.columnconfigure(0, pad=14)
        self.mode_frame.columnconfigure(1, pad=5)
        self.mode_frame.columnconfigure(2, pad=14)

        self.dna_button.grid(row=0, column=0)
        self.mrna_button.grid(row=0, column=1)
        self.trna_button.grid(row=0, column=2)

        # Always on top frame
        self.ontop_frame.pack()
        self.ontop_text.grid(row=0, column=0, padx=15)
        self.ontop_button.grid(row=0, column=1)

        # Convert Button
        self.convert_outline.pack(padx=5, pady=5, anchor="s", side="bottom")
        self.convert.config(font=("Times", 20, "bold", "italic"), padx=20, command=self.convert_func)
        self.convert.pack(padx=5, pady=5)

        # Output Frame
        self.output_frame.pack(padx=5, pady=5, side="right", anchor="ne")
        self.output_title.grid(row=0, column=0)
        self.output.grid(row=1, column=0)
        self.output.config(state=DISABLED, width=35, height=15)

        # Fire the mainloop so the window opens
        self.root.mainloop()

    def convert_func(self):
        # TODO: Do some stuff with the DNA and RNA modules finally, do something with mode selector first
        input_text: dict = self.box.get("1.0", "end-1c").replace(" ", "").replace("\n", "")
        if (input_text != ""):
            outputs = {"DNA": "", "RNA": ""}
            if (self.mode == "DNA"):
                    outputs["DNA"] = DNA(input_text)
                    outputs["RNA"] = RNA(outputs["DNA"].strand)
            elif (self.mode == "mRNA"):
                    outputs["RNA"] = RNA(input_text)
                    outputs["DNA"] = DNA(outputs["RNA"].complement)
            elif (self.mode == "tRNA"):
                    outputs["RNA"] = RNA(input_text)
                    outputs["DNA"] = DNA(outputs["RNA"].strand)
            
            if (outputs["DNA"].error or outputs["RNA"].error):
                self.put_output(f'ERROR:\n {str(outputs["DNA"].error) + "\n\n" + str(outputs["RNA"].error)}')
                return

            self.put_output(str(outputs["DNA"]) + str(outputs["RNA"]))
        else:
            self.put_output("ERROR: No Input")

    def put_output(self, text: str):
        self.output.config(state=NORMAL)
        self.output.delete("1.0", END)
        self.output.insert("1.0", text)
        self.output.config(state=DISABLED)
    
    def always_on_top(self):
        self.root.wm_attributes("-topmost", self.ontop.get())

    def mode_switcher(self, button_id: str):
        self.identifier_actual.config(text=button_id)
        self.mode = button_id

        # Probably will have to do this again for the convert function
        match button_id:
            case "DNA":
                self.identifier_frame.config(padx=45)
            case "mRNA":
                self.identifier_frame.config(padx=39)
            case "tRNA":
                self.identifier_frame.config(padx=43)


##  Start  ##

if (__name__ == "__main__"):
    WindowObject()
