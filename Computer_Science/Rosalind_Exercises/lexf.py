input = """A B C D E
4"""

input = input.split('\n')
alphabet = input[0].split(' ')
n = int(input[1])

def generate_strings(alphabet, n):
    if n == 1:
        return alphabet
    else:
      return [a + b for a in alphabet for b in generate_strings(alphabet, n-1)]


txt = ""
output = generate_strings(alphabet, n)
for line in output:
    txt += line + '\n'
with open("out6.txt", "w") as file:
    file.write(txt)

sorted(generate_strings(alphabet, n)) == output
