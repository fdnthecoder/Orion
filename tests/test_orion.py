from unittest import TestCase

import orion


class SengTestCase(TestCase):
    def test_main(self):
        self.assertTrue(orion.main() == orion.SUCCESS)

    def test_another_func(self):
        self.assertTrue(orion.another_func() == orion.SUCCESS)
