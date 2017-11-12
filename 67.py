''''

Question: Create an English to Serbian translation program.

The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.

d = dict(weather = "vreme", earth = "zemlja", rain = "kisa") 

Expected output: 

Enter word: earth
zemlja
That word doesn't exist!

'''
print('Simple Serbian Translator!!!')

d = dict(weather = "vreme", earth = "zemlja", rain = "kisa")

def translation(word):
    return d[word]

w = input('Please choose word (weather, earth, rain): ')
active = True

while active:
    print('Please print q if you want to exit!!')
    w = input('Please choose word (weather, earth, rain): ')
    if w != 'q':
        try:
            print("Your word in Serbian means: ", translation(w))
        except:
            print("This word doesn't exist!!\nPlease try again!!")
    else:
        active = False

print ('Thank You for Choosing MimiCom24!!!!')