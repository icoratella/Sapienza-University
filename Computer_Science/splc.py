def read_fasta(s):
    # initialize the dictionary
    d = {}
    # initialize the sequence name
    name = ''
    # loop over the lines in the file
    s = s.split('\n')
    for line in s:
        if line == '':
            continue
        # remove the newline character
        line = line.rstrip()
        # if the line starts with '>'
        if line.startswith('>'):
            # set the sequence name
            name = line[1:]
            # initialize the sequence
            d[name] = ''
        # otherwise
        else:
            # append the sequence
            d[name] += line
    return d

# read the fasta file
with open('rosalind_splc.txt') as f:
    data = f.read()
sequences = read_fasta(data)

# extract the gene and introns
gene = sequences.pop(list(sequences.keys())[0])
introns = list(sequences.values())

# remove the introns from the gene
for intron in introns:
    n = 0
    while n < (len(gene)-len(intron)):
        if gene[n:n+len(intron)] == intron:
            gene = gene[:n] + gene[n+len(intron):]
        n += 1

# translate the spliced gene
codon_table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'
}
protein = ''
for i in range(0, len(gene)-2, 3):
    codon = gene[i:i+3]
    aa = codon_table.get(codon, 'X')
    if aa == '*':
        break
    protein += aa

print(protein)