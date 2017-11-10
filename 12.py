# Complete the script so that it produces the expected output. Please use my_range  as input data.
# Expected output: 
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200] 

my_range = range(0, 201)

print (list(my_range[::10]))

# 2nd solution
print ([10*x for x in range(1,21)])