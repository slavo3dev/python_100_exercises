'''
Question: Create a function that takes a text file as input and returns the number of words contained in the text file. Please take into consideration that some words can be separated by a comma with no space. For example "Hi,it's me." would need to be counted as three words. For your convenience, you can use the text file in the attachment.
'''
import re 

file_name = 'words2.txt'

with open(file_name) as f:
    content = f.read()
my_str = content
'''
my_str = my_str.replace(',',' ')
my_str = my_str.replace("'", ' ')
my_str = my_str.replace('.', ' ')
print(my_str)
'''
my_str = re.split('\W+', my_str)
print(my_str)

