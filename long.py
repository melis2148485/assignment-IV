'''Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format 
(which represent reads deriving from the same strand of a single linear chromosome).
The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the 
entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their 
length.
Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed 
chromosome).'''
from Bio import SeqIO
def read_fasta(filename):
    sequences=[]
    for record in SeqIO.parse(filename,"fasta"):
        sequences.append(str(record.seq))
    return sequences

#find the maximum overlap between 2 strings
def max_overlap(s1,s2):
    max_o=0
    merged_strings=s1+s2
    for i in range(1,len(s1)):
        if s2.startswith(s1[-i:]):
            if i>max_o:
                max_o=i
                merged_strings=s1+s2[i:]
    return max_o, merged_strings

#function for shortest superstring 
def max_superstring(sequences):
    while len(sequences)>1:
        max_length=-1
        best_pair=(0,0)
        best_merged=""
        for i in range(len(sequences)):
            for j in range(len(sequences)):
                if i!=j:
                    overlap_length, merged=max_overlap(sequences[i], sequences[j])
                    if overlap_length>max_length:
                        max_length=overlap_length
                        best_pair=(i,j)
                        best_merged=merged
    #merge best pair found
        i,j=best_pair
        sequences[i]=best_merged
        sequences.pop(j)
    return sequences[0]
def main():
    filename="long.fasta"
    sequences=read_fasta(filename)
    superstring=max_superstring(sequences)
    print(superstring)

if __name__ == '__main__':
    main()
