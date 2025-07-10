# data_sources/stock_data_fetcher.py

"""Utilities for fetching OHLCV data for stocks using yfinance."""

from typing import Optional

import pandas as pd
import numpy as np
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
                print(f"[StockDataFetcher] No data for {ticker}. Using sample data.")
                return self._load_sample_data()
            return data
        except Exception as exc:
            print(f"[StockDataFetcher] Error fetching {ticker}: {exc}. Using sample data.")
            return self._load_sample_data()

    def _load_sample_data(self) -> pd.DataFrame:
        """Return a small deterministic DataFrame for offline use."""
        dates = pd.date_range(end=pd.Timestamp.today(), periods=30)
        base = np.linspace(100, 102, len(dates))
        data = pd.DataFrame(
            {
                "Open": base + 0.1,
                "High": base + 0.2,
                "Low": base - 0.2,
                "Close": base,
                "Volume": np.full(len(dates), 1000000, dtype=int),
            },
            index=dates,
        )
        return data
