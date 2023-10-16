import time

import network
import urequests
from machine import Pin

from env import config

wlan_ssid = config["wlan_ssid"]
wlan_pass = config["wlan_pass"]
server_host = config["server_host"]
room_id = config["room_id"]

LIGHT_PIN_NO = 18
FAN_PIN_NO = 16

led = Pin("LED", Pin.OUT)
light = Pin(LIGHT_PIN_NO, Pin.OUT)
fan = Pin(FAN_PIN_NO, Pin.OUT)


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)

    wlan.active(True)
    wlan.connect(wlan_ssid, wlan_pass)

    while not wlan.isconnected():
        print("WiFi connecting...")
        time.sleep(1)

    ip = wlan.ifconfig()[0]
    print(f"WiFi connected. IP = {ip}")


def initial_blink():
    for _ in range(3):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)


def main():
    # 起動したことが分かるよう、LEDを最初に数回点滅
    initial_blink()

    # WiFiに接続
    connect_wifi()

    # WiFiに接続完了したら、LEDを点灯ß
    led.on()

    # サーバに部屋を登録
    req = urequests.post(
        f"http://{server_host}/rooms/{room_id}/register",
        headers={"Content-Type": "application/json"},
    )
    room = req.json()
    print(f"Room registered. id = {room_id}")

    # 部屋の状態をポーリング
    while True:
        req = urequests.get(f"http://{server_host}/rooms/{room_id}/poll")
        room = req.json()
        is_light_on = room["is_light_on"]
        is_fan_on = room["is_fan_on"]
        print("Room detail received.")
        print(f"  room.is_light_on = {is_light_on}")
        print(f"  room.is_fan_on = {is_fan_on}")

        if is_light_on:
            led.on()
        else:
            led.off()

        if is_fan_on:
            fan.on()
        else:
            fan.off()


main()
