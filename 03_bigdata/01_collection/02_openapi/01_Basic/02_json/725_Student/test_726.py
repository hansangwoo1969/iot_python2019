import json

g_json_big_data=[]

with open('sample_json.json', encoding='UTF8') as json_file:
 json_object = json.load(json_file)
 json_string = json.dumps(json_object)
 g_json_big_data = json.loads(json_string)

 print(g_json_big_data)
 pr
 print(len(g_json_big_data))

# pass