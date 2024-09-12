
import itertools


def signed_permutations(input_file):

    with open(input_file, 'r') as f:
        n = int(f.readline().strip())

    # Creare lista 
    nums = []
    for i in range(1, n+1):
        nums.append(i)

    # creare permutations con itertools
    perms = list(itertools.permutations(nums))

    # generare i segni
    signs = list(itertools.product([-1, 1], repeat=n))

    signed_perms = []
    for perm in perms:
        for sign in signs:
            signed_perm = [perm[i]*sign[i] for i in range(n)]
            signed_perms.append(signed_perm)

    num_signed_perms = len(signed_perms)
    return num_signed_perms, signed_perms

input_file = 'rosalind_sign.txt'

total_perms, perm_list = signed_permutations(input_file)

print(total_perms)
for perm in perm_list:
    print(' '.join(map(str, perm)))