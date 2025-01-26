'''

    Written by Gregory Mejia
    Date: 1/25/2025

    Purpose: Resources
    This is mainly for the code to be more organized. This will be called by the 'main.py' file.
    
'''

##  Classes  ##

class pair_struct:
    # Define creation behavior
    def __init__(self, rules: list):
        # I wrote this before I wrote anything else so this may be redundant
        self.rules: list = rules

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
            if (len(elem) != 3): print(f'!! "{to_convert}" contains incomplete sequence: "{elem}" !!'); continue
            # We store 'index' as a separate variable since I don't want to treat it as a range() for loop
            # AND there can be multiple duplicates of the same character, so the .index() method wouldn't fit
            index: int = 0

            char: str
            for char in elem:
                # Used this over a case statement since there probably would be a bunch of repeated code
                index += 1
                if (not (char in self.rules)): print(f'!! {char} is not a valid member of {self.rules} !!'); break

                # Used a ternary here since it would be more appealing to look at than a normal if statement
                # If we find 'char' to be valid, add the character to 'final'; also add a space if it's the end.
                final += self.rules[char] + (" " if (index == len(elem)) else "")

        return final

    # This function is for the inheriting classes after they modify the '__init__' function
    def class_assignment(self, strand):
        self.strand: str = list_to_string(split_string_into_ns(strand, 3))
        self.complement: str = self.convert(self.strand)

# I have no idea if there's a better way to do this, but this is the best I can think of.
# DNA and RNA are defined as separate classes to make them easier to use in the main file.

class DNA(pair_struct):
    def __init__(self, strand: str):
        self.rules: list = {"A": "T", "T": "A", "G": "C", "C": "G"}
        self.class_assignment(strand)

class RNA(pair_struct):
    def __init__(self, strand: str):
        self.rules: list = {"A": "U", "T": "A", "G": "C", "C": "G", "U": "A"}
        self.class_assignment(strand)

##  Functions  ##

# Used to split a string every n characters
def split_string_into_ns(string: str, n: int) -> list:
    # Probably less readable but it works
    string = string.replace(" ", "").upper()

    # Used list comprehension over a regular for loop to take up less space and have less boilerplate code
    return [string[index: index + n] for index in range(0, len(string), n)]

def list_to_string(convert: list) -> str:
    # This basically is just for debugging purposes since my interpreter was acting funny
    return str(convert).upper().replace(",", "").replace("'", "").replace("[", "").replace("]", "")
