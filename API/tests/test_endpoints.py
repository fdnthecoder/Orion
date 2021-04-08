"""
This runs tests for endpoints.py.
"""

from unittest import TestCase
from flask_restx import Resource

from API.endpoints import HelloWorld , HELLO  # , AVAILABLE, Endpoints
# from API.endpoints import Games


class TestEndpoints(TestCase):
    def test_hello(self):
        """
        Test our "hello" endpoint.
        """
        hello_ep = HelloWorld(Resource)
        ret = hello_ep.get()
        self.assertIn(HELLO, ret)
