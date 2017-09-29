"""
Edit: Minor logic correction to my previously submitted(7 accepted) solutions.
Now, I'm also checking the length of the largest overlap and not just if they overlap
by more than half.

Problem 4: Genome Assembly as Shortest Superstring

Given: At most 50 DNA strings of equal length, not exceeding 1 kbp, in FASTA format
(which represent reads deriving from the same strand of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique
way to reconstruct the entire chromosome from these reads by gluing together pairs
of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).
--------------
Sample Dataset:
>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC

Sample Output:
ATTAGACCTGCCGGAATAC
"""
#Read the FASTA formatted file
def start_processing_strings(file):
    current_dna_string=''
    dna_strings=[]
    while True:
        line=file.readline().strip()
        if line == '':
            break
        else:
            if '>' in line:
                if (current_dna_string !=''):
                    dna_strings.append(current_dna_string)
                    current_dna_string=''
            else:
                current_dna_string+=line
    dna_strings.append(current_dna_string)
    return dna_strings

#Function containing actual logic of finding the shortest superstring.
def find_shortest_superstring(dna_strings, shortestsuperstring):
    current_target=''
    current_length=0
    final_target = ''
    final_length = 0
    startswith=False
    endswith=False
    if not len(dna_strings) == 0:
        #This condition is encountered when this function is called for the first time
        if len(shortestsuperstring) == 0:
            shortestsuperstring = dna_strings.pop(0)
            return find_shortest_superstring(dna_strings, shortestsuperstring)
        else:
            for i in range(len(dna_strings)):
                current_string = dna_strings[i]
                #Check for the largest overlap
                for j in range((len(current_string))/2):
                    if shortestsuperstring.startswith(current_string[j:]):
                        current_target = current_string[:j]
                        current_length = len(current_string)
                        if (current_length > final_length):
                            final_target = current_target
                            final_length = current_length
                            startswith = True

                    if shortestsuperstring.endswith(current_string[:(len(current_string)) - j]):
                        current_target = current_string[(len(current_string)) - j:]
                        current_length = len(current_string)
                        if (current_length > final_length):
                            final_target = current_target
                            final_length = current_length
                        endswith = True

                    if (startswith == True):
                        dna_strings.pop(i)
                        shortestsuperstring = final_target + shortestsuperstring
                        return find_shortest_superstring(dna_strings, shortestsuperstring)
                    if (endswith == True):
                        dna_strings.pop(i)
                        shortestsuperstring = shortestsuperstring + final_target
                        return find_shortest_superstring(dna_strings, shortestsuperstring)


    else:
        return shortestsuperstring

if __name__ == "__main__":

    shortestsuperstring=''
    with open('C:/Users/Aditi/Desktop/rosalind_long4.txt') as file:
        input_dataset = start_processing_strings(file)

    output_dataset= find_shortest_superstring(input_dataset,'')
    print output_dataset