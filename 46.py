import glob

letter = []

file_list = glob.glob('letters/*.txt')

for filename in file_list:
    with open(filename, 'r') as f:
        letter.append(f.read().strip('\n'))
        
print(letter)