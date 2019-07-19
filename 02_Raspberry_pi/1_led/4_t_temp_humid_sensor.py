# coding: cp949
# ����� �ڵ� :   python3 4_t_temp_sensor.py
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11

# �½��� ������ ����� ���̴� �Ʒ��� ���� ���̷�Ʈ�� ����
# Signal(���) - GPIO4 (Pin no. 7)
# Vcc(����) - 5V ���� (Pin no. 2)
# Ground(����) - GND (Pin no. 6)

pin = 4

try:
    while True:
        h, t = Adafruit_DHT.read_retry(sensor, pin)
        if h is not None and t is not None:
            print("Temperature = {0:0.1f}*C Humidity = {1:0.1f}%".format(t, h))
        else:
            print('Read error')
        time.sleep(100)

except KeyboardInterrupt:
    print("Terminated by Keyboard")

finally:
    print("End of Program")

