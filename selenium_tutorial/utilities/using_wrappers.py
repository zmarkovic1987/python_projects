from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.handy_wrappers import HandyWrapper


class UsingWrappers():

    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(5)

        imported_from_handy_wrappers = HandyWrapper(driver)

        text_field = imported_from_handy_wrappers.get_element('name')
        text_field.send_keys('Test')
        time.sleep(2)
        text_field2 = imported_from_handy_wrappers.get_element('//input[@id="name"]', locator_type='xpath')
        text_field2.clear()


start = UsingWrappers()
start.test()
