'''
Adding missing data to a file to a data
'''

s = ["Portugal", "Germany", "Spain"]
with open ('87_text.txt', 'r') as f:
    l_ctr = f.readlines()

l_ctr = [i.strip('\n') for i in l_ctr]

l_ctr = [i for i in s if i not in l_ctr]

