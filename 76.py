'''
Please print the scrip and expect date & Time output
'''

import datetime 

date_time = datetime.datetime.today()

print("Today is ", date_time)

# solution

from datetime import datetime
 
print(datetime.now().strftime("Today is %A, %B %d, %Y"))