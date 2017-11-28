'''
Create a program that asks the user to enter a new password and check that the submitted password 
should contain at least one number, one uppercase letter and at least 5 characters. 
If the conditions are generated, 
print out the reason why pointing to the specific condition/s that has not been satisfied.
'''

while True:
    psw = input("Enter new password: ")
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
        print("Password is fine")
        break
    else:
        print("Passowrd is not fine")