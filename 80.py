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
    elif any(i.isdigit() for i in psw) and any(i.isupper() for i in psw):
        print ("Your don't have 6 characters in password!")
        pass
    elif any(i.isupper() for i in psw) and len(psw) >= 5:
        print ("You need to have a digits also please try again!")
        pass
    elif any(i.isdigit() for i in psw) and len(psw) >= 5:
        print ('Your password need at least one uppler case letter!')
        pass
    else:
        print("Passowrd is not fine")

