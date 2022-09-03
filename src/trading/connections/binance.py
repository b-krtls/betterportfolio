"""The module defines relevant classes and functions relevant to
cryptocurrencies price data.

:REVIEW:: TODO: 
"""
# import sys
# import json
import logging  # Be sure that this does not have security issues
from urllib.parse import urljoin

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

from src.auxiliary.price import PriceHistory
from connection import _SimpleConnection

logger = logging.getLogger("Binance")
logger.setLevel("CRITICAL") #DEBUG
logger.addHandler(logging.StreamHandler())

class BinanceConnection():
    """
    An abstraction of Connection to Binance API
    """

    bases = [
        r"https://api{}.binance.com".format(i) for i in [None, 1, 2, 3]
    ]
    # :TODO: If retrieval fails, test others, api1-2-3

    # :NOTE: 
    # All endpoints return either a JSON object or array.
    # Data is returned in ascending order. Oldest first, newest last.

    def __init__(self):
        self.base_url:str = None
        self.metadata = None
        self.connection:_SimpleConnection = None
        self.get_url = lambda endpoint_: urljoin(self.base_url, endpoint_) 
        self._check_connection()

    def _check_connection(self):
        endpoint = "/api/v3/ping"

        for base_url in self.bases:
            connection = _SimpleConnection(
                base_url, 
                endpoint, 
                success_status_code=200
            )

            response = connection.response
            if response.json() == {}:
                self.base_url = base_url
                self.connection = connection
                logger.debug("API Base URL = {}".format(base_url))
                return
        
        logger.warning(
            "Binance Connection cannot be established, Error Code: {}".\
                format(response.status_code)
        )
        return
    
    def get_average_price(self, symbol:str="BTCUSDT"):
        endpoint = r"/api/v3/avgPrice"
        url = self.get_url(endpoint)
        
        response = requests.get(url, params={"symbol":symbol})
        
        return response


    def __get_kline(
            self, 
            symbol:str="BTCUSDT",
            interval:str="1D",
            start_time=None,
            end_time=None,
            limit=500
        ):
        # :TODO: explain what the parameters are
        # https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-data

        # [
        #   [
        #     1499040000000,      // Kline open time
        #     "0.01634790",       // Open price
        #     "0.80000000",       // High price
        #     "0.01575800",       // Low price
        #     "0.01577100",       // Close price
        #     "148976.11427815",  // Volume
        #     1499644799999,      // Kline close time
        #     "2434.19055334",    // Quote asset volume
        #     308,                // Number of trades
        #     "1756.87402397",    // Taker buy base asset volume
        #     "28.46694368",      // Taker buy quote asset volume
        #     "0"                 // Unused field. Ignore.
        #   ]
        # ]

        endpoint = "/api/v3/klines"
        url = self.get_url(endpoint)

        response = requests.get(
            url, 
            params={
                "symbol":symbol,
                "interval":interval,
                "startTime": start_time,
                "endTime": end_time,
                "limit": limit
                },
            )
        
        if response.status_code != 200:
            logging.warning("Klines / Candlestick data cannot be retrieved")
            return

        price_data = pd.DataFrame(
            data=np.array(response.json()),
            columns = [
                "Kline open time",
                "Open price",
                "High price",
                "Low price",
                "Close price",
                "Volume",
                "Kline close time",
                "Quote asset volume",
                "Number of trades",
                "Taker buy base asset volume",
                "Taker buy quote asset volume",
                "Unused field. Ignore."
            ],
            dtype=np.float32
        )

        plt.plot(price_data["Kline open time"], price_data["Close price"])
        plt.draw()
        plt.show(block=True)
