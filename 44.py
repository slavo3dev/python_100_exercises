'''
Create a script that generates a file where all letters of English alphabet are listed three in each line. The inside of the text file would look like:
abc
def
ghi
and so on.
'''
import string

file_name = 'word5.text'

alphabet_str = string.ascii_lowercase
print(alphabet_str[0:3])

