"""
Problem 3: RNA Splicing

Given: A DNA string ss (of length at most 1 kbp) and a collection of
substrings of ss acting as introns. All strings are given in FASTA
format.

Return: A protein string resulting from transcribing and translating
the exons of ss.
(Note: Only one solution will exist for the dataset provided.)

---------------

Sample dataset:
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT

Sample output:
MVYIADKQHVASREAYGHMFKVCA

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

#Function to calculate the protein string
def rnaSplicing(file):
    intron=''
    dnaString=''
    protein=''
    dnaStringRead=True
    dnaStringIdentifier=file.readline()
    #Handling FASTA format to read the file. Anything following '>' is ignored
    #as it is the identifier name. The string immediately in the next line is
    #read. The first such string occurring is the complete DNA string. Such
    #subsequent strings(i.e substrings of the main string) are the introns.
    while True:
        line=file.readline().strip()
        intron=''
        if line=='':
            break
        else:
            #Read the DNA string
            while (('>' not in line) & (dnaStringRead == True)):
                dnaString+=line
                line = file.readline().strip()
            dnaStringRead=False
            if ('>' not in line):
                intron=line
                #Delete the introns and concatenate the exons
                dnaString=dnaString.replace(intron,'')

# Transcribe the DNA to an RNA string
    rnaString = dnaString.replace('T', 'U')

 # Translate the exons of the RNA string to a protein
    for i in range(0, len(rnaString)-2, 3):
        if RNA_CODON_TABLE[rnaString[i:i + 3]] == 'Stop':
            return protein
        else:
            protein = protein + RNA_CODON_TABLE[rnaString[i:i + 3]]
    return protein

if __name__ == '__main__':
    with open('C:/Users/Aditi/Desktop/rosalind_splc.txt') as file:
        output_dataset = rnaSplicing(file)
    print output_dataset