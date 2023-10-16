# cloudserver

## 環境構築手順 (EC2 の場合)

### 1. Docker をインストール

参考: https://github.com/docker/docker-install

### 2. ソースコードを取得

```console
git clone https://github.com/os1ma/langchain-ai-assistant-hands-on.git
cd langchain-ai-assistant-hands-on/cloudserver
```

### 3. `.env` ファイルを作成

`.env.template` ファイルをコピーして `.env` ファイルを作成し、内容を編集します。

### 4. サーバを起動

```console
sudo docker compose up -d
```

### 5. 起動確認

```console
sudo docker compose ps
sudo docker compose logs -f
```

### 6. 動作確認用コマンド実行

```console
BASIC_AUTH_USER=testuser BASIC_AUTH_PASSWORD=testpassword ./test.sh
```
