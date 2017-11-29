'''
Write a script that detects and prints out your monitor resolution
'''

import screeninfo

from screeninfo import get_monitors
for m in get_monitors():
    print(str(m))
