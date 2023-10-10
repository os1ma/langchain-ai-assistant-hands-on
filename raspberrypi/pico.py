import time

from machine import Pin

led = Pin("LED", Pin.OUT)

while True:
    time.sleep(1)
    led.on()

    time.sleep(1)
    led.off()
