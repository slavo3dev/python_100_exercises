# Question: Complete the script so that it removes duplicate items from list a .
# Expected output: ['1', 2, 1] 

a = ["1", 1, "1", 2]

print(set(a))
 
# 2nd Solution

from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)

# 3rd solution

a = ["1", 1, "1", 2]
b = []
for i in a:
    if i not in b:
        b.append(i)