import _thread
import time

from machine import Pin

LIGHT_1_PIN_NO = 15
LIGHT_2_PIN_NO = 16
LIGHT_BLINK_INTERVAL_SEC = 0.5

led = Pin("LED", Pin.OUT)
light1 = Pin(LIGHT_1_PIN_NO, Pin.OUT)
light2 = Pin(LIGHT_2_PIN_NO, Pin.OUT)

led.on()

while True:
    light1.on()
    light2.off()
    time.sleep(LIGHT_BLINK_INTERVAL_SEC)
    light1.off()
    light2.on()
    time.sleep(LIGHT_BLINK_INTERVAL_SEC)
