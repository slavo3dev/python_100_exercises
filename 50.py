'''
Question: The code produces an error. Please understand the error and try to fix it

age = input("What's your age? ")
age_last_year = age - 1
print("Last year you were %s." % age_last_year)
Note: Please use raw_input instead of input if you are on Python 2. For Python 3 input is fine.
'''

age = input("What's your age? ")
age_last_year = int(age) - 1
age_last_year = str(age_last_year)

print("Last year you were %s." %age_last_year)

# we need to covert our variable to string to print , and age needs to be covertet to integer