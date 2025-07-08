# data_sources/news_fetcher.py

"""Fetch recent news headlines for a ticker using the NewsAPI service."""

from datetime import datetime, timedelta
from typing import List, Dict, Optional

import requests

from config.env_loader import load_env


class NewsFetcher:
    """Retrieve news headlines for specific tickers."""

    BASE_URL = "https://newsapi.org/v2/everything"

    def __init__(self):
        self.config = load_env()
        self.api_key = self.config.get("NEWS_API_KEY", "")

    def fetch(self, query: str, days: int = 3) -> Optional[List[Dict[str, str]]]:
        if not self.api_key:
            print("[NewsFetcher] Missing NEWS_API_KEY")
            return None
        params = {
            "q": query,
            "from": (datetime.utcnow() - timedelta(days=days)).strftime("%Y-%m-%d"),
            "sortBy": "publishedAt",
            "apiKey": self.api_key,
            "language": "en",
        }
        try:
            resp = requests.get(self.BASE_URL, params=params, timeout=10)
            resp.raise_for_status()
            articles = resp.json().get("articles", [])
            return [
                {
                    "title": art.get("title"),
                    "url": art.get("url"),
                    "publishedAt": art.get("publishedAt"),
                }
                for art in articles
            ]
        except Exception as exc:
            print(f"[NewsFetcher] Error fetching news for {query}: {exc}")
            return None
