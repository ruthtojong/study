import json

with open("json2.json") as data:
    json_data = data.read()

json_dict = json.loads(json_data)

json_dict["interface"]["description"] = "Backup Link" 

print(json_dict)

with open("json2.json", "w") as fh:
    json.dump(json_dict, fh, indent = 4)