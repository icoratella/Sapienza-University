def mendelfirstlaw(k, m, n):

    organisms = k+m+n

    
    het = (m/organisms)*((m-1)/(organisms-1))
    rec = (n/organisms)*((n-1)/(organisms-1))
    het_rec = (n/organisms)*(m/(organisms-1)) + (m/organisms)*(n/(organisms-1))

    p_rec = rec + het*1/4 + het_rec*1/2
    print(1-p_rec) 

with open ("rosalind_iprb.txt", "r") as file:
    line =file.readline().split()
    k, m, n= [int(n) for n in line]
    print(k, m, n)
file.close()
print(mendelfirstlaw(k, m, n))
