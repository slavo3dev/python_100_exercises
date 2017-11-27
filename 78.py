'''
Creat a program that Generates a password
'''

from random import random
import string
print (string.ascii_letters)
num = random()
print(int(20*num))
l = list(string.ascii_letters)
print(l)
print(len(l))

while i < 10:
    print(l[(52*random())].join())
    i = i + 1
