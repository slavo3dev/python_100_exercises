# Question: Count the number of "a" characters in this text file: http://www.pythonhow.com/data/universe.txt

# download a txt document, and make a var for a new file
import requests 
r = requests.get('http://www.pythonhow.com/data/universe.txt')
text = r.text
file_name = "word6.txt"
# write a new txt file and save the content from the internet
with open(file_name, 'w') as f:
    f.write(text)
# load a new file and save text as string
text_content = ''
with open('word6.txt', 'r') as f:
    text_content = f.read()
    print(text_content)
# looping all the letters and count only when is letter a 
count = 0
for letter in text_content:
    if letter == 'a':
        count += 1
        
print("Count number of letter 'a' is: ", count)

# advance solution

import requests
 
response = requests.get("http://www.pythonhow.com/data/universe.txt")
text = response.text
count_a = text.count("a")
print(count_a)