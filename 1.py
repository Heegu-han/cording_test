import json
with open('bread.json', 'r') as f:

    json_data = json.load(f)

print(json.dumps(json_data, indent="\t") )
