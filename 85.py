'''
Please download the attached countries_raw.txt file. 
The file contains the list of country names, 
but it also contains some unnecessary text among the countries. 

Please clean the list with Python by generating 
a new text file that contains a flawless list of country names
 without any other text or break lines in it. 
 The new file content should look like in the expected output.
'''

with open('85_text.txt', 'r') as f:
    ctr = f.readlines()

ctr = [i.strip('\n') for i in ctr if '\n' in i]
ctr = [i for i in ctr if i !="" and i !='Top of Page' and len(i) != 1]
print(ctr)

    