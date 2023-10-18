# Step5: ネットワークの向こうの電気・扇風機を操作させよう

## 注意

このステップは実機 (Raspberry Pi Pico W) を操作します。
全員分の実機はないため、何名かに代表して挑戦していただきます。

## ハンズオン手順

### 1. `agent_app.py` を編集して、エージェントがネットワークの向こうの電気を操作できるようにしてください。

以下の箇所を...

```python
    # Step5: ネットワークの向こうの電気・扇風機を操作させよう
    # ※ Step5のツールはStep4のツールと同時に使えません。どちらかだけ有効化してください
    # remote_room_tools = load_remote_room_tools(
    #     host="localhost",
    #     room_id="myroom",
    #     basic_auth_username="testuser",
    #     basic_auth_password="testpassword",
    # )
    # tools.extend(remote_room_tools)
```

次のようにしてください。

```python
    # Step5: ネットワークの向こうの電気・扇風機を操作させよう
    # ※ Step5のツールはStep4のツールと同時に使えません。どちらかだけ有効化してください
    remote_room_tools = load_remote_room_tools(
        host="localhost",
        room_id="myroom",
        basic_auth_username="testuser",
        basic_auth_password="testpassword",
    )
    tools.extend(remote_room_tools)
```

ツールに設定する `host`、`room_id`、`basic_auth_username`、`basic_auth_password` の値は講師に確認してください。

> **Warning**
> このとき、Step4 で有効化したツールはコメントアウトして無効化してください。

> **Warning**
> agent_app.py の編集後、ファイルの保存を忘れないように注意してください。

### 2. Web アプリを読み込み直してください。

Streamlit の画面右上に表示される「Rerun」をクリックするか、ブラウザのリロードを実施してください。

> **Warning**
> ブラウザのリロードのほうが確実な動作になります。
> 「Rerun」でコードの変更がうまく反映されない場合は、ブラウザのリロードを試してみてください。

### 3. 電気・扇風機を操作させてみましょう。（例「電気つけて」「扇風機つけて」）

例えば「電気つけて」「扇風機つけて」と依頼してみてください。
