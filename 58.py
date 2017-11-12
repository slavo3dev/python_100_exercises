'''
Add a new employee to the content of the JSON file company1.json
'''
import json
from pprint import pprint

json_file = ('company1.json')


with open(json_file, 'r') as target:
    data_file = json.load(target)
    data_file["employees"][{'firstName': 'Slavo', 'lastName': 'Popovic'}]
    pprint(data_file)