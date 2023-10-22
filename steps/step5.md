# Step5: Streamlit 上の部屋の電気・扇風機を操作させよう

## ハンズオン手順

### 1. `agent_app.py` を編集して、エージェントが Streamlit 上の部屋の電気・扇風機（の画像）を操作できるようにしてください。

以下の箇所を...

```python
    # Step5: Streamlit 上の部屋の電気・扇風機（の画像）を操作させよう
    # streamlit_image_tools = load_streamlit_image_tools()
    # tools.extend(streamlit_image_tools)
```

次のようにしてください。

```python
    # Step5: Streamlit 上の部屋の電気・扇風機（の画像）を操作させよう
    streamlit_image_tools = load_streamlit_image_tools()
    tools.extend(streamlit_image_tools)
```

> **Warning**
> agent_app.py の編集後、ファイルの保存を忘れないように注意してください。

### 2. Web アプリを読み込み直してください。

Streamlit の画面右上に表示される「Rerun」をクリックするか、ブラウザのリロードを実施してください。

> **Warning**
> ブラウザのリロードのほうが確実な動作になります。
> 「Rerun」でコードの変更がうまく反映されない場合は、ブラウザのリロードを試してみてください。

### 3. 電気・扇風機を操作させてみましょう。（例「電気つけて」「扇風機つけて」）

例えば「電気つけて」「扇風機つけて」と依頼してみてください。
