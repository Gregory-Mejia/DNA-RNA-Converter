class pair_struct:
    def __init__(self, rules: dict):
        self.rules: dict = rules
        self.error: list = []

    def __str__(self):
        strand_str: str = self.strand.rjust(len(self.strand) + 6)
        complement_str: str = self.complement.rjust(len(self.complement) + 2)

        str_current_class: str = str(type(self))
        formatted_class: str = str_current_class[8 : len(str_current_class) - 2]
        return f'\nClass: {formatted_class}\nStrand: {strand_str}\nComplement: {complement_str}\n'

    def convert(self, to_convert: str) -> str:
        to_convert: list = split_string_into_ns(to_convert, 3)
        final: str = ""

        elem: str
        for elem in to_convert:
            if (len(elem) != 3):
                self.error.append(f'!! "{to_convert}" contains incomplete sequence: "{elem}" !!'); continue
            index: int = 0

            char: str
            for char in elem:
                index += 1
                if (not (char in self.rules)):
                    self.error.append(f'!! {char} is not a valid member of {self.rules} !!'); break

                final += self.rules[char] + (" " if (index == len(elem)) else "")

        return final
    
    def list_to_string(self, convert: list) -> str:
        return str(convert).replace(",", "").replace("'", "").replace("[", "").replace("]", "")

class DNA(pair_struct):
    def __init__(self, strand: str, to=False):
        self.rules: dict = {"A": "T", "T": "A", "G": "C", "C": "G", "U": "A"}
        self.error: list = []

        storage: str = self.list_to_string(split_string_into_ns(strand, 3))
        self.strand: str = self.convert(storage) if (to) else storage
        self.complement: str = self.convert(self.strand)

        if ("U" in self.strand):
            self.error.append("!! U was found in DNA strand !!")

class RNA(pair_struct):
    def __init__(self, dna_strand: str, is_rna=False, mRNA=True):
        self.rules: dict = {"A": "U", "T": "A", "G": "C", "C": "G", "U": "A"}
        self.error: list = []
        template: str = self.list_to_string(split_string_into_ns(dna_strand, 3))

        self.mRNA: str = self.convert(template)
        self.tRNA: str = self.convert(self.mRNA)

        if (is_rna):
            self.mRNA = template if (mRNA) else self.convert(template)
            self.tRNA = self.convert(template) if (mRNA) else template

            if ("T" in self.tRNA or "T" in self.mRNA):
                self.error.append(f'!! T was found in {("T" in self.tRNA) and "tRNA" or "mRNA"} !!')

        self.strand = self.mRNA
        self.complement = self.tRNA

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

    codon_regular_cases: dict = {
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

    codon_exact_match: dict = {
        "UGA": "Stop",
        "UGG": "Trp",
        "AUG": "Met"
    }

    def match_codons_to_amino_acids(self, codon_string: str) -> list:
        codon_string: list = split_string_into_ns(codon_string, 3)
        aaList: list = []

        codon: str
        for codon in codon_string:
            if (codon in self.codon_exact_match): aaList.append(self.codon_exact_match[codon]); continue

            beginning: str = codon[0:2]
            last: str = codon[2:3]
            if (beginning in self.codon_special_cases): aaList.append(self.codon_special_cases[beginning]); continue
            if (beginning in self.codon_regular_cases):
                letters: str
                for letters in self.codon_regular_cases[beginning]:
                    if (last in letters): break
                aaList.append(self.codon_regular_cases[beginning][letters])
                continue

            print(f'!! {codon} is not recognized in any dictionary !!')
            aaList.append("ERROR")

        return aaList
    
    def match_amino_acid_full(self, amino_acid_list: list) -> list:
        storage: list = []
        for acid in amino_acid_list:
            if (acid == "Stop"): storage.append("Stop"); continue
            if (not acid in self.amino_acids): storage.append("ERROR"); continue
            storage.append(self.amino_acids[acid])
        return storage

def split_string_into_ns(string: str, n: int) -> list:
    string = string.replace(" ", "").upper()

    return [string[index: index + n] for index in range(0, len(string), n)]
  
