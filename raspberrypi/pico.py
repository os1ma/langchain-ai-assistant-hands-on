import time

import network
import urequests
from machine import Pin

from env import config

wlan_ssid = config["wlan_ssid"]
wlan_pass = config["wlan_pass"]
server_host = config["server_host"]
room_id = config["room_id"]

PIN_NO = 15


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)

    wlan.active(True)
    wlan.connect(wlan_ssid, wlan_pass)

    while not wlan.isconnected():
        print("WiFi connecting...")
        time.sleep(1)

    ip = wlan.ifconfig()[0]
    print(f"WiFi connected. IP = {ip}")


connect_wifi()

led = Pin(PIN_NO, Pin.OUT)

req = urequests.post(
    f"http://{server_host}/rooms/{room_id}/register",
    headers={"Content-Type": "application/json"},
)
room = req.json()
room_id = room["id"]
print(f"Room registered. id = {room_id}")

while True:
    req = urequests.get(f"http://{server_host}/rooms/{room_id}/poll")
    room = req.json()
    room_id = room["id"]
    is_light_on = room["is_light_on"]
    print(
        f"Room detail received. room.id = {room_id}, room.is_light_on = {is_light_on}"
    )

    if is_light_on:
        led.on()
    else:
        led.off()
