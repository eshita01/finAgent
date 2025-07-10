"""Simple decision logic based on technical indicators."""

from typing import Dict, Optional
import pandas as pd


class DecisionSynthesizer:
    """Generate a basic trading signal from technical indicators."""

    def synthesize(self, data: Dict[str, pd.DataFrame]) -> Optional[str]:
        """Return 'BUY', 'SELL', or 'HOLD' based on indicators."""
        if not data:
            return None
        indicators = data.get("indicators", {})
        ohlcv = data.get("ohlcv")
        if ohlcv is None:
            return None

        close = ohlcv["Close"]
        sma = indicators.get("sma_20")
        rsi = indicators.get("rsi_14")
        if sma is None or rsi is None:
            return None

        latest_close = close.iloc[-1]
        latest_sma = sma.iloc[-1]
        latest_rsi = rsi.iloc[-1]

        if latest_close > latest_sma and latest_rsi > 55:
            return "BUY"
        if latest_close < latest_sma and latest_rsi < 45:
            return "SELL"
        return "HOLD"
