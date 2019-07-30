# 공공데이터 포털 / 대기오염정보 조회 서비스 / 시군구별 실시간 평균 정보 조회
import  urllib.request
import datetime
import json

yymmdd = datetime.datetime.now().strftime("%Y%m%d")

# def down_json():
access_key = "XCeRmN%2B%2BubaLKjj%2BA8W%2Bx1QghqjBqMqJRZYXcFRhJiZ%2BZJUOH%2FPvWvsc8mcBE0M9YUC7T0iJ9LM%2FjWg2cD2o9Q%3D%3D"
end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst"
parameters = "?_returnType=json&ServiceKey=" + access_key
parameters += "&sidoName=%s" % (urllib.parse.quote('대구'))
parameters += "&searchCondition=" + 'HOUR'

url = end_point  + parameters

req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
# response.read()
retData = response.read().decode('utf8')
# return retData

# def data_store(retD):
retData = json.loads(retData)
# print(retData)
# print(retData['list'])
# print(len(retData['list']))   # 8개
# print(retData['list'][0])
datas = retData['list']
# print(datas[0]['cityName'])

daegu_gu_fndust_value=[]
for data in datas:
    daegu_gu_fndust_value.append({'dataTime': data['dataTime'], 'cityName':data['cityName'], 'pm10Value':data['pm10Value']})
    print(data['dataTime'],data['sidoName'], data['cityName'], "미세먼지 농도: ", data['pm10Value'])

# print(daegu_gu_fndust_value)

with open('대구 구군별 미세먼지 농도_%s'% yymmdd , 'w', encoding='utf8') as outfile:
    retJson = json.dumps(daegu_gu_fndust_value, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(retJson)
    print("저장완료!")

# if datas['cityName'].value= '동구':
#     print("%s, pm10Value: %s"  % (datas['cityName'], datas['pm10Value']))

# down_json()
# data_store()