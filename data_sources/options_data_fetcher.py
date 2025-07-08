# data_sources/options_data_fetcher.py

"""Fetch options market data to detect unusual activity."""

from typing import Any, Dict, Optional
from datetime import datetime

import requests

from config.env_loader import load_env


class OptionsDataFetcher:
    """Retrieve options flow information using the Tradier API."""

    BASE_URL = "https://api.tradier.com/v1/markets/options"

    def __init__(self):
        self.config = load_env()
        self.api_key = self.config.get("TRADIER_API_KEY", "")

    def _headers(self) -> Dict[str, str]:
        return {"Authorization": f"Bearer {self.api_key}", "Accept": "application/json"}

    def fetch_chains(self, ticker: str, expiration: str) -> Optional[Dict[str, Any]]:
        if not self.api_key:
            print("[OptionsDataFetcher] Missing TRADIER_API_KEY")
            return None
        url = f"{self.BASE_URL}/chains"
        params = {"symbol": ticker, "expiration": expiration}
        try:
            resp = requests.get(url, params=params, headers=self._headers(), timeout=10)
            resp.raise_for_status()
            return resp.json()
        except Exception as exc:
            print(f"[OptionsDataFetcher] Error fetching chains for {ticker}: {exc}")
            return None

    def fetch_expirations(self, ticker: str) -> Optional[Dict[str, Any]]:
        if not self.api_key:
            print("[OptionsDataFetcher] Missing TRADIER_API_KEY")
            return None
        url = f"{self.BASE_URL}/expirations"
        params = {"symbol": ticker}
        try:
            resp = requests.get(url, params=params, headers=self._headers(), timeout=10)
            resp.raise_for_status()
            return resp.json()
        except Exception as exc:
            print(f"[OptionsDataFetcher] Error fetching expirations for {ticker}: {exc}")
            return None
