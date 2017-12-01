'''
Write a script that detects and prints out your monitor resolution
'''
# Solutions
# code its not working on iOS envitoment
from screeninfo import get_monitors
for m in get_monitors('osx'):
    print(str(m))