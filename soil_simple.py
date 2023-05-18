import RPi.GPIO as GPIO
import time

soil_sensor = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(soil_sensor, GPIO.IN)

while True:
    needsWater = GPIO.input(soil_sensor)

    if needsWater:
        print("needs water!")
    else:
        print("no need to water!")
    time.sleep(5)
