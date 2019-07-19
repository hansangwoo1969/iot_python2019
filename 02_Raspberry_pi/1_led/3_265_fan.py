# coding: cp949

import RPi.GPIO as GPIO
import time
import curses               # 키 조작을 위한 라이브러리

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwmoutput = GPIO.PWM(18, 50) # GPIO18을 'pwmoutpur'객체로 작성, pwm주파수를 50Hz로 설정

pwmoutput.start(0)          # PWM초기화, 초기출력을 0으로 설정
stdscr = curses.initscr()   # 키 입력을 하는 객체를 작성
curses.noecho()             # 화면상에 입력한 문자가 표시나지 않게,,
fanduty=0                   # 출력값에 이용하는 변수값을 0으로 설정
while True:
    c = stdscr.getch()      # 키 입력을 읽고,
    if(c==ord('a')and(fanduty<100)):        # 'a'키가 눌리고, fanduty가 100미만 때,
        fanduty=fanduty+10
        pwmoutput.ChangeDutyCycle(fanduty)
    elif(c==ord('z')and (fanduty>0)):       # 'z'키가 눌리고, fanduty가 0초과일때,
        fanduty = fanduty - 10
        pwmoutput.ChangeDutyCycle(fanduty)  # GPIO18출력을 fanduty로 변경
    elif c==ord('q'):       # 'q'키를 누르면 루프에서 빠져 나옵니다.
        break
    pwmoutput.stop()        # PWM출력 멈춤
    curses.echo()           # 키 입력 문자를 표시하게 되돌림
    curses.endwin()         # 터미널표시가 이상하게 되지 않게 상태를 원래대로 되돌림