# write a file that check and print 'python' from files

import glob

file_name = glob.glob("test_case/*.txt")


for files in file_name:
    with open(files, 'r') as f:
        cont = f.read()
        print(cont)


