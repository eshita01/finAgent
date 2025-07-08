# data_sources/finance_api.py

import yfinance as yf
import pandas as pd
from typing import Optional

def fetch_ohlcv(
    ticker: str,
    period: str = "7d",        # Options: '1d', '5d', '1mo', '3mo', '6mo', '1y', etc.
    interval: str = "1h"       # Options: '1m', '2m', '5m', '15m', '1h', '1d', etc.
) -> Optional[pd.DataFrame]:
    """
    Fetch OHLCV (Open-High-Low-Close-Volume) data for a given ticker.

    Returns:
        pd.DataFrame or None
    """
    try:
        data = yf.download(ticker, period=period, interval=interval, progress=False)
        if data.empty:
            print(f"[FinanceAPI] No data found for ticker: {ticker}")
            return None
        return data
    except Exception as e:
        print(f"[FinanceAPI] Error fetching data for {ticker}: {e}")
        return None
