with open('rosalind_dna.txt', 'r') as f:
    sequence = f.read().strip()

Ac = 0
Cc = 0
Gc = 0
Tc = 0

for char in sequence:
    if char == 'A':
        Ac += 1
    elif char == 'C':
        Cc += 1
    elif char == 'G':
        Gc += 1
    elif char == 'T':
        Tc += 1

res = f"{Ac} {Cc} {Gc} {Tc}"
print(res)
 
    

    