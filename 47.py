# write a file that check and print 'python' from files

import glob

file_name = glob.glob("test_case/*.txt")
check_name = 'python'
new_list = []

for files in file_name:
    with open(files, 'r') as f:
        cont = f.read().strip('\n')
        if cont in check_name:
            new_list.append(cont)

print(new_list)


