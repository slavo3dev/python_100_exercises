'''
Creat a input for username - if username exits in date ask for a password

'''




# password checker
while True:
    psw = input("Enter new password: ")
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
        print("Password is fine")
        break
    elif any(i.isdigit() for i in psw) and any(i.isupper() for i in psw):
        print ("Your don't have 6 characters in password!")
        pass
    elif any(i.isupper() for i in psw) and len(psw) >= 5:
        print ("You need to have a digit and Character!")
        pass
    elif any(i.isdigit() for i in psw) and len(psw) >= 5:
        print ('Your password need at least one upper case letter!')
        pass
    else:
        print("Passowrd is not fine!(Missing at least one upper case letter,  symbol, charater ")
