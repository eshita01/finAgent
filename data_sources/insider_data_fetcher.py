# data_sources/insider_data_fetcher.py

"""Fetch insider trading information using OpenInsider."""

from typing import List, Dict, Optional
import csv
import io

import requests

from config.env_loader import load_env


class InsiderDataFetcher:
    """Retrieve insider trading activity."""

    def __init__(self):
        self.config = load_env()

    def fetch_insider_trades(self, ticker: str) -> Optional[List[Dict[str, str]]]:
        url = f"https://openinsider.com/screener?s={ticker}&output=1"
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            csv_data = resp.text
            reader = csv.DictReader(io.StringIO(csv_data))
            return list(reader)
        except Exception as exc:
            print(f"[InsiderDataFetcher] Error fetching trades for {ticker}: {exc}")
            return None
