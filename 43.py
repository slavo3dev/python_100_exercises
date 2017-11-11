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
            f.write(letter + alph_str[alph_str.index(letter) + 1])



