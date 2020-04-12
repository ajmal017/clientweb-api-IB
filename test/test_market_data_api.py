# coding: utf-8

"""
    Client Portal Web API

    Production version of the Client Portal Web API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ib_web_api
from ib_web_api.api.market_data_api import MarketDataApi  # noqa: E501
from ib_web_api.rest import ApiException


class TestMarketDataApi(unittest.TestCase):
    """MarketDataApi unit test stubs"""

    def setUp(self):
        self.api = ib_web_api.api.market_data_api.MarketDataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_iserver_marketdata_history_get(self):
        """Test case for iserver_marketdata_history_get

        Market Data History  # noqa: E501
        """
        pass

    def test_iserver_marketdata_snapshot_get(self):
        """Test case for iserver_marketdata_snapshot_get

        Market Data  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
