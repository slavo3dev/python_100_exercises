# Question: Create a script that generates a text file with all letters of English alphabet inside it, one letter per line.

import string

file_text = 'word3.txt'

def add_string(str_name):
    with open(file_text, 'w') as f:
        for letter in str_name:
            f.write(letter + '\n')      
my_str = string.ascii_lowercase
add_string(my_str)
    
# 2nd solution to problem

with open("letters.txt", "w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n") 