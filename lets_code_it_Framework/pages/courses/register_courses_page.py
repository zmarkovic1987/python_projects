"""
1) - reach page
2) - Click on Login / type email / type password / click Log in
3) - (click or just send keys to search for JavaScript
4) - Click on Course
5) scroll to bottom
6) - Click Enroll
7) - switch the Iframe
8) - type cc name, number, date, cvv, click enroll
9) - verify error
"""

from base.base_page import BasePage
from selenium.webdriver.common.by import By
import logging
import time


class RegisterCoursesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    _search_field = "search-courses"  # ID
    _search_submit_btn = "search-course-button"  # ID
    # _course_list = "course-box-image"  # CLASS (select first from list)
    _course_list = "//img[@class='course-box-image']"  # CLASS (select first from list)
    _enroll_btn = "enroll-button"  # ID
    _iFrame_number_name = "__privateStripeFrame8"
    _cc_number = "//input[@name='cardnumber']"  # XPATH
    _iFrame_date_name = "__privateStripeFrame9"
    _exp_date = "//input[@name='exp-date']"
    _iFrame_cvc_name = "__privateStripeFrame10"
    _cvc = "//input[@name='cvc']"  # XPATH
    _iFrame_postal_code_name = "__privateStripeFrame11"
    _postal = "//input[@name='postal']"  # XPATH
    _checkbox_save_cc = "save-payment-details"  # ID
    _checkbox_terms = "agreed_to_terms_checkbox"  # ID
    _serbia_radio_btn = "input[value='RS']"  # CSS
    _confirm_order = "confirm-purchase"  # ID
    _invalid_red_numbers = "//input[@aria-invalid='true']"

    def search_for_course(self, course):
        self.sendKeys(course, self._search_field, By.ID)
        self.element_click(self._search_submit_btn, By.ID)

    def select_course_from_list(self):
        time.sleep(2)
        element_list = self.get_elements(self._course_list, By.XPATH)
        self.logger.info(str(len(element_list)))
        self.element_click(element=element_list[0])

    def scroll_to_enroll_btn(self):
        self.scroll_to_element(self._enroll_btn, By.ID)

    def click_enroll(self):
        self.element_click(self._enroll_btn, By.ID)

    def fill_payment_form(self, cc_num, exp_date, cvv, postal):
        self.switch_iframe_name(self._iFrame_number_name)
        self.sendKeys(cc_num, self._cc_number, By.XPATH)

        self.driver.switch_to.default_content()

        self.switch_iframe_name(self._iFrame_date_name)
        self.sendKeys(exp_date, self._exp_date, By.XPATH)

        self.driver.switch_to.default_content()

        self.switch_iframe_name(self._iFrame_cvc_name)
        self.sendKeys(cvv, self._cvc, By.XPATH)

        self.driver.switch_to.default_content()

        self.switch_iframe_name(self._iFrame_postal_code_name)
        self.sendKeys(postal, self._postal, By.XPATH)

        self.driver.switch_to.default_content()

    def uncheck_save_cc(self):
        self.element_click(self._checkbox_save_cc)

    def check_terms_checkbox(self):
        self.element_click(self._checkbox_terms)

    def select_RS_radio_btn(self):
        self.element_click(self._serbia_radio_btn, By.CSS_SELECTOR)

    # def submit_order(self):
    #     self.element_click(self._confirm_order)

    def test(self, course, cc_num, exp_date, cvv, postal):
        self.search_for_course(course)
        self.select_course_from_list()
        self.scroll_to_enroll_btn()
        self.click_enroll()
        self.fill_payment_form(cc_num, exp_date, cvv, postal)
        self.uncheck_save_cc()
        self.select_RS_radio_btn()
        self.check_terms_checkbox()

    def verify_card_invalid(self):
        self.switch_iframe_name(self._iFrame_number_name)
        result = self.isElementDisplayed(self._invalid_red_numbers, By.XPATH)
        self.driver.switch_to.default_content()
        return result

    def verify_enrol_btn_disabled(self):
        attr = self.get_element_attribute('class', self._confirm_order, By.ID)
        self.logger.info(attr)
        if 'is-disabled' in attr:
            return True
        else:
            return False

