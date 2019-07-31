import urllib.request
import datetime
import json
import threading
import time
import ctypes

access_key = 'Czhdxre7PaTpHvPbHMaY8GaqOwJ0QiKL4%2BS4u6XnQ3k6mr9QNR1o7AS%2BxNbteVRFyOZnIqlrpQ%2F5eEAiYuHksw%3D%3D'
g_Radiator = False
g_Gas_Valve = False
g_Door = False
g_Balcony_Windows = True
g_AI_Mode = False
schedule_cycle = 3600
json_weather_result = json_fine_dust_result =[]
gungu = '신암동'
sido = '대구'
x_condinate = '89'
y_condinate = '91'

def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 프로그램 종료")

def print_device_status(decive_name, device_status):
    print("%s 상태: "%decive_name, end="")
    if device_status == True : print("작동")
    else: print("정지")


def check_device_status():
    print("")
    print_device_status('난방기', g_Radiator)
    print_device_status('가스밸브', g_Gas_Valve)
    print_device_status('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('출입문 상태', g_Door)

def print_device_menu():
    print("\n상태 변경할 기기를 선택하세요.")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다) 창")
    print("4. 출입문")

def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door

    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))

    if menu_num == 1: g_Radiator = not g_Radiator
    if menu_num == 2: g_Gas_Valve = not g_Gas_Valve
    if menu_num == 3: g_Balcony_Windows = not g_Balcony_Windows
    if menu_num == 4: g_Door = not g_Door

    check_device_status()

def terminate_ai_mode():
    if not ai_scheduler.is_alive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(ai_scheduler.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ai_scheduler.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def get_Request_URL(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(), url))
        return None

def get_Weather_URL(day_time):
    end_point = 'http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData'
    parameters = "?ServiceKey="+access_key
    parameters+= "&base_date="+day_time[:-4]
    parameters+= "&base_time="+day_time[-4:]
    parameters+= "&nx="+x_condinate
    parameters+= "&ny="+y_condinate
    parameters+= "&numOfRows=100&_type=json"

    url = end_point+parameters
    retData = get_Request_URL(url)
    if retData == None:
        return None
    else:
        return json.loads(retData)

def Make_Weather_Json(day_time):
    global json_weather_result
    jsonData = get_Weather_URL(day_time)

    json_weather_result = jsonData['response']['body']['items']['item']

    with open('./data/동구_신암동_초단기예보조회_%s.json' %(day_time), 'w',encoding='utf8') as outfile:
        retJson = json.dumps(json_weather_result, indent=4, sort_keys=True,ensure_ascii=False)
        outfile.write(retJson)

    print('동구_신암동_초단기예보조회_%s.json SAVED\n' %day_time)

def get_Realtime_Weather_Info():
    day_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    if int(day_time[-2:]) in range(0,30):
        day_time = day_time[:-4]+str(int(day_time[-4:-2])-1).zfill(2)+'59'
    Make_Weather_Json(day_time)

    count = 0
    pty_result = []
    for one_dict in json_weather_result:
        if one_dict['category'] == 'PTY':
            if one_dict['fcstValue'] > 0:
                pty_result.append(one_dict['fcstValue'])
            count += 1
            if count == 1:
                break
    return pty_result

def get_fine_dust_URL():
    end_point = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
    parameters = "?ServiceKey="+access_key
    parameters+= "&numOfRows=30&pageNo=1&sidoName=%s&searchCondition=HOUR&_returnType=json"%urllib.parse.quote(sido)

    url = end_point+parameters
    retData = get_Request_URL(url)
    if retData == None:
        return None
    else:
        return json.loads(retData)

def Make_Fine_Dust_Json():
    global json_fine_dust_result
    json_fine_dust_result = get_fine_dust_URL()['list']

    day_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    with open('./data/대구_미세먼지조회_%s.json' %(day_time), 'w',encoding='utf8') as outfile:
        retJson = json.dumps(json_fine_dust_result, indent=4, sort_keys=True,ensure_ascii=False)
        outfile.write(retJson)

    print('대구_미세먼지조회_%s.json SAVED\n' %(day_time))

def get_the_concentration_of_fine_dust():
    Make_Fine_Dust_Json()
    for one_dict in json_fine_dust_result:
        if one_dict['stationName'] == gungu:
            pm10Grade = one_dict['pm10Grade']
            pm25Grade = one_dict['pm25Grade']
            return (pm10Grade, pm25Grade)


def update_scheduler():
    global g_Balcony_Windows
    while True:
        pty_result = get_Realtime_Weather_Info()
        pm10Grade,pm25Grade = get_the_concentration_of_fine_dust()

        if len(pty_result) > 0 or int(pm25Grade) > 1 or int(pm10Grade) > 1:
            g_Balcony_Windows = False
        elif len(pty_result) == 0 and int(pm25Grade) < 2 and int(pm10Grade) < 2:
            g_Balcony_Windows = True
        for count in range(schedule_cycle//10):
            time.sleep(10)
        print(f"스케줄러 작동..  {schedule_cycle}초 주기")


def smart_mode():
    ai_scheduler = threading.Thread(target=update_scheduler)
    global g_AI_Mode
    print("1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 Update")
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True:
            print("작동 완료!")
        else:
            print("중지!")
    if menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True:
            ai_scheduler.daemon = True
            ai_scheduler.start()
            print("작동 완료!")
        else:
            while ai_scheduler.is_alive():
                try:
                    terminate_ai_mode()
                except:
                    pass
            print("중지 완료!")
    elif menu_num == 3:
        get_Realtime_Weather_Info()
        print("실시간 기상정보가 업데이트되었습니다.")


print("<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>")
while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:
        check_device_status()
    elif menu_num == 2:
        control_device()
    elif menu_num == 3:
        smart_mode()
    elif menu_num == 4:
        break

