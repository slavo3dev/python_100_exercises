'''
Question: Create an English to Serbian translation program.

The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source. In addition, return the message "We couldn't find that word!" when the user enters a word that is not in the dictionary. Also, make the program non case-sensitive meaning that for example, both earth and Earth should return the translation correctly for that word.

d = dict(weather = "vreme", earth = "zemlja", rain = "kisa")
Expected output: 

Enter word: hello
We couldn't find that word!

'''

d = dict(weather = "vreme", earth = "zemlja", rain = "kisa")

def translation(word):
    try:
        return d[word]
    except:
        print("This word doesn't exist!!\nPlease try again!!")

active = True
while active:
    print('Please print q if you want to exit!!')
    w = input('Please choose word (weather, earth, rain): ')
    w = w.lower()
    if w != 'q':
        print("Your word in Serbian means: ", translation(w))
    else:
        active = False

print ('Thank You for Choosing MimiCom24!!!!')