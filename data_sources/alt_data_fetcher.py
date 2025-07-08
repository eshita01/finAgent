# data_sources/alt_data_fetcher.py

"""Fetch alternative business data such as web traffic or job postings."""

from typing import Any, Dict, Optional
from datetime import datetime

import requests

from config.env_loader import load_env


class AltDataFetcher:
    """Gather alternative data using external APIs."""

    def __init__(self):
        self.config = load_env()
        self.api_key = self.config.get("SIMILARWEB_API_KEY", "")

    def fetch_web_traffic(self, domain: str) -> Optional[Dict[str, Any]]:
        """Fetch monthly visits from SimilarWeb."""
        if not self.api_key:
            print("[AltDataFetcher] Missing SIMILARWEB_API_KEY")
            return None
        url = (
            f"https://api.similarweb.com/v1/website/{domain}/total-traffic-and-engagement/visits"
        )
        params = {
            "api_key": self.api_key,
            "start_date": datetime.now().strftime("%Y-%m"),
            "granularity": "monthly",
        }
        try:
            resp = requests.get(url, params=params, timeout=10)
            resp.raise_for_status()
            return resp.json()
        except Exception as exc:
            print(f"[AltDataFetcher] Error fetching traffic for {domain}: {exc}")
            return None
