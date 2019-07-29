# 템플릿_채우기_ 결과는?  못했음,,,,, 강사코드와 비교후 숙지할 것
import  urllib.request
import datetime
import json
import time

access_key = "XCeRmN%2B%2BubaLKjj%2BA8W%2Bx1QghqjBqMqJRZYXcFRhJiZ%2BZJUOH%2FPvWvsc8mcBE0M9YUC7T0iJ9LM%2FjWg2cD2o9Q%3D%3D"

def get_Request_URL(url):  # (1) 기상정보(동네예보정보 조회 서비스) / (2) 통합대기환경 정보(대기오염정보 조회서비스)
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % (datetime.datetime.now()))
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s" % (datetime.datetime.now(), url))
        return None

def get_Weather_URL(day_time): # (1) 기상정보(동네예보정보 조회 서비스) request 보내기전, url만드는 함수
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData" # ForecastTimeData서비스를 이요할 것

    parameters = "?_type=json&ServiceKey="+access_key  # 매뉴얼을 보고 요청 메세지를 완성할 것
    parameters += "&base_date=" + yymmdd
    parameters += "&base_time="+day_time
    parameters += "&nx="+x_condinate
    parameters += "&ny="+y_condinate
    parameters += "&numOfRows=100"


    url = end_point + parameters
    retData = get_Request_URL(url)

    if (retData==None):
        return None
    else:
        return json.loads(retData)

def Make_Weather_Json(day_time):  # (1) 기상정보 (동네예보정보 조회 서비스) json파일 생성하는 함수
    jsonData = get_Weather_URL(day_time)
    # print(jsonData)

    if (jsonData['response']['header']['resultMsg']=='OK'):
        for prn_data in jsonData['response']['body']['items']['item']:
            json_weather_result.append({'baseDate':  prn_data.get('baseDate'),
                                        'baseTime':  prn_data.get('baseTime'),
                                        'category':  prn_data.get('category'),
                                        'fcstDate': prn_data.get('fcstDate'),
                                        'fcstTime':  prn_data.get('fcstTime'),
                                        'fcstValue': prn_data.get('fcstValue'),
                                        'nx': prn_data.get('nx'),
                                        'ny': prn_data.get('ny')})

    # jsonData를 parsing하여 json_weather_result에 저장된 예제 샘플을 참고하여 데이터를 저장한다
    with open('동구_신암동_초단기예보조회_%s%s.json' % (yymmdd, day_time), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(json_weather_result, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print('동구_신암동_초단기예보조회_%s%s.json SAVED\n' % (yymmdd, day_time))

def get_Realtime_Weather_Info():  # 시간정보를 보정하여 Make_Weather_Json()를 호출한다.
    min_int = int(min)
    if 30 < min_int <= 59:
        day_time = time.strftime("%H%M", time.localtime(time.time()))
        print("\n<<  실시간 기상정보 업데이트 실시 >>\n".center(30))
        Make_Weather_Json(day_time)

    elif 0 < min_int <= 30:
        hour_int = int(hour)
        hour_int = hour_int - 1
        revised_min = 60 + (min_int - 30)  # 정확히 30분 빼고
        day_time = "{0:0>2}".format(hour_int) + str(revised_min)
        Make_Weather_Json(day_time)




json_weather_result = []
cur = datetime.datetime.now()
# ymdHM = cur.strftime("%Y%m%d %H%M")
yymmdd = cur.strftime("%Y%m%d")
day_time= cur.strftime("%H%M")
hour = cur.strftime("%H")
min = cur.strftime("%M")
# day_time = ymdHM.split()[1]
# yymmdd = ymdHM.split(" ")[0]

#  동구 신암동의 좌표를 세팅한다.
x_condinate = "89"
y_condinate = "91"

get_Realtime_Weather_Info()

