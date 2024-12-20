'''Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
Return: The adjacency list corresponding to O3. You may return edges in any order.'''
from Bio import SeqIO
def read_fasta(filename):
    identifiers=[]
    sequences=[]
    for record in SeqIO.parse(filename,"fasta"):#parse fasta using biopython function(record refers to header and seq)
        identifiers.append(record.id)
        sequences.append(str(record.seq))#add sequences of dna to empty list
    return identifiers, sequences#return list of sequences

# check if ending part of first string of length k matches starting part of second string of length k
def overlap_graph(identifiers,sequences, k):
    adjency_list=[]
    for i in range(len(sequences)):
        for j in range(len(sequences)):
            if i!=j:
                if sequences[i][-k:]==sequences[j][:k]:
                    adjency_list.append((identifiers[i],identifiers[j]))#if suffix of i of length  k is equal to prefix of j of length k, a match is found and the edge(the identifier pair)is added to the list
    return adjency_list
def main():
    filename="grph.fasta"
    identifiers, sequences=read_fasta(filename)
    adjency_list=overlap_graph(identifiers, sequences, k=3)
    for edge in adjency_list:
        print(edge[0], edge[1])
main()
