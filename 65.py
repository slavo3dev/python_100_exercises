'''
Fix the code

while True:
    print ('Hello')
    if 2 > 1:
        break
    print('Hi')

Output:

Hello
Hello
.
.

'''

while True:
    print ('Hello')
    if 2 > 1:
        continue
    print('Hi')