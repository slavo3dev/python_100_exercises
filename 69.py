''' 

Question: Please create an empty file (manually as you normally create Python files) and name it requests.py . Make sure the file has that name exactly.

Then just paste the following code in the file (manually):

import requests
 
r = requests.get("http://www.pythonhow.com")
print(r.text[:100])

Executing the script will throw an error. Please fix that error so that you get the expected output and explain why the error happened.

Expected output: 

<!DOCTYPE html>
<!--[if IE 7]>
<html class="ie ie7" lang="en-US" prefix="og: http://ogp.me/ns#">

'''

import requests
 
r = requests.get("http://www.pythonhow.com")
print(r.text[:100])

''' 

Answare:

In the code Python is actually referring to the script name which is requests  and it doesn't find a get attribute for that name. Script names load in the current namespace. They are actually stored in the __name__  variable. You could try to print that variable out and you would see that it prints your script name. Therefore you should not name your scripts under library names. 

'''