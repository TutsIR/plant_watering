import time

import RPi.GPIO as GPIO

relay_pin = 21
soil_sensor_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)
GPIO.setup(soil_sensor_pin, GPIO.IN)

while True:
    needsWater = GPIO.input(soil_sensor_pin)

    if needsWater:
        print("needs water!")
        GPIO.output(relay_pin, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(relay_pin, GPIO.LOW)
    else:
        print("no need to water!")
        GPIO.output(relay_pin, GPIO.LOW)
    time.sleep(5)
