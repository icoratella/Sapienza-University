table = {
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
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

def translateDNA(string):
    s = ""
    for i in range(int(len(string)/3)):
        s += table[string[i*3:i*3+3]]
    return s

def find_all(string):
    possible_substrings = []
    for start in range(0, len(string)):
        s = translateDNA(string[start:])
        if 'M' in s:
            start = s.find('M')
            if '_' in s[start:]:
                stop = s.find('_', start)
                possible_substrings.append(s[start:stop])
    return set(possible_substrings)
              

def reverse_complement(string):
    s = ''
    for c in string:
        if c == 'A':
            s += 'T'
        elif c == 'T':
            s += 'A'
        elif c == 'C':
            s += 'G'
        elif c == 'G':
            s += 'C'
    return s[::-1]

with open('rosalind_orf.txt') as f:
    txt = f.read()
    string = ''.join(txt.split('\n')[1:])


print(*(find_all(reverse_complement(string)).union(find_all(string))), sep='\n')
  