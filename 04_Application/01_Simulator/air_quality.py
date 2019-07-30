# 공공데이터 포털 / 대기오염정보 조회 서비스 / 시군구별 실시간 평균 정보 조회
import  urllib.request
import datetime
import json

access_key = "XCeRmN%2B%2BubaLKjj%2BA8W%2Bx1QghqjBqMqJRZYXcFRhJiZ%2BZJUOH%2FPvWvsc8mcBE0M9YUC7T0iJ9LM%2FjWg2cD2o9Q%3D%3D"

def json_down(url):
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

def get_sigungu_URL(): # (1) 기상정보(동네예보정보 조회 서비스) request 보내기전, url만드는 함수
    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst"
    parameters = "?_returnType=json&ServiceKey=" + access_key  # 매뉴얼을 보고 요청 메세지를 완성할 것
    parameters += "&sidoName=%s" % (urllib.parse.quote('대구'))
    parameters += "&searchCondition=" + 'HOUR'
    # parameters += "&ver=" + "1.3"

    url = end_point + parameters
    retData = json_down(url)

    print(retData)
    retData = json.loads(retData)

    if (retData==None):
        return None
    else:
        return json.loads(retData)

def Make_measure_info_Json():  # (1) 기상정보 (동네예보정보 조회 서비스) json파일 생성하는 함수
    jsonData = get_sigungu_URL()
    print(jsonData)
    # text = json_Data['records'][1]['informGrade']
    # txts = text.split('/')
    #     if (jsonData['response']['header']['resultMsg']=='OK'):
    # for txt in txts:
    #     json_air_quality_forecast_result.append(txt)

        # json_weather_result.append({'baseDate':  prn_data.get('baseDate'),
        #                             'baseTime':  prn_data.get('baseTime'),
        #                             'category':  prn_data.get('category'),
        #                             'fcstDate': prn_data.get('fcstDate'),
        #                             'fcstTime':  prn_data.get('fcstTime'),
        #                             'fcstValue': prn_data.get('fcstValue'),
        #                             'nx': prn_data.get('nx'),
        #                             'ny': prn_data.get('ny')})

    # jsonData를 parsing하여 json_weather_result에 저장된 예제 샘플을 참고하여 데이터를 저장한다
    # with open('대구 미세먼지 예보_%s.json' % yymmdd, 'w', encoding='utf8') as outfile:
    #     retJson = json.dumps(json_weather_result, indent=4, sort_keys=True, ensure_ascii=False)

        # outfile.write(retJson)

    # print('대구 미세먼지 예보_%s.json SAVED\n' % yymmdd)

# def get_Realtime_Weather_Info():  # 시간정보를 보정하여 Make_Weather_Json()를 호출한다.
#     global yymmdd
#     # min_int = int(min)
#     # if 30 < min_int <= 59:
#     #     day_time = time.strftime("%H%M", time.localtime(time.time()))
#     #     print("\n<<  실시간 기상정보 업데이트 실시 >>\n".center(30))
#     #     Make_Weather_Json(day_time)
#     #
#     # elif 0 < min_int <= 30:
#     #     hour_int = int(hour)
#     #     hour_int = hour_int - 1
#     #     revised_min = 60 + (min_int - 30)  # 정확히 30분 빼고
#     #     day_time = "{0:0>2}".format(hour_int) + str(revised_min)
#     #     Make_Weather_Json(day_time)
#     Make_Weather_Json(yymmdd)

# region_name = '대구'
get_sigungu_URL()



