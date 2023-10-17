import time

from machine import Pin

LIGHT_PIN_NO = 18
FAN_PIN_NO = 16

led = Pin("LED", Pin.OUT)
light = Pin(LIGHT_PIN_NO, Pin.OUT)
fan = Pin(FAN_PIN_NO, Pin.OUT)

led.on()
light.on()
fan.on()

time.sleep(5)

led.off()
light.off()
fan.off()
