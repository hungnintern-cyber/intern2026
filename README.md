# intern2026

## W01:環境構築とサーバー起動
### 前提条件
- **Python 3.x**
- **Git**
---

###  環境構築

**1. プロジェクトのクローン:**
```bash
git clone git@github.com:hungnintern-cyber/intern2026.git
cd intern2026
```
**2. 仮想環境の作成:**

```bash
# venvの作成 (pipエラー回避のため --without-pip を使用)
python -m venv venv --without-pip
# 仮想環境の有効化 (Windows用)
.\venv\Scripts\activate
```

### サーバーの起動

```bash
cd W01
python server.py
```
実行後、ブラウザまたはPostmanで http://localhost:8000/api/health のURLにアクセスして
{"status": "ok"}の結果と表示されると完了。