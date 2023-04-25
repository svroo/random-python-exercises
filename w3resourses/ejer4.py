# DNA complement
def dna_complements(dna):
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([complements[nucleotide] for nucleotide in dna])

print(dna_complements('ATTGC'))