'''
Plot text file 
'''

import matplotlib.pyplot as plt
import pandas
f_load = pandas.read_csv('75.txt')
print(f_load)
f_x = list(f_load['x'])
f_y = list(f_load['y'])
print(f_x)
print(f_y)


