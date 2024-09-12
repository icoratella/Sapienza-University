def hammer(s,t):
    h = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            h += 1
    return h

with open('rosalind_hamm.txt', 'r') as f:
    s = f.readline().strip()
    t = f.readline().strip()
    print(hammer(s,t))
