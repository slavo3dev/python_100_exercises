'''
Use Python to calculate the distance in kilometers between 
Jupiter and Sun on January 1, 1230. 
'''

import ephem
mars = ephem.Mars()
mars.compute('2008/1/1')
print (mars.ra, mars.dec)