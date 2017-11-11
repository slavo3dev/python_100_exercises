'''
Question: Create a function that takes a text file as input and returns the number of words contained in the text file. Please take into consideration that some words can be separated by a comma with no space. For example "Hi,it's me." would need to be counted as three words. For your convenience, you can use the text file in the attachment.
'''
import re 

my_str = ''
file_name = 'words2.txt'

def count_str(cnt_str):
    with open(file_name) as f:
        content = f.read()
    cnt_str = content
    cnt_str = re.split('\W+', cnt_str)
    cnt_str = cnt_str.remove(-1)
    print(cnt_str[9])
    print ('Your string has: ', len(cnt_str), ' number of words')

count_str(my_str)
