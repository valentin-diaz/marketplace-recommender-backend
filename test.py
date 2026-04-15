import json

json_s = "[{'large': 'https://m.media-amazon.com/images/I/51SYyCHMXDL.jpg', 'variant': MAIN}]"

json_s = json_s.replace("'", '"')
json_s = json_s.replace("MAIN", '"MAIN"')
data = json.loads(json_s)
print(data[0]['large'])