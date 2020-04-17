from selenium import webdriver
from pages.home.home_page import HomePage
import unittest
import time


class TestAddToCart(unittest.TestCase):

    def add_to_cart(self):

        base_url = 'http://automationpractice.com/index.php'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(7)
        driver.get(base_url)

        add_first_product_from_woman_tops = HomePage(driver)
        add_first_product_from_woman_tops.test_1()

        time.sleep(2)
        driver.quit()


# start = AddToCart()
# start.add_to_cart()


