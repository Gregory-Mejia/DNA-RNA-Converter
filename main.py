def split_string_into_ns(string: str, n: int) -> list:
    string = string.replace(" ", "")
    string = string.upper()
    return [string[index: index + n] for index in range(0, len(string), n)]

def list_to_string(convert: list) -> str:
    return str(convert).upper().replace(",", "").replace("'", "").replace("[", "").replace("]", "")

class pair_struct:
    def __init__(self, rules: list):
        self.rules: list = rules

    def __str__(self):
        strand_str: str = self.strand.rjust(len(self.strand) + 6)
        complement_str: str = self.complement.rjust(len(self.complement) + 2)

        class_str: str = str(type(self))
        return f'\nClass: {class_str[17 : len(class_str) - 2]}\nStrand: {strand_str}\nComplement: {complement_str}\n'

    def convert(self, to_convert: str) -> str:
        to_convert = split_string_into_ns(to_convert, 3)
        final = ""
        for elem in to_convert:
            if (len(elem) != 3): print(f'!! "{to_convert}" contains incomplete sequence: "{elem}" !!'); continue
            index = 0

            for char in elem:
                index += 1
                if (not (char in self.rules)): print(f'!! {char} is not a valid member of {self.rules} !!'); break
                final += self.rules[char] + (" " if (index == len(elem)) else "")

        return final

    def class_assignment(self, strand):
        self.strand: str = list_to_string(split_string_into_ns(strand, 3))
        self.complement: str = self.convert(self.strand)

class DNA(pair_struct):
    def __init__(self, strand: str):
        self.rules = {"A": "T", "T": "A", "G": "C", "C": "G"}
        self.class_assignment(strand)

class RNA(pair_struct):
    def __init__(self, strand: str):
        self.rules = {"A": "U", "T": "A", "G": "C", "C": "G", "U": "A"}
        self.class_assignment(strand)

print(DNA("attgttagccagcgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(RNA("aaauuutttgccgtu"))
