'''
Write a script that detects and prints out your monitor resolution
'''
# Solutions
from screeninfo import get_monitors
for m in get_monitors('osx'):
    print(str(m))