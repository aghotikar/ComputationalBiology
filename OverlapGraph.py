"""
Problem 7: Overlap Graphs

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3O3. You may return edges in any order.

-------------
Sample Dataset
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG

Sample Output
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323

"""
def construct_graph(file):
    dna_strings=[]
    edges=[]
    adjacency_list = []
    current_dna_string=''

    #Read the file line by line and store the edges and the corresponding dna strings in
    #their respective lists
    while True:
        line=file.readline().strip()
        if line == '':
            break
        else:
            if '>' in line:
                if (current_dna_string !=''):
                    dna_strings.append(current_dna_string)
                    current_dna_string=''
                edges.append(line[1:])
            else:
                current_dna_string+=line
    dna_strings.append(current_dna_string)

    #Check if 3 characters in the suffix of a string match 3 characters
    #in the succeeding string's prefix. If they do, insert the respective
    #edges into the adjacency list
    for ds1 in range(len(dna_strings)):
        for ds2 in range(ds1+1,len(dna_strings)):
            if ((dna_strings[ds1])[-3:] == (dna_strings[ds2])[0:3]):
                adjacency_list.append(edges[ds1])
                adjacency_list.append(edges[ds2])
            if ((dna_strings[ds2])[-3:] == (dna_strings[ds1])[0:3]):
                adjacency_list.append(edges[ds2])
                adjacency_list.append(edges[ds1])

    #Print the adjacency list as per the output dataset format
    for i in range(0, len(adjacency_list), 2):
        print adjacency_list[i], adjacency_list[i+1]

if __name__ == "__main__":
    with open('C:/Users/Aditi/Desktop/rosalind_grph.txt') as file:
            construct_graph(file)