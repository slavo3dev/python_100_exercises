import glob

letter = []

file_list = glob.glob('test_case/*.txt')

for filename in file_list:
    with open(filename, 'r') as f:
        letter.append(f.read().strip('\n'))
        
print(letter)