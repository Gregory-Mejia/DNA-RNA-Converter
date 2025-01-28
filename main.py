'''

    Written by Gregory Mejia
    Date: 1/25/2025

'''

##  Dependancies Importing  ##

from classes import DNA
from classes import RNA

##  Variables  ##

template_strand = DNA("taa gca gcg gga atc")
rna_strand = RNA(template_strand.strand)

##  Functions  ##

print(template_strand)
print(rna_strand)
print(rna_strand.match_codons_to_amino_acids(rna_strand.mRNA))
print(rna_strand.match_amino_acid_full(rna_strand.match_codons_to_amino_acids(rna_strand.mRNA)))