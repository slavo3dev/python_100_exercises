# Create a function that takes any string as input and returns the number of words for that string.

a = input('What is you name? ')
b = input('How old are you? ')

def info():
    print ('Your info is ', a," ",str(b))

info()
    
## this is answare

def count_words(strng): 
    strng_list = strng.split() 
    return len(strng_list) 
 
print(count_words("Hey there it's me!"))