from base.base_page import BasePage
from utilities.utils import Util
from selenium.webdriver.common.by import By
import time


class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()

    # Locators
    _remove_item = 'icon-trash'  # Class
    _increase_qty = 'icon-plus'  # CLASS
    _proceed_to_checkout_btn = 'standard-checkout'  # class
    _user_email = 'email'  #ID
    _user_password = 'passwd'  # ID
    _sign_in_btn = 'SubmitLogin'  # ID
    _password_error = '//p[contains(text(), "There is 1 error")]'  # Xpath
    _add_new_address = "//p[contains(@class, 'address_add')]/a"  # XPATH
    _first_name = 'firstname'  # ID
    _last_name = 'lastname'  # ID
    _address_1 = 'address1'
    _city = 'city'
    _zip_code = 'postcode'
    _mobile_phone = 'phone_mobile'
    _state_dropdown = 'id_state'
    _submit_address_btn = 'submitAddress'  # ID
    _state = 'Wisconsin'
    _save_address = 'alias'
    _saved_address_dropdown_shipping = 'id_address_delivery'  # Id
    _same_address = 'addressesAreEquals'  # ID
    _add_billing_address = '#address_invoice_form > a'  # CSS
    _proceed_to_4th_step = 'button[name="processAddress"]'  # CSS
    _agree_to_terms = 'cgv'  # ID
    _proceed_to_payment = '//button[@name="processCarrier"]'
    _payment_wire = 'bankwire'  # CLASS
    _payment_check = 'cheque'  # CLASS
    _place_order_btn = '#cart_navigation > button[type=submit]'  # CSS

    def remove_item(self, remove_i):
        self.click_element_from_list_number(self._remove_item, By.CLASS_NAME, remove_i)
        time.sleep(1)

    def increase_qty(self, increase_i):
        self.click_element_from_list_number(self._increase_qty, By.CLASS_NAME, increase_i)

    def cart_actions(self, remove_i, increase_i):
        self.remove_item(remove_i)
        self.increase_qty(increase_i)

    def click_proceed_to_checkout(self):
        self.click_element(self._proceed_to_checkout_btn, By.CLASS_NAME)

    def user_email_type(self, email):
        self.type_text(email, self._user_email, By.ID)

    def user_password_type(self, password):
        self.type_text(password, self._user_password, By.ID)

    def click_sign_in(self):
        self.click_element(self._sign_in_btn, By.ID)

    def login(self, email, password):
        self.user_email_type(email)
        self.user_password_type(password)
        self.click_sign_in()

    def verify_invalid_login(self):
        result = self.element_is_present(self._password_error, By.XPATH)
        return result

    def verify_valid_login(self):
        result = self.element_is_present(self._password_error, By.XPATH)
        if result is True:
            return False
        else:
            return True

    def select_state_by_text(self, state='Wisconsin'):
        self.dropdown_select(self._state_dropdown, state, 'text')

    # address_name = ''
    def save_address_title(self):
        input_field = self.get_element(self._save_address, By.ID)
        input_field.clear()
        # random_number = int(time.time()) * 10
        # address_name = 'Automation Test Address ' + str(random_number)
        address_name = self.util.getUniqueName()
        self.type_text(address_name, element=input_field)

    def select_shipping_address_dropdown(self):
        self.dropdown_select(self._saved_address_dropdown_shipping, 0, 'index')

    def select_billing_address_dropdown(self):
        self.dropdown_select(self._saved_address_dropdown_shipping, 0, 'index')

    def submit_address(self):
        self.click_element(self._submit_address_btn, By.ID)

    def add_new_address_btn(self):
        if self.element_is_present(self._add_new_address, By.XPATH) is True:
            self.click_element(self._add_new_address, By.XPATH)

    def add_billing_address(self):
        self.click_element(self._same_address, By.ID)
        self.click_element(self._add_billing_address, By.CSS_SELECTOR)

    def address_handling(self, name, last_name, address, city, zip_code, state, phone):
        self.wait_for_element(self._first_name, By.ID)
        self.type_text(name, self._first_name, By.ID)
        self.type_text(last_name, self._last_name, By.ID)
        self.type_text(address, self._address_1, By.ID)
        self.type_text(city, self._city, By.ID)
        self.type_text(zip_code, self._zip_code, By.ID)
        self.select_state_by_text(state)
        self.type_text(phone, self._mobile_phone, By.ID)
        self.save_address_title()
        self.submit_address()

    def verify_address_submit_success(self):
        result = self.verifyPageTitle('Order - My Store')
        return result

    def proceed_to_4th_step(self):
        self.click_element(self._proceed_to_4th_step, By.CSS_SELECTOR)

    def click_agree_terms(self):
        self.click_element(self._agree_to_terms, By.ID)

    def proceed_to_payment(self):
        self.click_element(self._proceed_to_payment, By.XPATH)

    def handling_4th_step(self):
        self.proceed_to_4th_step()
        self.click_agree_terms()
        self.proceed_to_payment()

    def verify_payment_method_wire(self):
        result = self.element_is_present(self._payment_wire, By.CLASS_NAME)
        return result

    def verify_payment_check(self):
        result = self.element_is_present(self._payment_check, By.CLASS_NAME)
        return result

    def place_order_wire(self):
        self.click_element(self._payment_wire, By.CLASS_NAME)
        self.click_element(self._place_order_btn, By.CSS_SELECTOR)


