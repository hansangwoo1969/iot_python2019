import  urllib.request
import time
import json

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Window = False
g_Door = False
g_AI_Mode = False

def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 프로그램 종료")

def print_device_status(device_name, device_status):
    print("%s 상태: " % device_name, end="")
    if device_status == True : print("작동")
    else: print("정지")

def check_device_status():
    print('')
    print_device_status('난방기', g_Radiator)
    print_device_status('가스밸브', g_Gas_Valve)
    print_device_status('발코니(베란다) 창문', g_Balcony_Window)
    print_device_status('출입문 상태', g_Door)

def print_device_menu():
    print("\n상태 변경할 기기를 선택하세요. ")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니 (베란다) 창")
    print("4. 출입문")

def control_device():     # 글로벌 변수의 값을 변경할 경우에는 변수선언 필요, 단순참조시는 불요필
    global g_Radiator, g_Gas_Valve, g_Balcony_Window, g_Door

    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))

    if menu_num == 1: g_Radiator = not g_Radiator
    if menu_num == 2: g_Gas_Valve = not g_Gas_Valve
    if menu_num == 3: g_Balcony_Window = not g_Balcony_Window
    if menu_num == 4: g_Door = not g_Door

    check_device_status()
def get_realtime_weather_info():              # ==============================작성할 것
    print("자! 메뉴얼 보고 작성해 보세요! == 미세먼지 값 보고, 메인메뉴로 가기 == ")


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
    retData = json.loads(retData)

    datas = retData['list']
    for data in datas:
        print(data['dataTime'],data['sidoName'], data['cityName'],'\t' "미세먼지 농도: ", data['pm10Value'])

    time.sleep(3000)
    print_main_menu()









def smart_mode():
    global  g_AI_Mode
    print("1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 Update")
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:
        print("현재 인공지능 모드 : ", end='')
        if g_AI_Mode == True:
            print("작동 완료!")
        else:
            print("중지!")
    if menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True: print("작동")
        else: print("중지!")
    elif menu_num == 3:
        get_realtime_weather_info()

print("<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>")
print("                               - 앨런 튜링-")
while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if(menu_num == 1):
        check_device_status()
    elif (menu_num == 2):
        control_device()
    elif (menu_num == 3):
        smart_mode()
    elif (menu_num == 4):
        break



