# -*- coding:utf-8 -*-
import threading
import time
import ctypes
import urllib.request
import json
from bs4 import BeautifulSoup
from socket import *

'''
1조 프로그램_문수
현 pc
'''
g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_AI_Mode = False
scheduler_cycle = 300


port = 8080
server_ip = '192.168.0.17'
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((server_ip, port))


def terminate_ai_mode():
    """Terminates a python thread from another thread.
    :param thread: a threading.Thread instance
    """
    if not ai_scheduler.isAlive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(ai_scheduler.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ai_scheduler.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def abcdefg(check):
    if check == '1':
        sendData = '1'
        clientSock.send((sendData.encode('utf-8')))
        recvData = clientSock.recv(1024).decode('utf-8')
        print('서버: ', recvData)
        if (recvData == 'close'):
            print('Server notify that service is over')
            clientSock.close()
            print('Client is shutdown')
            exit()
    elif check == '2':
        sendData = '2'
        clientSock.send((sendData.encode('utf-8')))
        recvData = clientSock.recv(1024).decode('utf-8')
        print('서버: ', recvData)
        if (recvData == 'close'):
            print('Server notify that service is over')
            clientSock.close()
            print('Client is shutdown')
            exit()
    elif check == '3':
        sendData = '3'
        clientSock.send((sendData.encode('utf-8')))
        recvData = clientSock.recv(1024).decode('utf-8')
        print('서버: ', recvData)
        if (recvData == 'close'):
            print('Server notify that service is over')
            clientSock.close()
            print('Client is shutdown')
            exit()
    elif check == '4':
        sendData = '4'
        clientSock.send((sendData.encode('utf-8')))
        recvData = clientSock.recv(1024).decode('utf-8')
        print('서버: ', recvData)
        if (recvData == 'close'):
            print('Server notify that service is over')
            clientSock.close()
            print('Client is shutdown')
            exit()


def update_scheduler():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door
    while True:
        print(f"스케줄러 작동..  {scheduler_cycle/60}분 주기")
        location = urllib.parse.quote('신암동')
        url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=' + location + '&dataTerm=month&pageNo=1&numOfRows=1&ServiceKey=PebawJAP7xKGM%2Bk81GkrscIY6Lsw9L%2BsOSb82wGvmGtemPjHz4M6HHm3oXCJYpL51c%2BE%2FCXYmjmEBH%2BVy0kQ0g%3D%3D&ver=1.3&_returnType=json'
        req = urllib.request.Request(url)
        # req = urllib.request.Request(url.encode('utf-8').strip())
        try:
            response = urllib.request.urlopen(req)
            if response.getcode() == 200:
                retData = response.read().decode('utf-8')
        except Exception as e:
            print(e)
            print(" Error for URL: %s" % url)
            exit()
        retData = json.loads(retData)

        b = retData['list'][0]['pm10Grade1h']

        c = retData['list'][0]['pm25Grade1h']


        html = urllib.request.urlopen('http://www.kweather.co.kr/kma/kma_digital.html?area2_name=%EB%8F%99%EA%B5%AC%0D%0A%09%092974%7C%EA%B3%B5%EC%82%B0%EB%8F%99%0D%0A%09%092965%7C%EB%8F%84%ED%8F%89%EB%8F%99%0D%0A%09%092968%7C%EB%8F%99%EC%B4%8C%EB%8F%99%0D%0A%09%092969%7C%EB%B0%A9%EC%B4%8C%EB%8F%99%0D%0A%09%092966%7C%EB%B6%88%EB%A1%9C.%EB%B4%89%EB%AC%B4%EB%8F%99%0D%0A%09%092955%7C%EC%8B%A0%EC%95%941%EB%8F%99%0D%0A%09%092956%7C%EC%8B%A0%EC%95%942%EB%8F%99%0D%0A%09%092957%7C%EC%8B%A0%EC%95%943%EB%8F%99%0D%0A%09%092958%7C%EC%8B%A0%EC%95%944%EB%8F%99%0D%0A%09%092959%7C%EC%8B%A0%EC%95%945%EB%8F%99%0D%0A%09%092960%7C%EC%8B%A0%EC%B2%9C1.2%EB%8F%99%0D%0A%09%092961%7C%EC%8B%A0%EC%B2%9C3%EB%8F%99%0D%0A%09%092962%7C%EC%8B%A0%EC%B2%9C4%EB%8F%99%0D%0A%09%092971%7C%EC%95%88%EC%8B%AC1%EB%8F%99%0D%0A%09%092972%7C%EC%95%88%EC%8B%AC2%EB%8F%99%0D%0A%09%092973%7C%EC%95%88%EC%8B%AC3.4%EB%8F%99%0D%0A%09%092967%7C%EC%A7%80%EC%A0%80%EB%8F%99%0D%0A%09%092970%7C%ED%95%B4%EC%95%88%EB%8F%99%0D%0A%09%092963%7C%ED%9A%A8%EB%AA%A91%EB%8F%99%0D%0A%09%092964%7C%ED%9A%A8%EB%AA%A92%EB%8F%99%0D%0A%09&area1=area_3&area2=3&area3=2958%7C%EC%8B%A0%EC%95%944%EB%8F%99&x=3&y=14')
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.findAll('ul', attrs={'class': 'kma_digital_predent_wtext'})

        test = tags[0].find('li').text
        test = test.split()
        weather = test[1]


        if '뇌우' == weather or '비' == weather or '소나기' == weather or weather == '눈':
            if g_Balcony_Windows == True:
                g_Balcony_Windows = not g_Balcony_Windows
                print(f'{weather} 때문에 창문을 닫습니다.')
        elif (int(b)>1 or int(c)>1) and g_Balcony_Windows == True:
            if g_Balcony_Windows == True:
                print("대기 상태가 좋지않아 창문을 닫습니다.")
                g_Balcony_Windows = not g_Balcony_Windows

        for i in range(scheduler_cycle//10+1):
            time.sleep(10)







def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 프로그램 종료")

def print_device_status(device_name,devcie_status):
    print("%s 상태: "%device_name, end="")
    if devcie_status == True : print("작동")
    else: print("정지")

def print_device_statuc(device_name,devcie_status):
    print("%s 상태: "%device_name, end="")
    if devcie_status == True : print("열림")
    else: print("닫힘")

def check_device_status():
    print('')
    print_device_status('가습기',g_Radiator)
    print_device_status('제습기', g_Gas_Valve)
    print_device_statuc('창문', g_Balcony_Windows)
    print_device_status('에어컨', g_Door)

def print_device_menu():
    print("\n상태 변경할 기기를 선택하세요.")
    print("1. 가습기")
    print("2. 제습기")
    print("3. 창문")
    print("4. 에어컨")

def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door

    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))

    if menu_num == 1:
        g_Radiator = not g_Radiator
        abcdefg('1')
    if menu_num == 2:
        g_Gas_Valve = not g_Gas_Valve
        abcdefg('2')
    if menu_num == 3:
        g_Balcony_Windows = not g_Balcony_Windows
        abcdefg('3')
    if menu_num == 4:
        g_Door = not g_Door
        abcdefg('4')

    check_device_status()
def get_realtime_weather_info():
    location = urllib.parse.quote('신암동')
    url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=' + location + '&dataTerm=month&pageNo=1&numOfRows=1&ServiceKey=PebawJAP7xKGM%2Bk81GkrscIY6Lsw9L%2BsOSb82wGvmGtemPjHz4M6HHm3oXCJYpL51c%2BE%2FCXYmjmEBH%2BVy0kQ0g%3D%3D&ver=1.3&_returnType=json'
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            #print(" Url Request Success")
            retData = response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print(" Error for URL: %s" % url)
        exit()
    retData = json.loads(retData)

    aa = retData['list'][0]['pm10Grade1h']
    bb = retData['list'][0]['pm25Grade1h']

    if aa == '1':
        aa = '좋음'
    elif aa == '2':
        aa = '보통'
    elif aa == '3':
        aa = '나쁨'
    elif aa == '4':
        aa = '매우나쁨'

    if bb == '1':
        bb = '좋음'
    elif bb == '2':
        bb = '보통'
    elif bb == '3':
        bb = '나쁨'
    elif bb == '4':
        bb = '매우나쁨'

    print("")
    print(f"{retData['parm']['stationName']}")
    print(f"미세먼지 등급: {aa}")
    print(f"초미세먼지 등급: {bb}")

    html = urllib.request.urlopen(
        'http://www.kweather.co.kr/kma/kma_digital.html?area2_name=%EB%8F%99%EA%B5%AC%0D%0A%09%092974%7C%EA%B3%B5%EC%82%B0%EB%8F%99%0D%0A%09%092965%7C%EB%8F%84%ED%8F%89%EB%8F%99%0D%0A%09%092968%7C%EB%8F%99%EC%B4%8C%EB%8F%99%0D%0A%09%092969%7C%EB%B0%A9%EC%B4%8C%EB%8F%99%0D%0A%09%092966%7C%EB%B6%88%EB%A1%9C.%EB%B4%89%EB%AC%B4%EB%8F%99%0D%0A%09%092955%7C%EC%8B%A0%EC%95%941%EB%8F%99%0D%0A%09%092956%7C%EC%8B%A0%EC%95%942%EB%8F%99%0D%0A%09%092957%7C%EC%8B%A0%EC%95%943%EB%8F%99%0D%0A%09%092958%7C%EC%8B%A0%EC%95%944%EB%8F%99%0D%0A%09%092959%7C%EC%8B%A0%EC%95%945%EB%8F%99%0D%0A%09%092960%7C%EC%8B%A0%EC%B2%9C1.2%EB%8F%99%0D%0A%09%092961%7C%EC%8B%A0%EC%B2%9C3%EB%8F%99%0D%0A%09%092962%7C%EC%8B%A0%EC%B2%9C4%EB%8F%99%0D%0A%09%092971%7C%EC%95%88%EC%8B%AC1%EB%8F%99%0D%0A%09%092972%7C%EC%95%88%EC%8B%AC2%EB%8F%99%0D%0A%09%092973%7C%EC%95%88%EC%8B%AC3.4%EB%8F%99%0D%0A%09%092967%7C%EC%A7%80%EC%A0%80%EB%8F%99%0D%0A%09%092970%7C%ED%95%B4%EC%95%88%EB%8F%99%0D%0A%09%092963%7C%ED%9A%A8%EB%AA%A91%EB%8F%99%0D%0A%09%092964%7C%ED%9A%A8%EB%AA%A92%EB%8F%99%0D%0A%09&area1=area_3&area2=3&area3=2958%7C%EC%8B%A0%EC%95%944%EB%8F%99&x=3&y=14')
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.findAll('ul', attrs={'class': 'kma_digital_predent_wtext'})
    tags2 = soup.findAll('li', attrs={'class': 'kma_digital_predent_humi'})

    test = tags[0].find('li').text
    test = test.split()
    temp = test[0]
    temp = temp.split('℃')
    temp = float(temp[0])
    weather = test[1]
    print(f'날씨: {weather}')

    humidity = tags2[0].text
    humidity = humidity.replace('·', '')
    humidity = humidity.split(':')
    humidity = humidity[1]
    humidity = humidity.split('%')
    humidity = humidity[0]
    humidity = humidity.lstrip()
    humidity = int(humidity)

    print(f'온도: {temp}℃')
    print(f'습도: {humidity}%')

def smart_mode():
    global g_AI_Mode
    print("1. 인공지능 모드 조회")
    print("2. 창문 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 Update")
    menu_num = int(input("메뉴를 선택하세요: "))


    if menu_num == 1:
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True:
            print("작동중!")
        else:
            print("중지!")
    if menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True:
            print("작동 완료!")
            ai_scheduler.daemon = True
            ai_scheduler.start()
            time.sleep(1)
        else:
            while ai_scheduler.is_alive():
                try:
                    terminate_ai_mode()
                except:
                    pass
            print("중지 완료!")
    elif menu_num == 3:
        get_realtime_weather_info()

print('Connecting to the server(%s) on %d port' %(server_ip, port))
print("<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>")
print("                                 - 1조 -")
ai_scheduler = threading.Thread(target=update_scheduler)
while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if(menu_num == 1):
        check_device_status()
    elif(menu_num ==2):
        control_device()
    elif(menu_num == 3):
        smart_mode()
    elif(menu_num == 4):
        sendData = 'q'
        clientSock.send((sendData.encode('utf-8')))
        recvData = clientSock.recv(1024).decode('utf-8')
        print('서버: ', recvData)
        print('Client is shutdown')
        print('Server notify that service is over')
        clientSock.close()
        print('Client is shutdown')
        break