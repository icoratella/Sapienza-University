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
with open('rosalind_sseq.txt') as file:
    txt = file.read()
    d = read_fasta(txt)

s, t = list(d.values())

indices = []
for i in range(len(t)):
    v = s.index(t[i], indices[-1]+1 if len(indices) > 0 else 0)
    indices.append(v)
print(' '.join(list(map(lambda k: str(k), indices))))