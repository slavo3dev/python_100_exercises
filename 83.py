'''
Write a script that detects and prints out your monitor resolution
'''

import screeninfo

from screeninfo import get_monitors
for m in get_monitors():
    print(str(m))


# Solutions

from screeninfo import get_monitors
 
width=get_monitors()[0].width
height=get_monitors()[0].height
 
print("Width: %s,  Height: %s" % (width, height))