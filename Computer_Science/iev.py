with open('rosalind_iev.txt') as f:
    txt = f.read()
    txt = txt.split(' ')
    ks = list(map(lambda k: int(k), txt))

ps = [1, 1, 1, 0.75, 0.5, 0]
def mean(ks):
    s = 0
    for i, k in enumerate(ks):
        s += ps[i] * k *2
    return s

print(mean(ks))

mean(ks)
