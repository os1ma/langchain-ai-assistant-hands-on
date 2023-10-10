# raspberrypi

## 実行手順

main.py をラズベリーパイにダウンロードして以下のように実行します。

```console
python main.py <サーバの IP アドレス> <ルーム ID>
```

※ ルーム ID には、適当な文字列を指定してください。

## Pico W の動作確認

```python
from machine import Pin
led = Pin(15, Pin.OUT)
led.on()
led.off()
```

## Pico W の場合

env.py に以下の内容を記述します。

```python
config = {
    "wlan_ssid": "SSID",
    "wlan_pass": "PASSWORD",
    "server_host": "IP Address",
    "room_id": "myroom",
}
```

env.py を Pico W にアップロードして pico.py を実行します。