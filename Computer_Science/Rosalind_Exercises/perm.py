from math import factorial
from itertools import permutations


with open("rosalind_perm.txt") as file:
  n = int(file.readline().strip())

print(factorial(n))

l = list(map(lambda k: str(k), range(1,n+1)))
l = list(permutations(list(l)))

for _l in l:
    print(' '.join(_l))