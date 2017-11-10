# make a list from 0 to 20, but dont add numbers manuale

list_one = []

for num in range(0,21):
    list_one.append(num)
print(list_one)

# 2nd solution

list_two = [num for num in range(0,21)]

print(list_two)

# 3rd solution

my_range = range(0, 21)
print(list(my_range))