'''

    Written by Gregory Mejia
    Date: 1/28/2025

    # For testing purposes

'''

##  Dependancies Importing  ##

from classes import DNA
from classes import RNA

##  Variables  ##

template_strand = DNA("CCA TAT GTA GAA GGG CGG AGT")
rna_strand = RNA(template_strand.strand)

codon_match = rna_strand.match_codons_to_amino_acids(rna_strand.mRNA)

##  Functions  ##

print(template_strand)
print(rna_strand)
print(codon_match)
print(rna_strand.match_amino_acid_full(codon_match))
