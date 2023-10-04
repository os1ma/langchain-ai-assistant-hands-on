# cloudserver

## 動作確認用コマンド

```console
curl -X POST \
  -H 'Content-Type: application/json' \
  http://localhost:8000/rooms \
  -d '{"id": "sample"}'
```

```console
curl -X POST \
  -H 'Content-Type: application/json' \
  http://localhost:8000/rooms/sample/update \
  -d '{"is_light_on": true}'
```
