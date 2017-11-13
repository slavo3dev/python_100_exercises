'''

Question: Print out the text of this file http://www.pythonhow.com/data/universe.txt. Please don't manually download the file. Let Python do all the work.


import requests
r = requests.get("http://www.pythonhow.com/data/universe.txt")
text_file = r.text
print(text_file)
'''

import requests
response = requests.get("http://www.pythonhow.com/data/universe.txt")
text = response.text
print(text)