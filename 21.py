# Question: Filter the dictionary by removing all items with a value of greater than 1.

d = {"a": 1, "b": 2, "c": 3}

for i in d:
    if d[i] > 1:
        d.pop[i]
    else:
        pass

print(d)

# Expected output: {'a': 1}  