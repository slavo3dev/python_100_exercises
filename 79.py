'''
Paassword checker

1. at leas one number
2. one upprcase letter
3. one character

'''

import random
 
characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
chosen = random.sample(characters, 6)
print (chosen)
password = "".join(chosen)
print(password)
numbers = '01234567890'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
character = '!@#$%^&*()?'
while True:
    user_password = input('Enter Password?' )
    print (user_password)
    for n in user_password:
        if numbers == n and uppercase == n and character == n and len(password) == len(user_password):
            True
            print('Password is fine, well done')
        
    print('Password is not good, please try again!')
        
