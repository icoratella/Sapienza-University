import requests

with open('rosalind_mprt.txt') as file:
    txt = file.read()

ids = txt.split('\n')
ids_right = ids
ids = list(map(lambda k: k.split('_')[0], ids))

pages = []
for id in ids:
    pages.append(requests.get('https://rest.uniprot.org/uniprotkb/' + id + '.fasta').text)

def char_match(pattern, char):
    if pattern.startswith('[') and pattern.endswith(']') and not '^' in pattern:
        if char in pattern[1:-1]:
            return True
    elif pattern.startswith('[') and pattern.endswith(']') and '^' in pattern:
        if char not in pattern[2:-1]:
            return True 
    else:
        if pattern == char:
            return True
    return False

def match(pattern, string):
    for i in range(len(pattern)):
        if not char_match(pattern[i], string[i:i+1]):
            return False
    return True
  
pattern = ['N' , '[^P]', '[ST]', '[^P]']

def match_all(pattern, string):
    matches = []
    for i in range(len(string)):
        if match(pattern, string[i:]):
            matches.append(i+1)
    return matches


for i in range(len(pages)):
    page = pages[i]
    protein = ''.join(page.split('\n')[1:-1])
    # matches = re.findall(pattern, protein)
    # matches = list(map(lambda k: protein.index(k)+1, matches))
    matches = match_all(pattern, protein)
    if len(matches) > 0:
        print(ids_right[i])
        print(*matches, sep=' ')