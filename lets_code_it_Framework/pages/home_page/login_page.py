from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pages.home_page.navigation_page import NavigationPage
import utilities.custom_logger as cl
import logging


class LoginPage(BasePage):

    # logger = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = 'Login'
    _email_field = 'user_email'
    _password_field = 'user_password'
    _login_button = "input[name='commit']"
    _sign_out = '//div[@id="navbar"]//a[@href="/sign_out"]'

    def click_login_link(self):
        self.element_click(self._login_link, locator_type=By.LINK_TEXT)

    def fill_email(self, email):
        self.sendKeys(email, self._email_field)

    def fill_password(self, password):
        self.sendKeys(password, self._password_field)

    def click_login_button(self):
        self.element_click(self._login_button, locator_type=By.CSS_SELECTOR)

    def login(self, user_name="", password=""):

        self.click_login_link()
        self.clear_fields()
        self.fill_email(user_name)
        self.fill_password(password)
        self.click_login_button()

    def verify_login_successfull(self):
        result = self.is_element_present('//span[contains(text(), "Test")]', By.XPATH)
        return result

    def verify_login_failed(self):
        result = self.is_element_present('//div[contains(text(), "Invalid email or password")]', By.XPATH)
        return result

    def clear_fields(self):
        self.get_element(self._email_field).clear()
        self.get_element(self._password_field).clear()

    def verify_title(self):
        # if self.get_title() == "Let's Kode It":
        if "Let's Kode It" in self.get_title():
            return True
        else:
            return False

    def logout(self):
        self.nav.navigate_to_settings()
        self.wait_for_element(self._sign_out, By.XPATH, timeout=5)
        self.element_click(self._sign_out, By.XPATH)
