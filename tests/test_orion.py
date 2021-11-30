from unittest import TestCase

import orion

from API.endpoints import DEMO_ID, DEMO_USERNAME

class OrionTestCase(TestCase):
    def setUp(self) -> None:
        pass


    def tearDown(self) -> None:
        pass


    def test_main(self):
        self.assertTrue(orion.main() == 0)


    def test_get_profile(self):
        momin = orion.get_profile(DEMO_USERNAME)
        self.assertIsInstance(momin,dict)


    def test_get_post(self):
        apost = orion.get_post(DEMO_ID)
        self.assertIsInstance(apost, dict)

    def test_user_exist_in_success(self):
        self.assertTrue(orion.user_exist(DEMO_USERNAME))
    
    def test_user_exist_in_fail(self):
        randomUserName = "sdfadfs"
        self.assertFalse(orion.user_exist(randomUserName))
