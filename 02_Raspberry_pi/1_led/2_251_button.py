# coding: cp949
# ��ư�� ������ ���� ī��Ʈ�� �����ϴ� �ڵ�,,, �ȵ�,,,������ �������� �� �����ϴ� ������ ����
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