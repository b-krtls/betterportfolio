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

    def __init__(self, base_url:str, endpoint:str=''):
        self.name:str = "SimpleConnection"
        self.base_url:str = base_url
        self.endpoint:str = endpoint
        self.status:bool = False 
        self.response:requests.Response = None
        self.metadata = None
        self.method = None
        self.parse_url = lambda endpoint_: urljoin(self.base_url, endpoint_)

    def establish(self,
                  method:str="get",
                  kwargs=dict(),
                  success_status_code:int=200):
        """
        Establish a connection to an endpoint

        :param method: _description_, defaults to "get"
        :type method: str, optional
        :param kwargs: Arguments to requests Methods, defaults to dict()
        :type kwargs: dict, optional
        :param success_status_code: The status code of a potential\
            successful connection, defaults to 200
        :type success_status_code: int, optional
        :raises ValueError: If the declared request method is NOT allowed 
        :return: Response of the request
        :rtype: requests.Response
        """
  
        self.method = method.casefold()

        # Checking for correct arguments
        allowed_methods = ["get", "post"]
        if method not in allowed_methods:
            raise ValueError(f"Connection Method is not allowed: {method}")

        # Establish Connection
        if method == "get":
            response = requests.get(
                urljoin(self.base_url, self.endpoint), **kwargs
            )
        elif method == "post":
            response = requests.post(
                urljoin(self.base_url, self.endpoint), **kwargs
            )

        if response.status_code == success_status_code:
            self.status = True
        else:
            logger.warning(
                "Connection cannot be established successfully: {} - "\
                "Response Status Code = {}\n"\
                "Successful Connection Status Code should be {}"\
                    .format(__class__.__name__, 
                            response.status_code, 
                            success_status_code)
            )

        self.response = response
        return response

    # def __repr__(self) -> str:
    #     pass