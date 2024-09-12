with open('rosalind_revc.txt') as f:
    lines = f.read()
new_dna = ''
for index_char in range(len(lines)-1, -1, -1):
    new_dna += lines[index_char]

comp = []
for char in new_dna:
    if char == 'A':
        comp.append('T')
    elif char == 'T':
        comp.append('A')
    elif char == 'C':
        comp.append('G')
    elif char == 'G':
        comp.append('C')
print(''.join(comp))

