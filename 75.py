'''
Plot text file 
'''

import matplotlib
import pandas


with open('75.txt') as f:
    file_load = f.read()

new_file = list(file_load)
print (new_file)