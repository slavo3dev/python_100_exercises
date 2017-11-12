'''
Add a new employee to the content of the JSON file company1.json
'''
import json
from pprint import pprint

json_file = ('company1.json')

new_eployee = "employees"[{'firstName': 'Slavo', 'lastName': 'Popovic'}]

with open(json_file, 'r') as target:
    data_file = json.load(target)
    data_file = data_file.append(new_eployee)
    pprint(data_file)