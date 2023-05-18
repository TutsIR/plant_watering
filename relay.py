import RPi.GPIO as GPIO
import time

relay_pin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

GPIO.output(relay_pin, GPIO.HIGH)
time.sleep(5)
GPIO.output(relay_pin, GPIO.LOW)
GPIO.cleanup()
