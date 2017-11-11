'''
Question: Create a script that generates a file where all letters of English alphabet are listed two in each line. The inside of the text file would look like:
ab
cd
ef
and so on.
'''
import string

file_name = 'word4.txt'


with open(file_name, 'w') as f:
    alph_str = string.ascii_lowercase
    for letter in alph_str:
        if alph_str.index(letter) % 2 == 0:
            f.write(letter + alph_str[alph_str.index(letter) + 1] + '\n')


# 2nd solution

with open(word4_2nd.txt, 'w') as file:
    for l1, l2 in zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2]):
        file.write(l1 + l2 + '\n')
