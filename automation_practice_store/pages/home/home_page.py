from base.selenium_driver import SeleniumDriver
from selenium.webdriver.common.by import By
import time


class HomePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _mmenu_woman = "a[title='Women']"
    _tops_link = 'a[title="Tops"]'
    _plp_list = 'product_img_link'
    _add_to_cart_btn = 'button[name="Submit"]'
    _cart_window = 'layer_cart'
    _close_cart_window = 'span[title="Close window"]'


    # Actions

    def click_woman_tops(self):
        self.hover_and_click(self._mmenu_woman, By.CSS_SELECTOR, self._tops_link, By.CSS_SELECTOR)
        time.sleep(2)
        print('Hovering over Woman')

    def click_first_product(self):
        self.click_element_from_list_number(self._plp_list, By.CLASS_NAME)
        print('Click product from list')

    def add_to_cart_click(self):
        self.wait_for_element(self._add_to_cart_btn, By.CSS_SELECTOR)
        self.click_element(self._add_to_cart_btn, By.CSS_SELECTOR)

    def switch_to_window_frame(self):
        self.frame_switch()

    def switch_original_window(self):
        self.driver.switch_to.default_content()

    def close_cart_window(self):
        self.wait_for_element(self._close_cart_window, By.CSS_SELECTOR)
        self.click_element(self._close_cart_window, By.CSS_SELECTOR)

    # Test
    def test_1(self):
        self.click_woman_tops()
        self.click_first_product()
        # self.driver.switch_to.frame(0)
        self.frame_switch()
        self.add_to_cart_click()
        self.switch_original_window()
        self.close_cart_window()




