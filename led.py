from gpiozero import LED
from time import sleep

blue = LED(20)
while True:
    blue.on()
    sleep(0.1)
    blue.off()
    sleep(0.1)
