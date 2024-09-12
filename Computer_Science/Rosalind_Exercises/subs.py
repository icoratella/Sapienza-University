with open('rosalind_subs.txt') as f:
    txt = f.read()
    txt = txt.split('\n')
    txt = list(filter(lambda k: k != '', txt))
    s = txt[0]
    t = txt[1]

indices = []
i = 0
while i < len(s):
    try:
        new_start = s.index(t, i) + 1
        i = new_start
        indices.append(new_start)

    except:
        break

print(' '.join(list(map(lambda k: str(k), indices))))