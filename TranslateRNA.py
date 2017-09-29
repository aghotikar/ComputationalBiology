"""
Problem 5: Translating RNA into Protein

Given: An RNA string ss corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by ss.

-----------
Sample Dataset:
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output:
MAMAPRTEINSTRING

"""
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

#Function to determine the protein encoded by the RNA string
def translateRNA(input_file):
    protein=''
    with open(input_file) as file:
        for rnaString in file:
            for i in range(0,len(rnaString),3):
                if RNA_CODON_TABLE[rnaString[i:i+3]] == 'Stop':
                    return protein
                else:
                    protein = protein + RNA_CODON_TABLE[rnaString[i:i+3]]

if __name__ == '__main__':
    file='C:/Users/Aditi/Desktop/rosalind_prot.txt'
    output_dataset = translateRNA(file)
    print output_dataset