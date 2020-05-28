from base.base_page import BasePage
from pages.checkout.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By
import time


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout = CheckoutPage(self.driver)

    # Locators
    _mmenu_woman = "a[title='Women']"
    _tops_link = 'a[title="Tops"]'
    _dresses_link = 'a[title="Dresses"]'
    _plp_list = 'product_img_link'
    _add_to_cart_btn = 'button[name="Submit"]'
    _cart_window = 'layer_cart'
    _close_cart_window = '//span[@title="Continue shopping"]'
    _my_account_nav = 'a[title="View my customer account"]'  # CSS
    _my_addresses = 'a[title="Addresses"]'
    _remove_2nd_address = "//ul[contains(@class, 'last_item')]//a[@title='Delete']"
    _remove_first_address = "//ul[contains(@class, 'first_item')]//a[@title='Delete']"
    _remove_buttons = "//a[@title='Delete']"
    _log_out_btn = 'a[title="Log me out"]'  # CSS
    _log_in_link = 'Sign in'  #link_text
    _account_heading = '#center_column > h1.page-heading'   # by css
    _logo = 'logo'  # By CLASS
    _add_to_wishlist = 'wishlist_button'  # ID
    _close_quick_view = 'a[title="Close"]'  # By CsS

    # Actions

    def go_to_account(self):
        self.click_element(self._my_account_nav, By.CSS_SELECTOR)

    def click_woman_tops(self):
        self.hover_and_click(self._mmenu_woman, By.CSS_SELECTOR, self._tops_link, By.CSS_SELECTOR)
        time.sleep(2)

    def click_woman_dresses(self):
        self.hover_and_click(self._mmenu_woman, By.CSS_SELECTOR, self._dresses_link, By.CSS_SELECTOR)
        time.sleep(2)

    def verify_woman_dresses_title(self, title_to_match):
        result = self.verifyPageTitle(title_to_match)
        return result

    def log_in(self):
        if self.element_is_present(self._log_in_link, By.LINK_TEXT) is True:
            self.click_element(self._log_in_link, By.LINK_TEXT)
            self.checkout.login(email='zmarkovic1987@gmail.com', password='Zarko321')

    def log_out(self):
        if self.element_is_present(self._log_out_btn) is True:
            self.click_element(self._log_out_btn, By.CSS_SELECTOR)

    def click_product_from_list(self, x=0):
        # self.click_element_from_list_number(self._plp_list, By.CLASS_NAME)
        self.click_element_from_list_number(self._plp_list, By.CLASS_NAME, x)

    def add_to_cart_click(self):
        self.wait_for_element(self._add_to_cart_btn, By.CSS_SELECTOR)
        self.click_element(self._add_to_cart_btn, By.CSS_SELECTOR)

    def switch_to_window_frame(self):
        self.frame_switch()

    def switch_original_window(self):
        self.driver.switch_to.default_content()

    def close_cart_window(self):
        self.wait_for_element(self._close_cart_window, By.XPATH)
        self.click_element(self._close_cart_window, By.XPATH)

    # Test
    def test_1(self):
        self.click_woman_tops()
        self.click_product_from_list()
        # self.driver.switch_to.frame(0)
        self.frame_switch()
        self.add_to_cart_click()
        self.switch_original_window()
        self.close_cart_window()

    def address_delete(self):
        self.go_to_account()
        self.click_element(self._my_addresses, By.CSS_SELECTOR)

        remove_buttons = self.get_elements(self._remove_buttons, By.XPATH)

        while len(remove_buttons) > 0:
            self.click_element(element=remove_buttons[0])
            self.confirm_alert()
            remove_buttons = self.get_elements(self._remove_buttons, By.XPATH)

    def verify_no_addresses(self):
        remove_buttons = self.get_elements(self._remove_buttons, By.XPATH)
        if len(remove_buttons) == 0:
            return True
        else:
            return False

    def verify_log_out(self):
        result = self.element_is_present(self._my_account_nav, By.CSS_SELECTOR)
        if result is True:
            return False
        else:
            return True

    def verify_log_in(self):
        result = self.element_is_present(self._log_out_btn, By.CSS_SELECTOR)
        if result is True:
            return True
        else:
            return False

    def go_to_homepage(self):
        self.click_element(self._logo, By.CLASS_NAME)

    def switch_to_item_iframe(self):
        self.frame_switch()

    def add_product_to_wishlist(self, x=0):
        self.click_product_from_list(x)
        time.sleep(1)
        self.frame_switch(1)
        self.click_element(self._add_to_wishlist, By.ID)
        # closing confirmaiton dialog
        self.click_element(self._close_quick_view, By.CSS_SELECTOR)
        # closing quick view
        self.frame_switch_default()
        self.click_element(self._close_quick_view, By.CSS_SELECTOR)
        # closing quick view
        # self.frame_switch_default()

    def adding_2_products_wishlist(self):
        self.add_product_to_wishlist(x=0)
        time.sleep(3)

        self.add_product_to_wishlist(x=1)
        time.sleep(2)










