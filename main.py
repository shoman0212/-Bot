import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# ====== 設定 ======
tickers = ["SMCI", "AAPL", "NVDA"]  # 任意の銘柄リスト
base_dir = "stock_data"  # 保存フォルダ

today = datetime.today().strftime('%Y-%m-%d')
output_dir = os.path.join(base_dir, today)
os.makedirs(output_dir, exist_ok=True)

# ====== 処理 ======
for ticker in tickers:
    try:
        data = yf.download(ticker, period="2d", interval="1d")
        if data.empty:
            print(f"No data for {ticker}")
            continue

        latest = data.tail(1)
        latest.reset_index(inplace=True)
        csv_path = os.path.join(output_dir, f"{ticker}.csv")
        latest.to_csv(csv_path, index=False)

        # チャート描画（終値）
        plt.figure(figsize=(8, 4))
        plt.plot(data.index, data['Close'], marker='o', label="Close Price")
        plt.title(f"{ticker} - Closing Prices")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.grid(True)
        plt.legend()

        chart_path = os.path.join(output_dir, f"{ticker}_chart.png")
        plt.savefig(chart_path)
        plt.close()

        print(f"Saved {ticker} data and chart.")

    except Exception as e:
        print(f"Error with {ticker}: {e}")
