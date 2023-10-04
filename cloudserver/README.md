# cloudserver

## 環境構築手順 (EC2 の場合)

### 1. Docker をインストール

参考: https://github.com/docker/docker-install

### 2. サーバを実行

```console
git clone https://github.com/os1ma/langchain-ai-assistant-hands-on.git
cd langchain-ai-assistant-hands-on/cloudserver
sudo docker compose up -d
```

### 3. 起動確認

```console
sudo docker compose ps
sudo docker compose logs -f
```

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
