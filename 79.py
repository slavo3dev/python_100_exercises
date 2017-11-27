'''
Paassword checker

1. at leas one number
2. one upprcase letter
3. one character

'''

while True:
    psw = input("Enter new password: ")
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
        print("Password is fine")
        break
    else:
        print("Passowrd is not fine")
        
