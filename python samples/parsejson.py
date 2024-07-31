import json

with open("json_sample.json") as data:
    json_data = data.read()

json_dict = json.loads(json_data)

type(json_dict)

json_dict ["interface"] ["description"] = "Backup Link"

print(json_dict)

with open("json_sample.json", "w") as fh:
    json.dump(json_dict, fh, indent = 4)
    