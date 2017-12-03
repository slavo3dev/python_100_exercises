'''
Please take a look at the following list:
checklist = ["Portugal", "Germany", "Munster", "Spain"]
One of the items is not a country. 
Please use Python and the file containing the list of countries (attached) 
as data source to filter out the checklist  of non-country items. 
Once you have filtered out checklist , then print it out.

Expected output: 
['Germany', 'Portugal', 'Spain']
'''
checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open('86_text.txt') as f:
    check = f.readlines()

    print(check)
