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


with open('rosalind_long.txt', 'r') as file:
    data = file.read()
    fasta_data = data.strip().split('>')[1:]
    sequences = {}
    for fasta in fasta_data:
        seq_id, *seq = fasta.split('\n')
        sequences[seq_id] = ''.join(seq)

G = nx.DiGraph()                                                       # unique way to unify the sequences
for seq_id in sequences:                                                 # overlap more than half of the sequence
    n = len(sequences[seq_id])//2
    for seq_id2 in sequences:
        if sequences[seq_id][:n] in sequences[seq_id2] and sequences[seq_id] != sequences[seq_id2]:  # create a graph wiht 
            m = 0
            G.add_edge(seq_id2, seq_id)

di = {}
for a in sequences:      # dictionary to collect data about nodes and to find the first seq
    di[a] = [0 , 0]
for a in G.edges():
    di[a[0]][0] += 1  # egdes starting from the node
    di[a[1]][1] += 1  # edges ending on the node


def connectstring(a, b):  # a string on the left. b string on th right
    sub = a[-100:]  # substing
    n = 0
    m = 100
    pos = 0
    while n < (len(b)-m+1):
        r_frame = b[n:n+m]   # I set the reading frame equal to len of substring
        if r_frame == sub:     #when i found a substring i immediatly save position in the list
            pos = n+m
            break
        n += 1
    return int(pos)

for a in di:
    if di[a][1] == 0:   # startin seq = node having no edges ending on it
        node = a  
s = sequences[node] #string where ill save the complete seq
for a in di:    
    for b in nx.neighbors(G,node):   # loop to axcess neighbor node of each node
        next_node = b
    if next_node == node:
        break
    cut_position = connectstring(sequences[node], sequences[next_node])  # function to find the point of join of two neighbors string
    s = s + sequences[next_node][cut_position:]
    node = next_node

print(s)