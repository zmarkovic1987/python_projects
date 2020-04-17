from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from wait_types.explicit_wait_framework import ExplicitWaitType
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time


class Screenshots():

    def test(self):
        base_url = 'https://learn.letskodeit.com'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(base_url)
        wait = ExplicitWaitType(driver)

        driver.find_element_by_link_text('Login').click()

        wait.wait_for_element('user_email', By.ID)
        driver.find_element_by_id('user_email').send_keys('abc@email.com')
        driver.find_element_by_id('user_password').send_keys('abc')
        driver.find_element_by_xpath('//input[@value="Log In"]').click()
        time.sleep(3)
        self.take_screenshot(driver)


    def take_screenshot(self, driver):
        """
        Takes a Screenshot
        :param driver:
        :return:
        """
        file_name = str(round(time.time() * 1000)) + '.png'
        screenshot_file_directory = "C:\\Users\\Zarko\\Desktop\\"
        screenshot_file_path = screenshot_file_directory + file_name

        try:
            driver.save_screenshot(screenshot_file_path)
            print("Screenshot is saved to: " + screenshot_file_path)
        except NotADirectoryError:
            print('Not a directory issue')


start = Screenshots()
start.test()