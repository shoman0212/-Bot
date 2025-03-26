# ====== fetcher.py ======
import yfinance as yf

def fetch_stock_data(ticker, period="2d", interval="1d"):
    data = yf.download(ticker, period=period, interval=interval)
    return data


# ====== plotter.py ======
import matplotlib.pyplot as plt
import os
import pandas as pd


def save_closing_price_chart(data, ticker, output_dir):
    plt.figure(figsize=(8, 4))
    plt.plot(data.index, data['Close'], marker='o', label="Close Price")

    # 移動平均線（5日）を追加（条件：データが5日以上ある場合）
    if len(data) >= 5:
        data['SMA_5'] = data['Close'].rolling(window=5).mean()
        plt.plot(data.index, data['SMA_5'], linestyle='--', label="5-Day SMA")

    plt.title(f"{ticker} - Closing Prices")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.legend()

    chart_path = os.path.join(output_dir, f"{ticker}_chart.png")
    plt.savefig(chart_path)
    plt.close()
    return chart_path


# ====== main.py ======
import pandas as pd
from datetime import datetime
import os

from fetcher import fetch_stock_data
from plotter import save_closing_price_chart

# ====== 設定 ======
tickers = ["SMCI", "AAPL", "NVDA"]
base_dir = "stock_data"

today = datetime.today().strftime('%Y-%m-%d')
output_dir = os.path.join(base_dir, today)
os.makedirs(output_dir, exist_ok=True)

# ====== 処理 ======
for ticker in tickers:
    try:
        data = fetch_stock_data(ticker, period="7d")  # SMAのために7日分取得
        if data.empty:
            print(f"No data for {ticker}")
            continue

        latest = data.tail(1)
        latest.reset_index(inplace=True)
        csv_path = os.path.join(output_dir, f"{ticker}.csv")
        latest.to_csv(csv_path, index=False)

        save_closing_price_chart(data, ticker, output_dir)

        print(f"Saved {ticker} data and chart.")

    except Exception as e:
        print(f"Error with {ticker}: {e}")
