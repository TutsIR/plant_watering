import time

import RPi.GPIO as GPIO

led_pin = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

while True:
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led_pin, GPIO.LOW)
    time.sleep(1)
