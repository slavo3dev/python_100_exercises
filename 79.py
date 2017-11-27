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

user_password: input('Enter Password?' )
