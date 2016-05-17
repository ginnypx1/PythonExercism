# Hamming - Write a program that can calculate the Hamming difference between two DNA strands.

#It is found by comparing two DNA strands and counting how many of the nucleotides are different from their equivalent in the other string.

#    GAGCCTACTAACGGGAT
#    CATCGTAATGACGGCCT
#    ^ ^ ^  ^ ^    ^^

#The Hamming distance between these two DNA strands is 7.

def distance(dna1, dna2):
    return sum((a != b) for (a, b) in zip(dna1, dna2))
