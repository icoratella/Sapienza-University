def solution(n, k):
    tot = [1, 1]
    for i in range(2, n ):
        #tot.append(tot[-1] * k)
        tot.append(( tot[-1] + k * tot[-2]))
    print(tot)
# 40238153982301

with open('rosalind_fib.txt', 'r') as f:
    n, k = map(int, f.readline().split())
    print(solution(n, k))