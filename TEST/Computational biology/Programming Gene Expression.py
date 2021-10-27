gene = "TCAGACTGGTGCCGTGGTGCTCTCGCCCGATGTGACGTCGACCGCCAGCGGCGCGATGACGCCGAGGATTTCCGTGATCGTTTCGGAGGGCACGCCGGCTGCGGTCAGCGCGTCGGCCAAGTGTCCGGCGACCAGGCTGAAGTGGTGCATGGTAATTCCGCGCCCCTGATGGACTTGCTTCATCGGCGCACCGGTATAGGGCTCGGGCCCGCCAAGCGCGGCCGCGAAAAACTCCACCTGCTTGCCCTTGAGGCGGCTCATGTTCGTACCGCTGAAGAAGGCCGATAGTTGGTCATCGGCAAGCACACGAACATAGAAGTCCTCGACGACGACTTCGATGGCCTCATGCCCGCCGATCTTGTCGTAGATGCTGATCGGCTCACGTTTGCGCAAGCGTGACAGTAGTCCCATTTTTATA"

def complement(seq):
    comp_seq = ""
    for x in seq:
        if x == "T":
            comp_seq +="A"
        elif x == "C":
            comp_seq +="G"
        elif x == "G":
            comp_seq +="C"
        elif x =="A" :
            comp_seq +="T"

    # Find complement sequence.
    return comp_seq
print(complement(gene))


# answer
def complement(Sequence):
    compseq = []
    ## Iterate through the sequence string, replacing each nucleotide with its complement
    ## according to the base-pairing rules
    for i in Sequence:
        if i == "T":
            compseq.append("A")
        elif i == "A":
            compseq.append("T")
        elif i == "G":
            compseq.append("C")
        elif i == "C":
            compseq.append("G")
    ## Return a combined string of the complement sequence.
    return ''.join(compseq)

def reverse(Sequence):
    return Sequence[::-1]

def reverse_complement(Sequence):
    compseq = []
    for i in Sequence:
        if i == "T":
            compseq.append("A")
        elif i == "A":
            compseq.append("T")
        elif i == "G":
            compseq.append("C")
        elif i == "C":
            compseq.append("G")
    compsequence = ''.join(compseq)
    return compsequence[::-1]

print(reverse_complement(gene))

# Import the sequence from the Biopython library
from Bio.Seq import *

# Define a sequence as a DNA Seq object
seq = Seq("CCTCAGCGAGGACAGCAAGGGACTAGCC")

# The complement() method can act just like your complement() function.
complement_1 = seq.complement()
print(complement_1)
# Similarly, we can use the reverse_complement() method.
reverse_complement = seq.reverse_complement()
print(reverse_complement)
# We can even use the transcribe() method to switch alphabets to RNA
RNA = seq.transcribe()
print(RNA)