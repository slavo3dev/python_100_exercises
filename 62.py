''''
Question: Create a program that once executed the program prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, 4, and so on the interval increases between prints.
Expected output: 

...
Hello
Hello
Hello
Hello
Hello
Hello
...

'''
from time import sleep

count = 0
while count < 5:
    print ("Welcom after ", count + 1, 's !! TIME MODULE!!!')
    sleep(count + 1)
    count = count + 1 