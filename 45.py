# Please create a script that generates 26 text files named a.txt, b.txt, and so on up to z.txt. Each file should contain a letter reflecting its filename. So, a.txt will contain letter a, b.txt will contain letter b and so on.

import string

str = string.ascii_lowercase

for letter in str:
    with open('test_case/' + letter + '.txt', 'w') as f:
        f.write('Slavo this is: ' + letter)

