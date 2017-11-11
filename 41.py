# Question: Create a script that generates a text file with all letters of English alphabet inside it, one letter per line.

import string

file_text = 'word3.txt'

def addin_strings(str_name):
    with open(file_text, 'w') as f:
        f.write(str_name)
        content = file_text
        print(content)

my_str = string.ascii_lowercase

addin_strings(my_str)
    