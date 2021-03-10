
"""
This runs tests for endpoints.py.
"""

from unittest import TestCase
from flask_restx import Resource

from endpoints import HelloWorld, HELLO, AVAILABLE, Endpoints


class TestEndpoints(TestCase):
    def test_hello(self):
        """
        Test our "hello" endpoint.
        """
        hello_ep = HelloWorld(Resource)
        ret = hello_ep.get()
        self.assertIn(HELLO, ret)

    def test_endpoints(self):
        """
        Test our "endpoints" endpoint.
        """
        epts = Endpoints(Resource)
        ret = epts.get()
        self.assertIn(AVAILABLE, ret)
