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

transition_d = [['A', 'G'], ['C', 'T']]


def transition_transversion(s1, s2):
    transition = 0 
    transversion = 0 
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            continue
        if sorted([s1[i], s2[i]]) in transition_d:
            transition += 1
        else:
            transversion += 1
    return transition/transversion
with open('rosalind_tran.txt') as file:
    txt = file.read()
    d = read_fasta(txt)

s1,s2 = list(d.values())
print(transition_transversion(s1, s2))