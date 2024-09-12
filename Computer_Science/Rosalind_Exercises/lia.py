import math
def binomial_coefficient(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def binomial_distribution(n, k, p):
    return binomial_coefficient(n, k) * p**k * (1 - p)**(n - k)

def solution(k, N):
    p = 0.25
    n = 2**k
    s = 0
    for i in range(N, n + 1):
        s += binomial_distribution(n, i, p)
    return s

with open('rosalind_lia.txt', 'r') as f:
    k, N = map(int, f.readline().split())
    print(solution(k, N))