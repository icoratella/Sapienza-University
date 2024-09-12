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




with open("rosalind_grph.txt") as file:
    txt = file.read()
d = read_fasta(txt)
strings = list(d.values())



k = 3

edges = [] # list of tuples

for stringName1 in d.keys():
    for stringName2 in d.keys():
        if stringName1 == stringName2:
            continue
        if d[stringName1][-k:] == d[stringName2][:k]:
            edges.append((stringName1, stringName2))

txt = ""
for t in edges:
    txt += t[0] +" " + t[1] + '\n'
with open('graph.txt', 'w') as file:
    file.write(txt)