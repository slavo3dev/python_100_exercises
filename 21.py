# Question: Filter the dictionary by removing all items with a value of greater than 1.

d = {"a": 1, "b": 2, "c": 3}

for k, v in d.items():
    if v > 1:
        del d[k]
    else:
        print(d)



# Expected output: {'a': 1}  