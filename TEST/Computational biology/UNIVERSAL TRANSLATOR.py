
codon_to_AA = {'AUG': 'M', 'GCG': 'A', 'UCA': 'S', 'GAA': 'E', 'GGG': 'G', 'GGU': 'G', 'AAA': 'K', 'GAG': 'E', 'AAU': 'N', 'CUA': 'L', 'CAU': 'H', 'UCG': 'S', 'UAG': 'STOP', 'GUG': 'V', 'UAU': 'Y', 'CCU': 'P', 'ACU': 'T', 'UCC': 's', 'CAG': 'Q', 'CCA': 'P', 'UAA': 'STOP', 'AGA': 'R', 'ACG': 'T', 'CAA': 'Q', 'UGU': 'C', 'GCU': 'A', 'UUC': 'F', 'AGU': 'S', 'AUA': 'I', 'UUA': 'L', 'CCG': 'P', 'AUC': 'I', 'UUU': 'F', 'CGU': 'R', 'UGA': 'STOP', 'GUA': 'V', 'UCU': 'S', 'CAC': 'H', 'GUU': 'V', 'GAU': 'D', 'CGA': 'R', 'GGA': 'G', 'GUC': 'V', 'GGC': 'G', 'UGC': 'C', 'CUG': 'L', 'CUC': 'L', 'CGC': 'R', 'CGG': 'R', 'AAC': 'N', 'GCC': 'A', 'AUU': 'I', 'AGG': 'R', 'GAC': 'D', 'ACC': 'T', 'AGC': 'S', 'UAC': 'Y', 'ACA': 'T', 'AAG': 'K', 'GCA': 'A', 'UUG': 'L', 'CCC': 'P', 'CUU': 'L', 'UGG': 'W'}

gdh = 'AUGGAUCAGACAUAUUCUCUGGAGUCAUUCCUCAACCAUGUCCAAAAGCGCGACCCGAAUCAAACCGAGUUCGCGCAAGCCGUUCGUGAAGUAAUGACCACACUCUGGCCUUUUCUUGAACAAAAUCCAAAAUAUCGCCAGAUGUCAUUACUGGAGCGUCUGGUUGAACCGGAGCGCGUGAUCCAGUUUCGCGUGGUAUGGGUUGAUGAUCGCAACCAGAUACAGGUCAACCGUGCAUGGCGUGUGCAGUUCAGCUCUGCCAUCGGCCCGUACAAAGGCGGUAUGCGCUUCCAUCCGUCAGUUAACCUUUCCAUUCUCAAAUUCCUCGGCUUUGAACAAACCUUCAAAAAUGCCCUGACUACUCUGCCGAUGGGCGGUGGUAAAGGCGGCAGCGAUUUCGAUCCGAAAGGAAAAAGCGAAGGUGAAGUGAUGCGUUUUUGCCAGGCGCUGAUGACUGAACUGUAUCGCCACCUGGGCGCGGAUACCGACGUUCCGGCAGGUGAUAUCGGGGUUGGUGGUCGUGAAGUCGGCUUUAUGGCGGGGAUGAUGAAAAAGCUCUCCAACAAUACCGCCUGCGUCUUCACCGGUAAGGGCCUUUCAUUUGGCGGCAGUCUUAUUCGCCCGGAAGCUACCGGCUACGGUCUGGUUUAUUUCACAGAAGCAAUGCUAAAACGCCACGGUAUGGGUUUUGAAGGGAUGCGCGUUUCCGUUUCUGGCUCCGGCAACGUCGCCCAGUACGCUAUCGAAAAAGCGAUGGAAUUUGGUGCUCGUGUGAUCACUGCGUCAGACUCCAGCGGCACUGUAGUUGAUGAAAGCGGAUUCACGAAAGAGAAACUGGCACGUCUUAUCGAAAUCAAAGCCAGCCGCGAUGGUCGAGUGGCAGAUUACGCCAAAGAAUUUGGUCUGGUCUAUCUCGAAGGCCAACAGCCGUGGUCUCUACCGGUUGAUAUCGCCCUGCCUUGCGCCACCCAGAAUGAACUGGAUGUUGACGCCGCGCAUCAGCUUAUCGCUAAUGGCGUUAAAGCCGUCGCCGAAGGGGCAAAUAUGCCGACCACCAUCGAAGCGACUGAACUGUUCCAGCAGGCAGGCGUACUAUUUGCACCGGGUAAAGCGGCUAAUGCUGGUGGCGUCGCUACAUCGGGCCUGGAAAUGGCACAAAACGCUGCGCGCCUGGGCUGGAAAGCCGAGAAAGUUGACGCACGUUUGCAUCACAUCAUGCUGGAUAUCCACCAUGCCUGUGUUGAGCAUGGUGGUGAAGGUGAGCAAACCAACUACGUGCAGGGCGCGAACAUUGCCGGUUUUGUGAAGGUUGCCGAUGCGAUGCUGGCGCAGGGUGUGAUUUAA'
map = {'AUG': 'M',
       'GCG': 'A',
       'UCA': 'S',
       'GAA': 'E',
       'GGG': 'G',
       'GGU': 'G',
       'AAA': 'K',
       'GAG': 'E',
       'AAU': 'N', 'CUA': 'L', 'CAU': 'H', 'UCG': 'S', 'UAG': 'STOP', 'GUG': 'V', 'UAU': 'Y', 'CCU': 'P', 'ACU': 'T', 'UCC': 's', 'CAG': 'Q', 'CCA': 'P', 'UAA': 'STOP', 'AGA': 'R', 'ACG': 'T', 'CAA': 'Q', 'UGU': 'C', 'GCU': 'A', 'UUC': 'F', 'AGU': 'S', 'AUA': 'I', 'UUA': 'L', 'CCG': 'P', 'AUC': 'I', 'UUU': 'F', 'CGU': 'R', 'UGA': 'STOP', 'GUA': 'V', 'UCU': 'S', 'CAC': 'H', 'GUU': 'V', 'GAU': 'D', 'CGA': 'R', 'GGA': 'G', 'GUC': 'V', 'GGC': 'G', 'UGC': 'C', 'CUG': 'L', 'CUC': 'L', 'CGC': 'R', 'CGG': 'R', 'AAC': 'N', 'GCC': 'A', 'AUU': 'I', 'AGG': 'R', 'GAC': 'D', 'ACC': 'T', 'AGC': 'S', 'UAC': 'Y', 'ACA': 'T', 'AAG': 'K', 'GCA': 'A', 'UUG': 'L', 'CCC': 'P', 'CUU': 'L', 'UGG': 'W'}

def translate(rna):
    # Modify the function here.
    # Read the RNA sequence codon-by-codon and write the string "protein" according to the genetic code dict.
    protein=[]
    start = 0
    while start + 2 < len(rna):
        codon = rna[start:start + 3]
        protein.append(map[codon])
        start += 3
    return ''.join(protein)

print(translate(gdh))

from Bio.Seq import *




# Answer
def translate(RNA):
    protein = []
    ## Find the start codon in the RNA sequence.
    start = RNA.find('AUG')
    ## Proceed forwards in the sequence until the end.
    while start+2 < len(RNA):
        ## Read in the next codon.
        codon = RNA[start:start+3]
        ## Break if the codon is a stop codon.
        if map[codon]=="STOP":
            print("STOPPED!");
            break
        ## Add the translated codon to the end of the protein string.
        protein.append(map[codon])
        start+=3
    return ''.join(protein)
print(translate(gdh))

# Import the sequence and alphabet toolboxes from the Biopython library
from Bio.Seq import Seq
import warnings
warnings.filterwarnings("ignore")

# Import the sequence of a bacterial DNA genome (called a plasmid) as a Seq object.
plasmid = open('data/salmonella.txt').readlines()[0]
table = 1
seq = Seq(plasmid)

# Define an ORF finding function
def orf_finder(seq):
    output = []
    # The function can search the RNA sequence offset by 0, 1 or 2
    for frame in range(3):
        # From the first frame on, the sequence is translated using the translate() method
        for pro in seq[frame:].translate(table).split("*"):
            # Modify the function here:
			# If the protein is longer than 100 amino acids, and it starts with
			# the starting codon M, record it. Right now it records everything.
            output.append("%s...%s" % (pro[:30], pro[-3:]))
    return output

orfs = orf_finder(seq)

for i in range(25):
    print("ORF ",i+1, " ",orfs[i])



# Define an ORF finding function
def orf_finder(seq):
    output = []
    # The function can search the RNA sequence offset by 0, 1 or 2
    for frame in range(3): 
        # From the first frame on, the sequence is translated using the translate() method
        for pro in seq[frame:].translate(table).split("*"):
            # If the protein is longer than 100 amino acids, and it starts with the starting codon M, record it.
            if len(pro) > 100 and pro[0] == "M":
                output.append("%s...%s Amino Acids: %i, Frame offset: %i" \
                % (pro[:30], pro[-3:], len(pro), frame))
    return output