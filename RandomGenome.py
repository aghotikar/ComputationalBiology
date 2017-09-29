"""
Problem 6: Introduction to Random Strings

Given: A DNA string ss of length at most 100 bp and an array
AA containing at most 20 numbers between 0 and 1.

Return: An array BB having the same length as AA in which
B[k]B[k] represents the common logarithm of the probability
that a random string constructed with the GC-content found
in A[k]A[k] will match ss exactly.

------------
Sample Dataset:
ACGATACAA
0.129 0.287 0.423 0.476 0.641 0.742 0.783

Sample Output:
-5.737 -5.217 -5.263 -5.360 -5.958 -6.628 -7.009

"""
import math

#Function to calculate the random genome probablities
def generate_random_genome(dnaString,gc_contents):
    sum_list=[]
    for gc_content in gc_contents:
        sum = 0
        for code in dnaString:
            if code in "GC":
                #symbol frequencies for G & C
                sum += math.log(gc_content/2,10)
            else:
                #symbol frequencies for A & T
                sum += math.log((1-gc_content)/2, 10)
        sum_list.append(format(sum,'.3f'))
        sum_list.append(' ')

    #format the array as per the output dataset requirements
    print ''.join(map(str,sum_list))

if __name__ == '__main__':
    fileLines = open('C:/Users/Aditi/Downloads/rosalind_prob.txt').readlines()
    dnaString = fileLines[0].strip()
    gc_contents = map(float, fileLines[1].strip().split())
    generate_random_genome(dnaString,gc_contents)