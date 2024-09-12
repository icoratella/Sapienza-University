def solution(n, m):
    tot = [1, 1]
    for i in range(2, n):
        if (i < m):
            tot.append(tot[-2] + tot[-1]) 
        elif (i == m or i == m+1):
            tot.append(tot[-2] + tot[-1] - 1)
        else:
            tot.append(tot[-2] + tot[-1] - tot[-(m+1)])
    return (tot[len(tot)-1])

with open('rosalind_fibd.txt', 'r') as f:
    n, m = map(int, f.readline().split())
    print(solution(n, m))
