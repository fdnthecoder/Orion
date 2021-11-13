from unittest import TestCase

import orion


class SengTestCase(TestCase):
    def test_main(self):
        self.assertTrue(orion.main() == orion.SUCCESS)

