# Question: Please download the words1.txt file from the attachment and then create a Python function that takes a text file as input and returns the number of words contained in the text file.

text_file = ('words1.txt')

my_str = ''

with open(text_file) as file_obj:
    content = file_obj.read()
    print (content)

my_str = content


def count_str(str_use):
    print('Your str lenght is: ', len(str_use.split()))

count_str(my_str)



    