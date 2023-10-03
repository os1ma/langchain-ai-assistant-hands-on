# 機能一覧

## クラウドサーバ

- 認証
- ルーム
  - 作成
  - 一覧
  - 詳細
    - 接続クライアント一覧
    - 電気や扇風機の状態を含む
- 接続クライアント
  - 登録
  - 切断時の自動登録解除

## API

- GET /rooms
- POST /rooms
- GET /rooms/{roomId}
- GET /rooms/{roomId}/poll
  - 接続クライアントの登録・解除もこの処理の内部で実行
