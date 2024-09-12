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
j = 0
for i in range(len(t)):
    found = False
    for k in range(j, len(s)):
        if t[i] == s[k]:
            indices.append(k + 1)
            j = k + 1
            found = True
            break
    if not found:
        break

print(' '.join(list(map(str, indices))))