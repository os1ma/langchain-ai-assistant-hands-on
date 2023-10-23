import _thread
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

LIGHT_1_PIN_NO = 15
LIGHT_2_PIN_NO = 16
LIGHT_BLINK_INTERVAL_SEC = 0.5

led = Pin("LED", Pin.OUT)
light1 = Pin(LIGHT_1_PIN_NO, Pin.OUT)
light2 = Pin(LIGHT_2_PIN_NO, Pin.OUT)

is_light_on = False


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)

    wlan.active(True)
    wlan.connect(wlan_ssid, wlan_pass)

    while not wlan.isconnected():
        print("WiFi connecting...")
        time.sleep(1)

    ip = wlan.ifconfig()[0]
    print(f"WiFi connected. IP = {ip}")


def blink_led(interval_sec = 0.1):
    for _ in range(3):
        led.on()
        time.sleep(interval_sec)
        led.off()
        time.sleep(interval_sec)


def blink_lights_thread():
    while True:
        if is_light_on:
            light1.on()
            light2.off()
            time.sleep(LIGHT_BLINK_INTERVAL_SEC)
            light1.off()
            light2.on()
            time.sleep(LIGHT_BLINK_INTERVAL_SEC)
        else:
            light1.off()
            light2.off()
            time.sleep(LIGHT_BLINK_INTERVAL_SEC)


def main():
    # 起動したことが分かるよう、LEDを最初に数回点滅
    print("Initializing...")
    blink_led(interval_sec=0.5)

    # WiFiに接続
    connect_wifi()

    # WiFiに接続完了したら、LEDを点灯
    led.on()

    # ライトの点灯・消灯のスレッドを開始
    _thread.start_new_thread(blink_lights_thread, ())

    # サーバに部屋を登録
    print(f"Room registering... server_host = {server_host}, room_id = {room_id}")
    urequests.post(
        f"http://{server_host}/rooms/{room_id}/register",
        headers={
            "Content-Type": "application/json",
        },
        auth=(basic_auth_username, basic_auth_password),
    )
    print(f"Room registered. room_id = {room_id}")

    # 部屋の状態をポーリング
    while True:
        print(f"Room polling... room_id = {room_id}")
        response = urequests.get(
            f"http://{server_host}/rooms/{room_id}/poll",
            auth=(basic_auth_username, basic_auth_password),
        )

        room = response.json()

        global is_light_on
        is_light_on = room["is_light_on"]
        print(f"Room received. is_light_on = {is_light_on}")
        blink_led()
        led.on()


if __name__ == "__main__":
    main()
