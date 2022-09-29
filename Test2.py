# -*- coding: utf-8 -*-
import json

with open("test4.json", "r", encoding="utf-8") as f:
    data_dict = json.loads(f.read())

# print(data_dict)
name = data_dict.get("name")

print(name)
for k,v in data_dict.items():
    if(isinstance(v,dict)):
        pass
    else:
        pass

