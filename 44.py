'''
Create a script that generates a file where all letters of English alphabet are listed three in each line. The inside of the text file would look like:
abc
def
ghi
and so on.
'''
import string

file_name = 'word5.text'

with open(file_name, 'w') as f:
    for l1, l2, l3 in zip(string.ascii_lowercase[0::3], string.ascii_lowercase[1::3], string.ascii_lowercase[2::3]):
        f.write(l1 + l2 + l3 + '\n')

