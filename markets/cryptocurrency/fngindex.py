"""The module defines relevant classes and functions relevant to
cryptocurrencies market analysis.

:REVIEW:: TODO: 
"""
from datetime import datetime
import logging  # Be sure that this does not have security issues
import numpy as np
import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import  DateFormatter

# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("CFG")
logger.setLevel("CRITICAL") #DEBUG
logger.addHandler(logging.StreamHandler())


# :TODO: write a docstring for the methods and the class in Sphinx format

class CryptoFearAndGreedIndex:  # CFG
    """ A class to represent the Crypto Fear and Greed Index -
    Bitcoin Sentiment, through Alternative.Me API or through a csv file

    Object should be instantiated through one of
        :from_api(): or :from_file(): methods

    :raises AssertionError: When the class is not instantiated the
        intended way(s), or if it is not deliberately overriden
    """
    def __init__(self, limit, source="api", override=False) -> None:
        assert override == True
        self.limit = limit
        self.source = source  # "api" or "file"
        self.nullval = NotImplemented # Default value to be set at mid-range [0,100]
        self.current_val = None
        self.X = None
        self.Y = None


    @classmethod
    def from_api(cls, limit: int):  # Initialize the class from the api
        """Initialize the class from the web api

        :param limit: Integer representing the past number of days to
            which the Fear & Greed Index is calculated.
        :type limit: int

        :return: An instance of :class:'CryptoFearAndGreedIndex'
            generated from the Web API
        :rtype: :class:'CryptoFearAndGreedIndex'
        """
        limit = 1 if not isinstance(limit, int) else limit
        cfg = cls(limit, override=True)

        cfg.limit = limit
        response = requests\
            .get(f"https://api.alternative.me/fng/?limit={limit}")\
            .json()

        try:
            cfg.current_val = int(response["data"][0]["value"])
        except KeyError:  
            cfg.current_val = cfg.nullval

        cfg._resolve_webdata(response)

        return cfg


    def _resolve_webdata(self, response):
        # For resolving the response object obtained from the web API
        X = list()
        Y = list()
        for data in response["data"]:
            timestamp = data["timestamp"]
            value = data["value"]
            dt = datetime.fromtimestamp(int(timestamp)).date()
            X.append(dt)
            Y.append(value)

        self.X = np.array(X, dtype="datetime64[D]")
        self.Y = np.array(Y, dtype=int)
        self.X = np.flip(self.X)
        self.Y = np.flip(self.Y)

    @classmethod
    def from_file(cls, filepath):
        #:TODO: Implement it
        data = pd.read_csv(filepath)
        limit = NotImplemented  #f(data)
        cfg = cls(limit, override=True)

        cfg.X = NotImplemented
        cfg.Y = NotImplemented

        return NotImplemented


    def plotter(self):
        """Method to plot the index distribution

        :return: The axes object of the plot :class:'Axes' from matplotlib
        :rtype: :class:'matplotlib.axes.Axes'
        """
        fig = plt.figure()
        ax = plt.axes()
        ax.plot(self.X, self.Y, 'k-',
                linewidth=1, 
                markersize=12
                )
        ax.set_title("Crypto Fear and Greed Index")
        ax.set_xlabel('Date')
        ax.set_ylabel('Index Value')

        myFmt = DateFormatter(r"%Y-%m-%d")
        ax.xaxis.set_major_formatter(myFmt)

        ax.set_ylim([0, 100])

        for label in ax.get_xticklabels():
            label.set_rotation(45)
            label.set_horizontalalignment("center")

        ax.grid(linestyle=':')

        # Horizontal lines for Extreme-Fear and Extreme-Greed sentiments
        ax.axhline(y=25, linewidth=2, color='green', linestyle="--")
        ax.axhline(y=75, linewidth=2, color='red', linestyle="--")

        logger.debug(f"limit={self.limit}:")  #DEBUG
        logger.debug(f"from {self.X[0]} to {self.X[-1]}")
        return ax


    #:TODO: A class method to update a table with the most current data
    @classmethod
    def update_table(self, args):
        pass


    @classmethod
    def _test_me(cls, token="api"):
        """Method reserved for testing the basic functionalities of the class

        :param token: A string 'api' or 'file', defaults to "api"
        :type token: str, optional
        """
        if token == "api":
            cfg = CryptoFearAndGreedIndex.from_api(0)
            ax = cfg.plotter()
            # ax.plot()
            plt.draw()


            plt.show(block=False)  # block=False
            input(":class:'CryptoFearAndGreedIndex' --> Test Complete")
            
            return 0

        elif token == "file":
            pass 
        

if __name__ == "__main__":
    CryptoFearAndGreedIndex._test_me()
