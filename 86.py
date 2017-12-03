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

def check_list(c_list):
    with open('86_text.txt') as f:
        check = f.readlines()
    check = [i.strip('\n') for i in check if '\n' in i ]
    for i in c_list:
        if i not in check:
            c_list.remove(i)
    return c_list

print(check_list(["Portugal", "Germany", "Munster", "Spain"]))