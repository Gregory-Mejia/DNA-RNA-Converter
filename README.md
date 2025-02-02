# DNA RNA Converter
## AP Computer Science Principals - Digital Portfolio
This project turned into my project for the AP CSP digital portfolio as my original idea, a graphing calculator made from scratch, became way more complicated than I anticipated. You can find the main app in this repository's **'app'** folder alongside the two modified versions of the original code that comply with the rules for submitting the digital portfolio in the **'AP CSP - Digital Portfolio 2025'** folder. These folders contain nearly identical contents, but with only removed credits and comments. I wasn't sure if I should write something else to grab the icon so I didn't have to upload the file with each iteration, so I just left it as is.

## Other Information
I first started this project in my Biology class because I was bored and was fed up having to continuously look at the codon tables to find the corresponding amino acid for a sequence of mRNA codons. This started out as a simple console application, but some things happened, and now we have this.

This project was originally written in the Lua/Luau programming language, but was later converted into Python. The decision to first use Lua/Luau was made because of my 3+ years of experience with the programming language, but was later revoked to using Python because of the lack of good interpreters for GitHub codespaces, which Python has a plethora of. I also made the choice to switch to Python since I wanted to practice more with this language, and there was many more features that are appealing to use specifically for this project, like the *tkinter* library.

Additionally, keep in mind that this is one of my first experiences with actually using Python for more serious applications such as this one, so don't expect perfection or perfectly adhered industry standard formatting. There may be the occasional formatting error, nonsensical variable name thrown here and there, or simply poorly written code due to this. Also, I had no idea if I should have made the amino acid conversion tables into a JSON file. This caused me to leave them in *classes.py* in the *RNA class*.

## About Downloading
There was originally going to be a download for an exe file; however, Python's *pyinstaller* library makes incredibly bloated exe files. Yes, there are ways to reduce its bloat, but I simply wish to not get into those methods-like virtual machines-just for this simple project.

If you wish to use this application, have the Python interpreter isntalled and go to the **'app'** folder. There you'll need to download everything but that other folder in that folder. Remember to keep all of these in the same folder and to just run *main.py* as everything else is just a resource for that file to access.
