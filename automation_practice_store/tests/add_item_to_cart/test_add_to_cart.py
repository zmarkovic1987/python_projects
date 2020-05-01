from pages.home.home_page import HomePage
import unittest
import pytest
import time


@pytest.mark.usefixtures('one_time_setup')
class TestAddToCart(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.add_first_product_from_woman_tops = HomePage(self.driver)

    @pytest.mark.run(order=1)
    def add_to_cart(self):
        self.add_first_product_from_woman_tops.test_1()

        # time.sleep(2)
        # self.driver.quit()

