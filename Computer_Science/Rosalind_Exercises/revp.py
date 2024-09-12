def read_fasta(file):
    # initialize the dictionary
    d = {}
    # initialize the sequence name
    name = ''
    # loop over the lines in the file
    for line in file:
        line = line.strip()
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

with open('rosalind_revp.txt') as file:
    d = read_fasta(file)
    s = list(d.values())[0]

def reversed_complement(s):
    d = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([d[c] for c in s[::-1]])

txt = ""
for i in range(len(s)-3):
    for k in range(min(len(s)-i, 12) , 3, -1):
        if (s[i:i+k] == reversed_complement(s[i:i+k])):
            txt += str(i+1) +' '+ str(k) + "\n"
            
with open("out5.txt", "w") as file:
    file.write(txt)