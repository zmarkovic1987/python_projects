from selenium import webdriver
from pages.home_page.login_page import LoginPage
from utilities.test_status import ErrorStatus
import unittest
import pytest
import time


@pytest.mark.usefixtures('one_time_setUp', 'setUp')
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setUp):
        self.log_in_page = LoginPage(self.driver)
        self.ts = ErrorStatus(self.driver)

    # @pytest.mark.run(order=2)
    def test_valid_login(self):
        # self.driver.get('https://learn.letskodeit.com/')
        self.log_in_page.login('test@email.com', 'abcabc')

        result_1 = self.log_in_page.verify_title()
        # time.sleep(20)
        self.ts.mark(result_1, " Title is Incorrect")

        result_2 = self.log_in_page.verify_login_successfull()
        self.ts.mark_final("Test Valid Login", result_2, "Loggin Failed")

        time.sleep(2)

    # @pytest.mark.run(order=1)
    def test_failed_login(self):
        self.log_in_page.logout()
        self.log_in_page.login('test@email.com', 'abcabcxyz')

        result = self.log_in_page.verify_login_failed()
        # self.ts.mark(result, "Failed Login test is Unsuccessful")
        assert result is True

        time.sleep(2)

