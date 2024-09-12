codons = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""

cod_dic = {}
for line in codons.strip().split('\n'):
    for codon, aa in zip(line.split()[::2], line.split()[1::2]):
        cod_dic[codon] = aa

# Read RNA sequence from file
with open('rosalind_prot.txt') as f:
    rna_seq = f.read().strip()

# Convert RNA sequence to amino acid sequence using genetic code
aa_seq = []
codon_count = len(rna_seq) // 3
for i in range(codon_count):
    codon = rna_seq[i*3:(i+1)*3]
    aa = cod_dic[codon]
    if aa == 'Stop':
        break
    aa_seq.append(aa)

# Print the amino acid sequence
print(''.join(aa_seq))