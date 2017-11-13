# Question: Count the number of "a" characters in this text file: http://www.pythonhow.com/data/universe.txt

import requests 
r = requests.get('http://www.pythonhow.com/data/universe.txt')
text = r.text
file_name = "word6.txt"
