📈 株価取得Bot（米国株 / Yahoo Finance API）

---

### 概要

米国株（例：SMCI, AAPL など）の株価データを自動で取得し、  
日々のデータをCSVに保存＆チャート化するPython製Botです。  
データ収集・記録・チャート描画・自動更新に対応し、トレードの振り返りや可視化にも活用できます。

---

### 使用技術

- Python（requests, pandas, yfinance, matplotlib）
- スケジューリング（cron / Task Scheduler）
- ファイル出力・ログ管理（CSV / JSON / PNG）

---

### 機能

- 任意の銘柄の株価（始値 / 終値 / 高値 / 安値 / 出来高）を取得
- 毎日定時にデータを自動取得・保存（CSV形式、日付ごと）
- 各銘柄の終値を折れ線グラフでチャート化（PNG出力）
- 自動でフォルダ分け＆日付タグ付き保存
- 複数銘柄を一括取得に対応（例：AAPL, SMCI, NVDA など）

---

### 今後の拡張予定

- LINEやSlackへの通知連携
- テクニカル指標（移動平均・RSIなど）の自動計算
- トレード日記との連携（取引履歴との統合）

---

### リンク

- [GitHubリポジトリURL]
- [Qiita / note 解説記事リンク]

