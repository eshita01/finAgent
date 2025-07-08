# config/env_loader.py

import os
from dotenv import load_dotenv

# Load .env variables into environment
load_dotenv()

def load_env():
    """Returns a dictionary of required environment variables."""
    return {
        "GOOGLE_API_KEY": os.getenv("GOOGLE_API_KEY"),
        "ALPHA_VANTAGE_API_KEY": os.getenv("ALPHA_VANTAGE_API_KEY", ""),   # optional
        "NEWS_API_KEY": os.getenv("NEWS_API_KEY", ""),                     # optional
        "FRED_API_KEY": os.getenv("FRED_API_KEY", ""),                     # optional
        "PUSHSHIFT_BASE_URL": "https://api.pushshift.io/reddit/search",   # constant
        "TWITTER_BEARER_TOKEN": os.getenv("TWITTER_BEARER_TOKEN", ""),    # optional
        "OPENINSIDER_API": os.getenv("OPENINSIDER_API", ""),              # optional
        "TRADIER_API_KEY": os.getenv("TRADIER_API_KEY", ""),              # optional
        "SIMILARWEB_API_KEY": os.getenv("SIMILARWEB_API_KEY", "")         # optional
    }
