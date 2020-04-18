from selenium import webdriver
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

        # base_url = 'http://automationpractice.com/index.php'
        # driver = webdriver.Chrome()
        # driver.maximize_window()
        # driver.implicitly_wait(7)
        # driver.get(base_url)

        self.add_first_product_from_woman_tops.test_1()

        time.sleep(2)
        self.driver.quit()


# start = AddToCart()
# start.add_to_cart()


