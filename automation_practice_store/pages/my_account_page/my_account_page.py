from base.base_page import BasePage
from pages.checkout.checkout_page import CheckoutPage
from pages.home.home_page import HomePage
from selenium.webdriver.common.by import By
import time


class MyAccount(BasePage):

    def __init__(self, driver):
        super().__init__(self)
        self.driver = driver
        self.checkout = CheckoutPage(self.driver)
        self.home = HomePage(self.driver)

    # LOCATORS
    _first_address = 'a[title="Add my first address"]'  # CSS
    _back_to_account = '//span[contains(text(), "Back to your account")]'  # Xpath
    _update_address = '//span[contains(text(), "Update")]'  # Xpath
    _wisconsin_present = '//span[contains(text(), "Wisconsin")]'  # Xpath
    _order_history_btn = '//a[@title="Orders"]'  # Xpath
    _order_ref = 'color-myaccount'  # class
    _reorder_btn = '//span[contains(text(), "Reorder")]'  # Xpath
    _proceed_to_checkout_btn = 'standard-checkout'  # class
    _navigate_to_wishlist = 'a[title="My wishlists"]'  # CSS
    _click_on_my_wishlist = "//a[contains(text(), 'My wishlist')]"  # Xptah
    _remove_item_from_wishlist = 'a[title="Delete"]'  # CSS
    _qty_field = '//div[@class="wishlist_product_detail"]//input'
    _save_changes = 'a[title="Save"]'  # CSS
    _new_wishlist_name = 'name'  # ID
    _save_new_wishlist = 'submitWishlist'
    _delete_wishlist_icon = "//i[@class='icon-remove']//parent::a"
    _verify_qty = "//td[contains(text(), '3')]"  # XPATH
    _verify_new_wishlist = "//a[contains(text(), 'New Wishlist')]"  # Xpath


    def click_add_first_address(self):
        if self.element_is_present(self._first_address, By.CSS_SELECTOR) is False:
            self.home.address_delete()
            self.click_element(self._back_to_account, By.XPATH)
        self.click_element(self._first_address, By.CSS_SELECTOR)

    def add_address(self):
        self.click_add_first_address()
        self.checkout.address_handling(
            'Zarko', 'Test', '565 W Orchard st', 'Milwaukee', '53204', "Washington", '2345678901')

    def update_address(self):
        self.click_element(self._update_address, By.XPATH)
        self.checkout.select_state_by_text("Wisconsin")

    def verify_updated_state(self):
        result = self.element_is_present(self._wisconsin_present, By.XPATH)
        return result

    def go_to_history(self):
        self.click_element(self._back_to_account, By.XPATH)
        self.click_element(self._order_history_btn, By.XPATH)
        self.click_element_from_list_number(self._order_ref, By.CLASS_NAME, 0)
        self.click_element(self._reorder_btn, By.XPATH)

    def verify_checkout_btn(self):
        result = self.element_is_present(self._proceed_to_checkout_btn, By.CLASS_NAME)
        return result

    def go_to_home(self):
        if self.check_url('http://automationpractice.com/index.php') is not True:
            self.home.go_to_homepage()

    def reach_wishlist(self):
        self.home.go_to_account()
        self.click_element(self._navigate_to_wishlist, By.CSS_SELECTOR)

    def delete_second_item(self):
        self.click_element_from_list_number(self._remove_item_from_wishlist, By.CSS_SELECTOR, 1)

    def update_qty_of_item(self):
        element = self.get_element_from_list(self._qty_field, By.XPATH, 0)
        self.type_text('3', element=element)

    def save_changes(self):
        self.click_element_from_list_number(self._save_changes, By.CSS_SELECTOR, 0)

    def expand_wishlist(self):
        self.click_element(self._click_on_my_wishlist, By.XPATH)

    def create_new_wishlist(self):
        self.type_text("New Wishlist", self._new_wishlist_name, By.ID)
        self.click_element(self._save_new_wishlist, By.ID)

    def verify_new_wishlist(self):
        result = self.element_is_present(self._verify_new_wishlist, By.XPATH)
        return result

    def delete_wishlists(self):
        elements = self.get_elements(self._delete_wishlist_icon, By.XPATH)
        for each in elements:
            if len(elements) > 0:
                self.click_element(element=each)
                self.confirm_alert()

    def verify_wishlist_removed(self):
        time.sleep(2)
        result = self.element_is_present(self._delete_wishlist_icon, By.XPATH)
        if result is False:
            return True
        else:
            return False

    def test_wishlist(self):
        self.reach_wishlist()
        self.expand_wishlist()
        self.delete_second_item()
        time.sleep(2)

    def verify_item_delete(self):
        self.refresh_page()
        self.expand_wishlist()
        number_of_items = self.get_elements(self._remove_item_from_wishlist, By.CSS_SELECTOR)
        if len(number_of_items) == 1:
            return True
        else:
            return False

    def qty_manipulation(self):
        self.expand_wishlist()
        self.update_qty_of_item()
        self.save_changes()
        time.sleep(5)

    def verify_product_qty(self):
        self.refresh_page()
        result = self.element_is_present(self._verify_qty, By.XPATH)
        return result

    def test_wishlist_2(self):
        self.create_new_wishlist()


        self.delete_wishlists()
        time.sleep(5)
