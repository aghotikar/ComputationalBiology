import fileinput

for line in fileinput.input('C:/Users/Aditi/Downloads/rosalind_dna (1).txt'):
    count_no_a = 0
    count_no_c = 0
    count_no_g = 0
    count_no_t = 0
    for i in line:
        if i == 'A':
            count_no_a=count_no_a+1
        elif i == 'C':
            count_no_c=count_no_c+1
        elif i == 'G':
            count_no_g=count_no_g+1
        elif i == 'T':
            count_no_t=count_no_t+1
    print str(count_no_a) + ' ' + str(count_no_c) + ' ' + str(count_no_g) + ' ' + str(count_no_t)
