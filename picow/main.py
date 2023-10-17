import time

import network
import urequests
from machine import Pin

from env import config

wlan_ssid = config["wlan_ssid"]
wlan_pass = config["wlan_pass"]
server_host = config["server_host"]
room_id = config["room_id"]
basic_auth_username = config["basic_auth_username"]
basic_auth_password = config["basic_auth_password"]

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
    print("Initializing...")
    initial_blink()

    # WiFiに接続
    connect_wifi()

    # WiFiに接続完了したら、LEDを点灯
    led.on()

    # サーバに部屋を登録
    print(f"Room registering... server_host = {server_host}, room_id = {room_id}")
    response = urequests.post(
        f"http://{server_host}/rooms/{room_id}/register",
        headers={
            "Content-Type": "application/json",
        },
        auth=(basic_auth_username, basic_auth_password),
    )

    room = response.json()
    print(f"Room registered. room_id = {room_id}")

    # 部屋の状態をポーリング
    while True:
        print(f"Room polling... room_id = {room_id}")
        response = urequests.get(
            f"http://{server_host}/rooms/{room_id}/poll",
            auth=(basic_auth_username, basic_auth_password),
        )

        room = response.json()
        is_light_on = room["is_light_on"]
        is_fan_on = room["is_fan_on"]
        print(f"Room received. is_light_on = {is_light_on}, is_fan_on = {is_fan_on}")

        if is_light_on:
            light.on()
        else:
            light.off()

        if is_fan_on:
            fan.on()
        else:
            fan.off()


main()
