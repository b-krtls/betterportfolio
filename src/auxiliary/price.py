"""The module defines relevant classes and functions relevant to
price data, that is used across different packages.

:REVIEW:: TODO: 
"""
import logging  # Be sure that this does not have security issues
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel("CRITICAL") #DEBUG
logger.addHandler(logging.StreamHandler())

class PriceHistory:
    def __init__(self, source:str) -> None:
        self.price_data:pd.DataFrame = None
        self.metadata:dict = None
        self.source = source

    def retrieve(self):
        pass
        return

    def plotter(self):
        # TODO::
        pass



