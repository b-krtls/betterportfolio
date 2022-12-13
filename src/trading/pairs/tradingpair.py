"""The module defines relevant classes and functions relevant to
price data, that is used across different packages.

:REVIEW:: TODO: 
"""
import logging  # Be sure that this does not have security issues
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# from trading.connections.connection import _SimpleConnection
from ..connections.connection import _SimpleConnection

# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel("CRITICAL")  # DEBUG
logger.addHandler(logging.StreamHandler())

class Asset:
    def __init__(self, name:str, symbol:str) -> None:
        self.name = name.casefold()
        self.symbol = symbol.casefold()

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            if ((self.name == other.name) and (...)):
                return True
        else:
            return False

class ReferenceAsset(Asset):
    def __init__(self, name, symbol) -> None:
        super().__init__(name, symbol)

class TradingPair:
    markets = {
        "crypto": {
            "BTC", "ETH", "STX", "EGLD", "ALGO", "AVAX", "HBAR", 
            "USDT", "BUSD", "USDC", "TUSD", "USDP", "DAI", 
        },
        "currencies": {
            "USD", "EUR","GBP", "SEK", "CHF", "KWD", "CNY", "JPY", "KWD", ...
        },
        "stocks": {
            ...
        },
        "commodities": {
            "BRENT", "NATGAS", "XAU", "XAG", ...
        },
        "indices": {
            "SNP500", "NASDAQ", "CAC40", "NIKKEI225", "DAX40", ...,
        }
    }

    def __init__(self, base_asset, quote_asset):
        self.base_asset = base_asset
        self.quote_asset = quote_asset

        for i, v in self.markets.items():
            if self.base_asset.symbol in v:
                # Define the market from the symbol of asset
                self.market:str = i
                break
        else:
            self.market = "n/a"

    def get_price_history(self):
        pass

if __name__ == "__main__":
    tp = TradingPair(
        Asset("bitcoin", "btc"), Asset("tether", "usdt")
    )
    tp.get_price_history()