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

plt.scatter(f_x, f_y, s=40)
plt.show()

# Solution 2

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data.plot(x='x', y='y', kind='scatter')
plt.show()

