"""The module defines relevant classes and functions relevant to
price data, that is used by inheriting across different packages.

:REVIEW:: TODO: 
"""
# import json
import logging
import typing
# from urllib import response  # Be sure that this does not have security issues
from urllib.parse import urljoin

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
import requests

logger = logging.getLogger(__name__)
logger.setLevel("CRITICAL") #DEBUG
logger.addHandler(logging.StreamHandler())

class _SimpleConnection:
    """
    Abstraction of a Simple Connection to an endpoint
    """

    def __init__(self, base_url, endpoint, success_status_code):
        self.name:str = "SimpleConnection"
        self.base_url:str = base_url
        self.endpoint:str = endpoint
        self.status:bool = False 
        self.response:requests.Response = None
        self.metadata = None

        self.connect(endpoint, success_status_code)


    def connect(self, endpoint:str, success_status_code:int=200):
        """
        Establish a connection to an endpoint

        :param endpoint: Endpoint to be connected
        :type endpoint: str
        :param success_status_code: The status code of a potential
            successful connection
        :type success_status_code: int
        :return: Response of the request
        :rtype: requests.Response
        """

        # Determine if base endpoint is available for connection
        response = requests.get(urljoin(self.base_url, endpoint))
        self.response = response

        if response.status_code == success_status_code:
            self.status = True
        else:
            logger.warning(
                "{} cannot be established".format(__class__.__name__)
            )
        return response
