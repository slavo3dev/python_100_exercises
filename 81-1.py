user_list = ['slavo', 'marko']

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