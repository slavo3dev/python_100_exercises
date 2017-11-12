'''

Question: Create an English to Serbian translation program.

The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.

d = dict(weather = "vreme", earth = "zemlja", rain = "kisa") 

Expected output: 

Enter word: earth
zemlja

'''
d = dict(weather = "vreme", earth = "zemlja", rain = "kisa")
def vocabulary(word):
    return d[word]
 
word = input("Enter word: ")
print(vocabulary(word))