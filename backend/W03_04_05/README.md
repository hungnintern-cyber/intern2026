# Book Store API

## 実行方法
1. インストール: `pip install -r requirements.txt`
2. 実行: `uvicorn main:app --reload`
Swagger UI: `http://127.0.0.1:8000/docs`

## 認証（Authentication）ガイド

当プロジェクトでは、認証メカニズムとして **JWT (JSON Web Token)** を採用しています。

### 1. 動作の仕組み
* **フロー:** ユーザーがログイン -> サーバーが `access_token` を返却 -> クライアントは以降のリクエストヘッダーにこのトークンを添付する。
* **トークンの有効期限:** 30分

### 2. 認証用API
* **ユーザー登録:** `POST /auth/register` (Body JSON: `email`, `password`)
* **ログイン:** `POST /auth/login`
    * **注意:** このAPIは **OAuth2** 標準に準拠しているため、入力データはJSON形式ではなく **Form Data** 形式で送信してください。

#### Swagger UIでのテスト方法
1. 画面右上の **Authorize** ボタンをクリックします。
2. `username` 欄にメールアドレス、`password` 欄にパスワードを入力します。
3. **Login** をクリックします。鍵のアイコンが閉じた状態になればログイン成功です。
4. 以降、API呼び出し（例: `POST /books`）を行う際、自動的にトークンが付与されます。

#### Postmanでのテスト方法
1. メソッド: **POST**
2. URL: `http://127.0.0.1:8000/auth/login`
3. Bodyタブ: **`x-www-form-urlencoded`** を選択します。
4. Key - Value を入力します:
   * `username`: (登録したメールアドレスを入力。例: `admin@gmail.com`)
   * `password`: (パスワードを入力)
5. **Response:** 返却された `access_token` をコピーします。
6. 他のAPIを呼び出す場合: **Authorization** タブ -> Typeで **Bearer Token** を選択 -> トークンを貼り付けます。

## 権限管理 (RBAC)
| ロール (Role) | 権限 |
| :--- | :--- |
| **Guest** | 一覧の閲覧 (`GET`) |
| **User** | 書籍の作成 (`POST`)、自身の書籍の編集 (`PUT`) |
| **Admin** | **全権限** (書籍の削除、任意の書籍の編集) |

## 管理者 (Admin) の手動作成
**DB Browser for SQLite** を使用して以下の手順で行ってください:
1. `database.db` ファイルを開きます。
2. **Browse Data** タブを選択し、`users` テーブルを選択します。
3. 対象ユーザーの `role` カラムを `user` から `admin` に変更します。
4. **Write Changes** をクリックして変更を保存します。