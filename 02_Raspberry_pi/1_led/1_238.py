import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmod(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, GPIO.HIGH)
while True:
    GPIO.output(4, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(4, GPIO.LOW)
    time.sleep(1)