s = '''
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G 
'''
s = s.split('\n')
l = []
for line in s:
    j  = line.split('  ')
    for d in j:
        if d == '':
            continue 
        else:
            l.append(d.strip().split(' '))

with open('rosalind_mrna.txt') as file:
    string = file.readline().strip()

tot = 1 
for i in range(len(string)):
    _l = list(filter(lambda k: k[1] == string[i], l))
    tot *= len(_l)

tot *= 3
print(tot % 1000000)