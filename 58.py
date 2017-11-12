'''
Add a new employee to the content of the JSON file company1.json
'''
import json
from pprint import pprint

json_file = ('company1.json')


with open(json_file, 'r+') as target:
    data_file = json.load(target)
    pprint(data_file)
    data_file['employees'].append(dict(firstName = 'Slavo', lastName = 'Popovic'))
    target.seek(0)
    json.dump(data_file, target, indent=4, sort_keys=True)
    target.truncate()
    


