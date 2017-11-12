'''
Question: Create a program that prints out Hello  every two seconds.

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
import time

count = 0
while count < 10:
    print ('Hello!!')
    count = count + 1
    time.sleep(2)
