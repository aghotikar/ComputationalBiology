"""
Problem 2: Inferring mRNA from Protein

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein
could have been translated, modulo 1,000,000.
(Don't neglect the importance of the stop codon in protein translation.)

---------------

Sample dataset:
MA

Sample output:
12

"""

#The RNA codon table that maps the RNA codons to amino acids
RNA_CODON_TABLE = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

#Function to calculate the number of RNA strings that can form a protein
from collections import defaultdict

def calculate_rna_strings(protein):
    count_occurrences = defaultdict(lambda: 0)
    for code, amino_acid in RNA_CODON_TABLE.iteritems():
        count_occurrences[amino_acid] += 1

    #Calculate the number of stop codons
    stop_codons = count_occurrences['Stop']
    total_rna_strings=stop_codons

    #The total number of different RNA strings is the product of the occurrences of all
    # the codes in the codon table (including the stop codons)
    for code in protein:
        total_rna_strings = (total_rna_strings * count_occurrences[code])%1000000

    print total_rna_strings

if __name__ == "__main__":
    with open('C:/Users/Aditi/Desktop/rosalind_mrna.txt') as file:
        temp=file.read().splitlines()
        for protein in temp:
            calculate_rna_strings(protein)