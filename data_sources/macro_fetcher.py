# data_sources/macro_fetcher.py

"""Fetch macroeconomic indicators from the FRED API."""

from typing import Optional, Dict
import requests
import pandas as pd

from config.env_loader import load_env


class MacroFetcher:
    """Retrieve macroeconomic data such as CPI or unemployment rates."""

    def __init__(self):
        self.config = load_env()
        self.api_key = self.config.get("FRED_API_KEY", "")

    def fetch_series(self, series_id: str) -> Optional[pd.DataFrame]:
        if not self.api_key:
            print("[MacroFetcher] Missing FRED_API_KEY")
            return None
        url = "https://api.stlouisfed.org/fred/series/observations"
        params = {
            "series_id": series_id,
            "api_key": self.api_key,
            "file_type": "json",
        }
        try:
            resp = requests.get(url, params=params, timeout=10)
            resp.raise_for_status()
            data = resp.json().get("observations", [])
            return pd.DataFrame(data)
        except Exception as exc:
            print(f"[MacroFetcher] Error fetching series {series_id}: {exc}")
            return None

    def snapshot(self) -> Dict[str, Optional[pd.DataFrame]]:
        """Return a dictionary of commonly used macro series."""
        series = ["CPIAUCSL", "UNRATE", "GDP", "DGS10"]
        return {sid: self.fetch_series(sid) for sid in series}
