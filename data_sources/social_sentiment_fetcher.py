# data_sources/social_sentiment_fetcher.py

"""Collect social media posts from Reddit using Pushshift."""

from typing import List, Dict, Optional
import requests

from config.env_loader import load_env


class SocialSentimentFetcher:
    """Fetch recent social media mentions."""

    BASE_URL = "https://api.pushshift.io/reddit/search/comment/"

    def __init__(self):
        self.config = load_env()

    def fetch_reddit_comments(self, query: str, limit: int = 100) -> Optional[List[Dict[str, str]]]:
        params = {"q": query, "size": limit}
        try:
            resp = requests.get(self.BASE_URL, params=params, timeout=10)
            resp.raise_for_status()
            data = resp.json().get("data", [])
            return [{"body": item.get("body"), "created_utc": item.get("created_utc")}
                    for item in data]
        except Exception as exc:
            print(f"[SocialSentimentFetcher] Error fetching reddit data: {exc}")
            return None
