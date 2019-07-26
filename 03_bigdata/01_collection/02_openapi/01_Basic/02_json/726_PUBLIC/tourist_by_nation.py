
import json


# with open('중국(112)_해외방문객정보_2017_2017.json', encoding='UTF8') as json_file:
#     json_object = json.load(json_file)
#     json_string = json.dumps(json_object)
#     china_data = json.loads(json_string)
#
# print(len(china_data))
# print(china_data[0])

with open('national_code_selected.txt', 'r', encoding='utf-8') as nations:
     searching_nation = nations.readlines()
     print(len(searching_nation))   #376
     print(searching_nation[0][1:4])

s_nat = []

for i in range(0, len(searching_nation)):
     if i==0:
          s_nat.append(searching_nation[i][1:4])
     else:
          s_nat.append(searching_nation[i][:3])

print(s_nat)

     #      print(searching_nation[nation*9:nation*9+3])


