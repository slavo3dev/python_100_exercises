'''

Question: Create a program that once executed the programs prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, and then the program prints out the message "End of the Loop" and stops.

Expected output: 

Hello
Hello
Hello
Hello
End of Loop

'''
from time import sleep 

count = 0 
active = True

while active:
    if count < 7:
        print('Welcome to Python World after ', count, ' s!!!!!')
        sleep(count)
    else: 
        print('End of the loop\nThank You and good buy')
        active = False
    count = count + 1