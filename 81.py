'''
Creat a input for username - if username exits in date ask for a password
'''
'''
user_file = open('81_users.txt', 'r')
users = user_file.readlines()
print(users)
user_list = []
for i in users:
    j = i.replace('\n', ' ')
    user_list.append(j)
print (user_list)
user_list = [x.strip(' ') for x in user_list]
print (user_list)
active = True
while active:
    user = (input('Please add your user name? ')).lower()
    for i in user_list:
        if user == i:
            print("Welcome %s!!" %(user.title()))
            active = False
            break
        else:
            print ('Please try again user is not valid!!')

'''
user_file = open('81_users.txt', 'r')
users = user_file.readlines()
users = [x.strip('\n') for x in users]
active = True
while active:
    user_input = (input('Please add your username? ')).lower()
    for i in users:
        if user_input == i:
            print ('Welcome %s' %(user_input.title()))
            active = False
            break
        else:
            print('Youser is not valid, Please try again!')
# refactoring the code


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
'''