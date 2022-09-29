# Python program to read 
# json file 


import json

# Opening JSON file 
f = open('example.json', encoding='utf-8')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['emp_details']:
    print(i)

# Closing file
f.close()