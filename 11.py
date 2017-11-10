# make a list from 0 to 20, but dont add numbers manuale

list = []

for num in range(0,21):
    list.append(num)
print(list)

# 2nd solution

list_two = [num for num in range(0,21)]

print(list_two)

# 3rd solution

list_tree = range(0,21)
print(list_tree)