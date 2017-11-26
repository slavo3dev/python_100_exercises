'''
Question: Create a script that asks the user to enter their age and the script calculates 
the user's year of birth and prints it out in a string like in the expected output. 
Please make sure you generate the current year dynamically.

Expected output: 

You were born back in 1988
'''

import datetime

today = datetime.datetime.now().year
active = True
while active:
    my_age = int(input('How old are you? '))
    quit = input('press X to exit program!')
    if quit == 'X':
        active = False
    else: 
        print ('You where born ', (today - my_age))

print ('Thank You, See you Soon!!')