'''
Adding missing data to a file to a data
'''

s = ["Portugal", "Germany", "Spain"]
s = [i + '\n' for i in s]

with open ('87_text.txt', 'r') as f:
    l_ctr = f.readlines()

update_list = sorted(l_ctr + s)

with open('87_text_new.txt', 'w') as f:
    for i in update_list:
        f.write(i)
