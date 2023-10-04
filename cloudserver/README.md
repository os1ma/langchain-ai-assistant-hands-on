# cloudserver

## 動作確認用コマンド

```console
curl http://localhost:8000
```

```console
curl http://localhost:8000/rooms
```

```console
curl -X POST \
  -H 'Content-Type: application/json' \
  http://localhost:8000/rooms/myroom/register
```

```console
curl -X POST \
  -H 'Content-Type: application/json' \
  http://localhost:8000/rooms/myroom/update \
  -d '{"is_light_on": true}'
```

```console
curl http://localhost:8000/rooms/myroom/poll
```
