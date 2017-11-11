'''
Question: Create a script that generates a file where all letters of English alphabet are listed two in each line. The inside of the text file would look like:
ab
cd
ef
and so on.
'''
import string

file_name = 'word4.txt'

''''
with open(file_name, 'w') as f:
    for letter in string.ascii_lowercase:
        f.write(letter + '\n')
'''
alph_str = string.ascii_lowercase
print(alph_str.index('c'))

for letter in alph_str:
    if alph_str.index(letter) % 2 == 0:
        print(letter)