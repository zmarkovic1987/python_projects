from base.base_page import BasePage
from pages.home.home_page import HomePage
from selenium.webdriver.common.by import By
import time


class ProductListingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home = HomePage(driver)

    #  Locators
    _plp_add_to_cart = 'a[title="Add to cart"]'  # CSS
    _list_view_type = 'a[title="List"]'  # CSS
    _grid_view_type = 'a[title="Grid"]'
    _color_click_path = '//ul[contains(@class, "product_list ")]/li[{0}]//ul[contains(@class, "color_to_pick_list ")]//li[{1}]/a'
    _color_click = _color_click_path.format('2', '1')  # first is number of the product div; second is color
    # _product_containers = '//ul[contains(@class, "product_list")]'  # Xpath
    # _color_container = '//ul[contains(@class, "color_to_pick_list ")]'
    _close_cart_icon = 'span[title="Close window"]'  # XPATH

    def switch_view(self, view_type):
        if view_type == 'List':
            self.click_element(self._list_view_type, By.CSS_SELECTOR)
        elif view_type == 'Grid':
            self.click_element(self._grid_view_type, By.CSS_SELECTOR)
        else:
            self.logger.error("Wrong View Type. It Should be either List or View")

    def nth_product_add_to_cart(self, i):
        self.click_element_from_list_number(self._plp_add_to_cart, By.CSS_SELECTOR, i)

    def close_modal_cart(self):
        self.wait_for_element(self._close_cart_icon, By.XPATH)
        self.home.close_cart_window()

    def click_container_color(self):
        self.click_element(self._color_click, By.XPATH)

    def plp_test_1(self, i):
        self.switch_view('List')
        self.nth_product_add_to_cart(i)

    def plp_test_2(self):
        self.close_modal_cart()
        time.sleep(2)

        self.click_container_color()
        time.sleep(2)

