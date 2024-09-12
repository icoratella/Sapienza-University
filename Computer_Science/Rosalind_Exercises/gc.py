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

with open('rosalind_gc.txt') as f:
    txt = f.read()

vmax = -100
vmax_name = ''
for name, s in read_fasta(txt).items():
    v = (s.count('C') + s.count('G'))/len(s)*100
    if v > vmax:
        vmax = v
        vmax_name = name

print(vmax_name)
print(round(vmax,7))