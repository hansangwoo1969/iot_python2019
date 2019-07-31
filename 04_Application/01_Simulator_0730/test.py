import json
import datetime

with open('시군구별_실시간_평균정보_조회.json', 'r', encoding='utf-8') as f:
    json_obj = json.load(f)
    json_string = json.dumps(json_obj)
    json_data = json.loads(json_string)

print(json_data)
print(len(json_data))
print(json_data['fields'])
# print(json_data[1])
print(json_data['records'])
print(len(json_data['records']))
print("====")
print(json_data['records'][2])
records = json_data['records']
for i, record in enumerate(records):
    print(i, record)

# print(json_data['records'][1]['informGrade'])
# text = json_data['records'][1]['informGrade']
# txts = text.split('/')
# print(txts[8])
# for i,txt in enumerate(txts):
#     print(i, txt)
#
# cur = datetime.datetime.now()
# print(cur.strftime("%Y-%m-%d"))
# for i, field in enumerate(json_data['fields']):
#     print(i, field)

# for i, record in enumerate(json_data['records']):
#     print(i, record)
# print(json_data['fields'][0]['id'])
# print(json_data['fields'][1]['id'])