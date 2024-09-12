import math

with open('Rosalind/rosalind_prob.txt') as f:
    lines = f.readlines()

s = lines[0].strip()
probs = list(map(float, lines[1].split()))

sol = []
for CG in probs:
    C = G = CG/2
    A = T = (1-CG)/2
    P = 1
    for nucleotide in s:
        if nucleotide == 'A':
            P *= A
        elif nucleotide == 'T':
            P *= T
        elif nucleotide == 'C':
            P *= C
        elif nucleotide == 'G':
            P *= G

    sol.append(math.log10(P))

print(*sol)