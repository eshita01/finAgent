"""Run technical analysis on fetched stock data."""

from typing import Dict, Optional

import pandas as pd

from data_sources.stock_data_fetcher import StockDataFetcher
from analysis.technical_analysis import TechnicalAnalysis



class TechnicalAnalysisNode:
    """Fetch data for a ticker and compute technical indicators."""

    def __init__(self, fetcher: Optional[StockDataFetcher] = None):
        self.fetcher = fetcher or StockDataFetcher()

    def run(
        self,
        ticker: str,
        period: str = "1mo",
        interval: str = "1d",
    ) -> Optional[Dict[str, pd.DataFrame]]:
        """Return OHLCV and indicator data for ``ticker``."""
        df = self.fetcher.fetch_ohlcv(ticker, period=period, interval=interval)
        if df is None:
            return None
        indicators = TechnicalAnalysis.compute_all(df)
        return {"ohlcv": df, "indicators": indicators}
