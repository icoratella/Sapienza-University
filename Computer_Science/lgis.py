def subsequence_inc(l):
    n = len(l)
    lis = [1] * n
    lis_l = [[l[i]] for i in range(0, n)]
    for i in range(1, n):
        for j in range(0, i):
            if l[i] > l[j] and lis[i] < (lis[j]+1):
                lis[i] = lis[j] + 1
                lis_l[i] = lis_l[j] + [l[i]]

    maximum = max(lis)
    maximum_i = lis.index(maximum)
    return lis_l[maximum_i]


def subsequence_dec(l):
    n = len(l)
    lis = [1] * n
    lis_l = [[l[i]] for i in range(0, n)]
    for i in range(1, n):
        for j in range(0, i):
            if l[i] < l[j] and lis[i] < (lis[j]+1):
                lis[i] = lis[j] + 1
                lis_l[i] = lis_l[j] + [l[i]]

    maximum = max(lis)
    maximum_i = lis.index(maximum)
    return lis_l[maximum_i]


# with open('in.txt') as file:
with open('rosalind_lgis.txt') as file:
    txt = file.read()
# txt = "5\n5 1 4 2 3"
l = txt.split('\n')[1].split(' ')[:]
l = list(map(lambda k: int(k), l))

# import matplotlib.pyplot as plt
# import numpy as np
# plt.hist(l)
# plt.savefig('/root/prova.png', dpi=200)


r1 = subsequence_inc(l)
r2 = subsequence_dec(l)

txt = ''
txt += ' '.join(list(map(lambda k: str(k), r1))) + '\n'
txt += ' '.join(list(map(lambda k: str(k), r2))) + '\n'
print(txt)
