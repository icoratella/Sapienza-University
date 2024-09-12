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


with open('rosalind_lcsm.txt', 'r') as file:
    s = file.read()
    d = read_fasta(s)



l = list(d.values())

substrings = []
for i in range(len(l[0])-1):
    for k in range(len(l[0])-i, 0, -1):
        substr = l[0][i : i+k]
        notFound = False
        for string in l:
            if substr not in string:
                notFound = True
                break

        if not notFound:
            substrings.append(substr)

print(sorted(substrings, key=len, reverse=True)[0])
