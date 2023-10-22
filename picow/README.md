# Raspberry Pi Pico W

## Pico W への MicroPython のセットアップ

### 1. ファームウェアをダウンロード

[こちらのページ](https://micropython.org/download/RPI_PICO_W/) から、`v1.21.0 (2023-10-05) .uf2` をダウンロードしてください。

### 2. Pico W を PC に接続

### 3. ファームウェアをアップロード

「RPI-RP2」にアップロードしてください。

アップロードが完了したら、Pico W を接続し直してください。

## 環境構築手順

### 1. ソースコードを取得

```console
git clone https://github.com/os1ma/langchain-ai-assistant-hands-on.git
```

### 2. picow ディレクトリを VSCode で開く

```console
cd langchain-ai-assistant-hands-on/picow
code .
```

> **Warning**
> langchain-ai-assistant-hands-on ディレクトリを開くとうまくいかない可能性があります。

### 3. VSCode に MicroPico プラグインをインストール

### 4. `env.py` ファイル作成

`env.py.template` ファイルをコピーして `env.py` ファイルを作成し、内容を編集します。

### 5. Pico W に接続

Ctrl + Shift + P でコマンドパレットを開き、`MicroPico: Connect` を選択します。

### 5. Pico W にプロジェクトをアップロード

Ctrl + Shift + P でコマンドパレットを開き、`MicroPico: Delete all files from board` を選択します。

Ctrl + Shift + P でコマンドパレットを開き、`MicroPico: Upload project to Pico` を選択します。

### 6. 起動

Ctrl + Shift + P でコマンドパレットを開き、`MicroPico: Reset > Soft (listen)` を選択します。

main.py の実行が始まると、LED が最初に数回点滅します。

その後、WiFi に接続が完了すると、LED が点灯し続けます。
