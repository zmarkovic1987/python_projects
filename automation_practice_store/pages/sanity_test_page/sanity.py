from base.base_page import BasePage
from pages.home.home_page import HomePage
from selenium.webdriver.common.by import By


class SanityTestPage1(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home_page = HomePage(driver)

    def reach_woman_dresses(self):
        self.home_page.click_woman_dresses()

