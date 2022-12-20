import json
import requests
from urllib.parse import urljoin

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    base_url = r"https://api.binance.com"

    endpoint = r"/api/v3/ping"  # r"/api/v3/avgPrice"
    url = urljoin(base_url, endpoint)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.json())

    assert response.status_code == 200

    endpoint = r"/api/v3/avgPrice"
    url = urljoin(base_url, endpoint)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.json())

    assert response.status_code != 200


    endpoint = r"/api/v3/avgPrice"
    url = urljoin(base_url, endpoint)
    response = requests.get(url, params={"symbol":"BTCUSDT"})
    # print(response.status_code)
    # print(response.json())
    assert response.status_code == 200


    endpoint = "/api/v3/klines"
    url = urljoin(base_url, endpoint)
    response = requests.get(
        url, 
        params={
            "symbol":"BTCUSDT",
            "interval":"15m",
            # "startTime":None,
            # "endTime":None,
            "limit":25
        }
    )
    print(response.status_code)
    print(response.json())
    print(len(response.json()))

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
    print(price_data.columns)
    x = np.array(price_data["Kline open time"])
    x= x.reshape((1,-1))
    y=np.array(price_data["Close price"])
    y= y.reshape((1,-1))
    print(x[0], y[0])
    plt.plot(x[0], y[0])
    # plt.ylim([15000, 30000])
    plt.draw()
    plt.show(block=True)
