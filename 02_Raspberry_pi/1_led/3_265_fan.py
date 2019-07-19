# coding: cp949

import RPi.GPIO as GPIO
import time
import curses               # Ű ������ ���� ���̺귯��

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwmoutput = GPIO.PWM(18, 50) # GPIO18�� 'pwmoutpur'��ü�� �ۼ�, pwm���ļ��� 50Hz�� ����

pwmoutput.start(0)          # PWM�ʱ�ȭ, �ʱ������ 0���� ����
stdscr = curses.initscr()   # Ű �Է��� �ϴ� ��ü�� �ۼ�
curses.noecho()             # ȭ��� �Է��� ���ڰ� ǥ�ó��� �ʰ�,,
fanduty=0                   # ��°��� �̿��ϴ� �������� 0���� ����
while True:
    c = stdscr.getch()      # Ű �Է��� �а�,
    if(c==ord('a')and(fanduty<100)):        # 'a'Ű�� ������, fanduty�� 100�̸� ��,
        fanduty=fanduty+10
        pwmoutput.ChangeDutyCycle(fanduty)
    elif(c==ord('z')and (fanduty>0)):       # 'z'Ű�� ������, fanduty�� 0�ʰ��϶�,
        fanduty = fanduty - 10
        pwmoutput.ChangeDutyCycle(fanduty)  # GPIO18����� fanduty�� ����
    elif c==ord('q'):       # 'q'Ű�� ������ �������� ���� ���ɴϴ�.
        break
    pwmoutput.stop()        # PWM��� ����
    curses.echo()           # Ű �Է� ���ڸ� ǥ���ϰ� �ǵ���
    curses.endwin()         # �͹̳�ǥ�ð� �̻��ϰ� ���� �ʰ� ���¸� ������� �ǵ���