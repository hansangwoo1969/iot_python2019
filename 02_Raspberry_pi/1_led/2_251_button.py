# coding: cp949
# 버튼을 누를때 마다 카운트가 증가하는 코드,,, 안됨,,,조건을 눌려졌을 때 증가하는 것으로 변경
import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)

count=0

while True:

    if(GPIO.input(9)==1):
        time.sleep(0.1)
        count=count+1
        print("Count:"+str(count))
        while(GPIO.input(9)==1):
            time.sleep(0.1)