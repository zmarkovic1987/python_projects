from selenium import webdriver
from pages.pdp.pdp_page import PDP
import unittest
import pytest
import time

@pytest.mark.usefixtures('one_time_setup')
class TestPDP(unittest.TestCase):

    # pdp_test = PDP(driver)
    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.pdp_test = PDP(self.driver)

    @pytest.mark.run(order=1)
    def test_pdp(self):
        self.pdp_test.test_pdp1()
        time.sleep(2)

        # result = self.pdp_test.products_in_cart('2')

        # assert result is True


    @pytest.mark.run(order=2)
    def test_2(self):
        self.pdp_test.test_pdp2()
        time.sleep(2)

        # result = self.pdp_test.products_in_cart('3')

        # assert result is True


    @pytest.mark.run(order=3)
    def test_3(self):
        self.pdp_test.test_pdp_remove_item()
        time.sleep(2)

        result = self.pdp_test.products_in_cart(1)

        assert result is True

        # self.driver.quit()


# start = TestPDP()
# start.test_pdp()