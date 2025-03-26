### 📈 株価取得Bot（米国株/Yahoo Finance API）

#### 概要
米国株（SMCIなど）の株価データを自動で取得し、日々のデータをCSVに保存するBotをPythonで作成。
データ収集、記録、自動更新に対応し、日々のトレード振り返りや可視化にも利用可能。

#### 使用技術
- Python（requests, pandas, yfinance）
- スケジューリング（cron / Task Scheduler）
- ログ管理・ファイル出力（CSV, JSON）

#### 機能
- 任意の銘柄の株価（始値/終値/高値/安値/出来高）を取得
- 毎日定時にデータを保存
- 自動でフォルダ分け＆日付付け保存
- 複数銘柄同時対応（AAPL, SMCI, NVDAなど）

#### リンク
- [GitHubリポジトリURL]
- [簡単な解説記事へのリンク（Qiita/note）]

