'''
Create a script that uses the attached countries_by_area.txt  
file as data source and prints out the top 5 most densely populated countries.
'''
 

import pandas as pd 

f = pd.read_csv('88.txt')
f["density"] = f["population_2013"] / f["area_sqkm"]
f = f.sort_values(by='density',ascending=False )
for index, row in f[:5].iterrows():
    print(row["country"])