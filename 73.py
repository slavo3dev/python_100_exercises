# Multiply the text values in the URL and export the output to the new file

import pandas
 
data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data_2 = data * 2
data_2.to_csv("word7_pandas.txt", index=None)