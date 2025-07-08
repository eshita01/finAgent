# data_sources/sector_etf_tracker.py

"""Track performance of sector ETFs using yfinance."""

from typing import Dict, List, Optional

import pandas as pd
import yfinance as yf


class SectorETFTracker:
    """Fetch historical sector ETF prices and compute returns."""

    @staticmethod
    def fetch_returns(etfs: List[str], period: str = "3mo") -> Optional[pd.DataFrame]:
        try:
            data = yf.download(etfs, period=period, interval="1d", progress=False)["Adj Close"]
            returns = data.pct_change().dropna()
            return returns
        except Exception as exc:
            print(f"[SectorETFTracker] Error fetching data: {exc}")
            return None
