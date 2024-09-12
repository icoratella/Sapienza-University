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

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

with open("rosalind_pmch.txt", "r") as c:
    data = c.read()

seq = list(read_fasta(data).values())[0]
n = 0
while n < len(seq):
    l = seq[n] + str(n)
    G.add_node(l)
    n += 1


nodes = list(G.nodes())
for i in range(len(nodes)-1):
    for j in range(i+1, len(nodes)):
        if (seq[i], seq[j]) in [('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')]:
            G.add_edge(nodes[i], nodes[j])

nx.draw_circular(G, with_labels=True, font_weight='bold')
plt.show()

def factorial(x):
    fattoriale = 1
    for i in range(1, x+1):
        fattoriale *= i
    return fattoriale

print(factorial(seq.count("A")) * factorial(seq.count("G")))