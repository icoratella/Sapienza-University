import numpy as np

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


with open('rosalind_cons.txt') as f:
    txt = f.read()

m = np.array(list(map(lambda k: list(k), list(read_fasta(txt).values()))))

cs = ['A', 'C', 'G', 'T']
d = [[], [], [], []]
for col in m.T:
    for c in cs:
        d[cs.index(c)].append((col == c).sum())

for i in range(m.shape[1]):
    print(cs[np.argmax(np.array(d)[:,i])], end='')
print('')
for i,c  in enumerate(cs):
    print(c, end=': ')
    print(*d[i], sep=' ')