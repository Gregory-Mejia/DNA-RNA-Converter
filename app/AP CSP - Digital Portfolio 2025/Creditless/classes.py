'''

    Date: 1/25/2025
    Purpose: Resources
    This is mainly for the code to be more organized. This will be called by the 'main.py' file.
    This is a modified version of the original 'classes.py' file to support RNA to DNA
    
'''

##  Classes  ##

class pair_struct:
    # Define creation behavior
    def __init__(self, rules: dict):
        # I wrote this before I wrote anything else so this may be redundant
        # 'rules' is like a look-up table. No case statement because I think this is faster.
        self.rules: dict = rules
        self.error: list = []

    # Define behavior so we can see what we need to see when we print
    def __str__(self):
        strand_str: str = self.strand.rjust(len(self.strand) + 6)
        complement_str: str = self.complement.rjust(len(self.complement) + 2)

        # Haha, these lines are just for printing the child class name.
        str_current_class: str = str(type(self))
        formatted_class: str = str_current_class[8 : len(str_current_class) - 2] # Subtract 2 because of the "'>"
        # I love fstrings because they're so much better than the constant type conversion and the + concat mess
        return f'\nClass: {formatted_class}\nStrand: {strand_str}\nComplement: {complement_str}\n'

    # Probably the more complicated function of the bunch. Does as it looks like it does.
    def convert(self, to_convert: str) -> str:
        # Add the characters to the final string after we convert the 'to_convert' parameter
        to_convert: list = split_string_into_ns(to_convert, 3)
        final: str = ""

        # We put elem outside so I can define its type (it's stupid I know)
        # I like type checking a little too much since it's very helpful for my text editor
        elem: str
        for elem in to_convert:
            if (len(elem) != 3):
                self.error.append(f'!! "{to_convert}" contains incomplete sequence: "{elem}" !!'); continue
            # We store 'index' as a separate variable since I don't want to treat it as a range() for loop
            # AND there can be multiple duplicates of the same character, so the .index() method wouldn't fit
            index: int = 0

            char: str
            for char in elem:
                # Used this over a case statement since there probably would be a bunch of repeated code
                index += 1
                if (not (char in self.rules)):
                    self.error.append(f'!! {char} is not a valid member of {self.rules} !!'); break

                # Used a ternary here since it would be more appealing to look at than a normal if statement
                # If we find 'char' to be valid, add the character to 'final'; also add a space if it's the end.
                final += self.rules[char] + (" " if (index == len(elem)) else "")

        return final
    
    def list_to_string(self, convert: list) -> str:
        # This basically is just for debugging purposes since my interpreter was acting funny
        return str(convert).replace(",", "").replace("'", "").replace("[", "").replace("]", "")
    
# DNA and RNA are defined as separate classes to make them easier to use in the main file.

class DNA(pair_struct):
    def __init__(self, strand: str, to=False):
        self.rules: dict = {"A": "T", "T": "A", "G": "C", "C": "G", "U": "A"}
        self.error: list = []

        storage: str = self.list_to_string(split_string_into_ns(strand, 3))
        self.strand: str = self.convert(storage) if (to) else storage
        self.complement: str = self.convert(self.strand)

        if ("U" in self.strand):
            self.error.append("!! U was found in DNA strand !!")

# Use the template DNA strand to get both the mRNA and tRNA
class RNA(pair_struct):
    def __init__(self, dna_strand: str, is_rna=False, mRNA=True):
        self.rules: dict = {"A": "U", "T": "A", "G": "C", "C": "G", "U": "A"}
        self.error: list = []
        template: str = self.list_to_string(split_string_into_ns(dna_strand, 3))

        self.mRNA: str = self.convert(template)
        self.tRNA: str = self.convert(self.mRNA)

        # Did this to avoid one long ternary
        if (is_rna):
            self.mRNA = template if (mRNA) else self.convert(template)
            self.tRNA = self.convert(template) if (mRNA) else template

            if ("T" in self.tRNA or "T" in self.mRNA):
                self.error.append(f'!! T was found in {("T" in self.tRNA) and "tRNA" or "mRNA"} !!')

        # Legacy components for the string function
        self.strand = self.mRNA
        self.complement = self.tRNA

    # Define the longer name versions of amino acids to match later
    amino_acids: dict = {
        "Ala": "Alanine",
        "Arg": "Arginine",
        "Asp": "Aspartic acid",
        "Asn": "Asparagine",
        "Cys": "Cysteine",
        "Gln": "Glutamine",
        "Glu": "Glutamic acid",
        "Gly": "Glycine",
        "His": "Histidine",
        "Ile": "Isoleucine",
        "Leu": "Leucine",
        "Lys": "Lycine",
        "Met": "Methionine",
        "Phe": "Phenylalanine",
        "Pro": "Proline",
        "Ser": "Serine",
        "Thr": "Threonine",
        "Trp": "Tryptophan",
        "Tyr": "Tyrosine",
        "Val": "Valine"
    }

    # These cases are entirely reliant on the first two letters
    codon_special_cases: dict = {
        "GU": "Val",
        "GC": "Ala",
        "GG": "Gly",
        "AC": "Thr",
        "CU": "Leu",
        "CC": "Pro",
        "CG": "Arg",
        "UC": "Ser"
    }

    # Now, the other ones. :sob: This could probably be done in a more efficient manor
    codon_regular_cases: dict = {
        # First key is the first 2 letters, second key is either letter
        "UU": {
            "UC": "Phe",
            "AG": "Leu"
        },
        "UA": {
            "UC": "Tyr",
            "AG": "Stop"
        },
        "UG": {
            "UC": "Cys"
        },
        "CA": {
            "UC": "His",
            "AG": "Gln"
        },
        "AU": {
            "UCA": "Ile"
        },
        "AA": {
            "UC": "Asn",
            "AG": "Lys"
        },
        "AG": {
            "UC": "Ser",
            "AG": "Arg"
        },
        "GA": {
            "UC": "Asp",
            "AG": "Glu"
        }
    }

    # The codon is not able to be generalized
    codon_exact_match: dict = {
        "UGA": "Stop",
        "UGG": "Trp",
        "AUG": "Met"
    }

    # Match the codons to the specific RNA sequence amino acids
    def match_codons_to_amino_acids(self, codon_string: str) -> list:
        # Resplit the string into thirds
        codon_string: list = split_string_into_ns(codon_string, 3)
        aaList: list = []

        # Done for more type checking shenanigans
        codon: str
        for codon in codon_string:
            # TODO: Determine which mRNA codon matches the amino acid, start with shortest searches first
            # Will have to search through 3-5 dicts :( and then append the result to 'aaList'
            
            # Easiest one down, now the others
            if (codon in self.codon_exact_match): aaList.append(self.codon_exact_match[codon]); continue

            # These two rely on the first two letters to get started
            beginning: str = codon[0:2]
            last: str = codon[2:3]
            if (beginning in self.codon_special_cases): aaList.append(self.codon_special_cases[beginning]); continue
            if (beginning in self.codon_regular_cases):
                letters: str
                for letters in self.codon_regular_cases[beginning]:
                    if (last in letters): break
                aaList.append(self.codon_regular_cases[beginning][letters])
                continue

            # Error detection
            print(f'!! {codon} is not recognized in any dictionary !!')
            aaList.append("ERROR")

        return aaList
    
    def match_amino_acid_full(self, amino_acid_list: list) -> list:
        # Use an empty storage list so we don't change our former list and potentially mess it up
        # Also, we may want to still use the old amino_acid list so we can't change it
        storage: list = []
        for acid in amino_acid_list:
            # Error detection
            if (acid == "Stop"): storage.append("Stop"); continue
            if (not acid in self.amino_acids): storage.append("ERROR"); continue
            storage.append(self.amino_acids[acid])
        return storage

##  Functions  ##

# Used to split a string every n characters
def split_string_into_ns(string: str, n: int) -> list:
    # Probably less readable but it works
    string = string.replace(" ", "").upper()

    # Used list comprehension over a regular for loop to take up less space and have less boilerplate code
    return [string[index: index + n] for index in range(0, len(string), n)]
