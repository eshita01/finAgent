# data_sources/technical_analysis.py

"""Basic technical indicator calculations using pandas."""

from typing import Dict

import pandas as pd


class TechnicalAnalysis:
    """Compute common technical indicators from OHLCV data."""

    @staticmethod
    def sma(data: pd.Series, period: int = 20) -> pd.Series:
        return data.rolling(window=period).mean()

    @staticmethod
    def rsi(data: pd.Series, period: int = 14) -> pd.Series:
        delta = data.diff()
        gain = (delta.where(delta > 0, 0)).rolling(period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    @staticmethod
    def macd(data: pd.Series) -> pd.DataFrame:
        exp1 = data.ewm(span=12, adjust=False).mean()
        exp2 = data.ewm(span=26, adjust=False).mean()
        macd = exp1 - exp2
        signal = macd.ewm(span=9, adjust=False).mean()
        hist = macd - signal
        return pd.DataFrame({'macd': macd, 'signal': signal, 'hist': hist})

    @staticmethod
    def bollinger_bands(data: pd.Series, period: int = 20, std_dev: int = 2) -> pd.DataFrame:
        sma = data.rolling(window=period).mean()
        std = data.rolling(window=period).std()
        upper = sma + std_dev * std
        lower = sma - std_dev * std
        return pd.DataFrame({'upper': upper, 'sma': sma, 'lower': lower})

    @classmethod
    def compute_all(cls, df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
        close = df['Close']
        indicators = {
            'sma_20': cls.sma(close, 20),
            'rsi_14': cls.rsi(close, 14),
            'macd': cls.macd(close),
            'bollinger': cls.bollinger_bands(close, 20, 2),
        }
        return indicators
