'''
Question:  Please write a function that calculates liquid volume in a sphere using the following formula. The radius r  is always 10, so consider making it a default parameter.
You can then test your solution by passing 2 for h and you should get the expected output.
'''

def liquid_volume(h, r=10, pi=3.14):
    l_volume = ((4*pi*(r**3))/3) - (pi*(h**2)*(3*r-h)/3)
    return l_volume

print("Liquid Volume is: ", liquid_volume(2))