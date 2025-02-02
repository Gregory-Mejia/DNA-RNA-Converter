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

class WindowObject:
    def __init__(self):

        self.root: Tk = Tk()

        self.title_frame = LabelFrame(self.root, padx=100, pady=-15)
        self.title_label = Label(self.title_frame, text="Genetic Coder", font=("Helvetica", 20, "bold"), padx=15)

        self.ontop = BooleanVar()
        self.mode = "DNA"

        self.input_frame = LabelFrame(self.root)
        self.input_title = Label(self.input_frame, text="Input", font=("Helvetica", 10))

        self.box = Text(self.input_frame)

        self.output_frame = LabelFrame(self.root)
        self.output_title = Label(self.output_frame, text="Output", font=("Helvetica", 10))

        self.output = Text(self.output_frame)

        self.middle_frame = LabelFrame(self.root, pady=4)
        self.middle_title = Label(self.middle_frame, text="Controls", font=("Helvetica", 25, "bold"))

        self.convert_outline = LabelFrame(self.middle_frame)
        self.convert = Button(self.convert_outline, text="Convert Strand")

        identifier_font = ("Helvetica", 13)
        self.identifier_frame = LabelFrame(self.middle_frame, padx=45, pady=5)
        self.identifier_text = Label(self.identifier_frame, text="Current Mode: ", font=identifier_font)
        self.identifier_actual = Label(self.identifier_frame, text="DNA", font=identifier_font)

        mode_font = ("Helvetica", 12)

        self.mode_frame = LabelFrame(self.middle_frame, padx=5, pady=5)
        self.dna_button = Button(
                self.mode_frame, text="DNA", padx=10, font=mode_font, command=lambda: self.mode_switcher("DNA")
            )
        self.mrna_button = Button(
                self.mode_frame, text="mRNA", padx=5, font=mode_font, command=lambda: self.mode_switcher("mRNA")
            )
        self.trna_button = Button(
                self.mode_frame, text="tRNA", padx=10, font=mode_font, command=lambda: self.mode_switcher("tRNA")
            )

        self.ontop_frame = LabelFrame(self.middle_frame, padx=37, pady=3)
        self.ontop_button = Checkbutton(self.ontop_frame, command=self.always_on_top, variable=self.ontop)
        self.ontop_text = Label(self.ontop_frame, text="Always Ontop?", font=identifier_font)

        self.root.title("Genetic Coder")
        self.root.resizable(False, False)

        self.title_frame.pack(padx=5, pady=5, side="top", anchor="center")
        self.title_label.pack()

        self.input_frame.pack(padx=5, pady=5, side="left", anchor="nw")
        self.input_title.grid(row=0, column=0)
        self.box.grid(row=1, column=0)
        self.box.config(width=35, height=15)

        self.middle_frame.pack(padx=3, pady=5, anchor="center", side="left")
        self.middle_title.pack(anchor="center", side="top")

        self.identifier_frame.pack(padx=5, pady=3)
        self.identifier_text.grid(row=0, column=0)
        self.identifier_actual.grid(row=0, column=1)

        self.mode_frame.pack(padx=5, pady=5)
        self.mode_frame.columnconfigure(0, pad=14)
        self.mode_frame.columnconfigure(1, pad=5)
        self.mode_frame.columnconfigure(2, pad=14)

        self.dna_button.grid(row=0, column=0)
        self.mrna_button.grid(row=0, column=1)
        self.trna_button.grid(row=0, column=2)

        self.ontop_frame.pack()
        self.ontop_text.grid(row=0, column=0, padx=15)
        self.ontop_button.grid(row=0, column=1)

        self.convert_outline.pack(padx=5, pady=5, anchor="s", side="bottom")
        self.convert.config(font=("Times", 20, "bold", "italic"), padx=20, command=self.convert_func)
        self.convert.pack(padx=5, pady=5)
      
        self.output_frame.pack(padx=5, pady=5, side="right", anchor="ne")
        self.output_title.grid(row=0, column=0)
        self.output.grid(row=1, column=0)
        self.output.config(state=DISABLED, width=35, height=15)

        self.root.after(25, lambda: self.root.iconbitmap("icon.ico"))
        self.root.mainloop()

    def convert_func(self):
        input_text: dict = self.box.get("1.0", "end-1c").replace(" ", "").replace("\n", "")
        if (input_text != ""):
            outputs = {"DNA": "", "RNA": "", "Amino Acids": []}
            if (self.mode == "DNA"):
                outputs["DNA"] = DNA(input_text)
                outputs["RNA"] = RNA(outputs["DNA"].strand)
            else:
                outputs["RNA"] = RNA(input_text, is_rna=True, mRNA=True if (self.mode == "mRNA") else False)
                outputs["DNA"] = DNA(outputs["RNA"].strand, True)
            
            if (outputs["DNA"].error or outputs["RNA"].error):
                self.put_output(f'ERROR:\n {str(outputs["DNA"].error) + "\n\n" + str(outputs["RNA"].error)}')
                return

            outputs["Amino Acids"] = outputs["RNA"].match_codons_to_amino_acids(outputs["RNA"].mRNA)
            self.put_output(f'''Class DNA:
    Strand:     {outputs["DNA"].strand}
    Complement: {outputs["DNA"].complement}

Class RNA:
    mRNA: {outputs["RNA"].mRNA}
    tRNA: {outputs["RNA"].tRNA}

Amino Acids:
{outputs["RNA"].list_to_string(outputs["Amino Acids"])}

Full Amino Acid Names:
{outputs["RNA"].list_to_string(outputs["RNA"].match_amino_acid_full(outputs["Amino Acids"]))}''')
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

        match button_id:
            case "DNA":
                self.identifier_frame.config(padx=45)
            case "mRNA":
                self.identifier_frame.config(padx=39)
            case "tRNA":
                self.identifier_frame.config(padx=43)

if (__name__ == "__main__"):
    WindowObject()
  
