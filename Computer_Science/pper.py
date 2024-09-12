with open('rosalind_pper.txt') as f:
    n, k = map(int, f.readline().strip().split())

def fac(n):
    f = 1
    for i in range(n):
        f *= (i+1)
    return f

print((fac(n) // fac(n-k)) % 1000000)

