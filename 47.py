# write a file that check and print 'python' from files

import glob

file_name = glob.glob("test_case/*.txt")

with open(file_name) as f:
    cont = f.read()
    print(cont)

    
