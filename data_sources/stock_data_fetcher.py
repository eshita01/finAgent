# data_sources/stock_data_fetcher.py

"""Utilities for fetching OHLCV data for stocks using yfinance."""

from typing import Optional

import pandas as pd
import yfinance as yf

from config.env_loader import load_env


class StockDataFetcher:
    """Fetch OHLCV price and volume data for tickers."""

    def __init__(self):
        self.config = load_env()

    def fetch_ohlcv(
        self,
        ticker: str,
        period: str = "1mo",
        interval: str = "1d",
    ) -> Optional[pd.DataFrame]:
        """Return OHLCV data for ``ticker`` or ``None`` on failure."""
        try:
            data = yf.download(ticker, period=period, interval=interval, progress=False)
            if data.empty:
                print(f"[StockDataFetcher] No data for {ticker}")
                return None
            return data
        except Exception as exc:
            print(f"[StockDataFetcher] Error fetching {ticker}: {exc}")
            return None
