import time

import Adafruit_DHT
import RPi.GPIO as GPIO

dht22_pin = 26

GPIO.setmode(GPIO.BCM)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(22, dht22_pin)

    if humidity is not None and temperature is not None:
        print(f'Temperature: {temperature:.2f} C')
        print(f'Humidity: {humidity:.2f} %')
    else:
        print('Failed to read data from DHT22 sensor')

    time.sleep(5)
