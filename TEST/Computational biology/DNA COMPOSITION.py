genome = "AGCTCAAAGCTTCAGCTA"

seq1 = "ATTG"
seq2 = "TAG"

print(seq1 + seq2)#"ATTGTAG"

seq3 = "ATTGATTGACC"
print(seq3[0])
#"A"
print(seq3[1:10])
#"TTGATTGAC"


# Input sequence
test_sequence = "ACAACATACAAAGGGCCACAGATACATCAAAAAATGCTCAACATCACTATTTGTCAGGGAAGTACTAATTAAAACCAAAATGAGATGTCCCCTCAAACCTGTTAGAATGGCTATTATCAAAAAGATGAAAGATAGCAACTATCAGAGAGGATGATAGAAAAGGGAACCCTTGCATCATGTACAAATTAAAAATAGAACTATCACATGATCCAAGAATCCTACTTCTGGGTATATAGCCAAAGGAATTGAAATCAATATGTCAAAGGGATATCTGCACTCCTATGTTATTGCAGCATGTTCACAATGGCCAAGATATAGAATCAACCTAACTGTTCATAGACAGATGAATGGATAAATGAAATGTGATATGGAAAATTATTCAGCCTTAAAAACAGTAGGAAATTCTGTCATTTGAGACAACGTGGATGAACCTAGAGGACATTAAGCTAAGTGAAATAAGCTAGACACAGAAAGACAAATATTGCATGATCTCACTTAGAATCTAAAAAATCTGAACTCATAGAAGCAGAGAATAGTATGATGGTTACTAGGGTTATCTGGCAGGGAGAGGATGAGGAAATGGGACATTGTTAATAAAAGGAAAAAAATTCAATTAGTAGG"

def length(string):
    length = 0
    # Make a function here that counts the number of nucleotides in the input
    # sequence, return as variable "length".
    for i in string:
        length+=1
    return length

# Print your result.
print(length(test_sequence))

def freq_lists(dna_list):
    n = len(dna_list[0])
    A = [0] * n
    T = [0] * n
    G = [0] * n
    C = [0] * n
    for dna in dna_list:
        for index, base in enumerate(dna):
            if base == 'A':
                A[index] += 1
            elif base == 'C':
                C[index] += 1
            elif base == 'G':
                G[index] += 1
            elif base == 'T':
                T[index] += 1
    return A, C, G, T
print(freq_lists(test_sequence))

# Putting it all together, our thymine counting function is
def thymine_counter(sequence):
    thymines = 0
    for base in sequence:
        if base is "T":
            thymines = thymines + 1
    return thymines

def composition(string):
    # Initialize all the counters to zero
    (thymines, cytosines, adenosines, guanines) = (0, 0, 0, 0)
    for base in string:
        if base is "A":
            adenosines = adenosines + 1
        elif base is "T":
            thymines = thymines + 1
        elif base is "C":
            cytosines = cytosines + 1
        elif base is "G":
            guanines = guanines + 1
    return {"adenosine" : adenosines, "thymine" : thymines,
            "cytosine" : cytosines, "guanine" : guanines}

print(composition(test_sequence))

h_sapiens = open('/Users/romankoval/PycharmProjects/Learning/Computational biology/human-PrR1jPIaAG.txt').readlines()[0]

print(composition(h_sapiens))

phage = open('data/phage.txt').readlines()[0]
