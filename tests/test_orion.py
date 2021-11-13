from unittest import TestCase

import orion

from API.endpoints import DEMO_ID

class SengTestCase(TestCase):
    def setUp(self) -> None:
        pass


    def tearDown(self) -> None:
        pass


    def test_main(self):
        self.assertTrue(orion.main() == orion.SUCCESS)


    def test_get_profle(self):
        momin = orion.get_profile("qadriid")
        self.assertIsInstance(momin,dict)


    def test_get_post(self):
        self.assertIsInstance(orion.get_post(DEMO_ID), dict)

    def test_get_application(self):
        self.assertIsInstance(orion.get_application(DEMO_ID), dict)
    