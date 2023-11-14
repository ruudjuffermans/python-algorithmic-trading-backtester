"""
indicators module

This module provides classes for various financial indicators.

Classes:
    - MA: Moving Average indicator.
    - RSI: Relative Strength Index indicator.

Usage:
    from indicators.ma import MA
    from indicators.rsi import RSI

Example:
    ma_instance = MA(data, window=12)
    rsi_instance = RSI(data, window=14)

    # Use the instances to calculate and analyze indicators for financial data.

Author: Your Name
"""

from .ma import MA
from .rsi import RSI
